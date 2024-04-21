<template>
  <div>
    <input type="text" v-model="mytext">
    <ul></ul>
    <!-- -->
  </div>
</template>

<script>
import { computed, reactive, ref } from 'vue'
function Search(state){
    const mytext=ref("")
    const computedList = computed(()=>{
        return state.datalist.filter(item=>item.incudes(mytext.value))
    })
        return {
            mytext,
            computedList
        }

    }
export default {
    setup(){
        const state = reactive({
            datalist:[]
        })
        setTimeout(()=>{
            state.datalist="aaa","as","sss"
        })
        const {mytext,computedList} =Search(state)
        // const objName = computed(()=>obj.name+"杀杀杀")
        return{
            computedList,
            mytext
        }
    }
}
</script>
