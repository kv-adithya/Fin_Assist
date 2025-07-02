const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");
const imageContainer = document.getElementById("imageContainer");
const darkModeToggle = document.getElementById("darkModeToggle");
const modal = document.getElementById("imageModal");
const modalImg = document.getElementById("modalImg");
const closeModal = document.getElementById("closeModal");

let query = "";
let page = 1;
const perPage = 9;
const API_KEY = "cdWEaJZdEb6LskUowaD4FQowQNyBdGgmEhx_-yZx3QQ";
const API_URL = "https://api.unsplash.com/search/photos";

// Function to fetch images
async function fetchImages() {
    if (!query) return;

    try {
        document.querySelector(".loading").style.display = "block";
        const response = await fetch(`${API_URL}?query=${query}&page=${page}&per_page=${perPage}&client_id=${API_KEY}`);
        const data = await response.json();
        document.querySelector(".loading").style.display = "none";

        if (data.results.length === 0) {
            return;
        }

        displayImages(data.results);
        page++;
    } catch (error) {
        console.error("Error fetching images:", error);
    }
}

// Function to display images
function displayImages(images) {
    images.forEach(image => {
        const card = document.createElement("div");
        card.classList.add("card");

        const img = document.createElement("img");
        img.src = image.urls.small;
        img.alt = image.alt_description;

        // Open modal on image click
        img.addEventListener("click", () => {
            modal.style.display = "flex";
            modalImg.src = image.urls.regular;
            modalImg.style.transform = "scale(1)"; // Reset zoom
        });

        card.appendChild(img);
        imageContainer.appendChild(card);
    });
}

// Close modal when clicking outside the image
modal.addEventListener("click", (e) => {
    if (e.target === modal || e.target === closeModal) {
        modal.style.display = "none";
    }
});

// Zoom In / Out functionality
let scale = 1;
modalImg.addEventListener("wheel", (e) => {
    e.preventDefault();
    scale += e.deltaY * -0.01;
    scale = Math.min(Math.max(1, scale), 3); 
    modalImg.style.transform = `scale(${scale})`;
});

// Search button event
searchButton.addEventListener("click", () => {
    query = searchInput.value.trim();
    page = 1;
    imageContainer.innerHTML = "";
    fetchImages();
});

// Infinite scrolling
window.addEventListener("scroll", () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 500) {
        fetchImages();
    }
});

// Dark mode toggle
darkModeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    localStorage.setItem("darkMode", document.body.classList.contains("dark-mode") ? "enabled" : "disabled");
});

if (localStorage.getItem("darkMode") === "enabled") {
    document.body.classList.add("dark-mode");
}