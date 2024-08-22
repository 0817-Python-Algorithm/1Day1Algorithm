//
//  BOJ_5597.swift
//  SwiftAlgorithm
//
//  Created by 윤동주 on 8/23/24.
//

import Foundation

var students = [Int](1...30)

for _ in 0..<28 {
    let num = Int(readLine()!)!
    students = students.filter { $0 != num }
}

print(students.map {String($0)}.joined(separator: " "))
