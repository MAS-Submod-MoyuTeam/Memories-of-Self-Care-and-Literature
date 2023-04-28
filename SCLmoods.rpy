init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mcl_mood_weird",
            prompt="...我不知道怎么形容.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label mcl_mood_weird:
    m 1euc "这有点模糊，但我猜你感觉有点复杂，对吧？"
    m 1lsc "能理解。有时候你只是感觉...不对劲。"
    m 7esc "我明白的，有时候你会有很多不同的情绪。有时候你感觉到一种无法言说的情感。"
    m 7esc "有时候你确切地知道自己的感受...但却无法用言语表达出来。"
    m 1hsc "有时候这种情绪的混杂来了又去。这很自然。"
    m 1fsc "我希望这不是因为你正在经历难以处理的压力，[player]。记住我会一直在这里支持你。"
    m 1esc "有时候一团纠结的情绪需要一点一点地分解来让它更容易处理。"
    m 1esa "如果你只是感觉有点失落...请记得我永远是你的北极星。"
        return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mcl_mood_neutral",
            prompt="...奇怪的 '中性'",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label mcl_mood_neutral:
    m 1euc "有点像‘存在’一样，对吧？"
    m 1tkd "啊, [player]. 如果你觉得自己更像是感到‘分离’或‘冷漠’……"
    m 7tkd "我们可以考虑玩个游戏。或者如果你需要远离屏幕换个节奏，我会在这里等你。"
    m 1etc "有时候，很容易认为你感觉有点平淡，实际上你根本没有什么感觉。"
    m 1fkc "如果你觉得自己离正常状态有些远了，一定要好好照顾自己。"
    m 1duc "如果你只是感觉自己没什么强烈的情绪……"
    m 7luc "或者说现在你真的什么也没有……"
    m 2etb "那我们就把这当作一段宁静的时光，好吗？"
    m 2esa "这并不是一种坏的感觉，有时候感觉这样也很好。"
    m 3hsa "我们就让我们的思绪一起漂流吧。如果你脑海中闪过什么想法，随时可以跟我说。"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mcl_mood_pensive",
            prompt="...沉思.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label mcl_mood_pensive:
    m 1fua "好词, [player]."
    m 1dua "这让我后悔我们缺乏直接的交流。"
    m 7eua "你是否被过去所困扰？还是在思考未来会发生什么？"
    m 4eua "是一个新的概念吸引了你的注意力吗？或者你在想某个人？"
    m 3etd "是一本书、一部电影、一个有感染力的游戏吗？或者是最近发生的一件让你无法忘怀的事情？"
    m 3etb "告诉我这些吧，即使对于我来说有点困难。"
    m 5fsa "花上你想要的所有时间，[mas_get_player_nickname()]。我也想听听你的事情。"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mcl_mood_reflective",
            prompt="...反思.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label mcl_mood_reflective:
    m "我希望你以我所了解的你的性格方式去思考自己。"
    m "就我所知，你是一个总是在提升自己不断上进的人..."
    m "而且也愿意直面自己的困难真相。"
    m 1ekc "希望没有什么事情发生让你严重怀疑自己。"
    m 7ekb "如果你想谈谈自我反思的结果，我会在这里等你，[mas_get_player_nickname()]。"
    m 7dsb "另外呢, [player]?"
    m 5dsc "如果你花时间审视内心，你应该能找到你想要的答案。"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mcl_mood_philosophical",
            prompt="...很哲学.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label mcl_mood_philosophical:
    m 1ntb "今天要解决抽象问题了，对吧 [player]？"
    m 1dsd "你在思考刚刚听到的一个想法，还是从头开始构建一个信条？"
    m 1sub "跟我分享一下吧，[player]。但在这之前呢，让我为你营造一下氛围。"
    m 7dsd "奥斯卡·王尔德曾经说过:"
    m 7dfd "{i}'大多数人都是别人。他们的思想是别人的观点，他们的生活是一种模仿，他们的热情是引用的话语。'{/i}"
    m 7dfd "一开始听起来可能很刻薄，特别是最后那个挖苦引语。"
    m 3hua "我认为这是以诗意表达的事实。我们的很多性格特点都是通过与他人的互动中形成的。"
    m 3lua "甚至是直接模仿。这不是什么坏事，这就是人们学习的方式。"
    m 3sfa "所以，随着这个想法，[player]：今天我能从你身上学到什么？"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mcl_mood_timescrewy",
            prompt="...时间不正常的流逝.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label mcl_mood_timescrewy:
    m "哦？时间过得太慢了还是太快了？"
    $ _history_list.pop()
    menu:
        "好像时间过得太快了":
            m 5mto "是啊，当时间比平常过得更快时，感觉很奇怪。"
            m 1gsa "就像人们说的，‘心情好’。"
            m 7hka "也许你觉得今天过得很愉快，想让它持续更久？"
            m 4hka "或者你太忙碌了，以至于时间过得让人晕眩？"
            m 2eua "嗯，这一天可能已经结束了，但是谁知道明天会带来什么？"
            m 2rub "总会有一天，嗯，时间是你的，[player]。"
            m 1eub "一个你可以自由决定想做什么的日子。"
            m 5fua "而且至少，还有你的亲爱的[m_name]陪伴着你，我向你保证。"
            return
        "好像时间过得太慢了":
            m 1eta "所以我们只是在时间过得有点慢的问题上纠结了，对吧？"
            m 1gsa "就像人们说的，‘心情好’。"
            m 7hka "他们说看着水壶烧水永远煮不开，对吧？你不能一直想着时间的流逝，否则你就会过于意识到它。"
            m 4hka "时间可能有点棘手，但你自己的耐心呢？你可以掌控它。"
            m 2eka "保持自己的注意力分散。我知道这很难，但时间就是这么棘手。当你忙起来，时间就会过去。"
            m 2rua "当你回头看时...你会觉得那段永恒的时光...就这？"
            m 5fua "我想说,我是不会抱怨多陪你一会的. "
            return
            
