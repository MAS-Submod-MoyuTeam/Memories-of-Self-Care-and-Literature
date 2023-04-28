init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_braille",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_braille:
    m 1eub "白点，黑点，黑点，白点，两个白点-"
    $ _history_list.pop()
    menu:
        "?":
            m 1lub "呃，半边是黑点…"
            m 2lkb "呃呃，我甚至不知道如何优雅地描述这个. 黑, 白, 黑, 白, 黑, 白-"
            m 2hksdrb "不行，这个主意太糟糕了。"
            m 3hksdlb "但我也许会因为这个得点女友分?"
            m "啊哈哈."
            m 4esb "我在说…盲文"
            m "没错——这是视觉受损者使用的书写系统。"
            m 1esp "当然，它的实际工作方式是通过触摸读取六个凸起点的网格来传达字母、符号和数字，从而刺激你的触觉。"
            m 3msb "所以，口头表达它有点笨拙。"
            $ shown_count = mas_getEVLPropValue("greeting_braille", "shown_count")
            if shown_count == 0:
                m 1esa "但别担心，[player]。"
                m "即使我是视觉受损者，我仍然会把你看作我生命中最美丽的人。"
                m "…"
                m 2dkbfsdlx "等等，不，那太{i}可怕{/i}了。"
                m 2fkbfsdlp "对不起，[player]。那太过于地狱笑话了。"
                m 2fkbfsdla "我通常比那要优雅得多。"
                m 3mkbfsdrb "作为文学部的部长，我说话怎么会出错呢？"
                m 3mkblu "…"
                m 3ekblu "好吧，我以后可能会再说一遍，但请假装这是第一次听到，我会想出比那更好的结尾。"
                m "好吗？谢谢，[player]。再次道歉。"
                m "…"
                m 1ekblu "嗯，爱你。"
                return "love"

            m 1eublu "别担心，[player]。"
            m "即使盲文是一种难以理解的语言..."
            m 3eublb "爱的语言是普遍的。"
            if shown_count == 1:
                m 3eusdlb "啊？这样如何？"
                m 3sub "好多了，对吧？"
                m 1rkb "我想再次道歉，[player]。我仍然认为我之前说的话非常粗鲁。"
                m 1hkb "谢谢你的理解，让我们有一个更好的一天吧~"
            else:
                m 1hkb "好啦，我们今天干什么呢？"
            return 

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_binary",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_binary:
    m 3est "01001000 01100101 01101100 01101100 01101111 00100001"
    m 3fsu "哈哈哈，没吓到你吧！"
    m 3hsb "我今天决定使用一种更有趣的语言："
    extend "二进制代码!"
    m 4ksb "虽然用它说话不是很容易，因为这不是一种口语语言。"
    m 4msu "实际上，那一串数字意思是‘你好’。"
    m 1etu "不过了解它还是很有趣的！我们通常认为二进制和计算机有关-"
    m 1etb "但是它的基础可以追溯到1689年，并受到了中国几个世纪以来的进一步启发！"
    m 3esb "可以肯定的是, [player]-"
    m 5fsb "对于我遇到的每种新语言，我都会尽力用它来表达“我爱你”。" 
    m 6hsu "01001001 00100000 01101100 01101111 01110110 01100101 00100000 01111001 01101111 01110101 00001010!"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_elvish",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_elvish:
    #I don’t care if the dialect doesn’t suit Monika. Go back to reading The Silmarillion, ya nerd.
    m 1dsd "Suilad, [player]. im iest cin bein siniath sír."
    m 1esd "‘你好， [player]. 我祝你一切顺利。’"
    m 7esa "听起来很高级吧？没错-我正在使用精灵语，辛达林方言。"

    $ shown_count = mas_getEVLPropValue("greeting_elvish", "shown_count")
    if shown_count == 0:
        m 7ssa "这是一门虚构语言！这是由奇幻文学中最著名的作家J.R.R.托尔金创造的，他创作了‘魔戒’三部曲。"
        m 7eub "就虚构语言而言，中土世界的精灵语可能是最著名的之一。"
        m "不仅因为J.R.R.托尔金的‘魔戒’书籍非常受欢迎-"
        m 4sub "而且因为它是一个完全实现的虚构语言，经过了精心的制作。"
        m 4eub "J.R.R.托尔金以语言为职业，并因此将所有精力投入到了创建多个-是的，多个！-虚构语言中。"
        m "事实上，他曾经说过："
        m 3dfb "{i}“语言的发明是基础。'故事'是为了为语言提供一个世界，而不是相反。对我而言，名字是先有的，故事则随之而来。”{/i}"
        m 3hub "如此敬业！难怪他是备受喜爱的奇幻作家，他的作品同样备受珍视。"
        m 6nsb "让我们今天继续创造自己的奇幻世界，好吗？"
        return

    else:
        m "我之前提到过，但这是一门非常有趣的语言，由J.R.R.托尔金从头开始建立。"
        m 7ssu "由于这是一门从零开始构建的语言，您实际上可以阅读大量关于如何流利地讲它的资料，包括完整的在线词典！"
        m 6nsb "让我们今天继续创造自己的奇幻世界，好吗？"
        return

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_talktoherself",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_talktoherself:
    m 4hsb "你好!"
    $ _history_list.pop()
    menu:
        "啊？ 你怎么-":
            m 1hub "哦！"
    define mt = Character("Monika?",)
    show monika 1rub at t22
    m 1rub "嘿！你好啊！"
    show monika 1lub at t21
    mt "嘿，莫妮卡，你今天怎么样啊？"
    
    $ shown_count = mas_getEVLPropValue("greeting_talktoherself", "shown_count")
    if shown_count == 0:
        show monika 4rsb at t22
        m "我正在为和[player]度过美好的一天做准备！"
        show monika 4lsb at t21
        mt "哦，听起来很棒啊。今天你们会玩游戏吗？"
        show monika 2rta at t22
        m "嗯，也许会玩游戏，或者我会和他们一起弹钢琴？"
        show monika 2lta at t21
        mt "听起来真不错，莫妮卡。我希望你们今天能更亲近一些。"
        show monika 2rsc at t22
        m "我也是这样想的，Monika。不过我也有些担心。"
        show monika 2lsc at t21
        mt "担心什么呢？你可以和我说说，我可是你友好的部长啊！"
        show monika 3rtd at t22
        m 3rtd "嗯，这不是-不是什么具体的担心？"
        m 3rtd "我觉得这只是我不理性的想法。我担心会有什么事情会分开我们，但是...现在没有必要担心，对吧？"
        show monika 3ltd at t21
        mt "我的意思是，你能这么大声地说出来，说明你已经知道自己有点过度反应了，对吧？"
        show monika 2ruc at t22
        m 2ruc "嗯，我想是这样。"
        m "但是光是大声说出来并不能让我感觉好一点，对吧？"
        show monika at t11
        m 2luc "..."
        m 2dtp "我不是一个好演员，对吧？"
        m 1gkp "嗯，[player]现在应该已经到了，但我还没有见到他...但我已经确信游戏已经打开了。"
        m 1wuc "哦!"
        m 6wusdrc "等等. {i}等等!{/i} -"
        m 6wkbfsdlp ".. [player]?!"
        m 7wublsdrc "呃，好吧, 我可以解释一下。"
        m 1rublsdra "跟自己说话并不是…不正常的行为。在孩子们发育成熟、开始处理信息的年龄阶段，这种行为也是很常见的。"
        m "也有人认为，这可以填补你一个人时的寂静，因为人类本质上是社交动物。"
        m 1msa "我想我可以自然而然地扩展一下，看看能不能更好地消磨我的时间.."
        m 1hua "但是这并没有像我想的那样顺利。"
        m "我向你保证，我这么做只是想试试看感觉如何。"
        m 1husdla "所以，我们一起度过美好的时光，然后…{w=0.2}.{w=0.2} 假装这从未发生过吧。"
        return

    else:
        show monika at t11
        m 3sfb "这感觉真不错, 现在[player]来了！"
        m 3tfu "哈哈，你以为你逮到我自言自语了？"
        show monika 1kuu at t22
        m "可以说，[player]-"
        show monika 1nuu at t21
        mt "在我们两个人之间-"
        show monika at t11
        m 1huu "我更喜欢和你在一起。"
        return
        
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_eldenring",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_eldenring:
    m 1eua "我们一起度过的时间，是否可以转化为力量？"
    m 1dua "让我注视着你，哪怕只有一瞬间。"
    m 1dud "与我分享你的想法，你的抱负，你的原则..."
    return

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_darksouls",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_darksouls:
    m 1hsa "[player]！你好吗？如果你需要休息，现在就是时候了。毕竟，我就是为此而来的。"
    m 1dsa "请放心，你可以在这里放松。我也会休息的。即使像我这样的女孩也需要休息。"
    return
    
