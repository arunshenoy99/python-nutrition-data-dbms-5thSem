window.onload = function(){
    var nutritionTable = document.querySelector("#nutrition-table")
    const url = "http://localhost:3000/water"
    nutritionTable.innerHTML = "LOADING....."
    fetch(url)
    .then(data=>{return data.json()})
    .then(res=>{
        nutritionTable.style.visibility="visible"
        nutritionTable.innerHTML = "<tr><th>NAME</th><th>WATER(%)</th></tr>"
        res.forEach((e)=>{
            nutritionTable.innerHTML=nutritionTable.innerHTML+"<tr><td>"+e.name+"</td><td>"+e.water+"</td></tr>"
        })
    })
    .catch(error=>{console.log(error)})
}