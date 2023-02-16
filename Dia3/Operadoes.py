firstName = "Pablo"
lastName = "Huertas"
country = "Espapña"
city = "Jerez"
age = 16
isMarried = false

console.log(typeof firstName)
console.log(typeof lastName)
console.log(typeof country)
console.log(typeof age)
console.log(typeof isMarried)

console.log('10' === 10)
console.log('10' == 10)

num = parseInt('9.8')
console.log(num == 10)

base_num = parseInt(prompt("Cual es la altura del triangulo: "))
height_num = parseInt(prompt("Cual es la altura del triangulo: "))
triangle_area = 0.5 * base_num * height_num;
console.log("El area del triangulo es " + triangle_area)

sideA = parseInt(prompt("enter side A: "))
sideB = parseInt(prompt("enter side B: "))
sideC = parseInt(prompt("enter side C. "))
triangle_perimeter = sideA + sideB + sideC
console.log("El perimetro del rectangulo es " + triangle_perimeter)

length_num = parseInt(prompt("enter length: "))
width_num = parseInt(prompt("enter width: "))
rectangle_area = length_num * width_num
console.log(rectangle_area)

rectangle_perimeter = 2 * (length_num + width_num)
console.log(rectangle_perimeter)

const PI = 3.14
radius_num = parseInt(prompt("enter radius number: "))
radius_squared = radius_num * radius_num
circle_area = PI * radius_squared
console.log("El area del circulo es " + circle_area)

circle_circum = 2 * PI * radius_num
console.log("La circunferencia del circulo es " + circle_circum)

num_hours = parseInt(prompt("Number of hours you work: "))
rate_hour = parseInt(prompt("amount you earn per hour: "))
day_pay = num_hours * rate_hour
console.log("The amount of money you earn per day is + day_pay")
