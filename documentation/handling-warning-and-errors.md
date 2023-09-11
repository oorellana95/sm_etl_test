# Handling Warnings, Errors an Logs

### Log Levels

- **INFO**: These log messages provide information about the program's normal execution, such as the start and successful completion of certain tasks.
- **WARNING**: These log messages highlight potential issues or warnings during program execution. While they don't necessarily result in program termination, they indicate that something might need attention.
- **ERROR**: These log messages indicate errors that occurred during the program's execution. These errors are uncontrolled exceptions and may lead to the termination of the program or an incorrect processing of part of it.

### Handling Exceptions

Exceptions are errors that were not anticipated by the program and can lead to program termination. These exceptions need to be investigated and resolved to ensure the etl's stability and data insertion.


In the log message for an exception, you see:
- {datetime} - {PROJECT_NAME}:{SERVICE_NAME}: Registers the timestamp, the project and the service module.
- Error code: It indicates the type of error and exception. For completely unconsidered exceptions, it is labeled as "UNCONTROLLED EXCEPTION."
- Additional information (optional): This may include contextual details in a dictionary format.
- Registered items (optional): This section lists items or errors, typically used for batched processes or other relevant information.

For example:
```
2023-09-08 15:23:48.225155 - sm_etl_test:ETL_Service - 
Error code: UNCONTROLLED EXCEPTION;
Traceback (most recent call last):
File w/sm_etl_test/etl/main.py",line15,in<module>
raise Exception ("Testing uncontrolled errors")
Exception: Testing uncontrolled errors
```

```
2023-09-08 15:25:22.622550 - sm_etl_test:ETL_Service - 
Error code: ERROR.FILE_PROCESSING.DATABASE_LOAD;
Additional information: {'file_path': '/sm_etl_test/data_test/input/RAW_interactions.csv','database_url':mysql+pymysql://master:***@localhost:3306/culinary_recipes_mysql};
Registered items:
- f'error_number': 0, 'batch': '0:1000', 'error_message': IntegrityError ("(pymysql.err. IntegrityError) (1452, 'Cannot add or update a child row: a foreign key constraint fails ('culinary_recipes_mysql. 'rating',
Traceback (most recent call last):
File "/sm_etitest/etl/main.py",line15,in<module>
FileDataProcessorInteractions(db_session=db).execute()
File "sm_eti_test/eti/process_file/file_data_processor.ny",Line35,inexecute self._load_data()
File "sm_eti_test/eti/process_file/file_data_processor.ny",line110,in_Load_data raise e
File "sm_etl_test/etl/process_file/file_data_processor.py",Line105,in_load_data self.load_data()
File "Lsm_etItest/etl/process_file/file_data_processor_interactions.ny",line37,inload_data load_ratings(db_session=self.db_session, ratings_dfeself.data)
File "/sm_ett_test/etl/nepositories/nating.ny",line16,inload_ratings _upsert_ratings (db_session, processed_df)
File "/sm_ettest/etl/repositories/nating.py",line40,in_upsert_ratings _upsert_ratings_df_with_valid_id_user (db_session, ratings_df, existing_user_ids)
File "Lsm_etl_test/etl/repositories/rating.py",line48,in_upsert_ratings_df_with_valid_id_user upsert_data(
File "/smetitest/etl/repositories/repository_functions.py",line 1452, in wrapper raise DatabaseTransactionError
etl.exceptions.file_processing_exeptions.database_load_file_processing_error.DatabaseTransactionError
```

### Handling Warnings
Warnings are expected to be processed separately from the regular program flow, owing to inconsistent data. These warnings serve as indicators of additional events, such as the generation of blueprint users or the recording of entries with missing mandatory values. These occurrences are saved in an external folder for further review, as specified in the decision records.

```
WARNING:etl.services.logger:2023-09-08 21:51:24.817987 - sm_etl_test:ETL_Service - A total of 2536 blueprint users have been created with the corresponding ids.
WARNING:etl.services.logger:2023-09-08 21:51:24.858112 - sm_etl_test:ETL_Service - A total of 2536 recipes_file with invalid user IDs have been added to /sm_etl_test/data_test/output/
WARNING:etl.services.logger:2023-09-08 21:57:51.158124 - sm_etl_test:ETL_Service - There are 1 ratings with invalid recipe IDs.
WARNING:etl.services.logger:2023-09-08 21:57:51.158825 - sm_etl_test:ETL_Service - Ratings with invalid recipe IDs have been added to /sm_etl_test/data_test/output/20230908215751_1_ratings_with_invalid_id_recipe.csv for further analysis.
WARNING:etl.services.logger:2023-09-08 21:59:04.067919 - sm_etl_test:ETL_Service - A total of 114358 blueprint users have been created with the corresponding ids.
WARNING:etl.services.logger:2023-09-08 21:59:12.172787 - sm_etl_test:ETL_Service - A total of 114358 ratings with invalid user IDs have been added to /sm_etl_test/data_test/output/
```


