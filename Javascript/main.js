//<script src="main.js" defer type="module"/> //defer makes the script load just after the html and type module so that the js is treated as a module 

/*------------------------------------------VARIABLES AND OBJECTS------------------------------------------*/
var name = 'Gwyn';
var age = 29;
var hasHobbies = true;

let baseUser;
let baseAge;

const person = {
  name: 'Max',
  age: 29,
  greet() {
    console.log('Hi, I am ' + this.name);
  }
};

baseUser = "Artorias"
baseAge = 30;
/*------------------------------------------DOM FUNCTION------------------------------------------*/
document.getElementById("demo").innerHTML = "Hello";
alert("boy")
/*------------------------------------------FUNCTIONS------------------------------------------*/
function summarizeUser(userName, userAge, userHasHobby) {
  return (
    `Name is ${userName}, age is ${userAge} and the user has hobbies: ${userHasHobby}`
  );
}

console.log(summarizeUser(name, age, hasHobbies));
person.greet();

console.log(Date())
/*------------------------------------------JSON FUNCTIONS------------------------------------------*/
const text = '{"name":"Artorias", "age":30, "city":"New York"}';
const personData = JSON.parse(text);

const employee = {
  name: "Artorias",
  age: 30,
  city: "New York"
};
const textEmployee = JSON.stringify(person);
/*------------------------------------------XML FUNCTIONS------------------------------------------*/
const text = "<person><name>Gwyn</name></person>";
const parser = new DOMParser();
const xmlDoc = parser.parseFromString(text, "text/xml");
const name = xmlDoc.getElementsByTagName("name")[0].textContent;