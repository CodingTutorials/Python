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
Do you want an apple? [Y|N]:[](https://vignette.wikia.nocookie.net/uncyclopedia/images/b/b8/Thin_cursor.gif/revision/latest?cb=20091129041432)
```

### Example 2:
```python
apples = "alot"
if apples == "alot":
  print("You have",apples,"apples")
```
Run:
```
You have alot apples
```


### Example 3:
```python
apples = 1
if apples == 1:
  print("You have",apples,"apples")
apples = 2
if apples == 2:
  print("You have",apples,"apples")
```
Run:
```
You have 1 apples
You have 2 apples
```

## Example 4:
```python
apples = 1
if apples == 1:
  print("You have",apples,"apples")
  apples = 2
if apples == 2:
  print("You have",apples,"apples")
  apples += 1
if apples == 3:
  print("You have",apples,"apples")
```
Run:
```
You have 1 apples
You have 2 apples
You have 3 apples
```
