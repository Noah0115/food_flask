<template>
  <div>
    <!-- 面包屑导航 -->
    <div class="breadcrumb">
      <el-breadcrumb>
        <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>公告管理</el-breadcrumb-item>
        <el-breadcrumb-item>公告列表</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <el-card class="box-card">
      <div>
        <el-button type="primary" @click="showAddDialog">添加公告</el-button>

        <el-table stripe border :data="pushList" style="width: 100%">
          <el-table-column
            type="index"
            label="索引"
            width="90"
          ></el-table-column>
          <el-table-column prop="title" label="公告标题"> </el-table-column>
          <el-table-column prop="content" label="公告详情"> </el-table-column>
          <el-table-column label="查看" width="80px">
            <template v-slot="scope">
              <!-- 查 -->
              <el-button
                icon="el-icon-search"
                type="success"
                size="mini"
                @click="showDialog(scope.row.content)"
              ></el-button>
             
            </template>
          </el-table-column>
          <el-table-column label="修改" width="80px">
            <template v-slot="scope">
              
              <!--  改 -->
              <el-button
                type="info"
                size="mini"
                @click="showEditDialog(scope.row.id)"
                icon="el-icon-edit"
              ></el-button>
            </template>
          </el-table-column>
          <el-table-column label="状态" width="180px">
            <template v-slot="scope">
              <!-- 删除按钮 -->
              <el-switch
                v-model="scope.row.status"
                @change="StateChanged(scope.row.id)"
                active-text="激活"
                inactive-text="禁用"
              >
              </el-switch>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <!-- 查窗口 -->
      <el-dialog
        title="查看公告详情"
        :visible.sync="showDialogVisible"
        width="50%"
        @close="showDialogClosed"
      >
        <div v-html="detail"></div>
      </el-dialog>
      <!-- 改窗口 -->
      <el-dialog
        title="修改公告信息"
        :visible.sync="showEditDialogVisible"
        width="50%"
        @close="showEditDialogClosed"
      >
        <el-form
          :model="editForm"
          :rules="editFormRules"
          ref="editFormRef"
          label-width="100px"
        >
          <el-form-item label="公告标题" prop="title">
            <el-input v-model="editForm.title"></el-input>
          </el-form-item>

          <!-- <el-form-item label="公告状态" prop="status">
            <el-switch v-model="statusBoolean" @change="StateChanged">
            </el-switch>
          </el-form-item> -->
          <el-form-item label="公告详情" prop="content">
            <quill-editor v-model="editForm.content"></quill-editor>
          </el-form-item>
          <el-form-item class="btns">
            <el-button type="primary" @click="saveEdit">保存</el-button>
          </el-form-item>
        </el-form>
      </el-dialog>
      <!-- 增窗口 -->
      <el-dialog
        title="增加公告信息"
        :visible.sync="showAddDialogVisible"
        width="50%"
        @close="showAddDialogClosed"
      >
        <el-form
          :model="addForm"
          :rules="addFormRules"
          ref="addFormRef"
          label-width="100px"
        >
          <el-form-item label="公告标题" prop="title">
            <el-input v-model="addForm.title"></el-input>
          </el-form-item>

          <el-form-item label="公告详情" prop="content">
            <quill-editor v-model="addForm.content"></quill-editor>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="showAddDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="addPush">确 定</el-button>
        </span>
      </el-dialog>
    </el-card>
  </div>
</template>

<script>

export default {
  data() {
    return {
      rolestate: true,
      userInfo: [],
      pushList: [],
      detail: '',
      showDialogVisible: false,
      showEditDialogVisible: false,
      showAddDialogVisible: false,
      editForm: {

      },


      addForm: {
        title:'',
        content:''
      },
      addFormRules: {
        title: [
          { required: true, message: "请输入公告标题", trigger: "blur" },

        ],

        content: [
          { required: true, message: "请输入公告详情", trigger: "blur" },

        ],
      },
      editFormRules: {
        title: [
          { required: true, message: "请输入公告标题", trigger: "blur" },

        ],
        news_time: [
          { required: true, message: "请输入公告时间", trigger: "blur" },

        ],
        source: [
          { required: true, message: "请输入公告来源", trigger: "blur" },

        ],
        content: [
          { required: true, message: "请输入公告详情", trigger: "blur" },

        ],
      },
    };
  },

  created() {
    this.getPushList();
  },
  methods: {
    //获取公告列表
    async getPushList() {
      //调用请求，第一个参数是请求地址
      const { data: res } = await this.$http.get("/back/get_all_news_admin",);
      if (res.code !== 200) {

        return this.$message.error("获取公告列表失败");
      }
      this.$message.success(res.msg);
      this.pushList = res.data;
      this.pushList = this.pushList.map(item => ({
        ...item,
        status: item.status === 1
      }));
      
    },
    //展示详情窗口
    async showDialog(content) {

      this.detail = content
      this.showDialogVisible = true;

    },
    //关闭详情窗口
    showDialogClosed() {
      this.showDialogVisible = false;
    },
    //打开编辑窗口
    async showEditDialog(id) {
      const selectedItem = this.pushList.find(item => item.id === id);
      if (selectedItem) {
        this.editForm = selectedItem;
        // 打开编辑对话框或执行其他操作
      } else {
        console.log("Item not found with id:", id);
      }
      /* console.log(id) */

      this.showEditDialogVisible = true;
    },
    //保存编辑公告
    async saveEdit() {

      const { data: res } = await this.$http.post("/back/update_news", this.editForm);
      
      if (res.code !== 200) {
        return this.$message.error("更新失败");
      }
      this.$message.success("更新成功");
      this.showEditDialogVisible = false;
      this.getPushList()
    },
    //滑块改变
    //滑块改变
    async StateChanged(id) {
      const selectedItem = this.pushList.find(item => item.id === id);
      console.log(selectedItem.status)
      if (selectedItem) {
        this.editForm = selectedItem;
        // 打开编辑对话框或执行其他操作
      } else {
        console.log("Item not found with id:", id);
      }

      this.editForm.status = this.editForm.status ? 1 : 0;

      const { data: res } = await this.$http.post("/back/update_news", this.editForm);
      console.log(this.editForm)
      if (res.code !== 200) {
        return this.$message.error("禁用失败");

      }
      this.$message.success("修改成功");
      console.log(this.editForm)
      this.getPushList();

    },

    //关闭编辑窗口
    showEditDialogClosed() {
      this.showEditDialogVisible = false;
    },
    //打开添加窗口
    showAddDialog() {
      this.showAddDialogVisible = true;
    },
    //关闭添加窗口
    showAddDialogClosed() {
      this.$refs.addFormRef.resetFields();
    },
    //添加公告
    addPush() {
      this.$refs.addFormRef.validate(async (valid) => {
        /* console.log(valid) */
        if (!valid) return;
        //可以发起添加用户的网络请求
        console.log(this.addForm)
        const { data: res } = await this.$http.post("/back/add_news", this.addForm);
        if (res.code !== 200) {
          return this.$message.error(res.msg);
        }
        this.$message.success("添加成功");
        this.showAddDialogVisible = false;
        this.getPushList()
      });

    },


  },


}

</script>
<style lang='less' scoped>
.breadcrumb .el-breadcrumb {
  font-size: 17px !important;
}
.el-table {
  margin-top: 20px;
}
.btns {
  display: flex; //弹性模型
  justify-content: flex-end; //尾部对齐
}
</style>