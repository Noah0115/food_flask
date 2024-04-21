<template>
  <div>
    <!-- 面包屑导航 -->
    <div class="breadcrumb">
      <el-breadcrumb>
        <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>用户管理</el-breadcrumb-item>
        <el-breadcrumb-item>用户列表</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <!-- 卡片区域 -->
    <el-card class="box-card">
      <div>
        <!-- 分栏间隔 -->
        <el-row :gutter="20">
          <el-col :span="6"
            ><div class="grid-content bg-purple">
              <!-- 搜索框 -->
              <el-input
                placeholder="请输入内容"
                v-model="queryInfo.query"
                clearable
                @clear="getUserList"
              >
                <el-button
                  slot="append"
                  icon="el-icon-search"
                  @click="searchUserList"
                ></el-button>
              </el-input></div
          ></el-col>
          <el-col :span="6"
            ><div class="grid-content bg-purple">
              <el-button type="primary" @click="addDialogVisible = true"
                >添加用户</el-button
              >
            </div></el-col
          >
        </el-row>
        <!-- 用户列表区 -->
        <el-table stripe border :data="userlist" style="width: 100%">
          <el-table-column
            type="index"
            label="索引"
            width="90"
          ></el-table-column>
          <el-table-column prop="name" label="姓名"> </el-table-column>
          <el-table-column prop="email" label="邮箱"> </el-table-column>
          <el-table-column prop="phone" label="电话"> </el-table-column>
          <el-table-column prop="is_admin" label="角色">
            <template slot-scope="{ row }">
              {{ row.is_admin ? "管理员" : "普通用户" }}
            </template>
          </el-table-column>

          <el-table-column label="操作" width="180px">
            <template v-slot="scope">
              <el-button
                type="primary"
                icon="el-icon-edit"
                size="small"
                @click="showEditDialog(scope.row.id)"
              ></el-button>
              <!-- 删除按钮 -->
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
      <!-- 分页 -->
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="currentChange"
        :current-page="currentPage"
        :page-sizes="[1, 2, 5, 10]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      >
      </el-pagination>
      <!-- 弹出框 -->
      <el-dialog
        title="添加用户"
        :visible.sync="addDialogVisible"
        width="50%"
        @close="addDialogClosed"
      >
        <el-form
          :model="addForm"
          :rules="addFormRules"
          ref="addFormRef"
          label-width="70px"
        >
          <el-form-item label="用户名" prop="name">
            <el-input v-model="addForm.name"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input v-model="addForm.password"></el-input>
          </el-form-item>
          <el-form-item label="邮箱" prop="email">
            <el-input v-model="addForm.email"></el-input>
          </el-form-item>
          <el-form-item label="手机" prop="phone">
            <el-input v-model="addForm.phone"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="addDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="addUser">确 定</el-button>
        </span>
      </el-dialog>
      <el-dialog
        title="修改用户"
        :visible.sync="editDialogVisible"
        width="50%"
        @close="editDialogClosed"
      >
        <el-form
          :model="editForm"
          :rules="editFormRules"
          ref="editFormRef"
          label-width="70px"
        >
          <el-form-item label="用户名" prop="name">
            <el-input v-model="editForm.name" disabed></el-input>
          </el-form-item>

          <el-form-item label="邮箱" prop="email">
            <el-input v-model="editForm.email" disabled></el-input>
          </el-form-item>
          <el-form-item label="手机" prop="phone">
            <el-input v-model="editForm.phone"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="editDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="editUserInfo">确 定</el-button>
        </span>
      </el-dialog>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    //验证邮箱规则
    var checkEmail = (rule, value, cb) => {
      const regEmail =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      if (regEmail.test(value)) {
        return cb();
      }
      cb(new Error("请输入合法邮箱"));
    };
    //手机号验证
    var checkMobile = (rule, value, cb) => {
      const regMobile = /^(?:(?:\+|00)86)?1[3-9]\d{9}$/;
      if (regMobile.test(value)) {
        return cb();
      }
      cb(new Error("请输入合法手机号"));
    };

    return {
      //获取用户列表参数对象
      queryInfo: {
        query: "",

      },
      userlist: [],
      total: 0, // 商品总量
      pageSize: 10, // 每页显示的商品数量
      currentPage: 1, //当前页码
      addDialogVisible: false,
      //添加用户的表单数据
      addForm: {
        name: "",
        email: "",
        phone: "",
        password: "",
        is_admin: false
      },
      //添加表单的验证规则和对象
      addFormRules: {
        name: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          {
            min: 1,
            max: 10,
            message: "请输入1-10个字符",
            trigger: "blur",
          },
        ],
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          {
            min: 6,
            max: 15,
            message: "请输入6-15个字符",
            trigger: "blur",
          },
        ],
        email: [
          { required: true, message: "请输入邮箱", trigger: "blur" },
          {
            validator: checkEmail,
            trigger: "blur",
          },
        ],
        phone: [
          { required: true, message: "请输入手机号", trigger: "blur" },
          {
            validator: checkMobile,
            trigger: "blur",
          },
        ],
      },
      editDialogVisible: false,
      editForm: {},
      editFormRules: {
        name: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          {
            min: 1,
            max: 10,
            message: "请输入1-10个字符",
            trigger: "blur",
          },
        ],
        email: [
          { message: "请输入邮箱", trigger: "blur" },
          {
            validator: checkEmail,
            trigger: "blur",
          },
        ],
        phone: [
          { required: true, message: "请输入手机号", trigger: "blur" },
          {
            validator: checkMobile,
            trigger: "blur",
          },
        ],
      },
      setRoleDialogVisible: false,
      //需要被分配角色的用户信息
      UserInfo: {},
      //所有角色数据列表
      rolesList: [],
      //已选中的角色id
      selectedRoleId: "",
      userlistall:[],
    };
  },
  //创建生命周期对象
  created() {
    this.getUserList();
  },
  methods: {
    async getUserList() {
      //调用请求，第一个参数是请求地址
      const { data: res } = await this.$http.get("back/get_all_user");
      if (res.code !== 200) {
        
        this.$message.error(res.msg);
      }
      this.$message.success(res.msg);
      this.total = res.data.length;
      this.userlistall = res.data;
      this.userlistall = this.userlistall.map(item => ({
        ...item,
        status: item.status === 1
      }));
      this.fenye();
    },
    fenye() {
      // 计算起始索引
      const startIndex = (this.currentPage - 1) * this.pageSize;
      // 计算结束索引
      const endIndex = startIndex + this.pageSize;
      this.userlist = this.userlistall.slice(startIndex, endIndex);;
    },
    async searchUserList() {
      //调用请求，第一个参数是请求地址
      const { data: res } = await this.$http.post("back/search_user", {
        "name": this.queryInfo.query

      });
      if (res.code !== 200) {
        /* console.log(res); */
        this.$message.error(res.msg);
      }
      this.$message.success(res.msg);
      this.total = res.data.length;
      this.userlistall = res.data;
      this.userlistall = this.userlistall.map(item => ({
        ...item,
        status: item.status === 1
      }));
      this.fenye();
      // this.total = res.data.total;
      
    },

    //监听Pagesize改变的事件
    handleSizeChange(newSize) {

      this.pageSize = newSize;

      this.fenye();
    },
    //监听页码值改变的事件
    currentChange(newPage) {
      this.currentPage = newPage;
      this.fenye();
      
    },
    //监听switch开关状态改变
    async userStateChanged(userinfo) {
      /* console.log(userinfo); */
      const { data: res } = await this.$http.put(
        //不要忘了$
        `users/${userinfo.id}/state/${userinfo.mg_state}`
      );
      if (res.meta.status !== 200) {
        userinfo.mg_state = !userinfo.mg_state;
        return this.$message.error("更新用户状态失败");
      }
      this.$message.success("更新用户状态成功");
    },
    //监听对话框close事件
    addDialogClosed() {
      this.$refs.addFormRef.resetFields();
    },
    addUser() {
      this.$refs.addFormRef.validate(async (valid) => {
        /* console.log(valid) */
        if (!valid) return;
        //可以发起添加用户的网络请求
        const { data: res } = await this.$http.post("/back/add_user", this.addForm);
        if (res.code !== 200) {
          return this.$message.error(res.msg);
        }
        this.$message.success(res.msg);
        this.addDialogVisible = false;
        this.getUserList();
      });
    },
    //显示编辑用户的对话框
    async showEditDialog(id) {
      const { data: res } = await this.$http.post("/back/search_user", { 'id': id });
      if (res.code !== 200) {
        return this.$message.error(res.msg);
      }
      this.$message.success(res.msg);
      this.editForm = res.data[0];


      this.editDialogVisible = true;
    },
    //监听对话框close事件
    editDialogClosed() {
      this.$refs.editFormRef.resetFields();
    },
    editUserInfo() {
      this.$refs.editFormRef.validate(async (valid) => {
        /* console.log(valid) */
        if (!valid) return;
        //可以发起添加用户的网络请求
        const { data: res } = await this.$http.post(
          "/back/update_user", this.editForm
        );

        if (res.code !== 200) {
          return this.$message.error(res.msg);
        }
        this.$message.success(res.msg);
        this.editDialogVisible = false;
        this.getUserList();
      });
    },

  
  


    //滑块改变
    async StateChanged(id) {
      const selectedItem = this.userlist.find(item => item.id === id);
      console.log(selectedItem.status)
      if (selectedItem) {
        this.editForm = selectedItem;
        // 打开编辑对话框或执行其他操作
      } else {
        console.log("Item not found with id:", id);
      }

      this.editForm.status = this.editForm.status ? 1 : 0;

      const { data: res } = await this.$http.post("/back/update_user", this.editForm);
      console.log(this.editForm)
      if (res.code !== 200) {
        return this.$message.error(res.msg);

      }
      this.$message.success(res.msg);
      console.log(this.editForm)
      this.getUserList();

    },


  },
};
</script>

<style lang='less' scoped>
.breadcrumb .el-breadcrumb {
  font-size: 16px !important;
}
.el-table {
  margin-top: 20px;
}
</style>