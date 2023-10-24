const form = document.querySelector(".k123")
const inputemail = document.querySelector(".q1")
const l1 = document.querySelector("#l1")
//const form1=document.querySelector(".k1")


console.log(inputemail.value)
console.log(form)
console.log(l1)


form.addEventListener("submit", (e) => {
        e.preventDefault()
        const h2 = document.createElement("h5")
        h2.style.color = "black"
        h2.style.margin = "12px"
        h2.innerHTML = "You Are Subscribed!"
        form.appendChild(h2)
        console.log(23)
    
})




console.log(66767)
//form.addEventListener("")
