addTodo = function() {
  myLi = document.createElement("li");

  newIn = document.createElement("input");
  newIn.type = "checkbox";
  inputcontents = document.querySelector("#input");
  licontents = document.createTextNode(inputcontents.value);
  inputcontents.appendChild(licontents);
  newIn.appendChild(inputcontents);
  myUl.appendChild(myLi);
  myLi.appendChild(newIn);
  document.body.appendChild(myUl);

}
