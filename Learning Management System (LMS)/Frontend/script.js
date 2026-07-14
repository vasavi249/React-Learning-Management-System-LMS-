// Set this to your deployed Django backend server URL (e.g. https://lms-api.onrender.com)
const DEPLOYED_BACKEND_URL = "https://your-backend-api-domain.com";

// Checks if loaded locally or on local network (127.x.x.x, localhost, or private IP ranges)
const host = window.location.hostname;
const isLocalNetwork = host === "localhost" || host === "127.0.0.1" || 
                       host.startsWith("192.168.") || host.startsWith("10.") || 
                       host.startsWith("172.") || window.location.protocol === "file:";

const API_BASE = isLocalNetwork
    ? `http://${(host === "" || window.location.protocol === "file:") ? "127.0.0.1" : host}:8000`
    : DEPLOYED_BACKEND_URL;

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