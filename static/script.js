const root = document.documentElement;
const themeButtons = document.querySelectorAll(".theme-option");

function setTheme(theme) {
    root.dataset.theme = theme;
    localStorage.setItem("goalgetter-theme", theme);

    themeButtons.forEach((button) => {
        const active = button.dataset.theme === theme;
        button.classList.toggle("active", active);
        button.setAttribute("aria-pressed", String(active));
    });
}

const storedTheme = localStorage.getItem("goalgetter-theme");
const preferredTheme = window.matchMedia("(prefers-color-scheme: dark)").matches
    ? "dark"
    : "light";

setTheme(storedTheme || preferredTheme);

themeButtons.forEach((button) => {
    button.addEventListener("click", () => {
        setTheme(button.dataset.theme);
    });
});