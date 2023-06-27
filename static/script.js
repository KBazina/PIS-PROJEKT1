document.getElementById("slika").addEventListener("change", function (e) {
  var fileName = "";
  if (this.files && this.files.length > 0) {
    fileName = this.files[0].name;
  }
  document.getElementById("slika-label").innerHTML = "Slika dodana";
});
let uredi = document.querySelectorAll(".uredi");
let overlay = document.querySelector(".overlay");

function otvori() {
  uredi.forEach(function (element) {
    element.addEventListener("click", function () {
      overlay.style.display = "block";

      let roditelj = element.parentElement;
      console.log(roditelj);

      let sljedeciDiv = roditelj.nextElementSibling;
      console.log(sljedeciDiv);

      sljedeciDiv.style.display = "block";
      overlay.addEventListener("click", function () {
        overlay.style.display = "none";
        sljedeciDiv.style.display = "none";
      });
    });
  });
}

otvori();
