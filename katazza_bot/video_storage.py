from singleton import Singleton


@Singleton
class VideoStorage:
    videos_ = {
        "Car driving advice": {
            3: "https://www.youtube.com/watch?v=ASp_OTZ5fN8",
            5: "https://www.youtube.com/watch?v=rKf2fRImrYI",
            7: "https://www.youtube.com/watch?v=EwmDdMzzDjY",
            10: "https://www.youtube.com/watch?v=WGHVIYpxQm4",
        },
        "Gardening": {
            3: "https://www.youtube.com/watch?v=Ub976UXEACY",
            5: "https://www.youtube.com/watch?v=ik3l4U_17bI",
            7: "https://www.youtube.com/watch?v=fwEVJw1Q-Gs",
            10: "https://www.youtube.com/watch?v=_wTCCNWuXz0",
        },
        "Java": {
            3: "https://www.youtube.com/watch?v=DnQnteSF35Q",
            5: "https://www.youtube.com/watch?v=NcMt9Bl3SL0",
            7: "https://www.youtube.com/watch?v=sIkG0X4fqs4",
            10: "https://www.youtube.com/watch?v=oNiOUiAS70w",
        },
        "How does house work": {
            3: "https://www.youtube.com/watch?v=QlUZwwKDqXo",
            5: "https://www.youtube.com/watch?v=eSMUnuoxdZQ",
            7: "https://www.youtube.com/watch?v=8jxRn-T_LCs&t=27s",
            10: "https://www.youtube.com/watch?v=Hz6qomFM_dw",
        },
        "Skiing tricks": {
            3: "https://www.youtube.com/watch?v=mLSMvU0ABD8",
            5: "https://www.youtube.com/watch?v=WYPxH5AkuEA",
            7: "https://www.youtube.com/watch?v=afaYTN-fIiQ",
            10: "https://www.youtube.com/watch?v=WfvAxHmecII",
        },
        "Germany": {
            3: "https://www.youtube.com/watch?v=AuaVGK7xXaM&ab_channel=DWEuromaxx",
            5: "https://www.youtube.com/watch?v=WHd28MTV4cE&ab_channel=GeographyNow",
            7: "https://www.youtube.com/watch?v=lrrBNFqG1oI&ab_channel=EasyGerman",
            10: "https://www.youtube.com/watch?v=WgPZkuG63ow&ab_channel=SpencerMoeller",
        },
        "Makeup": {
            3: "https://www.youtube.com/watch?v=GUwlbrSqDIs&t=1s&ab_channel=Vogue",
            5: "https://www.youtube.com/watch?v=vgBQLmdzkMA&ab_channel=Allure",
            7: "https://www.youtube.com/watch?v=gPa2Rqb8mzo&ab_channel=ChristenDominique",
            10: "https://www.youtube.com/watch?v=ylLFIvZy4z8&ab_channel=Tati",
        },
        "Interior design": {
            3: "https://www.youtube.com/watch?v=gC8ec_y6ewg&ab_channel=TrendsTV",
            5: "https://www.youtube.com/watch?v=fkSUPsQ9TMQ&t=181s&ab_channel=ClaCali",
            7: "https://www.youtube.com/watch?v=D-Xnn1CQ3VQ&ab_channel=Dunn-EdwardsPaints",
            10: "https://www.youtube.com/watch?v=TXzcmr2WcDA&ab_channel=MsMojo",
        },
        "Football": {
            3: "https://www.youtube.com/watch?v=GePlbCsGniA&ab_channel=LifeOnPaul",
            5: "https://www.youtube.com/watch?v=DztAp4p0PW0&ab_channel=TifoFootball",
            7: "https://www.youtube.com/watch?v=OSGneV1pjXU&ab_channel=Unisport",
            10: "https://www.youtube.com/watch?v=ExD_Sql_4So&ab_channel=FootballDaily",
        },
        "Trading": {
            3: "https://www.youtube.com/watch?v=F3QpgXBtDeo&ab_channel=Kurzgesagt%E2%80%93InaNutshell",
            5: "https://www.youtube.com/watch?v=DztAp4p0PW0&ab_channel=TifoFootball",
            7: "https://www.youtube.com/watch?v=OSGneV1pjXU&ab_channel=Unisport",
            10: "https://www.youtube.com/watch?v=ExD_Sql_4So&ab_channel=FootballDaily",
        },
    }
    themes_ = ['aesc']
    times_ = ['3', '5', '7', '10']

    rick_rolling_video_ = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

    def get_video(self, length, theme):
        key = (length, theme)
        if key in self.videos_:
            return self.videos_[key]
        else:
            return self.rick_rolling_video_

    def get_random_themes(self):
        return random.sample(self.themes_, 3)

    def get_times(self):
        return self.times_

    def get_times(self):
        return self.times_