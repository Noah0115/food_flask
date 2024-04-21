import { createStore } from "vuex";
const store = createStore({
  state() {
    return { isTabbarShow: true };
  },
  mutations:{
    showTabbar(state){
        state.isTabbarShow=true
    },
    showTabbar(state){
        state.isTabbarShow=true
    },
  }
});
export default store;
