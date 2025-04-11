// assets/script.js

// When the DOM content is fully loaded, initialize the page behaviors.
document.addEventListener('DOMContentLoaded', function () {
    console.log("Custom dashboard script loaded!");

    // Create a notification banner for displaying temporary messages.
    createNotificationElement();

    // Attach click event listeners to the metric buttons.
    attachMetricButtonListeners();

    // Set up additional UI interactivity (optional enhancements).
    setupUIEffects();
});

/////////////////////////////
// Utility Functions
/////////////////////////////

/**
 * Creates a hidden notification element that can be used to display messages.
 */
function createNotificationElement() {
    if (!document.getElementById("notification-banner")) {
        var notificationBanner = document.createElement("div");
        notificationBanner.id = "notification-banner";
        // Styling the notification banner
        notificationBanner.style.position = "fixed";
        notificationBanner.style.top = "20px";
        notificationBanner.style.right = "20px";
        notificationBanner.style.backgroundColor = "rgba(0, 0, 0, 0.7)";
        notificationBanner.style.color = "#fff";
        notificationBanner.style.padding = "10px 20px";
        notificationBanner.style.borderRadius = "4px";
        notificationBanner.style.boxShadow = "0 2px 10px rgba(0, 0, 0, 0.5)";
        notificationBanner.style.zIndex = "1000";
        notificationBanner.style.display = "none"; // Hidden by default
        document.body.appendChild(notificationBanner);
    }
}

/**
 * Displays a notification message for a specified duration.
 * @param {string} message - The message to display.
 * @param {number} duration - Duration in milliseconds for which the message is visible.
 */
function showNotification(message, duration) {
    var notificationBanner = document.getElementById("notification-banner");
    if (notificationBanner) {
        notificationBanner.textContent = message;
        notificationBanner.style.display = "block";
        notificationBanner.style.opacity = "1";
        // Automatically fade out the message after the given duration (default is 2000ms)
        setTimeout(function() {
            var fadeEffect = setInterval(function () {
                if (!notificationBanner.style.opacity) {
                    notificationBanner.style.opacity = "1";
                }
                // Gradually reduce opacity to create a fade effect.
                if (parseFloat(notificationBanner.style.opacity) > 0) {
                    notificationBanner.style.opacity = parseFloat(notificationBanner.style.opacity) - 0.1;
                } else {
                    clearInterval(fadeEffect);
                    notificationBanner.style.display = "none";
                }
            }, 50);
        }, duration || 2000);
    }
}

/**
 * Attaches event listeners to the metric toggle buttons ("Show RAM" and "Show CPU").
 * When clicked, they trigger a notification and a small animation.
 */
function attachMetricButtonListeners() {
    var showRamButton = document.getElementById("show-ram");
    var showCpuButton = document.getElementById("show-cpu");

    if (showRamButton) {
        showRamButton.addEventListener('click', function () {
            console.log("Show RAM button clicked.");
            showNotification("Switching to RAM monitoring", 2000);
            animateButtonClick(showRamButton);
        });
    }

    if (showCpuButton) {
        showCpuButton.addEventListener('click', function () {
            console.log("Show CPU button clicked.");
            showNotification("Switching to CPU monitoring", 2000);
            animateButtonClick(showCpuButton);
        });
    }
}

/**
 * Performs a simple scale animation on a button to provide visual feedback.
 * @param {HTMLElement} buttonElement - The button element to animate.
 */
function animateButtonClick(buttonElement) {
    if (!buttonElement) return;
    // Start the animation with a quick scaling effect.
    buttonElement.style.transition = "transform 0.1s ease";
    buttonElement.style.transform = "scale(0.95)";
    setTimeout(function () {
        buttonElement.style.transform = "scale(1)";
    }, 100);
}

/**
 * Sets up additional UI effects to enhance the user experience.
 * This can be expanded to include more interactive behaviors.
 */
function setupUIEffects() {
    // Example: Adding a dynamic hover effect to the header
    var header = document.querySelector('header');
    if (header) {
        header.addEventListener('mouseover', function () {
            header.style.boxShadow = "0 4px 15px rgba(0, 0, 0, 0.3)";
        });
        header.addEventListener('mouseout', function () {
            header.style.boxShadow = "none";
        });
    }

    // Additional optional UI effects or event listeners can be added here.
    // For instance, monitoring window resizing or integrating other interactive elements.
}
