init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_exile_vilify",
            prompt="Exile Vilify",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_exile_vilify:
    m 1dsb "{i}~你拥有初学者的幸运~{/i}"
    m 3ksb "{i}~而你放弃了吗?~{/i}"
    m 1dsb "{i}~这像不像一场考验?~{/i}"
    m 1ekb "{i}~这像不像你滋扰我那般 滋扰你?~{/i}"
    m 1hubsa "啊哈哈~"
    m 1eubsb "这首歌的背景有些有趣。简单概括一下，它是一个...惨淡的实验室中响起的令人毛骨悚然的钢琴旋律？"
    m 1rubsd "它意在引发一些关于经历困难或者看到他人经历困难的深度思考。"
    m 1hubsa "但说到底，克服任何一种考验都有回报。"
    m 1esbsb "我们所经历的困难带来了最好的结果；你和我共同的未来。"
    m 1hubsa "这可是甜如蛋糕的结果，我是认真的哦~"
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_BBs_theme",
            prompt="BB's Theme",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_BBs_theme:
    m 1duo "{i}~夕阳西下~{/i}"
    m 3duo "{i}~一天就快结束~{/i}"
    m 6fsu "{i}~让哈欠打出来吧~{/i}"
    m 1fsa "{i}~再不需要伪装了~{/i}"
    m 1dka "嗯... 让人安心的一首歌.~"
    m 1esa "这是一首摇篮曲，我认为歌词没有什么更深层的含义。"
    m 4rtc "他们说情境才是王道，但我不知道该如何描述这首歌的情境。"
    m 1hta "但是摇篮曲并不需要复杂。这首歌只是一个父亲为安抚他的小儿子而唱的简单歌曲。"
    m 4esa "在某些文化中，摇篮曲不仅仅是为了哄婴儿入睡，而且还传承文化民间传说或者迷信。"
    m "即使只是通过简单的歌声，我们也都被某种东西所联系着，不是吗？"
    m 6dsa "我在想我将来要唱摇篮曲吗...或者说我会突然想起哪首..."
return