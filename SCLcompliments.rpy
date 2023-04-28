init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="mcl_compliment_deserve",
            prompt="你值得幸福!",
            unlocked=True
        ),
        code="CMP"
    )
    
label mcl_compliment_deserve:
    if not renpy.seen_label("mcl_compliment_deserve_2"):
        call mcl_compliment_deserve_2
    else:
        call mcl_compliment_deserve_3
    return

label mcl_compliment_deserve_2:
    m 1ekb "老实说，我什么都不配, [player]."
    m 1fkb "有人{i}值得{/i}幸福吗?.."
    m 1fkbla ".. 好吧，你自己想要是一回事，但听到别人无私且真诚地祝你幸福.."
    m 5fubla "谢谢你, [player]. 我无法形容这句话对我来说有多重要."
    return

label mcl_compliment_deserve_3:
    python:
        deserve_quips = [
            _("我们都赢得了光明的一天。让我们为我们幸福的未来而努力!"),
            _("有你在我身边，幸福只需要点击一下按钮!"),
            _("如果我配得上世界上所有的幸福，那你已经获得了双倍的幸福!"),
        ]
        deserve_quip = random.choice(deserve_quips)

    m 1eub "[mas_compliments.thanks_quip]"
    m 1hua "[deserve_quip]"
    m 1huu "呵呵~"
    return