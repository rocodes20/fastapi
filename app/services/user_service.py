import pymysql
from app.schemas.user import UserPatch
def create_user(user,db):
    try:
        with db.cursor() as cursor:
            cursor.execute("INSERT INTO users(name,email) VALUES (%s,%s)",(user.name,user.email))
            user_id = cursor.lastrowid
            db.commit()
            return {
                "id":user_id,
                "name":user.name,
                "email":user.email
            }
    except pymysql.MySQLError:
        db.rollback()
        raise RuntimeError("database error")
    
def get_user_by_id(user_id,db):
    with db.cursor() as cursor:
        cursor.execute("SELECT name,email from users where id = %s",(user_id,))
        user = cursor.fetchone()
        if not user:
            raise LookupError("user not found")
        return user
    


def patch_user(user_id,user_update,db):
    updates = {}

    if user_update.name is not None:
        updates["name"] = user_update.name

    if user_update.email is not None:
        updates["email"] = user_update.email

    if not updates:
        raise LookupError("no fields")
    
    with db.cursor() as cursor:
        cursor.execute("Select id from user where id= %s",(user_id,))
        if not cursor.fetchone():
            raise LookupError("not found")
        

    fields = []
    values = []

    for key,value in updates.items():
        fields.append(f"{key}= %s")
        values.append(value)

    values.append(user_id)
    query = f"""
        UPDATE users
        SET {", ".join(fields)}
        WHERE id = %s
    """

    with db.cursor() as cursor:
        cursor.execute(query,tuple(values))
        db.commit()

    return {
        "id":user_id,
        **updates
    }