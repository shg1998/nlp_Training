
class RawData:
    @staticmethod
    def get_data():
        tweets = [
        'My daughter went to a laser quest birthday party yesterday. She set her username to “a girl”. I asked why she didn’t pick bloodstone’ ',
        'CRO at @WithSecure. Infosec speaker and author. My book "If Its Smart, Its Vulnerable" is coming out in August. I stand with Ukraine.',
        'Red Line Through HTTPS http://xkcd.com/2634',
        'What kind of ratings is the Apple ’Phone’ app getting in your App Store? If the Finnish App Store it gets 4.2 out of 5.',
        'Amazing indeed!',
        ' Old me. New me. Still me. #wehackhealth',
        ' I cancelled my talk earlier today and am home. I hope to record it soon and publish online.It was great to see everyone. The whole situation sucks, but the right decision to pull it.I wish everyone safe travels home.',
        'Recently wanted to see how difficult it would be to implement a native plugin in Sliver (something long running).  To that end, wrote up a keylogger For anyone else who saw this as a missing feature, Enjoy.  Thanks again to the Sliver team github.com GitHub - trustedsec/SliverKeyloggerContribute to trustedsec/SliverKeylogger development by creating an account on GitHub.',
        'Should I be concerned that all of my TS employees are hanging out with@strandjsand BHIS?',
        'Heading to #bsidescle, stop by the #TrustedSec booth for free protein, creatine, and pre workout',
        'If you look right now in the podcatcher of your choice, there is a brand new episode from the TrustedSec crew. Hear about the latest securitynews and stay for a special interview with the creator of the PWNton Pack, @W9HAX!  trustedsec.com Episode 5.5 - Outspending the Ransomware Gangs - TrustedSec Hear the latest news about information security, security program compliance, risk management, and more in the latest episode of TrustedSecs podcast.',
        'I know one podcast I’ll be listening to over the weekend. The  @TrustedSec  podcast latest episode podcasts.apple.com TrustedSec Security Podcast: 5.5 - Outspending the Ransomware Gangs on Apple Podcasts Show TrustedSec Security Podcast, Ep 5.5 - Outspending the Ransomware Gangs - Jun 17, 2022',
        ' Awww man, when you see someone identify an undetected threat in a customer environment and its @jw4lsec on @rpargman team. #BinaryDefense Great job dude!!',
        'Daughter wrote this on my whiteboard at office',
        'New bicep/tricep curl machine. Excited.',
        """
        I've officially caved and moved back to iPhone.

    I can't compete with the green bar text messages with my kids now that they all have phones.""",
        """
    PR'd on rack pulls today. About to PR on landmine rows.

    Lesssss gooooo #wehackhealth""",
        'Good morning beautiful #wehackhealth',
        ' The arm around the neck..',
        'Pic of me dying at the table',
        """My son Gavin just asked me “Dad what does pinching the loaf mean?”

    omggggg I’m so dead""",
        """We'll be releasing all of our private C2s at #BSIDESCLE right
    @HackingLZ


    (this is a joke, I swear)""",
        """ There's so much knowledge being shared in this industry from formalized college training, to self-taught online courses and certifications. The path is there for those that want to come, but we also have to fix the pipe to bring new folks into the industry.""", 'Open to ideas here, this is also more of a call for others to try and help to bring newcomers aboard and help fix the problem. ',
        """I'm almost apprehensive to tell others to come join this industry due to this problem. It's massive, and it's getting worse day by day.

    We don't have a skills shortage in cyber security - we have a commitment issue to the next generation of hackers. """,
        """My talk "CTRL-Z" from SPHERE.
    https://youtube.com/watch?v=Yjogm9ejcPQ…
    I stand with Ukraine.
    youtube.com
    Mikko Hypponen "Ctrl-Z" at #SPHERE22
    Enjoy Mikko's keynote from #SPHERE22 and follow him on Twitter at https://twitter.com/mikko.The SPHERE is a physical space and a state of mind – a place that.""",
        """ Now most of them might not know what a phone call is.
    Quote Tweet
    Mikko tweets from 2012
    @mikko__2012
    · Jun 15
    Listen up kids:
    Once upon a time, it wasn't possible to be on the net and have a phone call at the same time.
    True story.""",
        """ What kind of ratings is the Apple ’Phone’ app getting in your App Store? If the Finnish App Store it gets 4.2 out of 5.
    apps.apple.com
    Phone
    Make and receive calls with the Phone app. • Phone calls, FaceTime audio calls and FaceTime video calls all in one place. • Favourites offers one-tap shortcuts for calls and messages to your most...""",
        """People are really leaving reviews for the Phone app.""",
        'Red Line Through HTTPS http://xkcd.com/2634',
        """Amazing indeed!
    Quote Tweet
    Marcin Wichary""",
        'The pocket square switch.',
        """Nice photo,
    @tijd
    !
    https://tijd.be/de-tijd-vooruit/tech/de-gsm-van-de-premier-hacken-dat-kost-200-000-euro/10395091.html…""",
        """Nice photo,
    @impresacity
    ! https://impresacity.it/news/27288/levoluzione-del-cybercrime-dagli-unicorni-allai-parla-lesperto.html…""",
        """ Thank You for the interview,
    @ISMG_News
    !
    govinfosecurity.com
    Russia's Cyber Offensive Against Ukraine Continues Nonstop
    As Russia's invasion of Ukraine continues, it's notable that Ukraine's government - and much of the country - has remained connected to the internet. That's""",
        """ A 74-year-old man died on Sunday after bystanders were unable to call for emergency services or assistance during the #Arizona telecoms disruption.

    This instance of sabotage last weekend is the first time officials have linked a death to a network outage

    https://azcentral.com/story/news/local/arizona/2022/06/15/74-year-old-man-dies-during-phone-and-internet-outage-northern-az/7636856001/…
    Quote Tweet
    NetBlocks
    @netblocks
    · Jun 16
    Confirmed: Network data corroborate reports of an internet disruption in rural Arizona that left Navajo and Apache communities disconnected from Saturday.

    The incident is attributed to a shooting that targeted Frontier fiber cables serving the region.

    https://apnews.com/article/technology-arizona-phoenix-telecommunications-39e3f11fefb2e61747dc0b5cc80cbe1e…""",
        """Enable Content
    6.3%
    Enable Editing
    7.8%
    Just Run The Malware
    86%
    335 votes
    ·
    Final results""",
        """The GRU illegal exposed earlier today by Dutch intelligence graduated from SAIS. I didn't have him in class as a student, but my amazing colleague Eugene Finkel did. Here's Eugene's courageous and remarkable thread on this experience
    Quote Tweet
    Eugene Finkel
    @eugene_finkel
    · Jun 16
    I had good reasons to hate Russian security services before. Now I am just exploding. I feel angry, I feel stupid, I feel naive, I feel tired. I got played. I had him in class. Twice, in fact. One class was half-Zoom  during COVID, several interactions outside classroom twitter.com/PjotrSauer/sta…
    Show this thread""",
        """Every so often I love to be reminded of the biggest devtools bizdev fail of all time

    https://linuxjournal.com/content/git-origin-story…""",
        """Thank You for the follow,
    @pogue_matt
    ! You’re my 222222nd follower.""",
        """The Graphics Interchange Format (GIF; /dʒɪf/ or /ɡɪf/) is a bitmap image format that was developed by a team at the online services provider
    CompuServe led by American computer scientist Steve Wilhite and released on 15 June 1987""",
        """ At 35, GIF is one of the oldest file formats we use all the time. Another one is ZIP (which is 33 years old) and TXT (which is ancient).""",
        """According to our information, the American electronic warfare giant L3Harris is in the strongest position to buy the former Israeli leader in
    tactical interceptions NSO. #USA #Israel
    Quote Tweet
    Intelligence Online
    @Intel_Online_Fr
    · Jun 14
    Selon nos informations, c'est le géant américain de la guerre électronique L3Harris qui se positionne le plus fortement pour racheter l'ex-leader israélien des interceptions tactiques NSO. #USA #Israel http://ow.ly/GGsv30slYbP""",
        """just reversed some malware that does like four things then sleeps for 24h. so basically it behaves just like me"""

    ]
        return tweets
