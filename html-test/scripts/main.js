/*let myHeading = document.querySelector("h1");
myHeading.textContent = "Hello world!";
*/

/*
document.querySelector("html").addEventListener("click", function () {
  alert("别戳我，我怕疼。");
});
*/

let myImage = document.querySelector("img");

myImage.onclick = function () {
  let mySrc = myImage.getAttribute("src");
  if (mySrc === "images/qipao.jpeg") {
    myImage.setAttribute("src", "images/T-shirt.jpeg");
  } else {
    myImage.setAttribute("src", "images/qipao.jpeg");
  }
};

let myButton = document.querySelector("button");
let myHeading = document.querySelector("h1");

function setUserName() {
  let myName = prompt("请输入你的名字。");
  localStorage.setItem("name", myName);
  myHeading.textContent = myName + " 酷毙了"
}

if (!localStorage.getItem("name")) {
  setUserName();
} else {
  let storedName = localStorage.getItem("name");
  myHeading.textContent = storedName + " 酷毙了"
}

myButton.onclick = function () {
  setUserName();
};