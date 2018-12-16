var selectedStudent = {};
var selectedElements = [];

function moveL() {
  var students = document.getElementById('id_students');
  var list = students.value.split(',');
  if(selectedStudent.baseURI){
    selectedStudent.style = "";
    selectedStudent.parentNode.removeChild(selectedStudent);
    var noGroupStudentList = document.getElementById('noGroupStudentList');
    noGroupStudentList.appendChild(selectedStudent);
    var realItems = [];
    list.forEach(function (item) {
      console.log(item);
      console.log(selectedStudent.innerText);
      if(selectedStudent.innerText != item){
        realItems.push(item);
      }
    });
    students.value = realItems.join();
    selectedStudent = {};
  }
  else if(selectedElements.length > 0){
    selectedElements.forEach(function (elem) {
      elem.style = "";
      elem.parentNode.removeChild(elem);
      var noGroupStudentList = document.getElementById('noGroupStudentList');
      noGroupStudentList.appendChild(elem);
      var realItems = [];
      list.forEach(function (item) {
        if(elem.innerText != item){
          realItems.push(item);
        }
      });
      students.value = realItems.join();
    });
    selectedElements = [];
  }
};

function moveR() {
  var students = document.getElementById('id_students');
  var list = students.value.split(',');
  if(selectedStudent.baseURI){
    selectedStudent.style = "";
    selectedStudent.parentNode.removeChild(selectedStudent);
    var studentList = document.getElementById('studentList');
    studentList.appendChild(selectedStudent);
    students.value = students.value + ',' + selectedStudent.innerText;
    selectedStudent = {};
  }
  else if(selectedElements.length > 0){
    selectedElements.forEach(function (elem) {
      elem.style = "";
      elem.parentNode.removeChild(elem);
      var studentList = document.getElementById('studentList');
      studentList.appendChild(elem);
      students.value = students.value + ',' + elem.innerText;

    });
    selectedElements = [];
  }
};

function clearModal() {
  selectedStudent.style = "";
  selectedElements.forEach(function (item) {
    item.style = "";
  })
  selectedStudent = {};
  selectedElements = [];
}

function moveDbl(elementId, value) {
  var element = document.getElementById(elementId);
  var students = document.getElementById('id_students');
  var list = students.value.split(',');
  element.style = "";
  var noGroupStudentList = document.getElementById('noGroupStudentList');
  var studentList = document.getElementById('studentList');
  if(element.parentNode == studentList){
    element.parentNode.removeChild(element);
    var realItems = [];
    list.forEach(function (item) {
      if(element.innerText.trim() != item){
        realItems.push(item);
      }
    });
    console.log(realItems);
    students.value = realItems.join();
    console.log(students);
    noGroupStudentList.appendChild(element);
  }
  else if(element.parentNode == noGroupStudentList){
    element.parentNode.removeChild(element);
    studentList.appendChild(element);
    students.value = students.value + ',' + element.innerText;
  }
}

function paintDiv(event, elementId){
  console.log('paintDiv');
  var element = document.getElementById(elementId);
  if(event.ctrlKey){
    selectedStudent = {};
    selectedElements.push(element);
  }
  else {
    selectedStudent.style = "";
    selectedStudent = element;
    selectedElements.forEach(function (item) {
      item.style = "";
    });
    selectedElements = [];
  }
  element.style = 'background-color: blue';
};