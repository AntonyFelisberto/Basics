import Foundation

/*----------------------------------------CONSTANTS------------------------------------------------*/
let infi = -7           ///let - let are constants on swift
let f=1,n=2,m=3
let a = 10, b = 20
let greeting = "Hey"        
let pi: Double = 3.13159
let bool:Bool = true
let double:Double = 3.14
let constant = 10
let fixed = [1,2]
let firstName:String = "Roll", lastName: String = "Ross"
//fixed.append(3) //ERROR because it is a constant 
// constant = 12 //ERROR because it is a constant

/*----------------------------------------MUTABLE VARIABLES------------------------------------------------*/
/* Vars are normal variables
    /*You can declare the types just like ts*/
*/
var name = "bro"
var count: Int = 3
var firstName: String? = nil
var nickName: String? = nil
var counter = 1
var x = 1, y = 2
var nums = [1,2]
var nums_: [Int] = [1,3,4]
var i: Int = 1, j: Int = 2
var ages: [String:Int] = ["Artorias":30]
var letters: Set<Character> = ["a", "b"]

counter += 1
nickName = "KJ"
nums.append(3)
nums_.append(33)
ages["Elize"] = 25
/*----------------------------------------PRINTS------------------------------------------------*/
print(nums)
print(nums_[0])
print(min(3,8))
print(max(3,8))
print(pi,count)
print(abs(infi))
print(x, y, a, b)
print(nums_.count)
print(constant, counter)
print(greeting + " "+name)
print(letters.contains("a"))
print(ages["Artorias"] ?? 0)
print(i+j, firstName, lastName)
print("pi = \(pi), count = \(count)")
print(type(of: bool), type(of: double))
print(firstName ?? "none",nickName ?? "none")
print(f,n,m,separator: ", ", terminator:"; ")
/*----------------------------------------LOOPS------------------------------------------------*/
for n in 1...3 {
  print(n, terminator: " - ")
}

func add(_ a:Int,_ b:Int) -> Int {
  return a + b
}
print(add(4,4))
/*----------------------------------------IFS------------------------------------------------*/
if(1<2){
  let cc=3;let nn=6;
  print("\(cc+nn)")
}