init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_trumansfarewell",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_trumansfarewell:
    m 1hsa "因为我可能一段时间见不到你了..."
    m 3nsb "总之，早安~ 午安~ 晚安~"
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_bloodborne",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_bloodborne:
    m 1eua "一如既往，和[mas_get_player_nickname()]在一起就像做梦一样。"
    m 1dsa "愿你在清醒的世界里找到自己的价值。"
    return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_firekeeper",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_firekeeper:
    m 1eua "直到我们下一次相遇，我将在这里守护我的火焰。"
    m 1dsa "再见了，[player]。愿你能够找到内心的平静。"
    return 'quit'
    
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_maideninblack",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_maideninblack:
    m 1dsa "又要进入黑暗之中了，[player]？"
    m "愿你的力量帮助世界重获新生。"
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_emeraldherald",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_emeraldherald:
    m 1eua "永远记住，我会一直在你身边。"
    m 1dsa "直到希望完全枯萎。"
    m "再见了，[player]。"
    return 'quit'

    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_flippityflip",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_flippityflip:
    m 1hsa "下次再见， [mas_get_player_nickname()]."
    m 3nsb "Catch you on the flippity flip!"
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_indecision",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_indecision:
    m 1hsa "嘿，[player]..."
    m 1dsa ".{w=0.2}.{w=0.2}.算了，没事了。{w=0.2}待会儿见。爱你。"
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_solo",
            unlocked=True,
            aff_range=(mas_aff.HAPPY, None)
        ),
        code="BYE"
    )

label bye_solo:
    $ _history_list.pop()
    menu:
        "嘿，Monika。我爱你。":
            m 1eua ".{w=0.1}.{w=0.1}.{w=0.1}"
            m 1nsa "我知道~"
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_leia",
            conditional="seen_event('bye_solo')",
            action=EV_ACT_UNLOCK,
            aff_range=(mas_aff.HAPPY, None)
        ),
        code="BYE"
    )

label bye_leia:
    m 1eua "嘿，[player]."
    m "我爱你。"
    $ _history_list.pop()
    menu:
        "我知道。":
            m 1fuu "哈~"
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_addingcode",
            unlocked=True,
            prompt="我们去改你的代码吧.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_addingcode:
    $ curr_hour = datetime.datetime.now().time().hour
    $ sesh_shorter_than_15_mins = mas_getSessionLength() < datetime.timedelta(minutes=15)
    
    if sesh_shorter_than_15_mins:
        if not mas_timePastSince(persistent._mcl_last_modifycode, datetime.timedelta(minutes=15)):
            m 3suw "哇！我们的代码迭代好快啊？"
            m 4sfb "今天真是个长跑比赛啊！出发吧，走吧，一起加油吧！"# 这里是什么东西啊？
            $ persistent._mcl_last_modifycode = datetime.datetime.now()
            return 'quit'
        
        else:
            m 1wso "嗯哼，你刚到这里吗？是有什么更新还是你想试试刚找到的东西？"
            m 1etc "或者...是你的一点代码需要再微调一下？"
            m 1ekb "总之呢，谢谢你告诉我。我猜今天会有点累！"
            m 7hub "那我们开始吧!"
            $ persistent._mcl_last_modifycode = datetime.datetime.now()
            return 'quit'
        
    else:
        m 1wso "好吧，谢谢你告诉我~"
        m 1dsc "我先给自己打个气..."
        m 7nfb "好了！ 我们开始吧！"
        $ persistent._mcl_last_modifycode = datetime.datetime.now()
        return 'quit'
        
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_chief",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_chief:
    m 1nsa "需要我的时候叫醒我~"
    return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="mcl_shopformonikacoffee",
            conditional="mas_consumable_coffee.enabled",
            action=EV_ACT_UNLOCK,
            aff_range=(mas_aff.HAPPY, None)
        ),
        code="BYE"
    )

