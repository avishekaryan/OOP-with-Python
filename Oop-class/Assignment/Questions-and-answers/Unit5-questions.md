# Unit 5: Writing GUIs in Python : Questions

**Course:** BT151CO — Object-Oriented Programming  
**Level:** Bachelor

---

- **Q1:** Explain the event-driven programming model. How does it differ from traditional sequential programming?

- **Q2:** Why is `root.mainloop()` always placed as the last line in a Tkinter application?

- **Q3:** Can a Tkinter application run without calling `mainloop()`? What would happen?

- **Q4:** What is the purpose of a callback function in Tkinter? Provide an example scenario.

- **Q5:** What is the root window (`tk.Tk()`) and why is it essential?

- **Q6:** Explain the difference between `root.title()`, `root.geometry()`, and `root.configure()`.

- **Q7:** What does `root.protocol("WM_DELETE_WINDOW", func)` do? Why might you use it?

- **Q8:** How would you prevent a Tkinter window from being resized?

- **Q9:** Why is it incorrect to write `command=my_function()`? What is the correct syntax?

- **Q10:** Explain the "late-binding trap" in lambda functions within loops. Provide a solution.

- **Q11:** How can you pass arguments to a callback function? Give a practical example.

- **Q12:** What is the difference between button states `'normal'`, `'disabled'`, and `'active'`?

- **Q13:** Design a toggle button that switches between "ON" and "OFF" states. How would you implement it?

- **Q14:** What is the purpose of the `.strip()` method when reading Entry widget input?

- **Q15:** Explain three validation strategies for Entry widgets.

- **Q16:** How do you clear an Entry widget and set a default value programmatically?

- **Q17:** What does `entry.bind("<Return>", callback)` do?

- **Q18:** Design a password Entry field with a "Show/Hide Password" checkbox. Describe the logic.

- **Q19:** How would you implement an Entry widget that accepts only numeric input?

- **Q20:** Explain the concept of two-way binding between Tkinter variables and widgets.

- **Q21:** What are the four main Tkinter variable types? Give appropriate use cases for each.

- **Q22:** How does `tk.StringVar()` differ from a regular Python string? Why use it?

- **Q23:** Write code to track changes in a `StringVar` using `trace_add()`.

- **Q24:** Compare managing an Entry without `StringVar` versus with `StringVar`. What are the advantages?

- **Q25:** Explain the indexing format for Text widgets. What does `"line.column"` mean?

- **Q26:** What is the difference between `tk.END` and `"end-1c"` when reading Text widget content?

- **Q27:** How do you implement tags in a Text widget? Provide a practical example.

- **Q28:** Design a read-only Text widget that displays logs. How would you prevent user editing?

- **Q29:** Write code to automatically scroll a Text widget to the bottom when new text is added.

- **Q30:** How would you implement text selection in a Text widget? Explain the use of `"sel.first"` and `"sel.last"`.

- **Q31:** Explain how `BooleanVar` works with Checkbutton widgets.

- **Q32:** How would you create a "Select All / Deselect All" master checkbox?

- **Q33:** Design a form that collects multiple selected options and prints them. How would you implement it?

- **Q34:** When would you use Checkbutton instead of Radiobutton? Explain the semantic difference.

- **Q35:** Explain why you cannot mix `pack()` and `grid()` in the same container. How do you solve this?

- **Q36:** Compare `pack()`, `grid()`, and `place()`. In which scenarios is each best suited?

- **Q37:** Explain key `grid()` options: `row`, `column`, `sticky`, `columnspan`, and `rowspan`.

- **Q38:** Design a login form using `grid()` that aligns labels and entry fields. Include validation.

- **Q39:** What are the steps to build a complete multi-widget Tkinter application from scratch?

- **Q40:** What are common best practices for professional Tkinter applications?