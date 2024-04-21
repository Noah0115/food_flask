<template>
  <div id="myLogin">
    <el-dialog
      title="登录"
      width="600px"
      center
      :visible.sync="isLogin"
      :close-on-click-modal="false"
      :style="{ 'margin-top': '100px' }"
    >
      <el-form
        :model="LoginUser"
        :rules="rules"
        status-icon
        ref="ruleForm"
        class="demo-ruleForm"
      >
        <el-form-item prop="name">
          <el-input
            prefix-icon="el-icon-user-solid"
            placeholder="请输入邮箱"
            v-model="LoginUser.email"
          ></el-input>
        </el-form-item>
        <el-form-item prop="pass">
          <el-input
            prefix-icon="el-icon-view"
            type="password"
            placeholder="请输入密码"
            v-model="LoginUser.password"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button
            size="medium"
            type="primary"
            @click="Login"
            style="width: 100%"
            >登录</el-button
          >
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>
<script>
import { mapActions } from "vuex";


export default {
  name: "MyLogin",
  props:['receiveUsername'],
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

    return {
      LoginUser: {
        email: "",
        password: "",
        csrf_token: ""
      },
      UserInfo: {},
      // 用户信息校验规则,validator(校验方法),trigger(触发方式),blur为在组件 Input 失去焦点时触发

      rules: {

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

      },
    };
  },
  computed: {
    // 获取vuex中的showLogin，控制登录组件是否显示
    isLogin: {
      get() {
        return this.$store.getters.getShowLogin;
      },
      set(val) {
        this.$refs["ruleForm"].resetFields();
        this.setShowLogin(val);
      }
    }
  },
  methods: {
    ...mapActions(["setUser", "setShowLogin"]),
    Login() {
      // 通过element自定义表单校验规则，校验用户输入的用户信息
      this.$refs["ruleForm"].validate(valid => {
        //如果通过校验开始登录
        if (valid) {
          console.log(this.LoginUser);
          this.$http.get("/user/get_csrf").then(res => {
            this.$http
              .post("/user/login", {
                email: this.LoginUser.email,
                password: this.LoginUser.password,
                csrf_token: this.LoginUser.csrf_token,
              }).then(res => {
                // “001”代表登录成功，其他的均为失败
                if (res.data.code === 200) {
                  // 隐藏登录组件
                  this.$message({
                    type: 'success',
                    message: res.data.msg
                  });
                  // console.log('11',this.LoginUser)
                  this.$http.post("/user/profile", {
                    email: this.LoginUser.email
                  }).then(res => {
                    // console.log(res)
                    this.UserInfo = res.data.data[0]
                    let user = JSON.stringify(this.UserInfo);
                    this.UserInfo.password = this.LoginUser.password
                    this.setUser(this.UserInfo);
                    localStorage.setItem("user", user);
                    // console.log(JSON.parse(localStorage.getItem("user")).name);
                    // 登录信息存到vuex
                    // console.log('666', this.UserInfo.name)
                    // this.sendUsername(this.UserInfo.name)
                    this.$emit('sendUsername', this.UserInfo.name);
                  }
                  )
                  this.isLogin = false;
                } else {
                  this.$message({
                    type: 'error',
                    message: res.data.msg
                  });
                }
              })
              .catch(err => {
                return Promise.reject(err);
              });
          })

        } else {
          return false;
        }
      });

    },
    sendUsername(username) {
      // this.$emit('sendUsername', username);
      // this.receiveUsername(username)
    }
  }
};
</script>
<style>
</style>