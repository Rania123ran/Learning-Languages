let number , rand , cnt ;
rand = Math.floor(Math.random()*10+1);
cnt = 5;
document.getElementById("btn").onclick=function(){
    number = document.getElementById("input").value;
    if(number >10 || number <1){
        alert("un nombre entre 1 et 10 !!")}
    cnt -- ;
    if(number > rand){
        alert("Plus grand , il vous reste "+cnt+" tentatives.");
    }
    else if(number < rand){
        alert("Plus petit , il vous reste "+cnt+" tentatives.");}
    else {
        alert("Bravo vous avez pris "+(5-cnt)+ " tentatives");
    }
    if(cnt == 0){
        alert("vous avez depasser le nombre de tentative");
    }
 }
