function toggleMenu() {
  const linkMenu = document.getElementById("AppLinks");
  linkMenu.classList.toggle("hidden");
}

function loadDarkModeIcon() {
  const toggleIconElem = document.getElementById("AppDarkModeToggle");
  if (
    localStorage.theme === "dark" ||
    (!("theme" in localStorage) &&
      window.matchMedia("(prefers-color-scheme: dark)").matches)
  ) {
    document.documentElement.classList.add("dark");

    toggleIconElem.classList.remove("fa-regular");
    toggleIconElem.classList.remove("fa-moon");

    toggleIconElem.classList.add("fa-solid");
    toggleIconElem.classList.add("fa-sun");
  } else {
    document.documentElement.classList.remove("dark");

    toggleIconElem.classList.add("fa-regular");
    toggleIconElem.classList.add("fa-moon");

    toggleIconElem.classList.remove("fa-solid");
    toggleIconElem.classList.remove("fa-sun");
  }
}

addEventListener("load", loadDarkModeIcon);

function toggleDarkMode() {
  const toggleIconElem = document.getElementById("AppDarkModeToggle");

  document.documentElement.classList.toggle("dark");

  if (document.documentElement.classList.contains("dark")) {
    localStorage.theme = "dark";
    toggleIconElem.classList.add("fa-regular");
    toggleIconElem.classList.add("fa-moon");

    toggleIconElem.classList.remove("fa-solid");
    toggleIconElem.classList.remove("fa-sun");
  } else {
    localStorage.theme = "light";
    toggleIconElem.classList.remove("fa-regular");
    toggleIconElem.classList.remove("fa-moon");

    toggleIconElem.classList.add("fa-solid");
    toggleIconElem.classList.add("fa-sun");
  }

  toggleIconElem.classList.toggle("fa-regular");
  toggleIconElem.classList.toggle("fa-moon");
  toggleIconElem.classList.toggle("fa-solid");
  toggleIconElem.classList.toggle("fa-sun");
}
