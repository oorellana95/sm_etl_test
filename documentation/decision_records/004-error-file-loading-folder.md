#  External Folder for Error File Loading

Status: Accepted

Date: 2023-09-08


## Issue

The issue at hand is where and how to manage files in the ETL process, including logs and CSV files containing entries with errors. I need to decide how to handle those error items.


## Assumptions

- Error entries in CSV files need to be stored and processed separately to avoid interrupting the main ETL process.
- External folder creation is technically feasible and manageable within the ETL system.


## Constraints

- The external folder structure and access permissions should be well-defined and secured.
- The ETL process must be updated to handle the new folder structure.
- Regular cleanup and maintenance of logs and error-related files should be implemented to prevent storage issues.

## Positions

1. Create External Folder:
   - Pros: Organizes files, separates error-related CSVs from logs, and ensures smoother ETL processing.
   - Cons: Requires additional development to manage the folder and file interactions.

2. Do Not Create External Folder:
   - Pros: Simplicity .
   - Cons: Can make it harder to locate and process the entries with errors if required.


## Opinions

- I am in favor of creating an external folder to be able to register the entries for check and post-processing operations without stopping the current flow.


## Selection

I have decided to create an external folder for file loading and error logs. This decision is based on the following reasons:

- Organizing files in an external folder improves file management, making it easier to access error-related CSVs.
- Separating error-related CSVs from logs helps in the systematic processing of errors without interrupting the main ETL process.
- I believe this approach enhances ETL organization and error handling.


## Implications

- Development efforts will be required to create and manage the external folder structure within the ETL process.
- Access permissions and security measures should be applied to the external folder to safeguard sensitive data.
- Regular cleanup and maintenance procedures need to be established to prevent the folder from becoming cluttered over time.

## Related:

- Documentation should be updated to reflect the new file management approach.
- Team members should be informed about the folder structure and its purpose.
- Monitoring mechanisms should be in place to track folder usage and prevent storage issues.