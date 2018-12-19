var selectedStudent = {};
var selectedElements = [];

//remove student/students from group
function moveL() {
  //group students in form input
  var students = document.getElementById('id_students');
  var list = students.value.split(',');
  //groupless student list
  var noGroupStudentList = document.getElementById('noGroupStudentList');
  //if only one student is selected
  //else if selected multiple students at the same time
  if(selectedStudent.baseURI){
    //remove style from selected student
    selectedStudent.style = "";
    //remove from group's student list and add to groupless students
    selectedStudent.parentNode.removeChild(selectedStudent);
    noGroupStudentList.appendChild(selectedStudent);
    var realItems = [];
    //remove student from form's input value
    list.forEach(function (item) {
      if(selectedStudent.innerText != item){
        realItems.push(item);
      }
    });
    //create string from list
    students.value = realItems.join();
    selectedStudent = {};
  }
  else if(selectedElements.length > 0){
    selectedElements.forEach(function (elem) {
      //remove style from selected student
      elem.style = "";
      //remove from group's student list and add to groupless students
      elem.parentNode.removeChild(elem);
      noGroupStudentList.appendChild(elem);
      var realItems = [];
      //remove student from form's input value
      list.forEach(function (item) {
        if(elem.innerText != item){
          realItems.push(item);
        }
      });
      //create string from list
      students.value = realItems.join();
    });
    selectedElements = [];
  }
};

//add student/students to group
function moveR() {
  //group students in form input
  var students = document.getElementById('id_students');
  var list = students.value.split(',');
  //group's student list
  var studentList = document.getElementById('studentList');
  //if only one student selected
  //else if multiple students selected
  if(selectedStudent.baseURI){
    //remove style
    selectedStudent.style = "";
    //remove student from groupless students and add to group's students
    selectedStudent.parentNode.removeChild(selectedStudent);
    studentList.appendChild(selectedStudent);
    //add student to form input
    students.value = students.value + ',' + selectedStudent.innerText;
    selectedStudent = {};
  }
  else if(selectedElements.length > 0){
    selectedElements.forEach(function (elem) {
      //remove style
      elem.style = "";
      //remove student from groupless students and add to group's students
      elem.parentNode.removeChild(elem);
      studentList.appendChild(elem);
      //add student to form input
      students.value = students.value + ',' + elem.innerText;

    });
    selectedElements = [];
  }
};

//remove or add student/students to group by doubleclick
function moveStudentDoubleClick(elementId, value) {
  //get dblclicked element with id
  var element = document.getElementById(elementId);
  //group students in form input
  var students = document.getElementById('id_students');
  var list = students.value.split(',');
  //clear student's style
  element.style = "";
  //groupless student list and group's student list
  var noGroupStudentList = document.getElementById('noGroupStudentList');
  var studentList = document.getElementById('studentList');
  //if student is in group's student list
  //else if student is in groupless student list
  if(element.parentNode == studentList){
    element.parentNode.removeChild(element);
    var realItems = [];
    //remove student from form's input value
    list.forEach(function (item) {
      if(element.innerText.trim() != item){
        realItems.push(item);
      }
    });
    //add to groupless student list
    students.value = realItems.join();
    noGroupStudentList.appendChild(element);
  }
  else if(element.parentNode == noGroupStudentList){
    //remove from groupless student list and add to group's student list
    element.parentNode.removeChild(element);
    studentList.appendChild(element);
    //add student to form's input value
    students.value = students.value + ',' + element.innerText;
  }
}

//if student is clicked, paint div blue
function paintDiv(event, elementId){
  var element = document.getElementById(elementId);
  //if ctrl is pressed, add to student to selected student list
  //else clicked student is selected student
  if(event.ctrlKey){
    //clear selected student
    selectedStudent = {};
    selectedElements.push(element);
  }
  else {
    //clear previously selected student's style
    selectedStudent.style = "";
    selectedStudent = element;
    //clear selected student list's style's
    selectedElements.forEach(function (item) {
      item.style = "";
    });
    //clear selected student list
    selectedElements = [];
  }
  element.style = 'background-color: blue';
};
