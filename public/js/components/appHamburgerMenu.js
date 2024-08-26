function toggleHamburgerMenu(hamburger) {
    let menu = document.getElementById("HamburgerMenu");

    if (menu.classList.contains("hidden")) {
        menu.classList.remove("hidden");
    } else {
        menu.classList.add("hidden");
    }
}