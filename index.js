document.getElementById("navtoyourspace").onclick=function(){
    window.location.href="yourspace.html"
}
document.getElementById("navetogetinfo").onclick=function(){
    window.location.href="info.html"
}
document.addEventListener('DOMContentLoaded', function() {
    var text = "Welcome!";
    var index = 0;
    var intervalId = setInterval(function() {
      if (index < text.length) {
        document.querySelector('.typing-effect').textContent += text.charAt(index);
        index++;
      } else {
        clearInterval(intervalId);
      }
    }, 350); // Adjust the speed of typing here (milliseconds)
  });