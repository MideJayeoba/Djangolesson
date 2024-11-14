// document.addEventListener("DOMContentLoaded", function () {
//   const hamburger = document.getElementById("hamburgerBtn");
//   const navLinks = document.getElementById("navLinks");
//   const mainNav = document.getElementById("mainNav");

//   hamburger.addEventListener("click", function () {
//     navLinks.classList.toggle("active");
//     mainNav.classList.toggle("open");
//     hamburger.classList.toggle("active");
//   });

//   // Close menu when clicking outside
//   document.addEventListener("click", function (event) {
//     if (
//       !mainNav.contains(event.target) &&
//       navLinks.classList.contains("active")
//     ) {
//       navLinks.classList.remove("active");
//       mainNav.classList.remove("open");
//       hamburger.classList.remove("active");
//     }
//   });
// });