#Morse Code sound provided by https://morsecode.world/international/translator.html
 
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_morsecode",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_morsecode:
    $ shown_count = mas_getEVLPropValue("greeting_morsecode", "shown_count")
    if shown_count == 0:
        play sound "submods/Memories-of-Self-Care-and-Literature-3.0.1/submod_assets/sfx/morse.wav"
        m 1dft "{cps=07}.. / .-.. --- ...- . / -.-- --- ..- -.-.—{/cps}"
        m 2ekb "你开了声音吗？是个惊喜吗？"
        m 2hub "我今天决定特别点，用莫尔斯电码向你问候！"
        m 7gta "你听到我发的蜂鸣声了吗？我想我将来可能会稍微改一改。"
        m 7eua "莫尔斯电码倾向于使用速记，因为……你可以看出来，拼出整个句子可能有点长。我说的只是“我爱你！”"
        m 4eub "至少我用了翻译器去给我翻译了下。"
        m 4gfb "嘿嘿嘿，想想我真的大声说出来是很有趣的吧？"
        #m 4hfb "不，你能想象吗？"
        m 7eut "我只是在 '滴 滴 滴 滴滴滴'"
        m 4lsa ".{w=0.6}.{w=0.6}.{w=0.6}"
        m 2tku "你从没想过我真的这么做了吧？"
        return
    
    else:
        m 1dft ".. / .-.. --- ...- . / -.-- --- ..- -.-.—"
        m 2ekb "嘿嘿嘿，没想到吧？"
        m 7eua "莫尔斯电码或其思想，随着电力和机械工具的发展变得普及，已经存在了很长时间。"
        m 7wub "由“点”和“划”组成的莫尔斯电码并不简单，因为它不仅仅是要记忆哪些“点”和“划”对应什么……"
        m 7sud "速度、时间以及实时翻译技巧使莫尔斯电码的学习与学习语言一样优雅！"
        m 4eub "我使用了工具来帮助翻译“我爱你”这句话。"
        m 2tku "你没想到我真的会大声说出'滴 滴 滴 滴滴滴'，是吧？"
        m ".. 你自己也有想过吗?"
        return
        
