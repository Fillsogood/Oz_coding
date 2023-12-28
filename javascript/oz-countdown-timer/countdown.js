setInterval(function(){
    const days = document.getElementById("day")
    const hours =document.getElementById("hour")
    const mins = document.getElementById("min")
    const secs =document.getElementById("sec")

    const now = new Date()

    let day = now.getDate()
    let hour = now.getHours()
    let min =now.getMinutes()
    let sec =now.getSeconds()

    days.textContent = `${31-day}일`
    hours.textContent = `${23-hour}시`
    mins.textContent = `${59-min}분`
    secs.textContent = `${60-sec}초`

},1000)