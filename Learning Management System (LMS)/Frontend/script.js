// Set this to your local server link or IP address generated in CMD (e.g. http://127.0.0.1:8000 or http://192.168.1.15:8000)
const API_BASE = "https://unreal-unreeling-conduit.ngrok-free.dev";

// Standard helper to handle API calls using Fetch
async function apiCall(endpoint, method = "GET", data = null) {
    const url = `${API_BASE}${endpoint}`;
    const options = {
        method: method,
        headers: {
            "Content-Type": "application/json"
        }
    };
    if (data) {
        options.body = JSON.stringify(data);
    }

    try {
        const response = await fetch(url, options);
        if (!response.ok) {
            const errData = await response.json().catch(() => ({}));
            throw new Error(errData.error || `HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error(`API Call failed: ${method} ${endpoint}`, error);
        throw error;
    }
}

// Session Helpers
function getLoggedInUser() {
    const userStr = localStorage.getItem("lms_user");
    if (!userStr) return null;
    try {
        return JSON.parse(userStr);
    } catch (e) {
        return null;
    }
}

function setLoggedInUser(user) {
    localStorage.setItem("lms_user", JSON.stringify(user));
}

function logoutUser() {
    localStorage.removeItem("lms_user");
    window.location.href = "index.html";
}

// Update the Navbar UI based on user session status
function updateNavbar() {
    const navbar = document.querySelector(".navbar");
    if (!navbar) return;

    const user = getLoggedInUser();
    const ul = navbar.querySelector("ul");

    if (user) {
        // If logged in, customize menu options
        ul.innerHTML = `
            <li><a href="index.html">Home</a></li>
            <li><a href="courses.html">Courses</a></li>
            <li><a href="enrollments.html">My Enrollments</a></li>
            <li><a href="assignments.html">Assignments</a></li>
            <li><a href="dashboard.html">Dashboard</a></li>
            <li><a href="admin.html">Admin Panel</a></li>
            <li><span class="user-status"><i class="fa fa-user"></i> ${user.full_name}</span></li>
            <li><a href="#" class="btn-logout" onclick="logoutUser(); return false;"><i class="fa-solid fa-right-from-bracket"></i> Logout</a></li>
        `;
    } else {
        // If anonymous visitor
        ul.innerHTML = `
            <li><a href="index.html">Home</a></li>
            <li><a href="courses.html">Courses</a></li>
            <li><a href="login.html">Login</a></li>
            <li><a href="register.html">Register</a></li>
            <li><a href="admin.html">Admin Panel</a></li>
        `;
    }

    // Highlight the active page link
    const currentPath = window.location.pathname.split("/").pop() || "index.html";
    const links = ul.querySelectorAll("a");
    links.forEach(link => {
        const linkPath = link.getAttribute("href");
        if (linkPath === currentPath) {
            link.classList.add("active");
        } else {
            link.classList.remove("active");
        }
    });
}

// Set up UI updates on DOMContentLoaded
document.addEventListener("DOMContentLoaded", () => {
    updateNavbar();
});