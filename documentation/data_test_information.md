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

user id,encoded id,first name,last name,Sex,email,phone,date of birth,job title
1,4defE49671cF860,Sydney,Shannon,Male,tvang@example.net,574-440-1423x9799,2020-07-09,Technical brewer
2,F89B87bCf8f210b,Regina,Lin,Male,helen14@example.net,001-273-664-2268x90121,1909-06-20,"Teacher, adult education"
3,Cad6052BDd5DEaf,Pamela,Blake,Female,brent05@example.org,927-880-5785x85266,1964-08-19,Armed forces operational officer
4,e83E46f80f629CD,Dave,Hoffman,Female,munozcraig@example.org,001-147-429-8340x608,2009-02-19,Ship broker
5,60AAc4DcaBcE3b6,Ian,Campos,Female,brownevelyn@example.net,166-126-4390,1997-10-02,Media planner
6,7ACb92d81A42fdf,Valerie,Patel,Male,muellerjoel@example.net,001-379-612-1298x853,2021-04-07,"Engineer, materials"


## Attribute considerations across the files 

**id_recipe**
- File RAW_recipes: id
- File RAW_interactions: recipe_id

**id_user**
- File RAW_users.csv: user id
- File RAW_interactions.csv: user_id
- File RAW_recipes.csv: contributor_id