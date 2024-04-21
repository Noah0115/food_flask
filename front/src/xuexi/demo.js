/* const obj = {};
Object.defineProperty(obj, 'name', {
  // configurable: false,//默认为false
  // enumerable: false,//默认为false
  value: 'kongzhi',
  writable: true,//默认为false
  // get(){},
  // set(v){}
});
console.log(obj.name); // 输出 kongzhi
 
// 改写obj.name 的值
obj.name = 111;
console.log(obj.name); // 还是打印出 kongzhi,因为writable默认为false */
/* const window = {}
let current = 0;
Object.defineProperty(window, 'a', {
  get() {
    current++;
    console.log(current);
    return current;
  }
});

console.log(window.a === 1 && window.a === 2 && window.a === 3); // true */
/* let person = {
    name:'',
    age:0,
    sima:{
        ss:11
    }
}
function defineProperty(obj,key,val){
    if(typeof val==='object'){
        observer(val)
    }
    Object.defineProperty(obj,key,{
        get(){
            console.log(`访问了${key}属性`)
            return val
        },
        set(newVal){
            console.log(`${key}属性的值被修改成了${newVal}`)
        }
    })
}
function observer(obj){
    if(typeof obj!='object'||obj==null){
        return;
    }
    Object.keys(obj).forEach(key=>{
        defineProperty(obj,key,obj[key])
    })
}
observer(person);
person.sima */
/* var removeKdigits = function (num, k) {
    const stack = []

    for (let i = 0; i < num.length; i++) {
        const c = num[i]
        while (k > 0 && stack.length && stack[stack.length - 1] > c) {
            stack.pop()
            k--
        }
        if (c != '0' || stack.length != 0) {
            stack.push(c)
        }

    console.log(`第${i}次执行结束`,stack)
    }
    while (k > 0) {
        stack.pop()
        k--
    }
    return stack.length == 0 ? "0" : stack.join('');
}
removeKdigits("5632219",3) */

/* var n =71
for(var i=2;i<=n/2;i++){
    if(n%i===0){
        break
    }
}
if(i<=n/2){
    console.log('是')
}else{
    console.log('不是')
} */
/* var b = 100
function test2(a){
    console.log(b)
    var b=a
    console.log(b)
}
test2('ss') */
// console.log(a)
/* var obj={
    'name':'为民',
    age:10,
    simale:[[12,33],['sd']]
}
var obj2={}
for(var i in obj){
    obj2[i]=obj[i]
}
obj2.name=111 */
/* var arr1 =new Array(10,22)
console.log(arr1)
for(var i in arr1){
    console.log(arr1[i])
} */
/* 冒泡排序 */
/* var shuzu=[5,7,5,6,3,5]
var temp 
for(var i=0;i<shuzu.length-1;i++){
    for(var k=0;k<shuzu.length-i;k++)
        if(shuzu[k]<shuzu[k-1]){
            temp=shuzu[k-1]
            shuzu[k-1]=shuzu[k]
            shuzu[k]=temp
        }
}
console.log(shuzu) */
/* 选择排序 */
/* var shuzu = [5, 7, 5, 6, 3, 5, 1, 1];
var temp;
for (var i = 0; i < shuzu.length - 1; i++) {
  var minIndex = i;
  for (var n = i + 1; n < shuzu.length; n++) {
    if (shuzu[n] < shuzu[minIndex]) {
      minIndex = n;
    }
  }
  if (minIndex != i) {
    temp = shuzu[i];
    shuzu[i] = shuzu[minIndex];
    shuzu[minIndex] = temp;
  }
}
console.log(shuzu);
 */
// var arr1=[45,44,88,66,22]
// res=arr.push(2)
// arr.length=arr.length-1
// aa=arr.splice(arr.length+1,0,'bvv')
/* arr.sort(function(a,b){
    return a-b
})
console.log(arr) */
// var arr1=[43,45,88,66,22]
// /* var arr2=[55]
// var arr3 =arr1.indexOf(45,22)
// console.log(arr1) */
// sds=arr1.map(function(item,index,arr){
//     return item*item
// })
// console.log(sds)
// var arr =[
//     {
//         age:18
//     },
//     {
//         age:16
//     },
//     {
//         age:15
//     }
// ]
// var arr2= arr.filter(function(item){
//     return item.age>16
// })
// // console.log(arr2)
// var arr = [1, 2, 3, 4, 5];
// arr2=arr.reduce(function (prev, item) {
//   return prev + item;
// }, 0);
// var str1='asdasdasdasdff'
// var obj={

