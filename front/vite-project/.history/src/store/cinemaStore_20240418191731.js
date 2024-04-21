import { defineStore } from "pinia";
const useCStore = defineStore("tabbar",{

    state:()=>{
        return{
            isTabbarShow:true
        }
    },
    actions:{
        change(value){
            this.isTabbarShow=value
        }
    }
})
export default useTabbarStore