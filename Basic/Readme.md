<h1> 03. Python Indentation </h1>
<p>Python indentation refers to the spaces at the beginning of a code line, which are used to define the structure and flow of the code. Unlike many other programming languages that use braces or parentheses to define code blocks, Python uses indentation to specify the grouping of statements. </p>

<p>For example, consider the following code snippet:</p>

<pre>
age = 13
if age >= 13:
    print("He is a boy")
else:
    print("She is a girl")
</pre>

<p>In this code, indentation is important. The `if` and `else` blocks must have an indented line for the code to be considered part of their respective blocks. Without proper indentation, you will encounter an "IndentationError." </p>

<h1> 05. Python Variables </h1>
<p>Variables are container for storing data values </p>
<p>Python has no command for declaring a variable</p>
<p> A variable is Create  wehn we  just assign the moment we assign value to it <p/>
<p>For example, consider the following code snippet:</p>

<pre>
x = 5
y = "John"
print(x)
print(y)
</pre>

<p>Variables do not need to be declared with any particular type, and can even change type after they have been set </p>

<h3> Python- variable Names</h3>

<p> A variable can have a short name (like x and y) or a more descriptive name (age,carname, total_volume). Rules for Python variables: 

<pre>
myvar = "john" #it can be written down using all the small letter
my_var = "john" #it Can be written down by underscore to eliminate the gap
_my_var = "john" #it can be written down using first and middle underscore
MYVAR = "john" #it can be written down with all the capital letter 
MYVAR = "john" #it can be written down with  all the capital letter
myvar2 = "john"
    </pre>
<h3>Multiple value and Variable Assigning </h3>
    <h5>One variables and multiple variale assigning </h5>
    <p> we can take one variable and then assign using a comma </p>
    <pre>
        fruits = "apple", "banana" , "Orange"
        print(fruits)
    </pre>

You can output multiple variables by separating them with commas:

```python
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
```

### Using the `+` Operator for Concatenation

You can also use the `+` operator to concatenate strings:

```python
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
```

> **Note:** Be sure to add spaces between strings when concatenating if you want the output to be properly spaced. For example, `"Python" + "is" + "awesome"` would output `Pythonisawesome` without spaces between the words.

### Using `+` with Numbers

For numbers, the `+` operator works as a mathematical operator:

```python
x = 5
y = 10
print(x + y)  # Output: 15
```

### Error When Combining Strings and Numbers

If you try to combine a string and a number with the `+` operator, you will get an error:

```python
x = 5
y = "John"
print(x + y)  # This will raise an error: TypeError: can only concatenate str (not "int") to str
```

### Best Practice for Outputting Variables

The recommended way to output multiple variables of different data types is to separate them with commas in the `print()` function. This will automatically handle different data types:

```python
x = 5
y = "John"
print(x, y)  # Output: 5 John
```

## Conclusion

This repository demonstrates simple techniques for outputting variables in Python using the `print()` function. By following the examples above, you can effectively display variables of different data types and avoid common errors when combining them.
```
Here's a basic `README.md` file template for the Python print function examples:

---

# Python Output Variables - Examples

This README provides examples of how to use Python's `print()` function to output variables.

## Simple Variable Output

You can use the `print()` function to output a single variable.

```python
x = "Python is awesome"
print(x)
```

### Output:
```
Python is awesome
```

## Output Multiple Variables

You can output multiple variables in a single `print()` function by separating them with commas:

```python
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
```

### Output:
```
Python is awesome
```

## Concatenating Strings with the `+` Operator

You can also concatenate multiple strings using the `+` operator.

```python
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
```

### Output:
```
Python is awesome
```

> **Note**: Make sure to add spaces between words if needed to avoid a concatenated string without spaces.

## Math Operations in Print

For numbers, the `+` operator works as a mathematical operator.

```python
x = 5
y = 10
print(x + y)
```

### Output:
```
15
```

## Combining Strings and Numbers

If you try to combine a string and a number using the `+` operator, Python will throw an error.

```python
x = 5
y = "John"
print(x + y)
```

### Error:
```
TypeError: can only concatenate str (not "int") to str
```

### Best Practice: Using Commas for Mixed Data Types

The best way to output multiple variables of different data types (e.g., strings, integers) is by separating them with commas in the `print()` function.

```python
x = 5
y = "John"
print(x, y)
```

### Output:
```
5 John
```

---

This README covers some basic uses of the `print()` function in Python to output variables, from simple to advanced formatting techniques.



You can copy this text into a `README.md` file in your GitHub repository. This will explain how to use the `print()` function for outputting variables in Python. Let me know if you'd like any changes!