// }
// for(var i=0;i<str1.length;i++){
//     var key =str1[i]
//     if(obj[key]){
//         obj[key] ++
//     }else{
//         obj[key] =1
//     }
// }
// console.log(obj)
// var str1='asdasdasdasdff'
// console.log(str1.substr(2))
// var arr1=['sadas','aa','sdas']
// arr2=arr1.filter(function(item){
//     return item.indexOf('s')>-1
// })
// console.log(arr2)
// function getRed(min,max){
//     if(min>max){
//         return
//     }
//     return Math.floor(Math.random()*(max-min))+min

// }
// var data3 = new Date()
// console.log(data3)
/* var currentDate = new Date();
var targetDate = new Date("2025/6/18");
time1=diffTime(currentDate, targetDate);
console.log(time1)
function diffTime(currentDate, targetDate) {
  var sub = Math.ceil((targetDate - currentDate) / 1000);

  var day = parseInt(sub / (60 * 60 * 24));
  var hours = parseInt((sub % (60 * 60 * 24)) / (60 * 60));
  var minutes = parseInt((sub % (60 * 60)) / 60);
  var seconds = sub % 60;
  var obj ={
      day:day,
      hours:hours,
      minutes:minutes,
      seconds:seconds
  }
  return obj
} */

// var datestr ="time is from 2029-01-01 12:20:20 to 2029-11-0112:20:20"
// //2029/01/01 -2029/11/01
// var reg = /\d{4}-\d{1,2}-\d{1,2}/
// var newdatestr =reg.exec(datestr)
// console.log(newdatestr)
// console.log(newdatestr[0].split("-").join("/"))
// data=[1,5,9,7,1,5,2]
// console.log(data.sort)
// var obj1 ={
//     name:"obj1",
//     getName:function(a,b,c){
//         console.log("getName1",this.name)
//         console.log("参数",a,b,c)
//     }
// }
// var obj2 ={
//     name:"obj2",
//     getName:function(a,b,c){
//         console.log("getName1",this.name)
//         console.log("参数",a,b,c)
//     }
// }
// // obj1.getName.call(obj2,1,2,3)
// // obj1.getName.apply(obj1,[1,2,3])
// var fun1 =obj1.getName.bind(obj2,1,2,3)
// fun1()
// var a =20
// var b =10
// var [b,a]= [a,b]
// console.log(a,b)
// var a = [1,2,3]
// var b = [4,5,6]
// var c = [...a,...b]
// console.log(c)
// var arr =[1,2,3]
// var test = (a,b,c)=>{
//     console.log(a,b,c)
// }
// test(...arr)
// var obj1= {
//     name:"ke",
//     age:100
// }
// var obj2= {
//     location:"sd"
// }
// var obj={
//     ...obj1,
//     ...obj2
// }
// console.log(obj)
//工厂函数
// function createObj(name){
//     var obj= {}
//     obj.name=name
//     obj.material=[]
//     return obj
// }
// var obj1=createObj('大山')
// console.log(obj1)
// function createObj(name){
//     this.name=name
//     this.material=[]
//     this.cook=function(){

//     }
// }
// var obj1=new createObj()
// console.log(obj1)
// class CreateObj{
//     //构造器函数
//     constructor(name){
//         this.name=name
//     }
//     say(){
//         console.log(this.name)
//     }
// }
// class Student extends CreateObj {
//     constructor(name,age){
//         super(name)
//         this.age=age
//     }
//     say(){
//         super.say()
//         console.log(this.name,'Nihao')
//     }
// }
// var obj = new Student("ssd")
// console.log(obj)
// function Person(name,age){
//     this.name=name
//     this.age=age
// }
// function Student(name,age,grade){
//     // Person.call(this,name,age)
//     Person.apply(this,[name,age])
//     this.grade=grade
// }
// var obj = new Student("ker",100,100)
// console.log(obj)

