function updateArrowDirection() {
    const pageArrow = document.getElementById("AppScrollArrow");
    const currentScroll = document.documentElement.scrollTop || document.body.scrollTop;
    let nextScroll = currentScroll + 1 + window.innerHeight;
    
    if (nextScroll >= document.body.scrollHeight) {
        // up arrow
        pageArrow.classList.add("-scale-y-100");
    } else {
        // down arrow
        pageArrow.classList.remove("-scale-y-100");
    }
}

addEventListener("scroll", updateArrowDirection);

function clickScrollArrow() {
    const cur = document.documentElement.scrollTop || document.body.scrollTop;
    const next = cur + 1 + window.innerHeight;
    
    if (next >= document.body.scrollHeight) {
        window.scrollTo({top: 0, behavior: "smooth"});
    } else {
        window.scrollTo({top: next, behavior: "smooth"});
    }
}