window.addEventListener("load", (event) => {
   var swiperWrapper = document.querySelector(".swiper-wrapper");

   /* The Team */
   var team = [
      {
         name: "Alice Stone",
         role: "UI Designer",
         desc:
            "Far far away, behind the world mountains, far from the countries Vokalia and Consonantia, theres live the blind texts.",
         photo:
            "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?auto=compress&cs=tinysrgb&dpr=2&h=300&w=300",
         website: "https://rafaelalucas.com",
         email: "mailto:rafaelavlucas@gmail.com",
         linkedin: "https://www.linkedin.com/in/rafaelalucas/"
         
      },
      {
         name: "Adam Turner",
         role: "Project Manager",
         desc:
            "Far far away, behind the world mountains, far from the countries Vokalia and Consonantia, theres live the blind texts.",
         photo:
            "https://images.unsplash.com/photo-1522609925277-66fea332c575?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9?auto=compress&cs=tinysrgb&dpr=2&h=300&w=300",
         website: "https://rafaelalucas.com",
         email: "mailto:rafaelavlucas@gmail.com",
         linkedin: "https://www.linkedin.com/in/rafaelalucas/"
         
      },
      {
         name: "Nancy Hughes",
         role: "UX Specialist",
         desc:
            "Far far away, behind the world mountains, far from the countries Vokalia and Consonantia, theres live the blind texts.",
         photo:
            "https://images.pexels.com/photos/774909/pexels-photo-774909.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=300&w=300",
         website: "https://rafaelalucas.com",
         email: "mailto:rafaelavlucas@gmail.com",
         linkedin: "https://www.linkedin.com/in/rafaelalucas/"
         
      },
      {
         name: "Jonathan Campbell",
         role: "Front-End Developer",
         desc:
            "Far far away, behind the world mountains, far from the countries Vokalia and Consonantia, theres live the blind texts.",
         photo:
            "https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=300&w=300",
         website: "https://rafaelalucas.com",
         email: "mailto:rafaelavlucas@gmail.com",
         linkedin: "https://www.linkedin.com/in/rafaelalucas/"
        
      },
      {
         name: "Jack Keller",
         role: "Back-End Developer",
         desc:
            "Far far away, behind the world mountains, far from the countries Vokalia and Consonantia, theres live the blind texts.",
         photo:
            "https://images.pexels.com/photos/2379004/pexels-photo-2379004.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=300&w=300",
         website: "https://rafaelalucas.com",
         email: "mailto:rafaelavlucas@gmail.com",
         linkedin: "https://www.linkedin.com/in/rafaelalucas/"
         
      },
      {
         name: "Sara Carroll",
         role: "Head of UI Design",
         desc:
            "Far far away, behind the world mountains, far from the countries Vokalia and Consonantia, theres live the blind texts.",
         photo:
            "https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9?auto=compress&cs=tinysrgb&dpr=2&h=300&w=300",
         website: "https://rafaelalucas.com",
         email: "mailto:rafaelavlucas@gmail.com",
         linkedin: "https://www.linkedin.com/in/rafaelalucas/"
       
      }
   ];

   /* Social Icons */
   var icons = [
      {
         iWebsite: "https://rafaelalucas.com/dailyui/6/assets/link.svg",
         iEmail: "https://rafaelalucas.com/dailyui/6/assets/email.svg",
         iLinkedin: "https://rafaelalucas.com/dailyui/6/assets/linkedin.svg"
         
      }
   ];

   var iWebsite = icons[0].iWebsite,
      iEmail = icons[0].iEmail,
      iLinkedin = icons[0].iLinkedin
      

   /* Function to populate the team members */
   function addTeam() {
      for (let i = 0; i < team.length; i++) {
         /* Variables for the team */
         var name = team[i].name,
            role = team[i].role,
            desc = team[i].desc,
            photo = team[i].photo,
            website = team[i].website,
            email = team[i].email,
            linkedin = team[i].linkedin;

         /* Template for the Team Cards */
         var template = `
                <div class="swiper-slide">
                <div class="card">
                    <span class="bg"></span>
                    <span class="more"></span>
                    <figure class="photo"><img src="${photo}"></figure>
                        <article class="text">
                            <p class="name">${name}</p>
                            <p class="role">${role}</p> 
                            <p class="desc">${desc}</p> 
                        </article>
                        
                        <div class="social">
                        <span class="pointer"></span>
                        <div class="icons">
                            <a class="icon" href="${website}" target="_blank" data-index="0"><img src="${iWebsite}"></a>
                            <a class="icon" href="${email}" target="_blank" data-index="1"><img src="${iEmail}"></a>
                            <a class="icon" href="${linkedin}" target="_blank" data-index="2"><img src="${iLinkedin}"></a>
                            </div>
                            </div>
                    </div>
                </div>`;

         swiperWrapper.insertAdjacentHTML("beforeend", template);
      }
   }

   addTeam();

   /* Swiper Settings */

   var mySwiper = new Swiper(".swiper-container", {
      // Optional parameters
      direction: "horizontal",
      loop: true,
      centeredSlides: false,
      speed: 800,
      slidesPerView: 3,
      spaceBetween: 40,
      threshold: 5,

      // If we need pagination
      pagination: {
         el: ".swiper-pagination",
         clickable: true
      },

      // Navigation arrows
      navigation: {
         nextEl: ".swiper-button-next",
         prevEl: ".swiper-button-prev"
      },
      breakpoints: {
         1180: {
            slidesPerView: 2,
            spaceBetween: 40,
            centeredSlides: false
         },
         799: {
            slidesPerView: 1,
            spaceBetween: 20,
            centeredSlides: true,
            loop: true
         }
      }
   });

   /* Show More */

   var btnShow = document.querySelectorAll(".more");

   btnShow.forEach(function (el) {
      el.addEventListener("click", showMore);
   });

   function showMore(event) {
      var card = event.target.closest(".swiper-slide");

      if (card.classList.contains("show-more")) {
         card.classList.remove("show-more");
      } else {
         card.classList.add("show-more");
      }
   }


});




/* display the card for the data graphs */

(function(){
  $(".window").hide(0.001);
}());

var windowSelected = "";

$(".box").on("click", function(){
  windowSelected = $(this).attr("class").substring(4);
  selectBox(windowSelected);
}) /*box click*/

function selectBox(boxName){
  $(".window."+boxName).toggle(1000, closeTabN());
}

//Se agrega y quita la clase closeWindow al closeButton 
function closeTabN(){
  $(".closeButton").toggleClass("body closeWindow");
}

//Cuando se oprime el buttonClose se llama a CheckedWindow para encontrar la ventana "abierta" y cerrarla
$(".closeButton").on("click", function(){
  /*var windowName = checkedWindow();
  $(".window."+windowName.substring(7)).toggle("fast");*/
  $(".window."+windowSelected).toggle(1000);
  closeTabN();
})