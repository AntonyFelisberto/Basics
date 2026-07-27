/*---------------------------------VARIABLES---------------------------------*/
let age: number;
let userName: string;
let isInstructor: boolean;
let hobbies: string[];
let person: {
    name: string;
    age: number;
};
let people: {
    name: string;
    age: number;
}[];
let course: string | string[] | number | boolean = 'React - The Complete Guide';
const result = add(2, 5);
type Person = {
  name: string;
  age: number;
};

let newPeople: Person[];
/*---------------------------------SETTING VARIABLES---------------------------------*/
age = 12;
userName = 'Max';
isInstructor = true;
hobbies = ['Sports', 'Cooking'];
person = {
    name: 'Max',
  age: 32
};
course = 12341;
/*---------------------------------FUNCTIONS---------------------------------*/
function add(a: number, b: number) {
  return a + b;
}

