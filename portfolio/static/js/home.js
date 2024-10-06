function showSkills(category, button) {
    // Hide all skill cards
    document.querySelectorAll('.skill-cards').forEach(function (element) {
        element.style.display = 'none';
    });
    // Show the selected category
    document.getElementById(category).style.display = 'flex';

    // Remove active class from all buttons
    document.querySelectorAll('.btn').forEach(function (btn) {
        btn.classList.remove('active-btn');
    });

}

// Auto-click the "Programming Languages" button on page load
window.onload = function () {
    showSkills('programming'); // Show programming skills by default
};

const readMoreBtn = document.querySelector('.read-more-btn');
const aboutText = document.querySelector('.about-text');

readMoreBtn.addEventListener('click', () => {
  aboutText.classList.toggle('expanded'); // Toggle a class to expand the text
  if (aboutText.classList.contains('expanded')) {
    aboutText.style.display = 'block';
    aboutText.style.maxHeight = 'none'; /* Remove line clamp */
    readMoreBtn.textContent = 'Read Less';
  } else {
    aboutText.style.display = '-webkit-box';
    aboutText.style.maxHeight = '11em'; /* Restore line clamp */
    readMoreBtn.textContent = 'Read More';
  }
});

document.addEventListener("DOMContentLoaded", function () {
    const projectCards = document.querySelectorAll(".container-fixed-height");
    const loadMoreBtn = document.getElementById("loadMoreBtn");
    const collapseBtn = document.getElementById("collapseBtn");
    let cardsToShow = 3; // Initial number of cards to show

    // Show the first 3 cards
    projectCards.forEach((card, index) => {
      if (index < cardsToShow) {
        card.classList.add("visible");
      }
    });

    // Load more functionality
    loadMoreBtn.addEventListener("click", function () {
      console.log("load more button clicked")
      cardsToShow += 2; // Load 3 more cards on each click

      projectCards.forEach((card, index) => {
        if (index < cardsToShow) {
          card.classList.add("visible");
        }
      });

      // Show collapse button and hide load more if all cards are visible
      if (cardsToShow >= projectCards.length) {
        loadMoreBtn.style.display = "none";
        collapseBtn.style.display = "block";
      }
    });

    // Collapse functionality
    collapseBtn.addEventListener("click", function () {
      cardsToShow = 3; // Reset number of visible cards to 3
      projectCards.forEach((card, index) => {
        if (index >= cardsToShow) {
          card.classList.remove("visible");
        }
      });
      loadMoreBtn.style.display = "block"; // Show load more button again
      collapseBtn.style.display = "none";  // Hide collapse button
    });
});
