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