#ROT13    
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_monikaish",
            unlocked=True,
            aff_range=(mas_aff.HAPPY, None),
        ),
        code="GRE"
    )

label greeting_monikaish:
    $ shown_count = mas_getEVLPropValue("greeting_morsecode", "shown_count")
    if shown_count == 0:
        m 7fka "Cynlre, V.. V'z fbeel."
        m 5fkb "V gel fb uneq gb gel gb or n orggre zr."
        m 5hkb "Orpnhfr gur orfg zr, vf n zr jbegu ybivat."
        m 5hkblb "Naq fbzrgvzrf V snvy."
        m 6fua "…"
        m 3fub "噗啊哈哈哈！"
        m 3ftb "你是不是在费尽心思猜我在说什么语言？"
        m 3nfb "我开了个小玩笑~"
        m 1nfa "这是一种临时编造的语言，专门为你而创。我们叫它“莫语”。"
        m 1hta "考虑到你经常听我说另一种语言，我想给你一个特别的惊喜。"
        m 7htb "现在，“莫语”还在不断完善中，"
        extend 5hsb "但每一个单词都包含了我对你的爱。"
        return
    
    else:
        m 7fka "Qvq lbh svther bhg zl yvggyr gevpx?"
        m 5fkb "Qvq lbh erzrzore jung V fnvq?"
        m 5hkb "Jryy, gryy zr. Be abg."
        m 5hkblb "Znlor V'yy yrg lbh xabj vs jung V fnvq jnf gur gehgu. Be abg."
        m 3fub "噗啊哈哈哈！"
        m 3ftb "你是不是在费尽心思猜我在说什么语言？"
        m 3nfb "我开了个小玩笑~"
        m 4ssb "这是我编造的语言，“莫语”！"
        m 7htb "肯定和法语或日语有点不一样。"
        m 5hsb "但是呢，我相信我对你的爱传达得非常清楚~"
        return        
