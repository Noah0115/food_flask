<template>
  <div>
    <!-- 面包屑导航 -->
    <div class="breadcrumb1">
      <el-breadcrumb>
        <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>美食数据管理</el-breadcrumb-item>
        <el-breadcrumb-item>美食数据爬取</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <el-card>
      <el-button @click="sendCustomEvent" :disabled="isCrawling"
        >开始爬虫</el-button
      >
      <el-button @click="clickover" :disabled="!isCrawling">停止爬虫</el-button>
      <el-button @click="datainit" :disabled="!datashow">数据库导入</el-button>
    </el-card>
    <el-card body-style="height: 650px;">
      <ul
        class="infinite-list"
        style="overflow-y: auto; height: calc(100% - 45px); margin-bottom: 20px"
      >
        <h1
          v-for="(item, index) in displayedItems"
          :key="index"
          class="infinite-list-item"
        >
          {{ item }}
        </h1>
      </ul>
      <div>
        <el-button
          v-if="showCollapseButton"
          @click="toggleCollapse"
          plain
        >
          {{ collapsed ? "展开" : "折叠 " }}
        </el-button>
      </div>
      
    </el-card>
  </div>
</template>

<script>
import io from 'socket.io-client';

export default {
  data() {
    return {
      socket: null,
      showdata: [],
      isCrawling: false,
      collapsed: true, //true是折叠 false是展开,
      datashow: false,

    };
  },
  mounted() {
    // this.connectToSocket();
  },
  methods: {
    connectToSocket() {
      // 连接到后端服务
      this.socket = io('http://82.156.147.153:8025'); //建立链接
      this.$message.success("已连接到后端服务")
      // 监听连接
      this.socket.on('connect', () => {
        console.log('Connected to server');
      });

      // 监听自定义事件
      this.socket.on('event_response', (data) => {
        console.log('Received response from server:', data);
        this.showdata.push(data.data)
      });

      // 监听断开连接
      /* this.socket.on('disconnect', () => {
        console.log('Disconnected from server');
      }); */
    },
    sendCustomEvent() {
      this.showdata = []
      this.collapsed = true
      this.isCrawling = true;
      this.connectToSocket()

      console.log(this.showdata)
      // 向服务器发送自定义事件
      this.socket.emit('event', { data: 'Hello from Vue!' }); // event可变 相当于具体接口

      this.socket.emit('start_crawler', { start: true });
      this.dataRecover()

      /* this.socket.on('crawler_progress', (data) => {
        this.showdata.push(data.progress)
      });
      this.socket.on('crawler_status', (data) => {
        this.showdata.push(data.status)
      }); */

    },
    dataRecover() {

      this.socket.on('crawler_progress', (data) => {
        console.log(data)
        this.showdata.push(data.progress)
      });
      this.socket.on('crawler_status', (data) => {
        this.showdata.push(data.status)
        if (data.status === '爬虫完成或停止') {
          this.Over()

        }
      });
    },
    clickover() {
      this.socket.emit('stop_crawler', { stop: true });
    },

    Over() {
      // 发送停止爬虫的请求到服务器

      // 在你的方法中调用
      const h = this.$createElement;
      this.$msgbox({
        title: '消息',
        message: h('p', null, [
          h('span', null, '爬虫完成或停止 '),

        ]),
        closeOnClickModal: false, // 点击遮罩层不关闭对话框
        closeOnPressEscape: false, // 按下 ESC 键不关闭对话框
        showClose: false, // 隐藏关闭按钮
        showCancelButton: false,
        confirmButtonText: '确定',

        beforeClose: (action, instance, done) => {
          if (action === 'confirm') {
            instance.confirmButtonLoading = true;
            instance.confirmButtonText = '请等待3秒...';
            setTimeout(() => {
              done();
              this.datashow = true
              this.isCrawling = false;
              setTimeout(() => {
                instance.confirmButtonLoading = false;

              }, 300);
            }, 3000);
          } else {
            done();
          }
        }
      }).then(action => {
        this.$message({
          type: 'success',
          message: '已断开'
        });
      });
      setTimeout(() => {
        // 断开socket连接
        if (this.socket) {
          this.socket.disconnect();
          this.progress = '已停止';
          this.status = '连接已断开';



        }
      }, 3000);

    },
    toggleCollapse() {
      this.collapsed = !this.collapsed;
    },
    async datainit() {
      const { data: res } = await this.$http.get("/back/data_init");
      this.datashow = false
      if (res.code !== 200) {
          return this.$message.error(res.msg);
        }
        this.$message.success(res.msg);
    }
  },
  computed: {
    displayedItems() {
      if (this.collapsed && this.showdata.length > 4) {
        return this.showdata.slice(0, 3).concat(this.showdata.slice(-1)); // 显示前三项和最后一项
      } else {
        return this.showdata; // 显示所有项
      }
    },
    showCollapseButton() {
      return this.showdata.length > 3; // 只有在列表超过3个时才显示折叠按钮
    }
  }
};
</script>
<style lang='less' scoped>
.breadcrumb1 .el-breadcrumb {
  font-size: 16px !important;
}
</style>