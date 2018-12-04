/*var form_options = {
    target: '#editGroupModal',
    success: function() {  }
}
$('#editGroupForm').ajaxForm(form_options);*/

const selectedSudentElements = document.querySelectorAll('.studentItem');
const noGroupStudentList = document.getElementById("noGroupStudentList");
var selectedStudent = {};
var selectedElements = [];

function moveL() {
  if(selectedStudent.baseURI){
    selectedStudent.style = "";
    selectedStudent.parentNode.removeChild(selectedStudent);
    var noGroupStudentList = document.getElementById("noGroupStudentList");
    noGroupStudentList.appendChild(selectedStudent);
    selectedStudent = {};
  }
  else if(selectedElements.length > 0){
    selectedElements.forEach(function (elem) {
      elem.style = "";
      elem.parentNode.removeChild(elem);
      var noGroupStudentList = document.getElementById("noGroupStudentList");
      noGroupStudentList.appendChild(elem);
    });
    selectedElements = [];
  }
};

function moveR() {
  if(selectedStudent.baseURI){
    selectedStudent.style = "";
    selectedStudent.parentNode.removeChild(selectedStudent);
    var studentList = document.getElementById("studentList");
    studentList.appendChild(selectedStudent);
    selectedStudent = {};
  }
  else if(selectedElements.length > 0){
    selectedElements.forEach(function (elem) {
      elem.style = "";
      elem.parentNode.removeChild(elem);
      var studentList = document.getElementById("studentList");
      studentList.appendChild(elem);
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
  element.style = "";
  var noGroupStudentList = document.getElementById("noGroupStudentList");
  var studentList = document.getElementById("studentList");
  if(element.parentNode == studentList){
    element.parentNode.removeChild(element);
    noGroupStudentList.appendChild(element);
  }
  else if(element.parentNode == noGroupStudentList){
    element.parentNode.removeChild(element);
    studentList.appendChild(element);
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