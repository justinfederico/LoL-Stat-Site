var x = 0;

function dynamicButtons() {
    var string1 = "extended-match-container-" + x;
    var string2 = "match-analysis-" + x;
    var string3 = "gold-and-kills-" + x;
    var string4 = "match-analysis-tab-" + x;
    var string5 = "gold-and-kills-tab-" + x;
    document.getElementById("newButton").href = "#" + string1;
    document.getElementById("newButton").id = "button-" + x;
    document.getElementById("new-extended-match-container").id = string1;

    let matchAnalysisTab = document.getElementById("new-match-analysis-tab-button");
    matchAnalysisTab.id = string4;
    matchAnalysisTab.setAttribute('data-bs-target', '#' + string2);
    document.getElementById("newMatchAnalysisTab").id = string2;

    let goldAndKillsTab = document.getElementById("new-gold-and-kills-tab-button");
    goldAndKillsTab.id = string5;
    goldAndKillsTab.setAttribute("data-bs-target", '#' + string3);
    document.getElementById("newGoldAndKillsTab").id = string3;
    x++;
}