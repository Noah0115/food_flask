import { defineStore } from "pinia";
const useTabbarStore = defineStore("tabbar",{

    state:()=>{
        return{
            isTabbarShow:true
        }
    },
    actions:{
        change(va){

        }
    }
})
export default useTabbarStore