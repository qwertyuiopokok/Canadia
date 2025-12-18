const API_BASE = ""; // Set to your backend URL if needed

async function fetchPersonalizedContent(province) {
    try {
        const response = await fetch(`${API_BASE}/content/personalized?province=${province}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const news = await response.json();
        renderNews(news);
    } catch (error) {
        const container = document.getElementById("news-container");
        container.className = "error";
        container.textContent = "Erreur lors du chargement des actualités personnalisées.";
        console.error("Failed to fetch personalized content:", error);
    }
}

function saveProvince(province) {
    localStorage.setItem("province", province);
}

function getSavedProvince() {
    return localStorage.getItem("province") || "QC";
}

document.addEventListener("DOMContentLoaded", () => {
    const select = document.getElementById("province-select");
    if (select) {
        select.value = getSavedProvince();
        select.addEventListener("change", (e) => {
            const province = e.target.value;
            saveProvince(province);
            fetchPersonalizedContent(province);
        });
    }
    fetchPersonalizedContent(getSavedProvince());
});
async function fetchNews() {
    try {
        const response = await fetch("/api/news");
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const news = await response.json();
        renderNews(news);
    } catch (error) {
        const container = document.getElementById("news-container");
        container.className = "error";
        container.textContent = "Erreur lors du chargement des actualités.";
        console.error("Failed to fetch news:", error);
    }
}


function renderNews(news) {
    const container = document.getElementById("news-container");
    container.className = "";
    container.innerHTML = "";

    news.forEach(item => {
        const article = document.createElement("div");
        article.className = "news-item";
        article.innerHTML = `
            <div class="news-meta">${item.date} — ${item.author}</div>
            <h3>${item.title}</h3>
            <p>${item.content}</p>
            <div style="margin-top:8px;">
                <button onclick="sendFeedback('${item.fingerprint}', 1)">👍</button>
                <button onclick="sendFeedback('${item.fingerprint}', -1)">👎</button>
            </div>
        `;
        container.appendChild(article);
    });
}

async function sendFeedback(fingerprint, value) {
    try {
        const response = await fetch('/feedback', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ fingerprint, value })
        });
        if (!response.ok) {
            throw new Error('Erreur lors de l\'envoi du feedback');
        }
        // Optionally show a thank you message or update UI
        alert('Merci pour votre retour!');
    } catch (error) {
        alert('Erreur lors de l\'envoi du feedback.');
        console.error(error);
    }
}

fetchNews();
