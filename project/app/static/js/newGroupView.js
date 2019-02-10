

//add item to the list
function newItem() {
    let ul = document.getElementById("list");
    let li = document.createElement("li");

    li.appendChild(document.createTextNode("hei"));
    ul.appendChild(li);
}

//update selection
$(".list-group .list-group-item").click(function(e) {
    if ($(e.target).hasClass("active")) {
        $(e.target).removeClass("active");
    }
    else {
        $(e.target).addClass("active");
    }
});


//Detach elements to another list
$(".list-group .list-group-item").dblclick(function(e){
    let list1 = document.getElementById("list1");
    let list2 = document.getElementById("list2");

    if (this.parentNode === list1) {
        $(e.target).removeClass("active");
        list2.appendChild(this);
    }
    else if  (this.parentNode === list2) {
        $(e.target).removeClass("active");
        list1.appendChild(this);
    }
});

// Add selected items from list one to list two
$("#addButton").click(function(e) {
    let list = document.getElementById("list1");
    let list2 = document.getElementById("list2");
    let num = list.getElementsByTagName("li");
    for (let i=0; i <= num.length; i++) {
        if ($(num[i]).hasClass("active")) {
            $(num[i]).removeClass("active");
            list2.appendChild(num[i]);
        }
    }
});

// Remove selected items from list 2 and move them to list 1
$("#removeButton").click(function(e) {
    let list = document.getElementById("list1");
    let list2 = document.getElementById("list2");
    let num = list2.getElementsByTagName("li");
    for (let i=0; i <= num.length; i++) {
        if ($(num[i]).hasClass("active")) {
            $(num[i]).removeClass("active");
            list.appendChild(num[i]);
            i = 0;
        }
    }
});




