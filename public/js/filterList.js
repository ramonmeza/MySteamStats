function filterList() {
    const statsList = document.getElementById("StatsList");
    const lis = statsList.getElementsByTagName("li");
     const filter = document.getElementById("FilterInput").value.toLowerCase();

     for (i = 0; i < lis.length; i++) {
         const text = lis[i].innerText;
         if (text.toLowerCase().indexOf(filter) > -1) {
             lis[i].classList.remove("hidden");
         } else {
             lis[i].classList.add("hidden");
         }
    }
 }