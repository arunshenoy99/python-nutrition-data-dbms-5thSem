var nutritionTable = document.querySelector("#nutrition-table")
const nameInput = document.querySelector('#name-input')
const nameButton = document.querySelector("#name-button")
nameButton.addEventListener('click',function(){
    nameInput.style.backgroundColor="white";
    nutritionTable.style.visibility="visible"
    nutritionTable.innerHTML = "<tr><th>NAME</th><th>TOTAL FAT(g)</th><th>SATURATED FAT</th></tr>"
    const name= nameInput.value
    if (name === ""){
        nameInput.style.backgroundColor = "#F87B61";
        return;
    }
    const nameRes = split(name,"/")
    const url = "http://localhost:3000/food-fat?name="+name
    nutritionTable.innerHTML = "LOADING....."
    fetch(url)
    .then(data=>{return data.json()})
    .then(res=>{
        res.forEach((e)=>{
            nutritionTable.innerHTML=nutritionTable.innerHTML+"<tr><td>"+e.name+"</td>"+"<td>"+e.total_fat+"</td>"+"<td>"+e.saturated_fat+"</td></tr>"
        })
    })
    .catch(error=>{console.log(error)})
})



    
