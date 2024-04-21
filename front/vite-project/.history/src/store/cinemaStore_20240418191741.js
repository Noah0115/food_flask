import { defineStore } from "pinia";
const useCinemaStore = defineStore("cinema",{

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
export default useCinemaStore