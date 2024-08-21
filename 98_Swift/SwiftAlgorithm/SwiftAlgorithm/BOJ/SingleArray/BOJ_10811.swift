//
//  BOJ_10811.swift
//  SwiftAlgorithm
//
//  Created by 윤동주 on 8/22/24.
//

import Foundation

let NM = readLine()!.split(separator: " ").map { Int($0)! }
let N = NM[0]
let M = NM[1]

var basket = [Int](0...N)

for _ in 0..<M {
    let ij = readLine()!.split(separator: " ").map{ Int($0)! }
    let i = ij[0]
    let j = ij[1]
    
    for index in 0...(j-i)/2 {
        basket.swapAt(i+index, j-index)
    }
}
print(basket[1...N].map { String($0) }.joined(separator: " "))
