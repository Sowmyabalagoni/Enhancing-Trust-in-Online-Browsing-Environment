
let clicks=0
let scroll=0
let redirects=0

document.addEventListener("click",()=>{
clicks++
})

window.addEventListener("scroll",()=>{
scroll+=window.scrollY
})

window.addEventListener("beforeunload",()=>{
redirects++
})

setInterval(()=>{

fetch("http://127.0.0.1:5000/collect",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
click_interval:clicks,
scroll_amount:scroll,
redirect_count:redirects
})

})

clicks=0
scroll=0

},1000)
