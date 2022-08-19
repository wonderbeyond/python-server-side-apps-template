# Keeping common testing data

Shared testings data files can be placed here, with any structure you like.

👽 We also provide some utils for easy test data loading.

```python
import testdata  # yes, "testdata" is also used as a python module

# Loading a testing file relative to the current directory
testdata.load('a/b/c.json')

# Also, we can use glob to load multiple testing files
testdata.gload('a/b/*.json')
```
