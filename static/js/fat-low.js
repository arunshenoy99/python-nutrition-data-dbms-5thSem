window.onload = function(){
    var nutritionTable = document.querySelector("#nutrition-table")
    const url = "http://localhost:3000/low-fat"
    fetch(url)
    .then(data=>{return data.json()})
    .then(res=>{
        nutritionTable.style.visibility="visible"
        nutritionTable.innerHTML = "<tr><th>FID</th><th>NAME</th><th>SERVING SIZE(g)</th><th>CALORIES(kcal)</th><th>TOTAL FAT(g)</th></tr>"
        res.forEach((e)=>{
            nutritionTable.innerHTML=nutritionTable.innerHTML+"<tr><td>"+e.id+"</td>"+"<td>"+e.name+"</id>"+"<td>"+e.serving_size+"</td>"+"<td>"+e.calories+"</td>"+"<td>"+e.total_fat+"</td></tr>"
        })
    })
    .catch(error=>{console.log(error)})
}