<div class="row">
                <div class="column">
                  <img src="./assets/img/transferir (44).jpg" alt="kit" style="width:60%">
                  <div class="bottom-left"><h5>Onyx Oxygen Blue and Red</h5></div>
                </div>
                <div class="column">
                  <img src="./assets/img/transferir.jpg" alt="Blue" style="width:60%">
                  <div class="bottom-left"><h5>Onyx Oxygen Blue</h5></div>
                </div>
                <div class="column">
                  <img src="./assets/img/oxygen_vermelho.webp" alt="Red" style="width:60%">
                  <div class="bottom-left"><h5>Onyx Oxygen Red</h5></div>
                </div>
              </div>
   <button onclick="one()">1</button>
<button onclick="two()">2</button>
<button onclick="three()">3</button>

<script>
// Get the elements with class="column"
var elements = document.getElementsByClassName("column");

// Declare a "loop" variable
var i;

// Full-width images
function one() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.flex = "100%";
  }
}

// Two images side by side
function two() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.flex = "50%";
  }
}

// Three images side by side
function four() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.flex = "25%";
  }
}
</script>
<script>
    let botao = documet.getelEmentById('botao')
    botao.innerText = 'Este produto está em falta'