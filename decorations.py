# Decoration mavzusidan 10 da masala yechimi
#

# # masala 1

# is_logged_in = False
#
# def login_required(func):
#     def wrapper():
#         if is_logged_in:
#             return func()
#         else:
#             print("Iltimos, avval login qiling.")
#     return wrapper
#
# @login_required
# def profile():
#     print("Bu sizning profilingiz.")
#
# profile()
#
# is_logged_in = True
# profile()


# # # masala 2
#
# import time
#
# def time_tracker(func):
#     def wrapper():
#         start = time.time()
#         result = func()
#         end = time.time()
#         print(f"Funksiya bajarilishi {end - start:.2f} soniya oldi.")
#         return result
#     return wrapper
#
# @time_tracker
# def long_process():
#     for _ in range(1000000):
#         pass
#     print("Tugadi.")
#
# long_process()


# # masala 3
#
# user_role = "user"
#
# def admin_required(func):
#     def wrapper():
#         if user_role == "admin":
#             return func()
#         else:
#             print("Ushbu funksiya faqat adminlar uchun.")
#     return wrapper
#
# @admin_required
# def delete_user():
#     print("Foydalanuvchi o‘chirildi.")
#
# delete_user()
#
# user_role = "admin"
# delete_user()


# # masala 4



