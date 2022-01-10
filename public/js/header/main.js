// ======= Reload ======= //
window.addEventListener("load", function () {
  let preload = document.querySelector(".loader-wrapper");
  preload.classList.add("loader-finish");
});

$(document).ready(function () {
  // ======= Check login ======= //
  if (document.cookie.indexOf("loggedin=true") > -1) {
    $("header .actions .menu #logged-in").show()
    $("header .actions .menu #not-logged-in").hide()
  } else {
    $("header .actions .menu #not-logged-in").show()
    $("header .actions .menu #logged-in").hide()
  }

  // ======= Search ======= //
  $(".search form").submit(function (e) {
    e.preventDefault();
    let search = $("#search-input").val();
    location.href = `/products/search-results?q=${search}`;
  })

  // ======= Dropdown actions ======= //
  $(".header-top .dropdown-top").click(function () {
    $(this).next().toggleClass("show-dropdown");
    $(this).children(".flaticon-down-arrow").toggleClass("rotate-arrow");

    $(document).on("click", ".dropdownn ul li", function () {
      $(this).parent().prev().children(".wrapper").html($(this).html());
      $(this).parent().prev().children("i").removeClass("rotate-arrow");
      $(this).parent().removeClass("show-dropdown");
    });
  });

  $(".categories-top-content").click(function () {
    $(this).next().toggleClass("show-categories-dropdown");
    $(this).children(".flaticon-down-arrow").toggleClass("rotate-arrow");
  });

  // processes when click outside
  $(document).mouseup(function (e) {
    if (!$(".dropdownn").is(e.target) && $(".dropdownn").has(e.target).length === 0) {
      $(".dropdownn ul").removeClass("show-dropdown");
      $(".categories-dropdown").removeClass("show-categories-dropdown");
      $(".dropdown-top .flaticon-down-arrow").removeClass("rotate-arrow");
    }
  });

  // ======= Show or hide dark bg-color ======= //
  $("header .has-submenu").mouseover(function () {
    $(".dark-bg-color").show();
    $(".dark-bg-color").css("z-index", "99");
  });

  $("header .has-submenu").mouseout(function () {
    $(".dark-bg-color").hide();
    $(".dark-bg-color").css("z-index", "9999");
  });

  // ======= Show or hide sidebar nav-menu ======= //
  $("#navigation-list .nav-menu-btn").click(function () {
    $(".header-bottom .nav-links").addClass("show-sidebar-menu");
  });

  $(".nav-menu-header button").click(function () {
    $(".header-bottom .nav-links").removeClass("show-sidebar-menu");
  });

  // processes when click outside
  $(document).mouseup(function (e) {
    if (!$(".header-bottom .nav-links").is(e.target) &&
      $(".header-bottom .nav-links").has(e.target).length === 0) {
      $(".header-bottom .nav-links").removeClass("show-sidebar-menu");
    }
  });

  // ======= Show or hide Search ======= //
  $("#navigation-list .show-search-btn").click(function () {
    $(".header-middle .search").addClass("show-search");
  });

  // processes when click outside
  $(document).mouseup(function (e) {
    if (!$(".header-middle .search form").is(e.target) &&
      $(".header-middle .search form").has(e.target).length === 0) {
      $(".header-middle .search").removeClass("show-search");
    }
  });

  // ======= Show or hide sidebar categories ======= //
  $("#navigation-list .sidebar-categories-btn").click(function () {
    $(".header-bottom .categories-dropdown").addClass("show-sidebar-menu");
  });

  $(".categories-header button").click(function () {
    $(".header-bottom .categories-dropdown").removeClass("show-sidebar-menu");
  });

  // processes when click outside
  $(document).mouseup(function (e) {
    if (!$(".header-bottom .categories-dropdown").is(e.target) &&
      $(".header-bottom .categories-dropdown").has(e.target).length === 0) {
      $(".header-bottom .categories-dropdown").removeClass("show-sidebar-menu");
    }
  });

  // ======= Categories - actions ======= //
  if ($(window).width() < 992) {
    $(".header-bottom .has-submenu").click(function () {
      $(".header-bottom .categories-ul").removeClass("back-1").addClass("forward-1");
      $(".header-bottom .categories-ul").prev(".categories-header").removeClass("back-1").addClass("forward-1");
      $(this).find(".submenu").addClass("show-submenu");
    });

    $(".has-submenu .submenu-btn").click(function (e) {
      e.stopPropagation()
      $(".header-bottom .categories-ul").removeClass("forward-1 back-2 back-1").addClass("forward-2");
      $(".header-bottom .categories-ul").prev(".categories-header").removeClass("forward-1 back-2 back-1").addClass("forward-2");
      $(this).next(".wrapper").show();
      $(this).next(".wrapper").first("button").removeClass("d-none");
    });

    $(".header-bottom .back-btn-1").click(function (e) {
      e.stopPropagation()
      $(".header-bottom .categories-ul").removeClass("forward-1 back-2").addClass("back-1");
      $(".header-bottom .categories-ul").siblings(".categories-header").removeClass("forward-1 back-2").addClass("back-1");
      $(this).parent(".submenu").removeClass("show-submenu");
      $(this).closest(".has-submenu").siblings(".has-submenu").find(".submenu").addClass("show-submenu");
    });

    $(".header-bottom .back-btn-2").click(function (e) {
      e.stopPropagation()
      $(".header-bottom .categories-ul").removeClass("forward-2").addClass("back-2");
      $(".header-bottom .categories-ul").siblings(".categories-header").removeClass("forward-2").addClass("back-2");
      $(this).parent(".wrapper").hide();
    });
  };

  // ======= Events On Scroll ======= //
  $(window).scroll(function () {
    // back-to-top btn
    if ($(this).scrollTop() > 300) {
      $("#back-to-top-btn").show();
    } else {
      $("#back-to-top-btn").hide();
    }

    // making the header sticky
    if (($(window).width() > 992) && ($(this).scrollTop() >= 121)) {
      $(".header-bottom-wrapper").addClass("sticky");
      $(".header-bottom-wrapper .actions").show();
      $(".header-bottom-wrapper .brand").show();
      $(".header-bottom-wrapper .categories-top-content").css("background-color", "#fff");
      // $(".header-bottom-wrapper .categories-top-content p").hide();
    } else {
      $(".header-bottom-wrapper").removeClass("sticky");
      $(".header-bottom-wrapper .actions").hide();
      $(".header-bottom-wrapper .brand").hide();
      $(".header-bottom-wrapper .categories-top-content").css("background-color", "#fff");
      // $(".header-bottom-wrapper .categories-top-content p").show();
    }

    if (($(window).width() < 992) && ($(this).scrollTop() >= 43)) {
      $(".header-middle-wrapper").addClass("sticky");
    } else {
      $(".header-middle-wrapper").removeClass("sticky");
    }
  });

  $("#back-to-top-btn").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 100);
  });

});


// api get category
async function showCategory() {
  const res = await fetch("/api/products/categories");
  const data = await res.json();
  
  for (const { __data__: cate} of data) {
    const template = document.querySelector("#category-template").content;
    const clone = template.cloneNode(true);

    clone.querySelector("li").dataset.id = cate.id;
    clone.querySelector(".category-name").textContent = cate.name;
    clone.querySelector(".category-link").href = "/products/category/" + cate.id;

    document.querySelector(".categories-ul").appendChild(clone);
  }
}

showCategory();