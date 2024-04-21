import { createApp } from 'vue'
import './style.css'
import { createPinia } from 'pinia'
import App from './App.vue'
const pinia = createPinia()
app.use(pinia)
createApp(App).mount('#app')
