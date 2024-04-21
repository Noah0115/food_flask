<template>
  <div id="register">
    <el-dialog
      title="注册"
      width="600px"
      :style="{ 'margin-top': '100px' }"
      center
      :visible.sync="isRegister"
      :close-on-click-modal="false"
    >
      <el-form
        :model="RegisterUser"
        :rules="rules"
        status-icon
        ref="ruleForm"
        class="demo-ruleForm"
      >
        <el-form-item prop="name">
          <el-input
            prefix-icon="el-icon-user-solid"
            placeholder="请输入账号"
            v-model="RegisterUser.name"
          ></el-input>
        </el-form-item>
        <el-form-item prop="email">
          <el-input
            prefix-icon="el-icon-message"
            placeholder="请输入邮箱"
            v-model="RegisterUser.email"
          ></el-input>
        </el-form-item>
        <el-form-item prop="phone">
          <el-input
            prefix-icon="el-icon-phone"
            placeholder="请输入手机号"
            v-model="RegisterUser.phone"
          ></el-input>
        </el-form-item>
        <el-form-item prop="pass">
          <el-input
            prefix-icon="el-icon-view"
            type="password"
            placeholder="请输入密码"
            v-model="RegisterUser.pass"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button
            size="medium"
            type="primary"
            @click="Register"
            style="width: 100%"
            >注册</el-button
          >
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>
<script>
export default {
  name: "MyRegister",
  props: ["register"],
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
      isRegister: false, // 控制注册组件是否显示
      RegisterUser: {
        name: "",
        email: "",
        phone: "",
        pass: "",
        csrf_token: "",
      },
      // 用户信息校验规则,validator(校验方法),trigger(触发方式),blur为在组件 Input 失去焦点时触发
      rules: {
        name: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          {
            min: 1,
            max: 10,
            message: "请输入1-10个字符",
            trigger: "blur",
          },
        ],
        pass: [
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
    };
  },
  watch: {
    // 监听父组件传过来的register变量，设置this.isRegister的值
    register: function (val) {
      if (val) {
        this.isRegister = val;
      }
    },
    // 监听this.isRegister变量的值，更新父组件register变量的值
    isRegister: function (val) {
      if (!val) {
        this.$refs["ruleForm"].resetFields();
        this.$emit("fromChild", val);
      }
    },
  },
  methods: {
    async Register() {
      const { data: res } = await this.$http.get("/user/get_csrf");
      console.log(res);
      this.RegisterUser.csrf_token = res;
      // 通过element自定义表单校验规则，校验用户输入的用户信息
      this.$refs["ruleForm"].validate((valid) => {
        //如果通过校验开始注册
        if (valid) {
          console.log(this.RegisterUser);
          this.$http
            .post("/user/register", {
              name: this.RegisterUser.name,
              email: this.RegisterUser.email,
              phone: this.RegisterUser.phone,
              password: this.RegisterUser.pass,
              csrf_token: this.RegisterUser.csrf_token,
            })
            .then((res) => {
              console.log(res)
              // “001”代表注册成功，其他的均为失败
              if (res.data.code === 200) {
                // 隐藏注册组件
                this.isRegister = false;
                // 弹出通知框提示注册成功信息
                this.$message({
                    type: 'success',
                    message: res.data.msg
                  });
              } else {
                // 弹出通知框提示注册失败信息
                this.$message({
                    type: 'error',
                    message: res.data.msg
                  });
              }
            })
            .catch((err) => {
              return Promise.reject(err);
            });
        } else {
          return false;
        }
      });
    },
  },
};
</script>
<style >
</style>
