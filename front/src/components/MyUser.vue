
<template>
  <div id="register">
    <el-dialog
      title="修改用户信息"
      width="600px"
      :style="{ 'margin-top': '100px' }"
      center
      :visible.sync="isUserinfo"
      @close="editDialogClosed"
    >
      <el-form
        :model="editForm"
        :rules="rules"
        status-icon
        ref="editFormRef"
        class="demo-ruleForm"
      >
        <el-form-item prop="name">
          <el-input
            prefix-icon="el-icon-user-solid"
            v-model="editForm.name"
          ></el-input>
        </el-form-item>
        <el-form-item prop="email">
          <el-input
            prefix-icon="el-icon-message"
            placeholder="请输入邮箱"
            v-model="editForm.email"
          ></el-input>
        </el-form-item>
        <el-form-item prop="phone">
          <el-input
            prefix-icon="el-icon-phone"
            placeholder="请输入手机号"
            v-model="editForm.phone"
          ></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            prefix-icon="el-icon-view"
            type="password"
            placeholder="请输入密码"
            v-model="editForm.password"
          ></el-input>
        </el-form-item>

        <el-form-item>
          <el-button
            size="medium"
            type="primary"
            @click="editUserInfo"
            style="width: 100%"
            >提交</el-button
          >
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>
<script>
import { mapGetters } from 'vuex';
import { mapActions } from "vuex";
export default {
  name: "MyUser",
  props: ["userinfo"],
  data() {
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
      isUserinfo: false, // 控制个人信息组件是否显示

      // 用户信息校验规则,validator(校验方法),trigger(触发方式),blur为在组件 Input 失去焦点时触发
      rules: {
        username: [
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
      editForm: '',
      linshi:'',
    };
  },
  created() {
    /* this.getUserinfo(); */
  },
  watch: {
    // 监听父组件传过来的register变量，设置this.isRegister的值
    userinfo: function (val) {
      if (val) {
        this.isUserinfo = val;
        this.getUserinfo();
      }
    },
    // 监听this.isUserinfo变量的值，更新父组件register变量的值
    isUserinfo: function (val) {
      if (!val) {
        
        this.$emit("fromChild", val);
        
      }
    },
    
  },
  methods: {
    ...mapActions(["setUser"]),
    ...mapGetters(["getUser"]),
    getUserinfo() {
      this.editForm =this.$store.getters.getUser
      // this.editForm = this.getUser();
      // console.log('new',this.editForm)
    },
    editUserInfo() {
      this.$refs.editFormRef.validate(async (valid) => {
        /* console.log(valid) */
        if (!valid) return;
        //可以发起添加用户的网络请求
        // this.editForm.is_admin=true
        const { data: res } = await this.$http.post(
          "/back/update_user", this.editForm
        );
        if (res.code !== 200) {
          return this.$message.error(res.msg);
        }
        this.$message.success(res.msg);

        let user = JSON.stringify(this.editForm);
        localStorage.setItem("user", user);
        
        this.setUser(this.editForm);
        this.editForm = this.getUser();
        
        this.isUserinfo = false;
        

      });
    },
    editDialogClosed() {
      this.$refs.editFormRef.resetFields();
      
    },
  },
};
</script>
<style >
</style>