// 1.创建对象XHR newXMLHttpRequest()
// var xhr = new XMLHttpRequest()
// console.log(xhr)
// var q = new Promise(function () {});
// // pending执行中
// // fulfilled兑现承诺
// // reject 拒绝承诺
// q.then(function () {
//   //兑现承诺就会被执行
// }).catch(function () {
//   //拒绝承诺就会被执行
// });
// fetch("url").then((res)=>{
//     if(res.ok){
//         return res.json()
//     }
//     else{
//         //拒绝
//         return Promise.reject(
//             {
//                 status:res.status,
//                 statusText:res.statusText
//             }
//         )
//     }
// })
// fetch("url",{
//     method:"POST",
//     headers:{
//         "content-type":"application/x-www-form-urlencoded"
//     },
//     body="username=tiechui&password=123",
//     body=JSON.stringify({
//         username:"sas",
//         password:"23"
//     })
// }).then(res=res.json())
// .then(res=>{
//     console.log(res)
// })

// jsonp原理：动态创建script标签，src属性指向没有跨域限制
// 指向的是一个接口，接口的返回的格式一定是****()函数表达式
/* function test(obj){
    
}
mybtn.onclick = function(){
    var oscript = document.childElement("script")
    oscript.src="01.txt"
    document.body.appendChild(oscript)
    oscript.onload = function(){
        oscript.remove()
    }
} */
// let obj = {
//     name:'tiecui'
// }
// let name =Symbol()
// obj[name]="zhangyuc"
// console.log(obj[name])
// let name = Symbol()
// let age = Symbol()
// let obj ={
//     [name]:"sdsa",
//     [age]:100
// }
// let keys = {
//     name : Symbol('name'),
//     age:Symbol("age")
// }
// let obj={
//     [keys.name]:"sds",
//     [keys.age]:123,
// }
// console.log(obj)
// const video = Symbol()
// const audio = Symbol()
// const image = Symbol()
// function play(type) {
//   switch (type) {
//     case video:
//       console.log("sp2");
//       break;
//     case audio:
//       console.log("sp1");
//       break;
//     case image:
//       console.log("sp3");
//       break;
//   }
// }
// play(audio)
// [Symbol.iterator](){
//     let index = 0
//     return{
//         next:()=>{
//             return{value:list[index++],done:index===(this.list.length)?true:false}
//         }
//     }
// }
// let s1 =new Set([1,2,3,6,5,5,5,5])
// console.log([...s1])
// let s1 =new Set()
// s1.add(2)
// s1.add(2)
// console.log(s1.size)
// for(let i of s1.entries()){
//     console.log(i)

// }
// let list = ["a","a",22,33,33,[1,2],[1,2],{name:'zyc'},{name:'zyc'}]
// let s1 = new Set(list)
// function uni(arr){
//     let res = new Set()
//     return arr.filter(item=>{
//         let id = JSON.stringify(item)
//         if(res.has(id)){
//             return false
//         }else{
//             res.add(id)
//             return true
//         }
//     })
// }
// console.log(uni(list))
// let obj ={}
// Object.defineProperty(obj,"data",{
//     get(){
//         console.log("get")
//     },
//     set(value){
//         console.log("set",value)
//     }
// })
// console.log(obj.data)
// let obj = {};
// let proxy = new Proxy(obj, {
//   get(target,key) {
//     // 判断如果是方法，改变this指向
//     console.log("get");
//     let value =target[key]
//     if(value instanceof Function){
//         //call apply bind 只能选bind 因为bind 不执行
//         return value.bind(target)
//     }
//     return value
//   },
//   set(target, key, value) {
//     console.log("set", target, key, value);
//     target[key] = value;
//   },
//   has(){
//       return false
//   }
// });
// console.log((proxy.data = "11"));
// console.log(obj);
// Math.ceil
// let obj ={

// }
// Reflect.deleteProperty(obj,"name",{
//     value:"kerwin",
//     writable:false,
//     enumerable:false //可枚举
// })
// let str = "sadas"
// console.log(str.padStart(10,'x'))
// console.log(str.padEnd(10,'x'))
// function ajax(options){
//     const defaultOptions ={
//         methods:"get",
//         async:true
//     }
//     options = {...defaultOptions,...options}

// }
// ajax({
//     url:"/api",
//     methods:"post"
// })
// function timer(t){
//     return new Promise(resolve=>{
//         setTimeout(()=>{
//             resolve("data-"+t)
//         },t)

