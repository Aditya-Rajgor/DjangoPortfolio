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
    document.getElementById('default-skill-btn').click();
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