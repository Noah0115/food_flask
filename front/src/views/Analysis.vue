<template>
  <div class="goods" id="goods" name="goods">
    <!-- 面包屑 -->
    <div class="breadcrumb">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item to="/">首页</el-breadcrumb-item>
        <el-breadcrumb-item>美食分析</el-breadcrumb-item>
        <el-breadcrumb-item>可视化展示</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <!-- 面包屑END -->
    <div class="main">
      <el-row :gutter="20">
        <el-col :span="12">
          <el-card class="card" :style="{ height: '44vh' }">
            <!-- 内容1 -->

            <v-chart :option="option_column" style="height: 400px"></v-chart>
          </el-card>
        </el-col>
        <el-col :span="12">
          <el-card class="card" :style="{ height: '44vh' }">
            <!-- 内容2 -->
            <v-chart :option="option_ban" style="height: 400px"></v-chart>
          </el-card>
        </el-col>
      </el-row>
      <!-- 下面的一个 el-card 固定大小 -->
      <el-card class="card" :style="{ height: '44vh' }">
        <!-- 内容3 -->
        <v-chart :option="option_zhu" style="height: 400px"></v-chart>
      </el-card>
      <el-card class="card" :style="{ height: '55vh' }">
        <!-- 内容4 -->
        <v-chart :option="option_lei" style="height: 400px"></v-chart>
      </el-card>
    </div>
  </div>
</template>

<script>

export default {

  data() {
    return {
      option_column: {
        tooltip: {
          trigger: 'item'
        },
        legend: {
          top: '5%',
          left: 'center'
        },
        series: [
          {
            name: '',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: 40,
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              { value: 1048, name: 'Search Engine' },
              { value: 735, name: 'Direct' },
              { value: 580, name: 'Email' },
              { value: 484, name: 'Union Ads' },
              { value: 300, name: 'Video Ads' }
            ]
          }
        ]
      },
      option_ban: {
        tooltip: {
          trigger: 'item'
        },
        legend: {
          top: '5%',
          left: 'center',
          // doesn't perfectly work with our tricks, disable it
          selectedMode: false
        },
        series: [
          {
            name: '',
            type: 'pie',
            radius: ['40%', '70%'],
            center: ['50%', '70%'],
            // adjust the start angle
            startAngle: 180,
            label: {
              show: true,
              formatter(param) {
                // correct the percentage
                return param.name + ' (' + param.percent * 2 + '%)';
              }
            },
            data: [
              { value: 1048, name: 'Search Engine' },
              { value: 735, name: '' },
              { value: 580, name: 'Email' },
              { value: 484, name: 'Union Ads' },
              { value: 300, name: 'Video Ads' },
              {
                // make an record to fill the bottom 50%
                value: 1048 + 735 + 580 + 484 + 300,
                itemStyle: {
                  // stop the chart from rendering this piece
                  color: 'none',
                  decal: {
                    symbol: 'none'
                  }
                },
                label: {
                  show: false
                }
              }
            ]
          }
        ]
      },
      option_zhu: {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            axisTick: {
              alignWithLabel: true
            }
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: '数量',
            type: 'bar',
            barWidth: '60%',
            data: [10, 52, 200, 334, 390, 330, 220]
          }
        ]
      },
      option_lei: {
        title: {
          text: '家常菜特性雷达图'
        },


        tooltip: {},
        legend: {
          top: '7%',
          data: []
        },
        radar: {
          // 定义雷达图的指标，这里以味道类型、准备时间、难度等级为例
          indicator: [
            { name: '味道类型', max: 22 },
            { name: '准备时间', max: 100 },
            { name: '难度等级', max: 6 }
          ],
          center: ['50%', '75%'], // 调整雷达图的位置
          radius: '80%', // 调整雷达图的大小
          grid: {
            left: '15%',
            right: '15%',
            bottom: '15%',
            top: '20%', // 将雷达图往下移动
            containLabel: false
          },
        },

        series: [{

          name: '凉菜对比',
          type: 'radar',
          // 填充数据
          data: [
            {
              value: [3, 10, 1], // 假设值，分别对应上面的三个指标
              name: '凉拌木耳'
            },
            {
              value: [2, 30, 1],
              name: '凉拌洋葱木耳'
            },
            {
              value: [3, 30, 2],
              name: '凉拌海带丝'
            }
          ]
        }]
      }
    };
  },

  created() {
    this.getPie();
    this.getBan();
    this.getZhu();
    this.getLei();
  },

  methods: {
    async getPie() {
      const { data: res } = await this.$http.get("/index/data_anl_pie",);
      if (res.code !== 200) {

        return this.$message.error("数据获取失败");
      }
      this.option_column.series[0].data = res.data
      console.log(this.option_column.series[0].data)
    },
    async getBan() {
      const { data: res } = await this.$http.get("/index/data_anl_pie_flavour",);
      if (res.code !== 200) {

        return this.$message.error("数据获取失败");
      }
      this.option_ban.series[0].data = res.data[0]
      this.option_ban.series[0].data.push({
        value: res.data[1],
        itemStyle: {
          color: 'none',
          decal: {
            symbol: 'none'
          }
        },
        label: {
          show: false
        }
      });
      console.log(this.option_ban.series[0].data)
    },
    async getZhu() {
      const { data: res } = await this.$http.get("/index/data_anl_bar",);
      if (res.code !== 200) {

        return this.$message.error("数据获取失败");
      }
      this.option_zhu.xAxis[0].data = res.data[0]
      this.option_zhu.series[0].data = res.data[1]

    },
    async getLei() {
      const { data: res } = await this.$http.get("/index/data_rader",);
      if (res.code !== 200) {

        return this.$message.error("数据获取失败");
      }

      this.option_lei.series[0].data = res.data
      for (let k in res.data) {
        console.log(res.data[k].name);
        this.option_lei.legend.data.push(res.data[k].name)
      }

      // this.option_zhu.xAxis[0].data = res.data[0]
      // this.option_zhu.series[0].data = res.data[1]

    },



  },
  mounted() {
  }

}

</script>
<style scoped>
.goods {
  background-color: #f5f5f5;
}
/* 面包屑CSS */
.el-tabs--card .el-tabs__header {
  border-bottom: none;
}
.goods .breadcrumb {
  height: 50px;
  background-color: white;
}
.goods .breadcrumb .el-breadcrumb {
  width: 1225px;
  line-height: 30px;
  font-size: 16px;
  margin: 0 auto;
}
/* 面包屑CSS END */
.card {
  margin-top: 20px;
}
</style>