// map menu items into a NodeList
const menuElements = document.querySelectorAll('.menuItem');
// reference to the span element in the dropdown menu button
const chosenItem = document.getElementById("chosenItem");

menuElements.forEach(item => {
  item.addEventListener('click', e => switchChoice(e.target));
  // styling for the chosen menu item
  if (item.textContent === chosenItem.textContent) {
    item.style = "font-weight: bold;";
  };
});

// switches chosen menu item to the element passed as a parameter
switchChoice = (choice) => {
  // format menu items
  menuElements.forEach(e => {
    e.style = (e.textContent === choice.textContent) ? "font-weight: bold;" : "font-weight: normal;";
  });
  chosenItem.textContent = choice.textContent;
}

// placeholder function, will update once backend logic is functional
createGroups = () => {
  alert(`Chosen method: ${chosenItem.textContent}\nGroup size: ${document.getElementById("size").value}`);
}