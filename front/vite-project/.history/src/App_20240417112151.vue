<template>
  <div>
    <!-- -->
  </div>
</template>

<script>
import { computed, reactive } from 'vue'
export default {
    setup(){
        const obj = reactive({
            name:"小米"
        })
        objName = computed(()=>obj.name)
        return
    }
}
</script>
