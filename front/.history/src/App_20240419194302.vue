<template>
	<div>
		<h1> {{ form }} </h1>   <!--{name:'xxx'}/ {name:'xxx',age:10}-->
		<button @click="add">添加</button>
	</div>
</template>
<script>
export default{
	data(){
		return{
			form:{
				name: 'xxx',
			}
		}
	},
	methods:{
		add(){
			if(!this.form.age){
				this.$set(this.form, 'age, 10) // 成功
				
				// Vue2中监听不到动态给对象添加的属性的
				// this.form.age = 10   // 失败无法添加,更无法自增
                console.log(this.form.age);
                
			} else {
				this.form.age++
			}
		}
	}
}
</script>
