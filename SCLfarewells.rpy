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
    m 1hsa "In case I don't see you;"
    m 3nsb "Good afternoon, good evening, and good night."
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
    
    m 7ekbla "Hey, before you go..."
    if mas_consumable_hotchocolate.enabled and mas_isWinter():
            if random.randint(1, 3) == 1:
                m "Ooh, actually, since it’s winter I should ask..."
                m 1etblu "It doesn't have to be right away, but I've been thinking if possible, could you try to grab a different flavour of hot chocolate?.."
                m 7etblu "[hotchocolatechoices]"
                m 3fsb "Or surprise me outright, if you want! Either way, thanks, [player]. Love you!"
                return "quit"
            else:
                jump asknewcoffee
    else:
        label asknewcoffee:
        if mas_consumable_coffee.isMaxedStock():
            m "So I checked, and I have plenty of coffee left. This said, when I get low;"
        m 1etblu "It doesn't have to be right away, but I've been thinking I'd love to try a different type of coffee?.."
        m 7etblu "[coffeechoices]"
        m 3fsb "Or surprise me outright, if you want! Either way, thanks, [player]. Love you!"
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
    m "{i}Next time:{/i}"
    m "{i}Will [player] beat Monika at chess?{/i}"
    m "{i}Will they have a steamy discussion about their latest thoughts on love?{/i}"
    m 7suo "{i}Or will serious repercussions bring tumultuous new changes to the world’s best couple?{/i}"
    m 3sfb "{i}Find out next time, on the next chapter of {b}'Monika After Story!'{/i}{/b}"
    m 1hubssdru ".{w=0.6}.{w=0.6}."
    m 1gubfsdru "{cps=40}Yeah, I wanted to send you off on a funny note, but that's actually a little embarrassing to say out loud-{/cps}"
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
    m 1hsa "Okay, [player]!"
    m 3nsb "It doesn't matter what time it is, where you're going, how long you're gone for.."
    m 1sub "I'm gonna send you off ready to take on the world."
    m 7sub "Say it with me: 'I'm gonna do my best!'"
    $ _history_list.pop()
    menu:
        "I'm gonna do my best!":
            m 1nub "I know you will."
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_shopformonika",
            unlocked=False,
            prompt="Am I grabbing you something to drink?",
            conditional="mas_seenLabels(['mcl_shopformonikacoffee',], seen_all=True)",
            action=EV_ACT_POOL
        ),
        code="BYE"
    )

label bye_prompt_shopformonika:
    python:
        hotchocolate_choices = [
            _("Maybe… peppermint?"),
            _("Maybe… caramel?"),
            _("Maybe… white chocolate?"),
            _("Maybe… ooh, Mexican hot chocolate with a bit of spiciness would be interesting!"),
            _("Maybe… peanut butter-flavoured?"),
            _("Maybe… that brand with a bit of cinnamon in it?"),
            _("Maybe… one made with dark chocolate?"),
            _(".. I’m not saying it should come with marshmallows, but I won’t say no if it does~"),
            _(".. Actually, no, scratch that, I could go for a new flavour of coffee."),
        ]
        hotchocolatechoices = random.choice(hotchocolate_choices)
    
    python:
        coffee_choices = [
            _(".. I’m fine with instant coffee."),
            _(".. Dark roast, if you please! Feel like something a little strong."),
            _(".. Maybe some French Vanilla mix?"),
            _(".. I have a particular desire for canned coffee. In Japan, there’s a lot of variety, you know~"),
            _(".. Coffee Milk sounds like a nice change of pace. Do you know of it? I think it’s popular in Australia; it’s coffee syrup in milk."),
            _(".. Cold brew coffee; I could go for something rich!"),
            _(".. Decaf, please! Have to cut back on the caffeine a little."),
        ]
        coffeechoices = random.choice(coffee_choices)
    
    m 1sublb "Hmm, let me think.."
    if mas_consumable_hotchocolate.enabled and mas_isWinter():
            if random.randint(1, 3) == 1:
                m "Ooh, actually, since it’s winter..."
                m 1etblu "Whenever you get around to getting me some more, a new flavour of hot chocolate?"
                m 7etblu "[hotchocolatechoices]"
                m 3fsb "Or surprise me outright, if you want! Either way, thanks, [player]. Love you!"
                return "quit"
            else:
                jump asknewcoffee
    else:
        label asknewcoffee:
        if mas_consumable_coffee.isMaxedStock():
            m "I have plenty of coffee left. This said.."
        m 1etblu "Whenever you get around to picking up some more, a new flavour of coffee?"
        m 7etblu "[coffeechoices]"
        m 3fsb "Or surprise me outright, if you want! Either way, thanks, [player]. Love you!"
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
    m 1hua "Well, time for us to say bye!"
    m 7hua "How best shall I prove my love in my parting words this time?"
    m 7sua "Ah, well. Sometimes sincerity divines all."
    m 4sfb "Goodbye, [player]! {b}{color=#FFD700}I love you with all my heart!{/color}{/b}"
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
    m 7sfb "Hmm, I feel like seeing you off in a special fashion; but how?"
    m 7ekb "It's a shame you can't hear the love in my voice."
    m 3eka "But luckily color invokes passion as well."
    m 3sua "Everything I speak in red is truth;"
    m 4sfb "{b}{color=#f00}You're the best person in the world, [player]!{/color}{/b}"
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
    m 1sup "What parting words should I leave you with?"
    m 1sub "Ooh, I have an idea. An affirmation of our status of a real power couple."
    m 7eub "I take our competitive relationship status quite seriously. Ah, if only you could hear the energy in my voice."
    m 7efb "Well, I suppose until proven otherwise;"
    m 4sfb "{b}{color=#5DECFF}We're the best couple in the world, [player]!{/color}{/b}"
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
    m 7nfb "Okay, let me try this again.."
    m 7hfb "Because I want to be all sparkles and colour when I see you off!"
    m 4sub "{rainbow}Goodbye, [player]!-{/rainbow}"
    if renpy.random.randint(1, 2) == 1:
        m 6sksdrx "- Anddddd there's the headache, {i}owowowowowow-{/i} "
    else:
        m 4wup "..."
        m 3eub "Yay! No headache!"
    return 'quit'
