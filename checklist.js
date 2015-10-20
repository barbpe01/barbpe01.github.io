addTodo = function() {
  myLi = document.createElement("li");

  newIn = document.createElement("input");
  newIn.type = "checkbox";
  inputcontents = document.querySelector("#input");
  licontents = document.createTextNode(inputcontents.value);
  inputcontents.appendChild(licontents);
  newIn.appendChild(inputcontents);
  list.appendChild(myLi);
  myLi.appendChild(newIn);
  document.body.appendChild("#list");

  document.querySelector("#priority");
  document.getElementById("priority").className = "High";
  document.getElementById("priority").className = "Medium";
  document.getElementById("priority").className = "Low";
}
