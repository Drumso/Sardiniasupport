# Sardiniasupport

### Test pages
[Panada](https://drumso.github.io/Sardiniasupport/panada)

## Add a new ingredient list for a recipe:

Copy the following text:fregola

1. Copy the following text:
```
---
layout: ingredients_list
ingredients_group_name: Base
ingredients_list: [Fregola, Prezzemolo]
---
```

2. Create a new file in the main directory, with the recipe name. E.g. `nuraghe_pizza.md`.
3. Paste the text and choose your ingredients.


### To edit CSS
Go here: [assets/css/custom.css](https://github.com/Drumso/Sardiniasupport/blob/master/assets/css/custom.css)

- Each ingredient is `.ingredient`
- The whole form is `.ingredient_list`

### To edit ingredients layout (Jekill + HTML):
Go here: [_layouts/ingredients_list.html](https://github.com/Drumso/Sardiniasupport/blob/master/_layouts/ingredients_list.html)

### To edit main layout, including scripts or other CSS:
Go here: [_layouts/default.html](https://github.com/Drumso/Sardiniasupport/blob/master/_layouts/default.html)

