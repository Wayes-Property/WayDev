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

from secrets import choice

from AyiinXd import CMD_HELP
from AyiinXd.ayiin.truthdare import Dare as d, Truth as t
from AyiinXd.ayiin import ayiin_cmd, eor

from . import cmd


Tod = ["Truth", "Dare"]


@ayiin_cmd(pattern=r"tod( truth| dare|$)")
async def truth_or_dare(tord):
    trod = tord.pattern_match.group(1).strip()
    TorD = 'Truth' if troll == 'truth' else 'Dare'
    Ayiin = await eor(tord, f"__Memproses {TorD}__")
    troll = choice(Tod)
    if trod == "":
        await tord.edit(f"    __Truth Or Dare ???__\n\n__Didapatkan Secara Acak__\n**      »» {troll} ««**")

    if trod == "truth":
        trth = choice(t)
        await Ayiin.edit(f"__Mendapatkan Hasil Truth Tod__\n\n**»** __Truth__ :\n**»** __{trth}__")
        return

    if trod == "dare":
        dr = choice(d)
        await Ayiin.edit(f"__Mendapatkan Hasil Dare Tod__\n\n**»** __Dare__ :\n**»** __{dr}__")
        return


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "waytod": f"**Plugin:** `waytod`\
        \n\n  »  **Perintah :** `{cmd}tod`\
        \n  »  **Kegunaan :** __Mendapatkan Pilihan Secara Acak.__\
        \n\n  »  **Perintah :** `{cmd}tod <truth/dare>`\
        \n  »  **Kegunaan :** __Untuk Mendapatkan Truth or Dare Secara Acak.__\
    "
    }
)
