// courseState.js

import { atom } from 'recoil';

export const courseState = atom({
  key: 'courseState',
  default: [
    {
        "Year": 22,
        "Index": 10,
        "Category": "MA",
        "Credits Worth": 4,
        "ID": "MA22104",
        "Name": "Introduction to Linear Algebra",
        "Questions": [
          "How well did the course cover fundamental concepts of linear algebra such as vectors, matrices, and systems of equations?",
          "To what extent did the course provide insights into linear transformations, eigenvalues, and eigenvectors?",
          "How useful were the assignments and applications in understanding linear algebra in various fields?"
        ]
      },
      {
        "Year": 22,
        "Index": 1,
        "Category": "MA",
        "Credits Worth": 3,
        "ID": "MA22013",
        "Name": "Calculus I",
        "Questions": [
            "How well did the course cover fundamental concepts of calculus such as limits, derivatives, and integrals?",
            "To what extent did the course provide insights into applications of calculus in real-world problems?",
            "How useful were the assignments and problem-solving exercises in understanding calculus?"
        ]
    },
    {
        "Year": 22,
        "Index": 2,
        "Category": "MA",
        "Credits Worth": 3,
        "ID": "MA22023",
        "Name": "Calculus II",
        "Questions": [
            "How well did the course cover advanced topics in calculus such as techniques of integration and infinite series?",
            "To what extent did the course provide insights into applications of calculus in physics and engineering?",
            "How useful were the assignments and problem-solving exercises in mastering advanced calculus concepts?"
        ]
    }, {
        "Year": 22,
        "Index": 4,
        "Category": "MA",
        "Credits Worth": 3,
        "ID": "MA22043",
        "Name": "Differential Equations",
        "Questions": [
            "How well did the course cover topics such as first-order differential equations, second-order differential equations, and systems of differential equations?",
            "To what extent did the course provide insights into applications of differential equations in modeling real-world phenomena?",
            "How useful were the assignments and problem-solving exercises in mastering differential equations concepts?"
        ]
    },
    // Add more course objects here if needed
  ],
});
