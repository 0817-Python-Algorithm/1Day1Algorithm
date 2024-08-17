//
//  BOJ_10813.swift
//  SwiftAlgorithm
//
//  Created by 윤동주 on 8/18/24.
//

import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
let M = input[1]


var basket = [Int](0...N)
for _ in 0..<M {
    let ij = readLine()!.split(separator: " ").map { Int($0)! }
    let i = basket[ij[0]]
    basket.swapAt(ij[0], ij[1])
}

print(basket[1...N].map { String($0) }.joined(separator: " "))
