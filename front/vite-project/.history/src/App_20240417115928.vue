<template>
  <div>
    {{ obj.name }}
    {{ objName }}
    <!-- -->
  </div>
</template>

<script>
import { computed, reactive, ref } from 'vue'
function Search(state){
    const mytext=ref("")
    const computedList = computed
        return
    }
export default {
    setup(){
        const state = reactive({
            datalist:[]
        })
        setTimeout(()=>{
            state.datalist="aaa","as","sss"
        })

        const objName = computed(()=>obj.name+"杀杀杀")
        return{
            
        }
    }
}
</script>
