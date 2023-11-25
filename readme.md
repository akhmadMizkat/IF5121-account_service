""" 
Endpoints:
- /login (POST): User login
- /reset_password (POST): Reset user password
- /admin/login (POST): Admin login
- /admin/reset_password (POST): Reset admin password
"""

    """
    User login endpoint.

    Expected JSON parameters:
    - email: User email
    - password: User password

    Returns:
    - Success: User details with status code 200
    - Failure: Error message with status code 401
    
    """
    
        """
    Reset user password endpoint.

    Expected JSON parameters:
    - email: User email
    - current_password: User's current password
    - new_password: User's new password

    Returns:
    - Success: Success message with status code 200
    - Failure: Error message with status code 500
    """
    
       """
    Admin login endpoint.

    Expected JSON parameters:
    - email: Admin email
    - password: Admin password

    Returns:
    - Success: Admin details with status code 200
    - Failure: Error message with status code 401
    """
    
     """
    Reset admin password endpoint.

    Expected JSON parameters:
    - email: Admin email
    - current_password: Admin's current password
    - new_password: Admin's new password

    Returns:
    - Success: Success message with status code 200
    - Failure: Error message with status code 500
    """