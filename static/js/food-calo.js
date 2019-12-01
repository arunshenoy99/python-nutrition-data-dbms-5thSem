const caloButton = document.querySelector("#calo-button")
const caloInput = document.querySelector("#calo-input")
var nutritionTable = document.querySelector("#nutrition-table")
caloButton.addEventListener('click',function(){
    caloInput.style.backgroundColor="white";
    nutritionTable.style.visibility="visible"
    const calories= caloInput.value
    if (calories === null){
        caloInput.style.backgroundColor = "#F87B61";
        return;
    }
    const url = "http://localhost:3000/calories?calories="+calories
    nutritionTable.innerHTML = "LOADING....."
    window.scrollBy(0,300);
    fetch(url)
    .then(data=>{nutritionTable.innerHTML = "<tr><th>FID</th><th>NAME</th><th>SERVING SIZE(g)</th><th>CALORIES(kcal)</th></tr>"
    return data.json()})
    .then(res=>{
        res.forEach((e)=>{
            nutritionTable.innerHTML=nutritionTable.innerHTML+"<tr><td>"+e.id+"</td>"+"<td>"+e.name+"</id>"+"<td>"+e.serving_size+"</td>"+"<td>"+e.calories+"</td></tr>"
        })
        window.scrollBy(0,500)
    })
    .catch(error=>{console.log(error)})
})
