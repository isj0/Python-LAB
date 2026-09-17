from admin import Admin

new_admin = Admin('John', 'Doe', 40, 'U', 180, 80)
new_admin.describe_user()
new_admin.privileges.show_privileges()