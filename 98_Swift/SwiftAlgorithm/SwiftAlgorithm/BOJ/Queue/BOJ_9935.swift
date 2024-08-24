//
//  BOJ_9935.swift
//  SwiftAlgorithm
//
//  Created by 윤동주 on 8/23/24.
//

import Foundation

var arr = readLine()!
var bomb = readLine()!

var stack = [Character]()

for char in arr {
    stack.append(char)
    
    if stack.count >= bomb.count {
        // bomb의 마지막 문자부터 역순으로 비교
        var isMatch = true
        for i in 0..<bomb.count {
            if stack[stack.count - bomb.count + i] != bomb[bomb.index(bomb.startIndex, offsetBy: i)] {
                isMatch = false
                break
            }
        }
        
        // 일치하면 bomb.count만큼 요소를 제거
        if isMatch {
            stack.removeLast(bomb.count)
        }
    }
}

print(stack.isEmpty ? "FRULA" : String(stack))
