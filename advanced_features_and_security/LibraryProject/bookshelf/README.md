## Custom Permissions and Groups

- **Model**: `Book`
- **Permissions**: 
    - `can_view`: Allows viewing books.
    - `can_create`: Allows creating new books.
    - `can_edit`: Allows editing existing books.
    - `can_delete`: Allows deleting books.
- **Groups**:
    - `Editors`: Can create and edit books.
    - `Viewers`: Can view books.
    - `Admins`: Can view, create, edit, and delete books.

### Views with Permission Checks
- `book_list`: Requires `can_view` permission.
- `edit_book`: Requires `can_edit` permission.
## Implementing Security Best Practices in Django

### SECURE_BROWSER_XSS_FILTER
Enables the XSS filter in supported browsers to prevent Cross-Site Scripting attacks.

```python
SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = 'DENY'

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_CONTENT_TYPE_NOSNIFF = True
