import { defineStore } from "pinia";
const useTabbarStore = defineStore("tabbar",{

    state:()=>{
        return{
            isTabbarShow:true
        }
    }
})
export default useTabbarStore