//     })
// }
// //异步生成器
// async function *gen(){
//     yield  timer(1000)
//     yield  timer(2000)
//     yield  timer(3000)
// }
// async function test(){
//     let g= gen()
//     let arr =[g.next(),g.next(),g.next()]
//     for await(let item of arr){
//         console.log(item)
//     }
// }
// test()
// let arr=[["name","sds"],["ye0","sda"]]
// arr1=Object.fromEntries(arr)
// console.log(arr1)
// let m =new Map()
// m.set("name",'tiechui')
// m.set("age",100)
// arr1=Object.fromEntries(m)
// console.log(arr1)
// let str ="name=xiaoming&age=18"
// let searchParams = new URLSearchParams(str)
// arr1=Object.fromEntries(searchParams)
// console.log(searchParams)
// let obj ={
//     "A":["A1","A2","A3"],
//     "B":["B1","B2"]
// }
// let arr = Object.entries(obj)
// let mynewarr = arr.map(([key,value])=>
//    [key,value.length]
// )
// let lastarr = Object.fromEntries(mynewarr)
// console.log(lastarr)
// console.log(BigInt(2**53)+'')
// let ajax1 =function(){
//     return new Promise((resolve,reject)=>{
//         reject("沃尔玛")
//     })
// }
// let ajax2 =function(){
//     return new Promise((resolve,reject)=>{
//         resolve("华润万家")
//     })
// }
// let ajax3 =function(){
//     return new Promise((resolve,reject)=>{
//         resolve("盒马")
//     })
// }
// Promise.any([ajax1(),ajax2(),ajax3()]).then(res=>{
//     console.log(res)
// }).catch(err=>{
//     console.log(err)
// })
// let obj = {
//   name: "sda",
// };
// let s1 = new Set();
// s1.add(obj); //只是存了obj得一个引用
// s1.add("aass");
// console.log(s1.has(obj))
// obj = null;
// console.log(s1.has(obj)) //此时已经指向空了 obj此时没人能管他了，这种set结构多了 还在s1中引用，
// // 垃圾回收机制不执行就会造成内存泄漏
// for(let i  of s1){
//     console.log(i) //可以访问到
// }
// let obj = {
//     name: "sda",
//   };
//   let s1 = new WeakSet(); //要求只能1.只能是复杂类型
//   s1.add(obj); //
//   obj = null;
//   console.log(s1) //obj赋值为空 s1 里面没东西，Weak特性，引用obj  不会进行计数 不会加1
//   //如果obj赋值为null  垃圾回收机制直接执行
//   //2.weak 不存在引用计数加1
//   for(let i of s1){
//     console.log(i)
//   }
//   //3.不能使用for循环了，size属性也失效，因为里面数据是不确定得
// let obj = {
//   name: "sda",
// };
// let m1 = new WeakMap()
// m1.set(obj,"111")
// console.log(m1)
// obj=null
// // console.log(m1) //WeakMap不会计算引用 特性和weakset一样
// class Cache{


//     static #count = 0  //只能Cache.count
//     static getCount(){
//         return this.#count
//     }
//     static obj = new Map()
//     // 静态代码块，
//     static{
//         this.obj.set("name","sds")
//         console.log(this.obj)
        
//     }
    
//     #obj={   

//     }
//     //变为私有属性
//     get(key){
//         return this.#obj[key]
//     }
//     set(key,value){
//         this.#obj[key]=value
//     }
//     #prstore(){

//     }
//     hasObj(){
//         //in 判断一个属性是不是某个对象的私有属性
//         return #obj in this
//         // this.#obj拿到的是内容
//     }
// }
// let obj= new Cache()
// obj.set("name","sdasd")
// console.log(Cache.getCount())
// let arr = ["Sadasd","EQWEQW","qweqw"]
// console.log(arr[arr.length-1])
// console.log(arr.at(-2.0))
// d既能拿到开始索引又能拿到结束索引 
// let str ="今天是2022-11-10"
// let reg =/(?<year>[0-9]{4})-(?<month>[0-9]{2})-(?<day>[0-9]{2})/d
// let res =reg.exec(str)
// console.log(res)
// let arr = [11,55,22,1,1]
// //找到第一个元素
// let res = arr.find(value=>{
//     return value>13
// })
// // 找到第一个索引值
// let res1 = arr.findIndex(value=>{
//     return value>13
// })
// // 从后面找
// let res2 = arr.findLast(value=>{
//     return value>13
// })
// // 返回索引值
// let res3 = arr.findLastIndex(value=>{
//     return value>13
// })
// console.log(res3)
function getData(){
    try{
        
    }catch{
        throw new Error("传入的参数不符合规则",{cause:{
            a:1,
            b:2,
            c:3
        }})
    }
}
try{
    getData()
}catch(err){
    console.log(err,err,cause)
}
