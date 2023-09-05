# Documentation - Data

## The Files

### File: RAW_recipes.csv

**Description:**

The RAW_recipes.csv dataset contains a collection of culinary recipes in raw, unprocessed form.

**Attributes & Datatypes:**

1. **name:** String (No quotation marks)
2. **id:** Integer
3. **minutes:** Integer
4. **contributor_id:** Integer
5. **submitted:** Date
6. **tags:** Array of Strings (Quotation marks around the entire array)
7. **nutrition:** Array of Floats (Quotation marks around the entire array)
8. **n_steps:** Integer
9. **steps:** Array of Strings (Quotation marks around the entire array)
10. **description:** String and Nullable (Double quotation marks)
11. **ingredients:** Array of Strings (Quotation marks around the entire array)
12. **n_ingredients:** Integer

**Formatting Considerations:**

1. Each entry is separated by a line break.
2. Each attribute within an entry is separated by a comma.
3. Arrays, like "tags", "nutrition", "steps", and "ingredients" are enclosed in quotation marks.
4. Double quotation marks are used for the "description" attribute due to the potential presence of line breaks and special characters, including commas.
5. For attributes that use double quotation marks within their values, such as "description", four consecutive quotation marks represent the pair of double quotation marks (e.g., "He is the “”best”” developer").
6. There are some extra spaces within strings.

---

### File: RAW_interactions.csv

**Description:**

The RAW_interactions.csv dataset provides valuable insights into user interactions with respect to recipes. The dataset allows for the analysis of user preferences, recipe popularity, and user feedback on a wide variety of recipes. 

**Attributes & Datatypes:**

1. **user_id:** Integer
2. **recipe_id:** Integer
3. **date:** Date
4. **rating:** Integer
5. **review:** String

**Formatting Considerations:**

1. Each entry is separated by a line break.
2. Each attribute within an entry is separated by a comma.
3. Double quotation marks are used for the "review" attribute due to the potential presence of line breaks and special characters, including commas.
4. For attributes that use double quotation marks within their values, such as "review", four consecutive quotation marks represent the pair of double quotation marks (e.g., "He is the “”best”” developer").

---

### File: PP_recipes.csv

**Description:**

The PP_recipes.csv describes recipes with token details about ingredients, preparation steps, and other attributes related to the recipes.

**Attributes & Datatypes:**

1. **id**: Integer
2. **i**: Integer
3. **name_tokens**: Array of Integers (Quotation marks around the entire array)
4. **ingredient_tokens**: Array of Arrays of Integers (Quotation marks around the entire array)
5. **steps_tokens**: Array of Integers (Quotation marks around the entire array)
6. **techniques**: Array of Booleans (Quotation marks around the entire array)
7. **calorie_level**: Integer (Always 0?)
8. **ingredient_ids**: Array of Integers (Quotation marks around the entire array)

**Formatting Considerations:**

1. Each entry is separated by a line break.
2. Each attribute within an entry is separated by a comma.
3. Arrays, like "name_tokens", "ingredient_tokens", "steps_tokens", "techniques" and "ingredient_ids" are enclosed in quotation marks.

---

### File: PP_users.csv

**Description**

The PP_users.csv dataset appears to be related to some kind of recommendation system, where users are associated with certain techniques and items they have interacted with, and the ratings they have given to those items.

**Attributes & Datatypes:**

1. **u**: Integer
2. **techniques**: Array of Integers (Quotation marks around the entire array)
3. **items**: Array of Integers (Quotation marks around the entire array)
4. **n_items**: Integer
5. **ratings**: Array of Floats (Quotation marks around the entire array)
6. **n_ratings**: Integer

**Formatting Considerations:**

1. Each entry is separated by a line break.
2. Each attribute within an entry is separated by a comma.
3. Arrays, like "techniques", "items" and "ratings" are enclosed in quotation marks.

---

## Attribute considerations across the files 

**id_recipe**
- File RAW_recipes: id
- File RAW_interactions: recipe_id
- File PP_recipes: id
- File PP_users: items[i]

**ingredients**
RAW_recipes: ingredients[x] -> Ingredient's name
PP_recipes: ingredient_ids[x] -> Ingredient's id