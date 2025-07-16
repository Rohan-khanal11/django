document.addEventListener("DOMContentLoaded", () => {
    const postLinks = document.querySelectorAll(".text-decoration-none.text-dark");

    postLinks.forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();  

            const targetUrl = link.href;
            alert(`You clicked: ${link.textContent.trim()}`);

            // After alert finishes, navigate to the link
            window.location.href = targetUrl;
        });
    });
});
