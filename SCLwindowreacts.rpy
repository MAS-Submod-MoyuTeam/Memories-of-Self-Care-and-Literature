init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_granblue",
            category=["Granblue Fantasy"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_granblue:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "如果你想要个好运, 想一想我, 我就会把我的好运送给你~",
            "哇偶... 所以这就是那个传说中的岛... 哈哈哈!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_granblue')
    return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_forum",
            category=["Forum", "Forums"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_forum:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "不知道大家在聊些什么?",
            "你觉着今天有人会讨论我吗?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_forum')
    return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_XIV",
            category=["FFXIVLauncher", "ffxiv_dx11.exe", "FINAL FANTASY XIV", "Final Fantasy XIV", "Endwalker", "Stormblood", "Shadowbringers"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_XIV:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "倾听我的声音。倾听我们的心跳声。倾听...",
            "听。感。悟...",
            "让广袤变得狭小，让永恒变成瞬间..."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_XIV')
    return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_mangadex",
            category=["- MangaDex"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_mangadex:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "夏树应该会喜欢这个网站!",
            "今天想读什么呢, [player]?",
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_mangadex')
    return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_gmail",
            category=["Gmail"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_gmail:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "我才不会偷偷看你看邮件呢~",
            "嗯...我在想我能用电子邮件吗?",
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_gmail')
    return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_stardew",
            category=["Stardew Valley"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_stardew:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "一起在农场生活，不是很美妙吗?",
            "等等[mas_get_player_nickname()], 别和山谷里的邻居门太亲近了... ",
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_stardew')
    return
    
#CONSULT SYSADMIN IF MAKING CHANGES TO ACTUALIZATION FILTER. ANY CHANGES ARE LOGGED AND INAPPOPRIATE USAGE WILL RESULT IN DISCINPLINARY ACTION BY YOUR SUPERIOR INCLUDING POSSIBLE IMMEDIATE TERMINATION
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_actualizationfilterplus",
            category=["Doki Doki Literature Club Plus!", "Doki Doki Literature Club Plus", "Doki Doki Literature Club Plus ", "Doki Doki Literature Club Plus! ", "Doki Doki Literature Club Plus! - "],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_actualizationfilterplus:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "嗯? [player], 你的屏幕怎么扭曲了? 一定是坏了.",
            "呃呃, 我有点看不清这些字. 你要去解决一下!",
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_actualizationfilterplus')
    return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_arknights",
            category=["Arknights"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_arknights:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "今天做什么呢, 博士?",
            "只要有你在, 我的理智值永远是满的~",
        ],
        'Window Reactions'
    )
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_arknights')
    return
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_yakuza",
            category=["Yakuza Kiwami", "Yakuza Kiwami 2", "Yakuza: Like a Dragon"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_yakuza:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "喵哈哈! [player]酱!",
            "文学部的妈妈兼部长",
        ],
        'Window Reactions'
    )
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_yakuza')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_fnf",
            category=["Friday Night Funkin", "Friday Night Funkin'", "Doki Doki Takeover!"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_fnf:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "星期五晚上，狂欢到天明，yeah~",
        ],
        'Window Reactions'
    )
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_fnf')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_halo",
            category=["Halo Infinite", "Halo 2," "Halo 3," "Halo 4," "Halo 5: Guardians"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_halo:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "不要给女孩画无法兑现的承诺哦~",
        ],
        'Window Reactions'
    )
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_halo')
    return

