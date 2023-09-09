# Use SQLAlchemy ORM for ETL Project

Status: Accepted

Date: 2023-09-07


## Issue

The issue at hand is selecting the appropriate data access framework for our small ETL project, which needs to be delivered within a tight  deadline. I need to decide whether to use SQLAlchemy ORM or not.


## Assumptions

- I assume that the project's requirements could evolve, including the possibility of switching to different relational databases.
- The developer has expertise in working with SQLAlchemy ORM.


## Constraints

- Strict short timeline for project delivery.
- The team should have adequate knowledge and experience with SQLAlchemy ORM.


## Positions

1. Use SQLAlchemy ORM: This option offers versatility in switching between relational databases and leverages the developer's expertise.
2. Do not use any ORM: This option would involve writing custom SQL queries and better performance.



## Opinions

- I am generally in favor of using SQLAlchemy ORM due to its versatility and my expertise.


## Selection

I have decided to use SQLAlchemy ORM for the ETL project, considering the benefits it offers and comparing them with the benefits offered by not using an ORM for this projects:

1. Use SQLAlchemy ORM:
   - Rapid Development: SQLAlchemy ORM accelerates development by allowing Python objects instead of raw SQL queries.
   - Pythonic Approach: It aligns with our team's Pythonic coding style.
   - Code Maintainability: ORM improves code maintainability and readability.
   - Portability: It enables switching between database backends.
   - Security: Protects against SQL injection.

2. Do not use any ORM:
   - Performance: ORM may introduce overhead; however, for this small-scale project, the impact is minimal.
   - Small Projects: ORM overhead may not be justified for very simple projects with minimal database interaction.

In conclusion, given the project's constraints and the advantages of SQLAlchemy ORM in terms of development speed, maintainability, and security, I believe it's the most suitable choice for our ETL project.


## Implications

- The team needs to allocate time for setting up and configuring SQLAlchemy ORM for the project.
- The developer will need to ensure that the ORM is used efficiently to meet the tight deadline.
- Any future changes to the choice of database should be straightforward to implement due to the ORM's flexibility.


## Related

- Follow-up needs may include documenting best practices for using SQLAlchemy ORM within the team to ensure consistency in future projects.