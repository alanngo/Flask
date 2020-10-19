# Sample Backend

## File Structure
```text
- api/ ->           API routes, calls service layer
- repository/ ->    Database connector
    - database.py
- service/ ->       Performs DB operations by calling repository layer
- test/ ->          Unit Tests
    - tests.py
- util/ ->          Error Handling
    - error_advice.py
    - logger.py
- app.py ->         Main app
```


