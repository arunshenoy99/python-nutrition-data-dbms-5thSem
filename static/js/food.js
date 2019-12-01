var nutritionTable = document.querySelector("#nutrition-table")
const nameInput = document.querySelector('#name-input')
const nameButton = document.querySelector("#name-button")
nameButton.addEventListener('click',function(){
    nameInput.style.backgroundColor="white";
    nutritionTable.style.visibility="visible"
    const name= nameInput.value
    if (name === ""){
        nameInput.style.backgroundColor = "#F87B61";
        return;
    }
    const url = "http://localhost:3000/food?name="+name
    nutritionTable.innerHTML = "LOADING....."
    window.scrollBy(0,300);
    fetch(url)
    .then(data=>{nutritionTable.innerHTML = "<tr><th>FID</th><th>NAME</th><th>SERVING SIZE(g)</th><th>CALORIES(kcal)</th></tr>"
    return data.json()})
    .then(res=>{
        res.forEach((e)=>{
            nutritionTable.innerHTML=nutritionTable.innerHTML+"<tr><td>"+e.ID+"</td>"+"<td>"+e.name+"</td>"+"<td>"+e.serving_size+"</td>"+"<td>"+e.calories+"</td></tr>"
        })
        window.scrollBy(0,500)
    })
    .catch(error=>{console.log(error)})
})



    
