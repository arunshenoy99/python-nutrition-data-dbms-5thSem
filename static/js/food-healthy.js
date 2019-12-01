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
    const url = "http://localhost:3000/healthy?name="+name
    nutritionTable.innerHTML = "LOADING....."
    window.scrollBy(0,300);
    fetch(url)
    .then(data=>{ nutritionTable.innerHTML = "<tr><th>NAME</th><th>CALORIES</th><th>TOTAL_FAT</th><th>HEALTHY?</th></tr>" 
        return data.json()})
    .then(res=>{
        res.forEach((e)=>{
            nutritionTable.innerHTML=nutritionTable.innerHTML+"<tr><td>"+e.name+"</td><td>"+e.calories+"</td>"+"<td>"+e.total_fat+"</td>"+"<td>"+e.healthy+"</td></tr>"
        })
        window.scrollBy(0,500)
    })
    .catch(error=>{console.log(error)})
})



    
