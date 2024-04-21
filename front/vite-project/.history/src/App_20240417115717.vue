<template>
  <div>
    {{ obj.name }}
    {{ objName }}
    <!-- -->
  </div>
</template>

<script>
import { computed, reactive } from 'vue'
export default {
    setup(){
        const state = reactive({
            datalist:[]
        })
        const objName = computed(()=>obj.name+"杀杀杀")
        return{
            
        }
    }
}
</script>
