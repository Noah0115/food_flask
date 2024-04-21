import { defineStore } from "pinia";
const useTabbarStore = defineStore("tabbar",{

    state:()=>{
        return{
            isTabbarShow:true
        }
    },
    actions:{
        change()
    }
})
export default useTabbarStore