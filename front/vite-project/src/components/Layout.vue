<template>
  <div>
    <Sidebar v-if="isShow"></Sidebar>
    <Content></Content>
    <input v-model="searchText"/>
    <input :value="searchText" @input="searchText=$event.target.value"/>
  </div>
</template>
<script>
import { defineAsyncComponent } from "vue";
import Sidebar from "./Sidebar.vue";
// import Content from "./Content.vue";
export default {
  props: {
    myShow: Boolean,
  },
  components: {
    Sidebar,
    Content:defineAsyncComponent({
      //加载函数
      loader:()=> import('./foo.vue'),
      //加载异步组件时使用的组件
      loadingComponent:LoadingComponent,
      //展示加载组件前的延迟时间，默认为200ms
      delay:200,

      //加载失败后的展示组件
      errorComponent:errorComponent,
      //如果提供了一个 timeout 时间限制，并超时了
      //也会显示这里配置的报错组件，默认值是:Infinity
      timeout:2000

    }),
    
  },
  data() {
    return {
      isShow: true,
    };
  },
};
</script>
