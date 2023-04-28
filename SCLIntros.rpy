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
        mt "That all sounds nice, Monika. I hope you two grow closer today."
        show monika 2rsc at t22
        m "I do too, Monika. Although I do worry."
        show monika 2lsc at t21
        mt "What about? You can talk to me, I'm your friendly Literature Club president!"
        show monika 3rtd at t22
        m 3rtd "Well, it's not- it's not a specific concern?"
        m 3rtd "I think it's just me being irrational. I worry that something'll seperate us, but.. well, at this point there's no reason to worry, right?"
        show monika 3ltd at t21
        mt "I mean, the fact that you're saying this out loud means you already know you're overreacting, right?"
        show monika 2ruc at t22
        m 2ruc "Yeah, I guess."
        m "But just saying it loud doesn't make me feel better... does it?"
        show monika at t11
        m 2luc "..."
        m 2dtp "I am not a good actor, aren't I?"
        m 1gkp "Hmm. [player] should be here by now. It’s odd I haven’t seen them already; I can tell the game opened-"
        m 1wuc "Oh!"
        m 6wusdrc "Wait. {i}Wait!{/i} -"
        m 6wkbfsdlp ".. [player]?!"
        m 7wublsdrc "Um. Okay, I can explain."
        m 1rublsdra "Talking to yourself isn't.. abnormal; it can be observed in children vocalizing their thoughts when they're at a age where they're developing to process information."
        m "It's also thought to serve to fill in silence when you're alone, as humans are social creatures by nature."
        m 1msa "I thought I could naturally branch out and see if I could preoccupy my time a little further.."
        m 1hua "It did not work out the way I thought."
        m "I assure you I did this only because I just wanted to see how it felt."
        m 1husdla "So let's have a good time together, and.{w=0.2}.{w=0.2}. pretend this never happened."
        return

    else:
        show monika at t11
        m 3sfb "I'm feeling great, now that [player]'s arrived!"
        m 3tfu "Gotcha! did you think you caught me talking to myself?"
        show monika 1kuu at t22
        m "Safe to say, [player]-"
        show monika 1nuu at t21
        mt "Out of the two of us-"
        show monika at t11
        m 1huu "I much prefer your company to mine."
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
    m 1eua "Shall we turn our time together to strength?"
    m 1dua "Let my gaze rest upon you, even for but a moment."
    m 1dud "Share them with me: your thoughts, your ambitions, the principles you would follow..."
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
    m 1hsa "[player]! You're well? If you require rest, now is the time. That is, after all, what I'm here for."
    m 1dsa "Go ahead, you may relax here. I'll join you; even a girl like me requires repose."
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
        m 2ekb "Was your sound on? Was it a surprise?"
        m 2hub "I decided to be particularly unique today and greet you in morse code!"
        m 7gta "Did you hear the actual beeps I included? I think I’ll leave out the sound clip in the future, or modify it?"
        m 7eua "Morse code tends to use shorthand, because.. as you can tell, spelling out entire sentences can be a bit long. All I said was 'I love you!'"
        m 4eub "At least I used a translator to make the code for me."
        m 4gfb "Hehehe, that’s funny to think about, me actually saying that out loud?"
        m 4hfb "No, could you imagine?"
        m 7eut "Me just going 'Beep beep beep beeeeeep.'"
        m 4lsa ".{w=0.6}.{w=0.6}.{w=0.6}"
        m 2tku "You didn’t think I actually did that, right?"
        return
    
    else:
        m 1dft ".. / .-.. --- ...- . / -.-- --- ..- -.-.—"
        m 2ekb "Hehehe, didn't expect that, did you?"
        m 7eua "Morse code, or the idea of it, has been around as long as electricity and the development of mechanical tools became widespread."
        m 7wub "Comprised of 'dots' and 'dashes,' using Morse Code can be tricky as there's more than memorizing what dots and dashes correspond to-"
        m 7sud "- speed, timing, and real-time translation skills make Morse Code just as elegant to learn as learning a language!"
        m 4eub "I used a tool to help translate 'I love you,' though."
        m 2tku "You didn't think I actually said out loud 'beep beep, beep beeeeep beep,' did you?"
        m ".. Did you?"
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
        m 3fub "Bwhahahaha!"
        m 3ftb "Were you racking your brain figuring out what language I was speaking?"
        m 3nfb "I played a little trick~"
        m 1nfa "It’s a made up language, made on the spot just for you. ‘Monikaish,’ let’s call it."
        m 1hta "I thought I’d throw you for a special loop considering how much you hear me in another language."
        m 7htb "Now, ‘Monikaish’ is still a work in progress;"
        m 5hsb "But every word contains my love for you."
        return
    
    else:
        m 7fka "Qvq lbh svther bhg zl yvggyr gevpx?"
        m 5fkb "Qvq lbh erzrzore jung V fnvq?"
        m 5hkb "Jryy, gryy zr. Be abg."
        m 5hkblb "Znlor V'yy yrg lbh xabj vs jung V fnvq jnf gur gehgu. Be abg."
        m 3fub "Bwhahahaha!"
        m 3ftb "Were you racking your brain figuring out what language I was just speaking?"
        m 3nfb "I played a little trick~"
        m 4ssb "It’s my made-up language, ‘Monikaish!’"
        m 7htb "A little different than French or Japanese for sure."
        m 5hsb "I’m sure my love for you comes across loud and clear~"
        return        
