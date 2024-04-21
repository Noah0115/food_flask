import { createStore } from "vuex";
const store = createStore({
  state() {
    return { isTabbarShow: true };
  },
  mutations:{
    /* showTabbar(state){
        state.isTabbarShow=true
    },
    hideTabbar(state){
        state.isTabbarShow=false
    }, */
    changeTabbar(state,payload){
        state.isTabbarShow=payload
    },
    changeCinemaList(state,payload){
        state.cinemaList=payload
    },
  },
  actions:{
    //vue文件在写
    if(this.$store.state.cinemaList.lenmgth===0)
    getCinemaList(store){
        axios
        store.commit('changeCinemaList',res.data.cinemas)
    }
  }
});
export default store;
