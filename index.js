document.getElementById("navtoyourspace").onclick=function(){
    window.location.href="Page2.html"
}
document.getElementById("navetogetinfo").onclick=function(){
    window.location.href="about.html"
}
document.addEventListener('DOMContentLoaded', function() {
    var text = "We're Sign Sentry!";
    var index = 0;
    var intervalId = setInterval(function() {
      if (index < text.length) {
        document.querySelector('.typing-effect').textContent += text.charAt(index);
        index++;
      } else {
        clearInterval(intervalId);
      }
    }, 250); // Adjust the speed of typing here (milliseconds)
  });