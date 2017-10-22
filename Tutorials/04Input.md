# Input

Write "input".

```python
input
```

Add a pair of parenthesis

```python
input()
```

If you want there to be text before the input, put a variable or a pair of quotation marks and text

```python
input("Yes/No:")
```


## Examples

### Example 1:
```python
input("Do you want an apple? [Y|N]")
```
Run:
```
Do you want an apple? [Y|N]: 
```

### Example 2:
```python
name = "Bob"
input("Is " + name + " your name?")
```
Run:
```
Is Bob your name?
```


### Example 3:
```python
name = input("What is your name?")
print("Hello, " + name + "!")
if name == Bob:
  print("Have a great day, Bob!")
```
Run:
```
What is your name? [Bob]
Hello, Bob!
Have a great day, Bob!
```
Run 2:
```
What is your name? [Joe]
Hello, Joe
```
