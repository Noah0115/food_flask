import { createStore } from "vuex";
const store = createStore({
  state() {
    return { isTabbarShow: true };
  },
  mutations:{
    showTabbar
  }
});
export default store;
