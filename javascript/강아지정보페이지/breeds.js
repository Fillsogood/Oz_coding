const apiRandomDogs ="https://dog.ceo/api/breeds/image/random/42" 
const apiAllBreeds ="https://dog.ceo/api/breeds/list/all"
const request1 = new XMLHttpRequest()
const request2 = new XMLHttpRequest()

const header = document.getElementById("header")
const main = document.getElementById("main")
const input = document.getElementById("filter-text")
const button = document.getElementById("filter-button")
const select = document.getElementById("filter-select")
const more = document.getElementById("more")
const tothetop = document.getElementById("tothetop")
const reset =document.getElementById("reset")

const currentDogs = []

function displayDogs(item){
    const dogImagDiv =document.createElement("div")
    dogImagDiv.classList.add("flex-item")
    dogImagDiv.innerHTML = `
     <img src="${item}">
    `
    main.appendChild(dogImagDiv)
}


window.addEventListener("load",()=>{

    //강아지 사진 뿌리기
    request1.open("get",apiRandomDogs)
    request1.addEventListener("load",()=>{
        const response = JSON.parse(request1.response)
        response.message.forEach((item) => {
            currentDogs.push(item)
            displayDogs(item)
        })
    })
    request1.send()

    //셀렉트 견종 정보 뿌리기

    request2.open("get",apiAllBreeds)
    request2.addEventListener("load",()=>{
        const response =JSON.parse(request2.response)
        Object.keys(response.message).forEach((item)=>{
            const option =document.createElement("option")
            option.textContent = item
            option.value = item
            select.appendChild(option)
        })
    })
    request2.send()
})


button.addEventListener("click",()=>{
    main.innerHTML=""
    let filterdDogs = currentDogs.filter((item)=>{
        return item.indexOf(input.value) !== -1
    })

    input.value = ""

    filterdDogs.forEach((item) => {
        displayDogs(item)
    })
})

select.addEventListener("change",()=>{
    main.innerHTML=""
    let filterdDogs = currentDogs.filter((item)=>{
        return item.indexOf(select.value) !== -1
    })

    filterdDogs.forEach((item) => {
        displayDogs(item)
    })
})

more.addEventListener("click",()=>{
    request1.open("get",apiRandomDogs)
    request1.addEventListener("load",()=>{
        const response = JSON.parse(request1.response)
        response.message.forEach((item) => {
            currentDogs.push(item)
            displayDogs(item)
        })
    })
    request1.send()
})

tothetop.addEventListener("click",()=>{
    //주어진 위치로 스크롤을 이동한다.
    window.scrollTo({top: 0})

})

reset.addEventListener("click",()=>{
    main.innerHTML=""
    request2.open("get",apiRandomDogs)
    request2.addEventListener("load",()=>{
        const response = JSON.parse(request2.response)
        response.message.forEach((item) => {
            currentDogs.push(item)
            displayDogs(item)
        })
    })
    request2.send()
})