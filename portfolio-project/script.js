document.getElementById("btn").addEventListener("click", function () {
  const message = document.getElementById("message");

  if (message.classList.contains("hidden")) {
    message.classList.remove("hidden");
    this.textContent = "Hide Project Details";
  } else {
    message.classList.add("hidden");
    this.textContent = "View Project Details";
  }
});
