# A Simple Text Editor Example using Tkinter

The application under consideration is a simple text editor that supports basic text formatting operations. The system currently provides the following functionalities:
- Paragraph alignment options, including:
    - Left alignment
    - Right alignment
    - Center alignment
- Text styling features applied to selected text, including:
    - Bold formatting
    - Italic formatting
    - Underline formatting

### Problem Description
A critical limitation exists in the current implementation. When modifying global text attributes such as font type or text color, the changes are applied indiscriminately to the entire content of the text editor. This behavior is undesirable, as it prevents selective formatting and reduces the flexibility of the editor.

### Assignment Objective
The objective of this assignment is to identify and resolve the issue such that formatting changes (specifically font type and text color) are applied only to the selected portion of the text, rather than affecting the entire document.

Students are expected to modify the implementation so that text-level styling is handled in a manner that preserves independent formatting for different segments of the text.

### Reference: 
- [https://github.com/anshulhub/My-Editter](https://github.com/anshulhub/My-Editter)

`Note`: A lot of code has been changed from the reference, and the reference itself has the same problem, therefore, I do not believe you can solve the problem using the reference.