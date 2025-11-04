function setup() {
  createCanvas(1000, 1000,WEBGL);
}

function draw() {
  background(220);
  fill("green")
  orbitControl()
  fill("red")
  box(100,100,300,500)
  fill("grey")
  box(140,140,300,500)
  fill("grey")
  sphere(100,50,50)
    fill("brown")
  cone(50,-300,50,)
  fill("yellow")
  torus(60,50)
}