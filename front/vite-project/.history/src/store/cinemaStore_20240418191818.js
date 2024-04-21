import { defineStore } from "pinia";
const useCinemaStore = defineStore("cinema",{

    state:()=>{
        cinemaList:[]
    },
    actions:{
        async getCinemaList(){
            
        }
    }
})
export default useCinemaStore