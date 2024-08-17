//
//  BOJ_10871.swift
//  SwiftAlgorithm
//
//  Created by 윤동주 on 8/17/24.
//

import Foundation

var NX = readLine()!.split(separator: " ").map { Int($0)! }
var N = NX[0]
var X = NX[1]

let A = readLine()!.split(separator: " ").map { Int($0)! }

var result = [Int]()
for i in A {
    if i < X {
        result.append(i)
    }
}

print(result.map { String($0) }.joined(separator: " "))
