var page = window.location.pathname.split("/").pop().split(".")[0];
var aux = window.location.pathname.split("/");

if (!aux.includes("pages")) {
  page = "dashboard";
}

// ⬇️ carrega CSS e JS com base na pasta /static/
loadStylesheet(staticBase + "assets/css/perfect-scrollbar.css");
loadJS(staticBase + "assets/js/perfect-scrollbar.js", true);

if (document.querySelector("nav [navbar-trigger]")) {
  loadJS(staticBase + "assets/js/navbar-collapse.js", true);
}

if (document.querySelector("[data-target='tooltip']")) {
  loadJS(staticBase + "assets/js/tooltips.js", true);
  loadStylesheet(staticBase + "assets/css/tooltips.css");
}

if (document.querySelector("[nav-pills]")) {
  loadJS(staticBase + "assets/js/nav-pills.js", true);
}

if (document.querySelector("[dropdown-trigger]")) {
  loadJS(staticBase + "assets/js/dropdown.js", true);
}

if (document.querySelector("[fixed-plugin]")) {
  loadJS(staticBase + "assets/js/fixed-plugin.js", true);
}

if (document.querySelector("[navbar-main]")) {
  loadJS(staticBase + "assets/js/sidenav-burger.js", true);
  loadJS(staticBase + "assets/js/navbar-sticky.js", true);
}

if (document.querySelector("canvas")) {
  loadJS(staticBase + "assets/js/chart-1.js", true);
  loadJS(staticBase + "assets/js/chart-2.js", true);
}

function loadJS(FILE_URL, async) {
  let dynamicScript = document.createElement("script");
  dynamicScript.setAttribute("src", FILE_URL);
  dynamicScript.setAttribute("type", "text/javascript");
  dynamicScript.setAttribute("async", async);
  document.head.appendChild(dynamicScript);
}

function loadStylesheet(FILE_URL) {
  let dynamicStylesheet = document.createElement("link");
  dynamicStylesheet.setAttribute("href", FILE_URL);
  dynamicStylesheet.setAttribute("type", "text/css");
  dynamicStylesheet.setAttribute("rel", "stylesheet");
  document.head.appendChild(dynamicStylesheet);
}
