
let speech = new SpeechSynthesisUtterance();
speech.lang = "en";


document.querySelector("#start").addEventListener("click", () => {
  speech.text = document.querySelector("#start").value;
  window.speechSynthesis.speak(speech);
});

