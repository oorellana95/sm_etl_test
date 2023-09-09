#  Implement Batch Insert/Upsert and Rollback Decorator

Status: Accepted

Date: 2023-09-08


## Issue

There is a need for a mechanism to handle batch inserts and automatic rollback of transactions in case of exceptions during the ETL process.


## Assumptions

- I am working with SQLAlchemy and a relational database.
- he ETL process involves inserting large batches of data into the database.
- Automatic rollback on exceptions is a desirable behavior to maintain data integrity.


## Constraints

- There is a need to ensure that any exceptions during the batch insert do not leave the database in an inconsistent state.

## Positions

1. Implement a batch insert and rollback decorator for handling transactions during batch inserts.
2. Handle transactions manually without a decorator.


## Opinions

- Using a decorator for batch inserts is a clean and organized way to handle transactions.


## Selection

I selected the position of implementing a batch insert and rollback decorator because it promotes code maintainability, readability, and ensures that transactions are handled consistently across the ETL process. This approach aligns with best practices and reduces the chances of leaving the database in an inconsistent state in case of exceptions during batch inserts.


## Implications

- The decorator will need to be applied to relevant functions in the ETL process.
- The decorator should be well defined and other developers should be aware of and use the decorator for batch inserts to maintain consistency.
- The codebase will become more organized and robust as a result of this decision.


## Related

- This decision is related to our ongoing ETL process and database management practices.
- It may also impact how I handle error logging and exception handling in the ETL pipeline.