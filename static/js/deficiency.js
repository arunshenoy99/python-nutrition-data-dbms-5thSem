var nutritionTable = document.querySelector("#nutrition-table")
const nameInput = document.querySelector('#name-input')
const nameButton = document.querySelector("#name-button")
const def = document.querySelector("#def")
nameButton.addEventListener('click',function(){
    nameInput.style.backgroundColor="white";
    nutritionTable.style.visibility="visible"
    const name= nameInput.value
    if (name === ""){
        nameInput.style.backgroundColor = "#F87B61";
        return;
    }
    const url = "http://localhost:3000/deficiency?name="+name
    nutritionTable.innerHTML = "LOADING....."
    fetch(url)
    .then(data=>{
    return data.json()})
    .then(res=>{
        if(typeof res.protein != 'undefined'){
            def.innerHTML = "Your deficiency is in protein some foods you can take are"
            nutritionTable.innerHTML = "<tr><th>NAME</th><th>PROTEIN(g)</th>"
            res.forEach((e)=>{
                nutritionTable.innerHTML=nutritionTable.innerHTML+"<tr><td>"+e.name+"</td>"+"<td>"
            })
        }
        else{
            var keys = Object.keys(res[0])
            def.innerHTML = "Your deficiency is vitamin "+keys[0]+" some foods you can take are"
            nutritionTable.innerHTML = "<tr><th>NAME</th>"+"<th>"+keys[0]+"(mg)</th></tr>"
            res.forEach((e)=>{
                nutritionTable.innerHTML=nutritionTable.innerHTML+"<tr><td>"+e.name+"</td>"+"<td>"+e[keys[0]]+"</td></tr>"
            })
        }
        window.scrollBy(0,500)
    })
    .catch(error=>{console.log(error)})
})



    
