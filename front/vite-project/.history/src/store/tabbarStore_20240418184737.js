import { defineStore } from "pinia";
const useTabbarStore = defineStore("tabbar",{

    state:()=>{
        return{
            isTabbarShow:true
        }
    },
    actions:{
        change(value){

        }
    }
})
export default useTabbarStore