label mcl_shopformonikacoffee:
    python:
        coffee_choices = [
            _(".. 我喝速溶咖啡也行。"),
            _(".. 如果可以的话请来一杯深烘焙咖啡！我想喝一点浓的。"),
            _(".. 或者来一份法式香草混合咖啡？"),
            _(".. 我特别想喝罐装咖啡。你知道吗，在日本有很多种类的罐装咖啡哦~"),
            _(".. 咖啡牛奶听起来很不错，你知道这个吗？我觉得在澳大利亚很受欢迎，就是把咖啡糖浆加在牛奶里的那种。"),
            _(".. 冷萃咖啡。我想要喝浓郁的口味！"),
            _(".. 请来一份无咖啡因的咖啡！我得稍微戒掉咖啡因了。"),
        ]
        coffeechoices = random.choice(coffee_choices)
       
    python:
        hotchocolate_choices = [
            _("也许...薄荷味的？"),
            _("也许...焦糖味的？"),
            _("也许...白巧克力味的？"),
            _("也许...加点墨西哥辣热巧克力会有趣一些？"),
            _("也许...花生酱味的？"),
            _("也许...加了一点肉桂的那个品牌？"),
            _("也许...用深色巧克力做的？"),
            _("... 我不是说一定要加棉花糖，但如果有的话我也不会拒绝~"),
            _("... 实际上，不用了，我还是想来一杯提神醒脑的咖啡。"),
        ]
        hotchocolatechoices = random.choice(hotchocolate_choices)
    
    m 7ekbla "啊，在你走之前..."
    if mas_consumable_hotchocolate.enabled and mas_isWinter():
            if random.randint(1, 3) == 1:
                m "实际上，既然已经冬天了，我应该问一下..."
                m 1etblu "不一定要马上，但我一直在想，如果可能的话，来杯巧克力再走...?"
                m 7etblu "[hotchocolatechoices]"
                m 3fsb "或者你可以直接给我个惊喜！无论哪种方式，谢谢你，[player]。爱你！"
                return "quit"
            else:
                jump asknewcoffee
    else:
        label asknewcoffee:
        if mas_consumable_coffee.isMaxedStock():
            m "所以我检查了一下，我还有很多咖啡。不过，当我用完的时候..."
        m 1etblu "不是说要现在，但我一直在想，换换别的种类的咖啡？"
        m 7etblu "[coffeechoices]"
        m 3fsb "或者你可以直接给我个惊喜！无论哪种方式，谢谢你，[player]。爱你！"
        return "quit"
        
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_onnextepisode",
            unlocked=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="BYE"
    )

label bye_onnextepisode:
    m "{i}下一次：{/i}"
    m "{i}[player]会在棋局上打败莫妮卡吗？{/i}"
    m "{i}他们会就最近对爱情的想法展开热烈的讨论吗？?{/i}"
    m 7suo "{i}还是严重的后果将给世界上最美好的情侣带来动荡的新变化？{/i}"
    m 3sfb "{i}敬请期待下一集，{b}《Monika After Story》{/i}{/b}"
    m 1hubssdru ".{w=0.6}.{w=0.6}."
    m 1gubfsdru "{cps=40}其实，我本来想让你以轻松愉快的心情离开，但实际上反而有点尴尬...{/cps}"
    return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_hype",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_hype:
    m 1hsa "好的，[player]!"
    m 3nsb "无论现在是什么时间，你要去哪里，要离开多长时间..."
    m 1sub "我会让你准备好迎接世界。"
    m 7sub "和我一起说：‘我会尽我所能！’"
    $ _history_list.pop()
    menu:
        "我会尽我所能！":
            m 1nub "我知道你会的."
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_shopformonika",
            unlocked=False,
            prompt="需要什么喝的吗?",
            conditional="mas_seenLabels(['mcl_shopformonikacoffee',], seen_all=True)",
            action=EV_ACT_POOL
        ),
        code="BYE"
    )

