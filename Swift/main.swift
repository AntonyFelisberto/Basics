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
var nums_: [Int] = [1,3,4]
var ages: [String:Int] = ["Artorias":30]
var letters: Set<Character> = ["a", "b"]

counter += 1
nickName = "KJ"

/*----------------------------------------PRINTS------------------------------------------------*/
print(nums)
print(pi,count)
print(x, y, a, b)
print(constant, counter)
print(greeting + " "+name)
print("pi = \(pi), count = \(count)")
print(type(of: bool), type(of: double))
print(f,n,m,separator: ", ", terminator:"; ")