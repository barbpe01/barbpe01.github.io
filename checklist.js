addTodo = function {
  newLi = document.createElement("li");
  newIn = document.createElement("input");
  newIn.type="checkbox";
  contents = document.createTextNode(myPriority.value);
  newIn.appendChild(contents);
  document.body.appendChild(newIn);
  newIn.className= myPriority.value;
}
