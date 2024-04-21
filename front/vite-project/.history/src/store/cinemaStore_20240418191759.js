import { defineStore } from "pinia";
const useCinemaStore = defineStore("cinema",{

    state:()=>{
        cinemaList:[]
    },
    actions:{
        change(value){
            this.isTabbarShow=value
        }
    }
})
export default useCinemaStore