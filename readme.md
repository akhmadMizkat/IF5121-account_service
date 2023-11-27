# API Documentation

## Endpoints

### User Login (`/login` - POST)
- **Expected JSON parameters:**
    - `email`: User email
    - `password`: User password
- **Returns:**
    - Success (HTTP 200 OK): User details
    - Failure (HTTP 401 Unauthorized): Error message

### Reset User Password (`/reset_password` - POST)
- **Expected JSON parameters:**
    - `email`: User email
    - `current_password`: User's current password
    - `new_password`: User's new password
- **Returns:**
    - Success (HTTP 200 OK): Success message
    - Failure (HTTP 500 Internal Server Error): Error message

### Admin Login (`/admin/login` - POST)
- **Expected JSON parameters:**
    - `email`: Admin email
    - `password`: Admin password
- **Returns:**
    - Success (HTTP 200 OK): Admin details
    - Failure (HTTP 401 Unauthorized): Error message

### Reset Admin Password (`/admin/reset_password` - POST)
- **Expected JSON parameters:**
    - `email`: Admin email
    - `current_password`: Admin's current password
    - `new_password`: Admin's new password
- **Returns:**
    - Success (HTTP 200 OK): Success message
    - Failure (HTTP 500 Internal Server Error): Error message

### Create Membership (`/register-membership` - POST)
- **Expected JSON parameters:**
    - `email`: User email
- **Returns:**
    - Success (HTTP 200 OK): User email and membership invoice
    - Failure (HTTP 404 Not Found): Error message for email not found

### Update Status Membership (`/update-status-membership` - PUT)
- **Expected JSON parameters:**
    - `email`: User email
    - `status`: New membership status
- **Returns:**
    - Success (HTTP 200 OK): User email and updated membership status
    - Failure (HTTP 404 Not Found): Error message for email not found

### Check Status Membership (`/check-status-membership` - POST)
- **Expected JSON parameters:**
    - `email`: User email
- **Returns:**
    - Success (HTTP 200 OK): User email and membership status
    - Failure (HTTP 404 Not Found): Error message for email not found
