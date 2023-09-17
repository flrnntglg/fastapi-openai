document.addEventListener("DOMContentLoaded", () => {
    const getRecommendationsButton = document.getElementById("getRecommendations");
    const countrySelect = document.getElementById("country");
    const seasonSelect = document.getElementById("season");
    const recommendationsDiv = document.getElementById("recommendations");

    getRecommendationsButton.addEventListener("click", async () => {
        const country = countrySelect.value;
        const season = seasonSelect.value;

        try {
            const response = await fetch(`/recommendations/?country=${country}&season=${season}`);
            if (!response.ok) {
                throw new Error(`Server returned ${response.status} ${response.statusText}`);
            }
            const data = await response.json();

            recommendationsDiv.innerHTML = `
                ${data.Recommendations.map(item => `<p>${item}</p>`).join("")}
            `;
        } catch (error) {
            console.error("Error fetching recommendations:", error);
            recommendationsDiv.innerHTML = "<p>An error occurred while fetching recommendations.</p>";
        }
    });
});
