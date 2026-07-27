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
/*------------------------------------------FUNCTIONS------------------------------------------*/
function summarizeUser(userName, userAge, userHasHobby) {
  return (
    `Name is ${userName}, age is ${userAge} and the user has hobbies: ${userHasHobby}`
  );
}

console.log(summarizeUser(name, age, hasHobbies));
person.greet();