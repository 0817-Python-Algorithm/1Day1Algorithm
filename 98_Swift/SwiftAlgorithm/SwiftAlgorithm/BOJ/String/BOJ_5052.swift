//
//  main.swift
//  SwiftAlgorithm
//
//  Created by 윤동주 on 8/24/24.
//

import Foundation

let t = Int(readLine()!)!

for _ in 0..<t {
    let n = Int(readLine()!)!
    
    var numbers = [String]()
    
    for _ in 0..<n {
        numbers.append(readLine()!)
    }
    
    numbers.sort()
    
    var answer = "YES"
    
    for i in 0..<n-1 {
        if numbers[i + 1].hasPrefix(numbers[i]) {
            answer = "NO"
            break
        }
    }
    
    print(answer)
}
