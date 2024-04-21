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
    changeTabbar(state,payload){
        state.isTabbarShow=payload
    },
  },
  actions:{
    getCinemaList(store){
        axios
        store.commit()
    }
  }
});
export default store;