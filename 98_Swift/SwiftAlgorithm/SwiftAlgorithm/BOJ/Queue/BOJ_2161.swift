//
//  BOJ_2161.swift
//  SwiftAlgorithm
//
//  Created by 윤동주 on 8/24/24.
//

import Foundation

let N = Int(readLine()!)!

var cards = [Int](1...N)

var result = [Int]()

while cards.count > 0 {
    result.append(cards.removeFirst())
    
    if cards.count == 0 {
        break
    }
    
    let card = cards.removeFirst()
    cards.append(card)
}

print(result.map { String($0) }.joined(separator: " "))
