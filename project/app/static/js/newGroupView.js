

//add item to the list
function newItem() {
    var ul = document.getElementById("list");
    var li = document.createElement("li");

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
    var list1 = document.getElementById("list1");
    var list2 = document.getElementById("list2");

    if (this.parentNode === list1) {
        list2.appendChild(this);
    }
    else if  (this.parentNode === list2) {
        list1.appendChild(this);
    }
});

// TODO Make buttons work

