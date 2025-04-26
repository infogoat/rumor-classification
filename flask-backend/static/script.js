document.addEventListener("DOMContentLoaded", function () {
  const inputField = document.getElementById("hero-field");
  const checkButton = document.getElementById("checkButton");
  const resultText = document.getElementById("result");

  checkButton.addEventListener("click", async function () {
    const inputValue = inputField.value.trim();

    // Validate input: not empty and at least 3 words
    if (inputValue === "") {
      alert("Please enter a rumor headline.");
      return;
    }

    if (inputValue.split(/\s+/).length < 3) {
      alert("Please enter at least 3 words.");
      return;
    }

    checkButton.disabled = true;
    checkButton.textContent = "Checking...";

    try {
      const response = await fetch("/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ headline: inputValue }),
      });

      if (!response.ok) {
        throw new Error("Failed to get prediction");
      }

      const data = await response.json();

      //display prediction
      resultText.textContent = `Predicted Stance: ${data.result.label} (Confidence: ${(data.result.score * 100).toFixed(2)}%)`;
      resultText.classList.remove("hidden", "text-red-400");
      resultText.classList.add("text-green-400");

    } catch (error) {
      resultText.textContent = "Something went wrong while fetching the prediction.";
      resultText.classList.remove("hidden", "text-green-400");
      resultText.classList.add("text-red-400");
    } finally {
      checkButton.disabled = false;
      checkButton.textContent = "Check";
    }
  });

  // Handle signup form if it exists
  const signupForm = document.getElementById("signupForm");
  if (signupForm) {
    signupForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const password = document.getElementById("password").value;
      const confirmPassword = document.getElementById("confirm-password").value;
      const formMessage = document.getElementById("formMessage");

      if (password !== confirmPassword) {
        formMessage.textContent = "Passwords do not match!";
        formMessage.classList.remove("text-green-600");
        formMessage.classList.add("text-red-600");
        return;
      }

      // Here you would normally send the data to your backend
      formMessage.textContent = "Account created successfully!";
      formMessage.classList.remove("text-red-600");
      formMessage.classList.add("text-green-600");
      signupForm.reset();
    });
  }

  // Handle opinion form if it exists
  const opinionForm = document.getElementById("opinionForm");
  if (opinionForm) {
    opinionForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const name = document.getElementById("name").value.trim();
      const email = document.getElementById("email").value.trim();
      const message = document.getElementById("message").value.trim();

      if (!name || !email || !message) {
        alert("Please fill out all fields.");
        return;
      }

      alert(`Thank you, ${name}! Your opinion has been recorded.`);
      opinionForm.reset();
    });
  }

  // Handle FAQ toggles
  const toggleAnswer = (faqId) => {
    const answer = document.getElementById(faqId);
    if (answer) {
      answer.classList.toggle("hidden");
    }
  };

  // Expose toggleAnswer to global scope for onclick handlers
  window.toggleAnswer = toggleAnswer;
});

