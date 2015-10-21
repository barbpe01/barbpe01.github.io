addTodo = function() {
  myUl = document.querySelector("#list");
  myLi = document.createElement("li");
  myPriority = document.querySelector("#priority");
  myLi.classList.add(myPriority.value);
  
  newIn = document.createElement("input");
  newIn.type = "checkbox";
  
  myBox = document.querySelector("#input");
  licontents = document.createTextNode(myBox.value);
  
  myLi.appendChild(licontents);
  myLi.appendChild(newIn);
  myUl.appendChild(myLi);
  document.body.appendChild("#list");


  document.getElementById("priority").className = "High";
  document.getElementById("priority").className = "Medium";
  document.getElementById("priority").className = "Low";
  
}


