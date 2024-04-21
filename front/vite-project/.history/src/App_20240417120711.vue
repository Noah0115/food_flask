<template>
  <div>
    <input type="text" v-model="mytext">
    <ul>
        <li v-for="data in computedList" :key="data">
            {{ data }}
        </li>
    </ul>
    <!-- -->
  </div>
</template>

<script>
import { computed, reactive, ref } from 'vue'
function UseSearch(state){
    const mytext=ref("")
    const computedList = computed(()=>
        state.datalist.filter(item=>item.includes(mytext.value))
    )
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
            state.datalist=["aaa","as","sss"]
        })
        const {mytext,computedList} =UseSearch(state)
        // const objName = computed(()=>obj.name+"杀杀杀")
        return{
            computedList,
            mytext
        }
    }
}
</script>
