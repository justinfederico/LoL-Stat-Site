var x = 0;

function dynamicButtons() {
    var string = "extended-match-container-" + x;
    document.getElementById("newButton").href = "#" + string;
    document.getElementById("newButton").id = "button-" + x;
    document.getElementById("new-extended-match-container").id = string;
    console.log(x);
    x++;
}