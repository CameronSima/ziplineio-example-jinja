window.addEventListener("load", function () {
  const form = document
    .getElementById("mailing-list-form")
    .addEventListener("submit", async function (event) {
      event.preventDefault(); // Prevent default form submission
      const email = document.getElementById("email").value;
      const responseMessage = document.getElementById("response-message");

      try {
        const response = await fetch("/mailing_list/subscribe", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email: email }),
        });

        if (response.ok) {
          responseMessage.textContent = "Thank you for subscribing!";
          responseMessage.classList.remove("text-red-600");
          responseMessage.classList.add("text-indigo-800");

          // Clear the input field
          document.getElementById("email").value = "";
        } else {
          throw new Error("Failed to subscribe.");
        }
      } catch (error) {
        responseMessage.textContent = "There was an error. Please try again.";
        responseMessage.classList.remove("text-indigo-800");
        responseMessage.classList.add("text-red-600");
      }
    });
});
