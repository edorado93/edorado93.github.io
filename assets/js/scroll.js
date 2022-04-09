var scrollBarProgress = function () {
    var body = document.body;
    var html = document.documentElement;
  
    var maxHeigth =  Math.max( body.scrollHeight, body.offsetHeight, 
        html.clientHeight, html.scrollHeight, html.offsetHeight );

    var progressBar = document.getElementsByClassName("progress-bar")[0];
    var scrollTop = document.documentElement.scrollTop;
  
    // Calculate width in percentage
    var width = (scrollTop / maxHeigth) * 100;

    if (width > 90)
    {
        width += 7;
    }

    width = width + "%";
  
    progressBar.style.width = width;
}

window.onload = function() {
    scrollBarProgress();
}

document.onscroll = function() {
    scrollBarProgress();
}

window.onresize = function() {
    scrollBarProgress();
}