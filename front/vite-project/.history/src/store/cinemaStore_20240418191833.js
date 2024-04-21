import { defineStore } from "pinia";
const useCinemaStore = defineStore("cinema",{

    state:()=>{
        cinemaList:[]
    },
    actions:{
        async getCinemaList(){
            var res = await axios()
            
        }
    }
})
export default useCinemaStore