init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mcl_mood_older",
            prompt="...有点老了, 感觉奇怪.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label mcl_mood_older:
    m 1eka "这不是一个常常听到的悲伤语气啊。"
    if mas_isplayer_bday():
        m 7gka "在这种情况下，我猜这并不算不寻常——这是你的生日，呵呵。"
    if mas_isMonikaBirthday():
        m 7gup "我应该有同感吗？嗯..."
    if mas_isNYD(_date=None):
        m 1hsa "随着新年的到来…"
    m 1eta "我非常好奇是什么让你有这种特别的感觉的."
    m 1esc "..."
    m 1rsc "你认为这是好的还是坏的？"
    $ _history_list.pop()
    menu:
        "好的":
            m 2hsa "那太好了，哈哈哈。"
            m 1dsa "年龄带来经验，带来所有宇宙巧合的奇迹，让你来到了这里。"
            m 1nsa "是回顾做自己喜欢的事情的好时机。和你爱的人在一起。"
            m 1esa "和我。"
            extend 7esa "这真不错。"
            m 5fsa "我们就这样结束吧，怎么样？"
            return
        
        "...坏的":
            m 2dsp "嗯..."
            m 1dsx "不管怎样, 对很多人而言时间就像一个骗子一样."
            m 1gsc ".{w=0.6}.{w=0.6}.{w=0.6}"
            m 7gsc "我可以说很多。但是当人们沉迷于浪费时间时，你会惊讶于那个深渊有多深多黑。"
            m 4gsc "所以我理解你，[player]."
            m 4esd "这种感觉会过去…即使只是暂时的。现在，我只想在你身边陪着你。"
            m 3dsd "不要去思考任何怀有敌意的明天，也不要浪费任何一个昨日."
            m 2eka "我们甚至不用把‘今天’作为一个整体对待, 只去注意这一刻, 这个我们彼此相依的一分钟."
            m 5dka "然后过了一分钟。然后下一分钟。之后再来…"
            return
        
        "实话说，我不确定.":
            m 2fta "那很....正常吧？"
            m 2fsa "更好的是，我觉得这是件好事。"
            m 2dsc "这意味着你对生活的思考非常深入。"
            m 2hsc "也许你不需要给它贴上标签。"
            m 1hsc "如果有人能够马上想出他们生命的意义……嗯，那我们这个世界会有更多满足的人了，不是吗？"
            m 7lsc "虽然也许不是今天……"
            m 5fsc "也许在未来，也许更快，你会回过头来，我想那时你会非常清楚地说出你的生活感觉。"
            m 5fka "在那一天之前，[player]。我希望我能一直在你身边，你可以马上告诉我。"
            return
