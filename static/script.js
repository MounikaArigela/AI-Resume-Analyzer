function toggleBox(id){

    let box = document.getElementById(id);

    if(box.style.display === "block"){

        box.style.display = "none";

    }else{

        box.style.display = "block";
    }
}