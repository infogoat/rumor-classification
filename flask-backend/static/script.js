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
});
