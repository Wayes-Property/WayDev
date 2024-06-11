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

def cek_gcast(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2024-present WayMethod <https://github.com/Wayes-Property>
    """
    cursor = conn.execute(
        "SELECT bl_gcast FROM blacklist_gcast WHERE user_id = ?", (user_id,)
    )
    try:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    except:
        return []


def add_gcast(user_id: int, chat_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2024-present WayMethod <https://github.com/Wayes-Property>
    """
    x = cek_gcast(user_id)
    if x:
        xx = eval(x)
        xx.append(chat_id)
        conn.execute("""UPDATE blacklist_gcast SET bl_gcast = ? WHERE user_id = ?""", (str(xx), user_id))
    else:
        x.append(chat_id)
        conn.execute("""INSERT INTO blacklist_gcast (user_id, bl_gcast) VALUES(?,?)""", (user_id, str(x)))
    conn.commit()


def del_gcast(user_id: int, chat_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2024-present WayMethod <https://github.com/Wayes-Property>
    """
    x = eval(cek_gcast(user_id))
    x.remove(chat_id)
    conn.execute("""UPDATE blacklist_gcast SET bl_gcast = ? WHERE user_id = ?""", (str(x), user_id))
    conn.commit()
