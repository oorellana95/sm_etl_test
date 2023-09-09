# Input Data Documentation - Definition

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

### File: RAW_users.csv

**Description**

The RAW_users.csv dataset contains diverse user profiles, including individuals with a wide range of ages, genders, and occupations. 

**Attributes & Datatypes:**

1. **user id**: Integer
2. **encoded id**: String
3. **first name**: String
4. **Sex**: String (Male or Female)
5. **email**: String (Email format)
6. **phone**: String
7. **date of birth**: Date
8. **job title**: String

**Formatting Considerations:**

1. Each entry is separated by a line break.
2. Each attribute within an entry is separated by a comma.
3. Double quotation marks are used in some "job title" entries due to the presence of commas.
4. Sex can only be Male or Female
5. Phone has no specific format
6. "job title" values seem to be predefined. It repeats across multiple users.

---


## Attribute considerations across the files 

**id_recipe**
- File RAW_recipes: id
- File RAW_interactions: recipe_id

**id_user**
- File RAW_users.csv: user id
- File RAW_interactions.csv: user_id
- File RAW_recipes.csv: contributor_id