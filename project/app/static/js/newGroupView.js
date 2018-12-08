

//add item to the list
function newItem() {
    var ul = document.getElementById("list");
    var li = document.createElement("li");

    li.appendChild(document.createTextNode("hei"));
    ul.appendChild(li);
}

//update selection
$(".list-group .list-group-item").click(function(e) {
 //   $(".list-group .list-group-item").removeClass("active");
    $(e.target).addClass("active");
});


//Detach elements to another list
$(".list-group .list-group-item").click(function(e){
    var list1 = document.getElementById("list1");
    var list2 = document.getElementById("list2");
    var selected = this.parentNode;

    if (selected.isEqualNode(list1)) {
        list2.appendChild(this);
    }

    alert(this.parentNode);
    alert(list1);
    if (this.parentElement === list2){
        list1.appendChild(this);
    }
});