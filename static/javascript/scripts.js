document.addEventListener("DOMContentLoaded", function() {
    const popupOverlay = document.querySelector('.popup-overlay');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    const closeBtn = document.querySelector('.close-btn');
    const slidesContent = [
        {
            title: 'Welcome to Snapfolia',
            content: 'This is a popup reminder to help you navigate through our website. Use the navigation arrows to proceed.'
        },
        {
            title: 'Second Slide',
            content: 'This is the content for the second slide.'
        },
        {
            title: 'Third Slide',
            content: 'This is the content for the third slide.'
        }
        // Add more slides as needed
    ];

    let slideIndex = 0;

    // Show the popup when the page loads
    popupOverlay.style.display = 'block';

    // Function to close the popup
    function closePopup() {
        popupOverlay.style.display = 'none';
    }

    // Function to navigate to the previous slide
    function showPrevSlide() {
        slideIndex--;
        if (slideIndex < 0) {
            slideIndex = slidesContent.length - 1;
        }
        updatePopup();
    }

    // Function to navigate to the next slide
    function showNextSlide() {
        slideIndex++;
        if (slideIndex >= slidesContent.length) {
            slideIndex = 0;
        }
        updatePopup();
    }

    // Function to update the popup with the current slide content
    function updatePopup() {
        const currentSlide = slidesContent[slideIndex];
        const popupContainer = document.querySelector('.popup-container');
        popupContainer.querySelector('h2').textContent = currentSlide.title;
        popupContainer.querySelector('p').textContent = currentSlide.content;
    }

    // Function to handle file upload
    function handleFileUpload(event) {
        const file = event.target.files[0]; // Get the uploaded file
        const reader = new FileReader();

        // When the file is loaded
        reader.onload = function() {
            const imagePreview = document.querySelector('.upload-image img');
            imagePreview.src = reader.result; // Set the image preview source to the uploaded image
        };

        if (file) {
            reader.readAsDataURL(file); // Read the uploaded file as a data URL
        }
    }

    // Event listeners for navigation buttons
    prevBtn.addEventListener('click', showPrevSlide);
    nextBtn.addEventListener('click', showNextSlide);
    closeBtn.addEventListener('click', closePopup);

    // Event listener for file upload
    document.getElementById('upload').addEventListener('change', handleFileUpload);
});

// Get the button
let backToTopButton = document.getElementById("backToTop");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    let homeSection = document.getElementById("logo");
    let homeSectionHeight = homeSection.offsetHeight;

    if (document.body.scrollTop > homeSectionHeight || document.documentElement.scrollTop > homeSectionHeight) {
        backToTopButton.style.display = "block";
    } else {
        backToTopButton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
backToTopButton.onclick = function() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

// Search functionality
const searchInput = document.getElementById('search');
const boxes = document.querySelectorAll('.box');

searchInput.addEventListener('input', function() {
    const searchValue = searchInput.value.toLowerCase();
    boxes.forEach(box => {
        const text = box.textContent.toLowerCase();
        if (text.includes(searchValue)) {
            box.style.display = 'flex'; // Show the box
        } else {
            box.style.display = 'none'; // Hide the box
        }
    });
});

// Disable pinch zoom gesture on touch-enabled devices
document.addEventListener('touchmove', function(event) {
    if (event.scale !== 1) { event.preventDefault(); }
}, { passive: false });

// Disable zoom functionality on desktop browsers
window.addEventListener('wheel', function(event) {
    if (event.ctrlKey) { event.preventDefault(); }
}, { passive: false });

// Disable zooming using ctrl key and +/- keys
window.addEventListener('keydown', function(e) {
    if (e.ctrlKey && (e.key === '+' || e.key === '-' || e.key === '=')) {
        e.preventDefault();
    }
});
