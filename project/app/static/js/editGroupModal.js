//remove student/students from group
function moveL() {
  //group students in form input
  var students = document.getElementById('id_students');
  //group's student list
  var studentList = document.getElementById('studentList');
  //groupless student list
  var studentsWithoutGroup = document.getElementById('noGroupStudentList');
  //get selected students' ids
  var selectedStudents = getSelectValues(studentList);
  //unselect selected students in form select as well
  selectedStudents.forEach(function (selectedStudent) {
    var theOption;
    for (var i = 0; i < students.options.length; i++){
      var option = students.options[i];
      if (option.value == selectedStudent.id){
        theOption = option.index;
      }
    }
    students.options[theOption].selected = false;
    studentsWithoutGroup.add(selectedStudent);
  });
};

//returns selected students' ids
function getSelectValues(select) {
  var result = [];
  var options = select.options;
  var opt;
  for (var i=0, iLen=options.length; i<iLen; i++) {
    opt = options[i];
    if (opt.selected) {
      result.push(opt);
    }
  }
  return result;
}

//add student/students to group
function moveR() {
  //group students in form input
  var students = document.getElementById('id_students');
  //group's student list
  var studentList = document.getElementById('studentList');
  //groupless student list
  var studentsWithoutGroup = document.getElementById('noGroupStudentList');
  //get selected students' ids
  var selectedStudents = getSelectValues(studentsWithoutGroup);
  //select selected students in form select as well
  selectedStudents.forEach(function (selectedStudent) {
    var theOption;
    for (var i = 0; i < students.options.length; i++){
      var option = students.options[i];
      if (option.value == selectedStudent.id){
        theOption = option.index;
      }
    }
    students.options[theOption].selected = true;
    studentList.add(selectedStudent);
  });
};

//remove or add student/students to group by doubleclick
function moveStudentDoubleClick(e, element) {
  //group students in form input
  var students = document.getElementById('id_students');
  //groupless student list and group's student list
  var noGroupStudentList = document.getElementById('noGroupStudentList');
  var studentList = document.getElementById('studentList');
  //if student is in group's student list
  //else if student is in groupless student list
  if(element.parentNode == studentList){
    element.parentNode.removeChild(element);
    //remove student from form's input value
    var theOption;
    for (var i = 0; i < students.options.length; i++){
      var option = students.options[i];
      if (option.value == e.target.id){
        theOption = option.index;
      }
    }
    students.options[theOption].selected = false;
    //add to groupless student list
    noGroupStudentList.appendChild(element);
  }
  else if(element.parentNode == noGroupStudentList){
    //remove from groupless student list and add to group's student list
    element.parentNode.removeChild(element);
    studentList.appendChild(element);
    //add student to form's input value
    var theOption;
    for (var i = 0; i < students.options.length; i++){
      var option = students.options[i];
      if (option.value == e.target.id){
        theOption = option.index;
      }
    }
    students.options[theOption].selected = true;
  }
}