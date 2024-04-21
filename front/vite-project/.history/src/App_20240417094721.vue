<template>
  <div>
    <!-- -->{{ obj.myname }}
  </div>
</template>

<script>
import { reactive } from 'vue'
export default {
    setup(){
        const obj = reactive({
            myname:"kersi",
            mayage:100
        })
        return {
            obj
        }
    }
}
</script>
