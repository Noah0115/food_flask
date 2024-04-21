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
    getCinemaList(store){
        axios
        store.commit('changeCinemaList',res)
    }
  }
});
export default store;
