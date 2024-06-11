# Way - Userbot
# Copyright (C) 2024-2025 @wayMethodd
#
# This file is a part of < https://github.com/Wayes-Property/WayDev >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Wayes-Property/WayDev/blob/main/LICENSE/>.
#
# FROM Way-Userbot <https://github.com/Wayes-Property/WayDev>
# t.me/WayChatss & t.me/WayDevv


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from .core import db

conn = db.get_conn()


# ========================×========================
#              BLACKLIST GCAST DATABASE
# ========================×========================

def sudoer():
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2024-present WayMethod <https://github.com/Wayes-Property>
    """
    cursor = conn.execute(
        "SELECT user_id FROM sudoer"
    )
    try:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    except:
        return []


def add_sudo(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2024-present WayMethod <https://github.com/Wayes-Property>
    """
    x = sudoer()
    if x:
        xx = eval(x)
        xx.append(user_id)
        conn.execute("""UPDATE sudoer SET user_id = ?""", (str(xx), user_id))
    else:
        x.append(user_id)
        conn.execute("""INSERT INTO sudoer (user_id) VALUES(?)""", (str(x),))
    conn.commit()


def del_sudo(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2024-present WayMethod <https://github.com/Wayes-Property>
    """
    x = eval(sudoer())
    x.remove(user_id)
    conn.execute("""UPDATE sudoer SET user_id = ?""", (str(x),))
    conn.commit()