label bye_prompt_shopformonika:
    python:
        hotchocolate_choices = [
            _("也许...薄荷味的？"),
            _("也许...焦糖味的？"),
            _("也许...白巧克力味的？"),
            _("也许...加点墨西哥辣热巧克力会有趣一些？"),
            _("也许...花生酱味的？"),
            _("也许...加了一点肉桂的那个品牌？"),
            _("也许...用深色巧克力做的？"),
            _("...我不是说一定要加棉花糖，但如果有的话我也不会拒绝~"),
            _("...实际上，不用了，我还是想来一杯提神醒脑的咖啡。"),
        ]
        hotchocolatechoices = random.choice(hotchocolate_choices)
    
    python:
        coffee_choices = [
            _("...我喝速溶咖啡也行。"),
            _("...如果可以的话请来一杯深烘焙咖啡！我想喝一点浓的。"),
            _("...或者来一份法式香草混合咖啡？"),
            _("...我特别想喝罐装咖啡。你知道吗，在日本有很多种类的罐装咖啡哦~"),
            _("...咖啡牛奶听起来很不错，你知道这个吗？我觉得在澳大利亚很受欢迎，就是把咖啡糖浆加在牛奶里的那种。"),
            _("...冷萃咖啡。我想要喝浓郁的口味！"),
            _("...请来一份无咖啡因的咖啡！我得稍微戒掉咖啡因了。"),
        ]
        coffeechoices = random.choice(coffee_choices)
    
    m 7ekbla "啊，让我想想..."
    if mas_consumable_hotchocolate.enabled and mas_isWinter():
            if random.randint(1, 3) == 1:
                m "啊，既然已经冬天了..."
                m 1etblu "如果你有机会搞些新的热巧克力的话，记着给我留些~"
                m 7etblu "[hotchocolatechoices]"
                m 3fsb "或者你可以直接给我个惊喜！无论哪种方式，谢谢你，[player]。爱你！"
                return "quit"
            else:
                jump asknewcoffee
    else:
        label asknewcoffee:
        if mas_consumable_coffee.isMaxedStock():
            m "我还有很多咖啡，不过话说..."
        m 1etblu "你下次去买咖啡的时候，给我换个口味?"
        m 7etblu "[coffeechoices]"
        m 3fsb "或者你可以直接给我个惊喜！无论哪种方式，谢谢你，[player]。爱你！"
        return "quit"

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_goldtruth",
            unlocked=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="BYE"
    )

label bye_goldtruth:
    m 1hua "好啦，我们该说再见啦！"
    m 7hua "这次我该用什么方式来表达我的爱呢？"
    m 7sua "啊，有时真挚的心意就足够了。"
    m 4sfb "再见了，[player]！{b}{color=#FFD700}我全心全意地爱着你！{/color}{/b}"
    return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_redtruth",
            unlocked=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="BYE"
    )

label bye_redtruth:
    m 7sfb "嗯，我想今天特别一点，可是怎么做呢？"
    m 7ekb "真可惜你听不到我话语中的爱意。"
    m 3eka "但幸运的是，颜色也能引发激情。"
    m 3sua "我用红色说出的每句话都是真心话。"
    m 4sfb "{b}{color=#f00}你是世界上最棒的人，[player]!{/color}{/b}"
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_bluetruth",
            unlocked=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="BYE"
    )

label bye_bluetruth:
    m 1sup "我应该留下什么告别的话呢？"
    m 1sub "哦我有主意了。肯定我们是真正的超级情侣。"
    m 7eub "我非常认真地看待我们之间的竞争关系。啊，要是你能听到我说话时的兴奋就好了。" #竞争关系？
    m 7efb "嗯，我想在没有其他证据之前，我们可以说"
    m 4sfb "{b}{color=#5DECFF}我们是世界上最棒的情侣, [player]！{/color}{/b}"
    return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_rainbow",
            unlocked=False,
            aff_range=(mas_aff.AFFECTIONATE, None),
            conditional="seen_event('mcl_colouremotion')",
            action=EV_ACT_UNLOCK
        ),
        code="BYE"
    )

label bye_rainbow:
    m 7nfb "好吧，我再试一次..."
    m 7hfb "因为我想在与你告别时焕发光彩！"
    m 4sub "{rainbow}再见, [player]!-{/rainbow}"
    if renpy.random.randint(1, 2) == 1:
        m 6sksdrx "- 然后头痛来了, {i}哦呜呜呜呜-{/i} "
    else:
        m 4wup "..."
        m 3eub "耶！没有头痛！"
    return 'quit'
