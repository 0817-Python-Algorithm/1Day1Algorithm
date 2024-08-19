//
//  BOJ_10810.swift
//  SwiftAlgorithm
//
//  Created by 윤동주 on 8/22/24.
//

import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
let M = input[1]

var basket = [Int](repeating: 0, count: N+1)

for _ in 0..<M {
    let ijk = readLine()!.split(separator: " ").map { Int($0)! }
    for j in ijk[0]...ijk[1] {
        basket[j] = ijk[2]
    }
}

print(basket[1...N].map { String($0) }.joined(separator: " "))
