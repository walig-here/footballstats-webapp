import datetime

USERS_AFTER_REGISTERING_NEW_USER : tuple[dict] = (
    {'username': 'owner'}, 
    {'username': 'NewUser'}
)

USERS_BEFORE_REGISTERING_NEW_USER : tuple[dict] = (
    {'username': 'owner'},
) 

USERS_AFTER_DELETING_USER : tuple[dict] = (
    {'username': 'owner'},
    {'username': 'Adam'},
)

USERS_BEFORE_DELETING_USER : tuple[dict] = (
    {'username': 'owner'},
    {'username': 'Jerzy'},
    {'username': 'Adam'},
)

ADMIN_ACTIONS_AFTER_DELETING_USER: tuple[dict] = (
    {"id": 1, "action_date": datetime.date(2024,2,1), "action_type_id": 45, "user_id": None},
    {"id": 2, "action_date": datetime.date(2024,2,10), "action_type_id": 46, "user_id": None},
    {"id": 3, "action_date": datetime.date(2024,2,13), "action_type_id": 45, "user_id": None},
    {"id": 4, "action_date": datetime.date(2024,2,13), "action_type_id": 58, "user_id": None},
    {"id": 5, "action_date": datetime.date(2024,3,21), "action_type_id": 45, "user_id": None},
    {"id": 6, "action_date": datetime.date(2024,6,27), "action_type_id": 45, "user_id": None},
    {"id": 7, "action_date": datetime.date(2024,7,13), "action_type_id": 71, "user_id": 3},
    {"id": 8, "action_date": datetime.date(2024,10,14), "action_type_id": 38, "user_id": None},
    {"id": 9, "action_date": datetime.date(2024,10,14), "action_type_id": 59, "user_id": 3},
    {"id": 10, "action_date": datetime.date(2024,11,11), "action_type_id": 45, "user_id": None},
    {"id": 12, "action_date": datetime.date(2024,11,11), "action_type_id": 83, "user_id": 1},
)

ADMIN_ACTIONS_BEFORE_DELETING_USER: tuple[dict] = (
    {"id": 1, "action_date": datetime.date(2024,2,1), "action_type_id": 45, "user_id": 2},
    {"id": 2, "action_date": datetime.date(2024,2,10), "action_type_id": 46, "user_id": 2},
    {"id": 3, "action_date": datetime.date(2024,2,13), "action_type_id": 45, "user_id": 2},
    {"id": 4, "action_date": datetime.date(2024,2,13), "action_type_id": 58, "user_id": 2},
    {"id": 5, "action_date": datetime.date(2024,3,21), "action_type_id": 45, "user_id": 2},
    {"id": 6, "action_date": datetime.date(2024,6,27), "action_type_id": 45, "user_id": 2},
    {"id": 7, "action_date": datetime.date(2024,7,13), "action_type_id": 71, "user_id": 3},
    {"id": 8, "action_date": datetime.date(2024,10,14), "action_type_id": 38, "user_id": 2},
    {"id": 9, "action_date": datetime.date(2024,10,14), "action_type_id": 59, "user_id": 3},
    {"id": 10, "action_date": datetime.date(2024,11,11), "action_type_id": 45, "user_id": 2},
    {"id": 12, "action_date": datetime.date(2024,11,11), "action_type_id": 83, "user_id": 1},
)