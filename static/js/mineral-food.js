var nutritionTable = document.querySelector("#result-div")
const nameInput = document.querySelector('#name-input')
const nameButton = document.querySelector("#name-button")
const minInput = document.querySelector('#vit-input')
nameButton.addEventListener('click',function(){
    var url
    nameInput.style.backgroundColor="white";
    const name= nameInput.value
    if (name === ""){
        nameInput.style.backgroundColor = "#F87B61";
        return;
    }
    var requiredMin = minInput.value;
    if(requiredMin == ""){
        var requiredMinA = ['all']
    }
    var requiredMinA = requiredMin.split(',')
    url="http://localhost:3000/mineral?name="+name
    if(requiredMinA[0].toLowerCase()=="all"){
        url = url+"&all=1";
        requiredMinA = ['SODIUM','CALCIUM','IRON','POTASSIUM','CARB','WATER'];
    }
    else{
        requiredMinA.forEach((e)=>{
            url=url+"&"+e.toUpperCase()+"=1";
        })
    }
    nutritionTable.innerHTML = "LOADING....."
    window.scrollBy(0,300);
    fetch(url)
    .then(data=>{
        return data.json()})
    .then(res=>{
        nutritionTable.innerHTML = "SHOWING RESULTS"
        var names = res.name;
        var field = res.fields
        for(var i=0;i<names.length;i++)
        {
            nutritionTable.innerHTML = nutritionTable.innerHTML+"<div id='result-content'>"
            nutritionTable.innerHTML = nutritionTable.innerHTML+"<p>Name:"+names[i]+"</p>";
            for(var j=0;j<field[i].length;j++){
                nutritionTable.innerHTML = nutritionTable.innerHTML+"<p>"+requiredMinA[j]+":"+field[i][j]+"</p>";
            }
            nutritionTable.innerHTML = nutritionTable.innerHTML+"</div>"
        }
        window.scrollBy(0,500);
    })
    .catch(error=>{console.log(error)})
})



    
