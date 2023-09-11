# Create placeholder users when handling unmatched user_id

Status: Accepted

Date: 2023-09-07


## Issue

The issue at hand is handling unmatched user_id values in the ETL process for recipes and interactions file. I need to decide whether to create a placeholder user and insert it into the database to maintain data integrity.


## Assumptions

- It is assumed that the priority is to preserve the data related with recipes, even in cases where the associated user does not exist in the user_table.
- The ETL process has to have the capability to identify unmatched user_id values in the recipe data.
Placeholder users will have limited or default information


## Constraints

- The placeholder user approach assumes that preserving recipe data is more important than enforcing strict referential integrity with the user_table.
- The placeholder user data should be appropriately managed and documented to distinguish them from real users.


## Positions

1. Create Placeholder User:
   - Pros: Preserves all recipe data, maintains referential integrity, and allows continued processing of recipe data.
   - Cons: Introduces placeholder users that may have limited or default information.

2. Do Not Create Placeholder User:
   - Pros: Enforces strict referential integrity but may result in the loss of recipe data associated with unmatched user_id values.
   - Cons: Recipe data may be incomplete or lost, potentially impacting the ETL process.


## Opinions

- I am in favor of creating placeholder users to ensure data continuity.


## Selection

I have decided to create a placeholder user for unmatched user_id values in the ETL process. This decision is based on the following reasons:

   - Preserving all recipe data aligns with the project's primary goal, which is to process and load recipes into the database.
   - Creating placeholder users allows us to maintain referential integrity while continuing to process and analyze recipe data, minimizing data loss.
   - This approach strikes a balance between data integrity and practicality.


## Implications

- The ETL process will include logic to create and insert placeholder users when unmatched user_id values are encountered.
- Data continuity and completeness will be maintained, and the ETL process will not be disrupted by unmatched user_id values.


## Related

- Documentation and communication within a team to ensure everyone is aware of the use of placeholder users.
- Monitoring and periodic review of the placeholder user data to ensure it remains consistent with the project's objectives.