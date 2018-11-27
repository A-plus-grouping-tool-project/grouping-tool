// map menu items into a NodeList
const menuElements = document.querySelectorAll(".menuItem");
// reference to the span element in the dropdown menu button
const chosenItem = document.getElementById("chosenItem");

menuElements.forEach(item => {
  item.addEventListener("click", e => switchChoice(e.target));
  // styling for the chosen menu item
  if (item.textContent === chosenItem.textContent) {
    item.style = "font-weight: bold;";
  }
});

// updates the minimum value of the maxSize input
updateMaxSize = () => {
  let minVal = parseInt(document.getElementById("minSize").value);
  let max = document.getElementById("maxSize");

  max.min = minVal === 1 ? 1 : minVal - 1;
  if (parseInt(max.value) < minVal) {
    max.value = minVal;
  }
};

// updates the value of the minSize input
updateMinSize = () => {
  let min = document.getElementById("minSize");
  let max = document.getElementById("maxSize");

  if (parseInt(max.value) < parseInt(min.value)) {
    min.value = max.value;
    if (parseInt(max.value) > 1) {
      max.min = max.min - 1;
    }
  }
};

// switches chosen menu item to the element passed as a parameter
switchChoice = choice => {
  // format menu items
  menuElements.forEach(e => {
    e.style =
      e.textContent === choice.textContent
        ? "font-weight: bold;"
        : "font-weight: normal;";
  });
  chosenItem.textContent = choice.textContent;
};

// placeholder function, will update once backend logic is functional
createGroups = () => {
  alert(`Chosen method: ${chosenItem.textContent}\nGroup size:\n  min: ${parseInt(
    document.getElementById("minSize").value)}\n  max: ${parseInt(
    document.getElementById("maxSize").value)}`
  );
};
