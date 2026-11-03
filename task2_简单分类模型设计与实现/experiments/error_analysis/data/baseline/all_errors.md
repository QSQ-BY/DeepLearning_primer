# 最终模型全部误分类案例

共 607 条；原始测试集行号从 0 开始。保留完整原文，标签以 AG-news 原始标注为准。
自动特征标签用于定位样本，不等于已确认的错误原因；概率未经校准。

## 1. test:9 | Sci/Tech → Business

预测置信度 0.6421；真实类概率 0.2936；前两类概率差 0.3485。
分词数 33；未知词比例 0.00%；特征：商业与科技边界。

Card fraud unit nets 36,000 cards In its first two years, the UK's dedicated card fraud unit, has recovered 36,000 stolen cards and 171 arrests - and estimates it saved 65m.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：unit@18:0.6085 | dedicated@15:0.4614 | and@25:0.4585。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 2. test:55 | Sci/Tech → World

预测置信度 0.4758；真实类概率 0.0814；前两类概率差 0.2234。
分词数 28；未知词比例 3.57%；特征：需结合语义人工复核。

Promoting a Shared Vision As Michael Kaleko kept running into people who were getting older and having more vision problems, he realized he could do something about it.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：kept@7:0.9472 | michael@5:0.5795 | problems@19:0.4735。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 3. test:56 | World → Business

预测置信度 0.3828；真实类概率 0.3501；前两类概率差 0.0327。
分词数 44；未知词比例 4.55%；特征：世界与商业边界；前两类接近:概率差<0.2。

India's Tata expands regional footprint via NatSteel buyout (AFP) AFP - India's Tata Iron and Steel Company Ltd. took a strategic step to expand its Asian footprint with the announcement it will buy the Asia-Pacific steel operations of Singapore's NatSteel Ltd.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：company@17:1.4450 | ltd@18:1.3605 | steel@16:1.0162。
能把预测改为真实类的单词遮挡数：12。仅表示局部敏感性，不代表已证明因果原因。

## 4. test:61 | Sports → World

预测置信度 0.5093；真实类概率 0.4895；前两类概率差 0.0198。
分词数 35；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Haas and Cink Selected for Ryder Cup Team Jay Haas joined Stewart Cink as the two captain's picks for a U.S. team that will try to regain the cup from Europe next month.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：europe@32:1.7395 | next@33:1.2018 | s@22:1.1002。
能把预测改为真实类的单词遮挡数：19。仅表示局部敏感性，不代表已证明因果原因。

## 5. test:79 | World → Sports

预测置信度 0.9389；真实类概率 0.0279；前两类概率差 0.9110。
分词数 21；未知词比例 4.76%；特征：高置信错误>=0.9。

Live: Olympics day four Richard Faulds and Stephen Parry are going for gold for Great Britain on day four in Athens.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：olympics@1:2.1348 | day@2:1.2508 | parry@8:0.4798。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 6. test:83 | Business → Sci/Tech

预测置信度 0.9917；真实类概率 0.0079；前两类概率差 0.9838。
分词数 58；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Intel to delay product aimed for high-definition TVs SAN FRANCISCO -- In the latest of a series of product delays, Intel Corp. has postponed the launch of a video display chip it had previously planned to introduce by year end, putting off a showdown with Texas Instruments Inc. in the fast-growing market for high-definition television displays.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tvs@8:0.9033 | definition@7:0.8463 | display@29:0.3040。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 7. test:110 | Business → Sci/Tech

预测置信度 0.9217；真实类概率 0.0778；前两类概率差 0.8439。
分词数 47；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Yahoo! Ups Ante for Small Businesses Web giant Yahoo! is gambling that price cuts on its domain name registration and Web hosting products will make it more competitive with discounters in the space -- which means that small businesses looking to move online get a sweeter deal through ...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：web@6:0.4207 | space@32:0.3905 | yahoo@8:0.3874。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 8. test:111 | Sci/Tech → Business

预测置信度 0.5726；真实类概率 0.4267；前两类概率差 0.1459。
分词数 52；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

IBM Buys Two Danish Services Firms IBM said Tuesday it has acquired a pair of Danish IT services firms as part of its effort to broaden its presence in Scandinavia. As a result of the moves, IBM will add about 3,700 IT staffers to its global head count. Financial terms of ...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：financial@49:1.2316 | count@48:1.1489 | buys@1:0.6044。
能把预测改为真实类的单词遮挡数：7。仅表示局部敏感性，不代表已证明因果原因。

## 9. test:120 | World → Business

预测置信度 0.9739；真实类概率 0.0240；前两类概率差 0.9500。
分词数 51；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Oil prices bubble to record high The price of oil has continued its sharp rise overnight, closing at a record high. The main contract in New York, light sweet crude for delivery next month, has closed at a record \$US46.75 a barrel - up 70 cents on yesterday #39;s close. 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：prices@1:1.2943 | 39@48:1.1818 | crude@29:0.7544。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 10. test:139 | World → Business

预测置信度 0.5461；真实类概率 0.4279；前两类概率差 0.1182。
分词数 26；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

Sharon orders 1,000 homes in West Bank Israel announced plans for 1,000 houses in the West Bank yesterday, accelerating the expansion of the settlements. 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：bank@7:0.9899 | announced@9:0.9476 | bank@18:0.6046。
能把预测改为真实类的单词遮挡数：7。仅表示局部敏感性，不代表已证明因果原因。

## 11. test:154 | World → Sci/Tech

预测置信度 0.5478；真实类概率 0.3346；前两类概率差 0.2133。
分词数 50；未知词比例 0.00%；特征：需结合语义人工复核。

Google Lowers Its IPO Price Range SAN JOSE, Calif. - In a sign that Google Inc.'s initial public offering isn't as popular as expected, the company lowered its estimated price range to between \$85 and \$95 per share, down from the earlier prediction of \$108 and \$135 per share...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：google@13:0.5946 | ipo@3:0.5516 | price@4:0.4642。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 12. test:155 | World → Sci/Tech

预测置信度 0.7032；真实类概率 0.0350；前两类概率差 0.4421。
分词数 22；未知词比例 0.00%；特征：需结合语义人工复核。

Future Doctors, Crossing Borders Students at the Mount Sinai School of Medicine learn that diet and culture shape health in East Harlem.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：medicine@11:0.7828 | learn@12:0.7018 | diet@14:0.6404。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 13. test:196 | World → Business

预测置信度 0.5443；真实类概率 0.4274；前两类概率差 0.1170。
分词数 61；未知词比例 1.64%；特征：世界与商业边界；前两类接近:概率差<0.2。

Stock Prices Climb Ahead of Google IPO NEW YORK - Investors shrugged off rising crude futures Wednesday to capture well-priced shares, sending the Nasdaq composite index up 1.6 percent ahead of Google Inc.'s much-anticipated initial public offering of stock.    In afternoon trading, the Dow Jones industrial average gained 67.10, or 0.7 percent, to 10,039.93...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：stock@0:1.2984 | prices@1:1.0233 | climb@2:0.3470。
能把预测改为真实类的单词遮挡数：6。仅表示局部敏感性，不代表已证明因果原因。

## 14. test:207 | Sci/Tech → Business

预测置信度 0.5683；真实类概率 0.4298；前两类概率差 0.1385。
分词数 42；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

Intuit Posts Wider Loss After Charge (Reuters) Reuters - Intuit Inc. (INTU.O), maker of\the No. 1 U.S. tax presentation software TurboTax, on Wednesday\posted a wider quarterly loss after taking a goodwill\impairment charge during its seasonally weaker fourth quarter.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tax@19:2.1208 | wednesday@24:0.8049 | no@15:0.7181。
能把预测改为真实类的单词遮挡数：13。仅表示局部敏感性，不代表已证明因果原因。

## 15. test:234 | Business → Sci/Tech

预测置信度 0.5663；真实类概率 0.2458；前两类概率差 0.3206。
分词数 37；未知词比例 2.70%；特征：商业与科技边界。

Justices to debate mail-order wine Being freelance wine critics may sound like a sweet gig, but Ray and Eleanor Heald have soured on it. Because their home state, Michigan, blocks direct shipments from out-of-state 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：debate@2:0.9816 | mail@3:0.4512 | order@4:0.3334。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 16. test:241 | Sports → World

预测置信度 0.8431；真实类概率 0.1323；前两类概率差 0.7108。
分词数 40；未知词比例 5.00%；特征：含HTML实体或编码痕迹。

Harris #39; three-run double in ninth sinks Gagne LOS ANGELES - Paul Lo Duca never got to moonwalk to home plate, though he did skip gleefully to the dugout moments after facing former batterymate Eric Gagne for the first time. 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：los@9:3.3260 | gagne@8:1.7986 | ninth@6:0.7311。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 17. test:248 | Sci/Tech → Business

预测置信度 0.7817；真实类概率 0.1879；前两类概率差 0.5938。
分词数 32；未知词比例 6.25%；特征：商业与科技边界。

Caterpillar snaps up another remanufacturer of engines PEORIA - Caterpillar Inc. said Wednesday it will acquire a South Carolina remanufacturer of engines and automatic transmissions, increasing its US employment base by 500 people. 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：employment@27:1.1668 | inc@9:1.0344 | said@10:0.7170。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 18. test:262 | Sci/Tech → Business

预测置信度 0.6428；真实类概率 0.2768；前两类概率差 0.3661。
分词数 40；未知词比例 0.00%；特征：商业与科技边界。

Ecuadorean Lawsuit Vs Texaco Boils Down to Science (Reuters) Reuters - After a decade\of court battles, lawyers on Wednesday took a lawsuit by\Ecuadorean Indians accusing U.S. oil firm ChevronTexaco Corp..\of polluting the Amazon jungle into the field.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：oil@28:2.8853 | firm@29:1.2791 | chevrontexaco@30:1.0521。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 19. test:264 | Sci/Tech → Sports

预测置信度 0.4994；真实类概率 0.0851；前两类概率差 0.1282。
分词数 35；未知词比例 2.86%；特征：前两类接近:概率差<0.2。

Atlantis "Evidence" Found in Spain, Ireland In 360 B.C. the Greek philosopher Plato described an island he called Atlantis. Now contradicting new evidence claims the fabled city-state was based on a real place.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：greek@11:1.4521 | he@17:1.1901 | the@10:0.9804。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 20. test:288 | Business → World

预测置信度 0.8793；真实类概率 0.1141；前两类概率差 0.7652。
分词数 39；未知词比例 0.00%；特征：世界与商业边界。

Vt. sues over importing drugs Vermont's Republican governor challenged the Bush administration's prescription drug policy in federal court yesterday, marking the first time a state has chosen a legal avenue in the expanding battle over Canadian imports.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：governor@8:0.9335 | republican@7:0.8171 | challenged@9:0.6106。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 21. test:295 | World → Business

预测置信度 0.9810；真实类概率 0.0114；前两类概率差 0.9695。
分词数 22；未知词比例 4.55%；特征：世界与商业边界；高置信错误>=0.9。

Producer sues for Rings profits Hollywood producer Saul Zaentz sues the producers of The Lord of the Rings for \$20m in royalties.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：profits@4:3.2682 | producer@6:2.0406 | hollywood@5:1.4938。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 22. test:305 | Sports → Business

预测置信度 0.3388；真实类概率 0.0574；前两类概率差 0.0174。
分词数 66；未知词比例 0.00%；特征：前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Don #39;t expect Tiger to relinquish his top ranking without a fight They #39;re calling Ohio a  quot;battleground state, quot; one of the two or three places likely to decide November #39;s presidential election. On local TV, the Bush and Kerry ads air so frequently that it #39;s easy to forget it #39;s Bob Costas who actually runs the country. 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：presidential@36:1.3961 | election@37:1.3491 | bush@42:0.7994。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 23. test:310 | Business → Sci/Tech

预测置信度 0.7080；真实类概率 0.2917；前两类概率差 0.4163。
分词数 39；未知词比例 0.00%；特征：商业与科技边界。

Clicking on Profits The latest data from the US Department of Commerce further bolsters what we have all suspected: E-commerce sales are increasing. Not only might one suspect that consumer confidence has been bolstered since last year, there ...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：e@19:2.3754 | commerce@20:1.1238 | suspected@18:0.6304。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 24. test:311 | Sports → World

预测置信度 0.7183；真实类概率 0.2777；前两类概率差 0.4406。
分词数 48；未知词比例 8.33%；特征：需结合语义人工复核。

French Take Gold, Bronze in Single Kayak ATHENS, Greece - Winning on whitewater runs in the family for Frenchman Benoit Peschier, though an Olympic gold is something new. Peschier paddled his one-man kayak aggressively but penalty free in both his semifinal and final runs on the manmade Olympic ...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：greece@8:4.1361 | athens@7:2.8807 | gold@2:0.4972。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 25. test:312 | Sci/Tech → World

预测置信度 0.6201；真实类概率 0.1812；前两类概率差 0.4389。
分词数 31；未知词比例 3.23%；特征：含HTML实体或编码痕迹。

Dogs in Training to Sniff Out Cancer Experts have trained unwanted dogs into supersniffers that can detect drugs or bombs. Now they're focusing on a new threat #151;prostate cancer.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：drugs@17:1.5170 | detect@16:1.4437 | dogs@0:0.3358。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 26. test:316 | World → Business

预测置信度 0.5463；真实类概率 0.3137；前两类概率差 0.2326。
分词数 28；未知词比例 0.00%；特征：世界与商业边界。

Crude Price Spike May Send Gas Higher (AP) AP - Amid soaring crude oil prices, gasoline costs have been dropping. But don't expect that to last, economists say.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：prices@13:1.4758 | gasoline@14:1.2630 | crude@11:0.8048。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 27. test:317 | Business → Sci/Tech

预测置信度 0.9982；真实类概率 0.0017；前两类概率差 0.9965。
分词数 42；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Amazon Snaps Up China's Largest Web Retailer (NewsFactor) NewsFactor - Amazon.com (Nasdaq: AMZN) has said it will buy Joyo.com Limited -- a British Virgin Islands company that operates the largest Internet retail Web site in China -- for US #36;75 million.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：newsfactor@9:1.5206 | newsfactor@8:1.1007 | s@4:0.7246。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 28. test:323 | Sci/Tech → Business

预测置信度 0.6383；真实类概率 0.3592；前两类概率差 0.2791。
分词数 39；未知词比例 0.00%；特征：商业与科技边界。

Report: Consumers tuning in to plasma TVs First-quarter shipments of plasma televisions in the United States more than doubled from the previous year, according to research firm iSuppli. Prices fell by nearly \$1,000 over the same period. 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：prices@29:2.2527 | fell@30:2.2026 | 000@34:0.7968。
能把预测改为真实类的单词遮挡数：6。仅表示局部敏感性，不代表已证明因果原因。

## 29. test:327 | World → Business

预测置信度 0.4378；真实类概率 0.2924；前两类概率差 0.1454。
分词数 38；未知词比例 2.63%；特征：世界与商业边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Italian PM #39;s transplant confirmed After days of speculation sparked by the white bandanna worn by Mr Berlusconi on holiday in Sardinia, Piero Rosati said the results of the operation would show in a couple of months.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@2:1.7871 | transplant@4:0.7992 | by@16:0.7053。
能把预测改为真实类的单词遮挡数：6。仅表示局部敏感性，不代表已证明因果原因。

## 30. test:344 | Sports → World

预测置信度 0.6815；真实类概率 0.0034；前两类概率差 0.3913。
分词数 41；未知词比例 0.00%；特征：需结合语义人工复核。

Glory Comes Amid Empty Seats and Closed Shutters HERE in Old Europe, people install shutters outside their windows to keep out the heat, the pollution, the daylight, the noise. They also lock the shutters tight when they go away on holiday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：europe@11:3.2788 | people@12:2.5112 | old@10:1.4461。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 31. test:346 | Sci/Tech → Business

预测置信度 0.7191；真实类概率 0.2807；前两类概率差 0.4385。
分词数 40；未知词比例 0.00%；特征：商业与科技边界。

Salesforce.com 2Q Profit Up Sharply Software developer Salesforce.com Inc. posted a sharp rise in second-quarter profit on better-than-expected revenue during its first quarter as a public company, but investors shunned the stock in late trading 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：investors@33:1.3131 | profit@3:0.6892 | developer@7:0.5901。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 32. test:348 | World → Sports

预测置信度 0.9912；真实类概率 0.0081；前两类概率差 0.9831。
分词数 41；未知词比例 0.00%；特征：高置信错误>=0.9。

Unknown Nesterenko Makes World Headlines (Reuters) Reuters - Belarus' Yuliya Nesterenko won the top\women's athletics gold medal at the Olympics on Saturday,\triumphing over a field stripped of many big names because of\doping woes to win the 100 meters.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：medal@17:1.5238 | women@13:0.8592 | at@18:0.6380。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 33. test:355 | World → Sports

预测置信度 0.9605；真实类概率 0.0235；前两类概率差 0.9370。
分词数 22；未知词比例 0.00%；特征：高置信错误>=0.9。

Greek weightlifter awaits verdict Greek weightlifter Leonidas Sampanis will find out on Sunday if he is to be stripped of his medal.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：medal@21:1.4200 | he@14:1.1738 | sunday@12:0.4308。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 34. test:363 | World → Business

预测置信度 0.9553；真实类概率 0.0161；前两类概率差 0.9393。
分词数 30；未知词比例 3.33%；特征：世界与商业边界；高置信错误>=0.9；含HTML实体或编码痕迹。

A Founding Father? Give the guy some credit. Tung Chee-hwa, Hong Kong #39;s embattled Chief Executive, gets precious little of it from his people these daysand heaps of 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@13:2.1317 | credit@7:1.8107 | guy@5:0.7833。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 35. test:378 | Business → World

预测置信度 0.5213；真实类概率 0.4257；前两类概率差 0.0956。
分词数 62；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

Will High Oil Prices Lead to Recession? (AP) AP - High oil prices, which have been a factor in virtually all U.S. recessions over the past three decades, are surging again this year. And the higher crude oil prices climb, the more risk energy costs pose to what, until recently, many expected to be a banner year for the U.S. economy.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ap@8:2.7052 | ap@7:2.6944 | lead@4:0.5530。
能把预测改为真实类的单词遮挡数：7。仅表示局部敏感性，不代表已证明因果原因。

## 36. test:399 | Business → Sci/Tech

预测置信度 0.7207；真实类概率 0.2704；前两类概率差 0.4503。
分词数 37；未知词比例 2.70%；特征：商业与科技边界。

Nortel Downsizes Again Aug. 23, 2004 (TheDeal.com) Problem-plagued Nortel Networks Corp. announced plans Thursday, Aug. 19, to eliminate an additional 3,500 jobs and fire seven more senior executives as the company labors to reinvent 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：com@7:1.5702 | thedeal@6:0.7206 | again@2:0.2766。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 37. test:415 | Sports → Sci/Tech

预测置信度 0.5879；真实类概率 0.1279；前两类概率差 0.3152。
分词数 33；未知词比例 6.06%；特征：需结合语义人工复核。

Hamm should support Yang Paul Hamm needs a new marketing strategy. Either that, or he needs a clue. One harmless gesture separates him from lionization in America and canonization in South Korea, and 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：marketing@9:2.5866 | strategy@10:1.9206 | new@8:1.5333。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 38. test:440 | Business → Sci/Tech

预测置信度 0.4092；真实类概率 0.2886；前两类概率差 0.1206。
分词数 38；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

Northrop Grumman Gets \$408 Million Pact Defense contractor Northrop Grumman Corp. on Monday said it received a 10-year, \$408 million Army contract to provide simulated battle command training support to Army corps commanders - the latest award in 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：training@28:1.6380 | command@27:0.6951 | support@29:0.4243。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 39. test:448 | Business → World

预测置信度 0.7729；真实类概率 0.2043；前两类概率差 0.5686。
分词数 63；未知词比例 0.00%；特征：世界与商业边界；含HTML实体或编码痕迹。

Oil Eases as Iraq Resumes Exports &lt;p&gt;\&lt;/p&gt;&lt;p&gt; By Andrew Mitchell&lt;/p&gt;&lt;p&gt; LONDON (Reuters) - High-flying oil prices eased for a\second session on Monday as Iraq resumed exports from both its\northern and southern outlets after lengthy disruption, despite\fierce fighting in the holy city of Najaf.&lt;/p&gt;

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：p@7:0.5141 | p@13:0.4863 | lt@12:0.3163。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 40. test:449 | Business → Sci/Tech

预测置信度 0.4906；真实类概率 0.4301；前两类概率差 0.0605。
分词数 23；未知词比例 4.35%；特征：商业与科技边界；前两类接近:概率差<0.2。

Botswana miners 'face dismissal' Botswana's giant Debswana diamond mining firm says it will sack workers who carry on with an illegal stoppage.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：carry@17:0.6742 | s@5:0.5112 | stoppage@22:0.4620。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 41. test:453 | Sci/Tech → Business

预测置信度 0.8595；真实类概率 0.1088；前两类概率差 0.7507。
分词数 23；未知词比例 0.00%；特征：商业与科技边界。

Wiretaps may mute Nextel rivals Fed up with technical excuses, FBI wants carriers to support eavesdropping capabilities for push-to-talk technology now.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：nextel@3:2.2982 | fed@5:1.8730 | rivals@4:1.8543。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 42. test:467 | Business → Sci/Tech

预测置信度 0.7869；真实类概率 0.2124；前两类概率差 0.5745。
分词数 35；未知词比例 0.00%；特征：商业与科技边界。

Deal has S2io champing at the gigabit OTTAWA -- A local firm that says it can help shrink backup times at large data centres is growing its business thanks to an alliance with Sun Microsystems Inc.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：microsystems@33:1.7553 | sun@32:1.6773 | large@20:0.0725。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 43. test:511 | World → Sci/Tech

预测置信度 0.6470；真实类概率 0.0609；前两类概率差 0.4078。
分词数 22；未知词比例 4.55%；特征：需结合语义人工复核。

Mich. Elephant Gets Therapy for Arthritis ROYAL OAK, Mich. - Like any patient, Wanda needs positive reinforcement to wrestle through her physical therapy...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：elephant@1:1.9883 | gets@2:1.1992 | any@10:0.1188。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 44. test:527 | World → Sports

预测置信度 0.6228；真实类概率 0.1871；前两类概率差 0.4357。
分词数 44；未知词比例 9.09%；特征：含HTML实体或编码痕迹。

 #39;Somebody please save my dad #39; Nick du Toit #39;s wife and stepdaughter are distraught that there is nothing they can do to help him. On Monday his stepdaughter, Marilise Bezuidenhout, was forced to convey the news of his possible death sentence 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@10:2.1393 | dad@5:1.1248 | my@4:1.0264。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 45. test:553 | Sports → World

预测置信度 0.5348；真实类概率 0.4606；前两类概率差 0.0742。
分词数 34；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Careening Indians Fall Slumping Cleveland lost a three-run lead while Derek Jeter homered and stole two ninth-inning bases as New York sent the Indians to their ninth consecutive loss, 5-4, Tuesday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：york@22:1.6323 | bases@19:1.5581 | ninth@17:1.3875。
能把预测改为真实类的单词遮挡数：10。仅表示局部敏感性，不代表已证明因果原因。

## 46. test:556 | Sci/Tech → World

预测置信度 0.5244；真实类概率 0.4190；前两类概率差 0.1054。
分词数 21；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Site security gets a recount at Rock the Vote Grassroots movement to register younger voters leaves publishing tools accessible to outsiders.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：movement@10:2.4360 | voters@14:1.5111 | grassroots@9:1.0953。
能把预测改为真实类的单词遮挡数：8。仅表示局部敏感性，不代表已证明因果原因。

## 47. test:563 | Sci/Tech → Business

预测置信度 0.7053；真实类概率 0.2472；前两类概率差 0.4581。
分词数 41；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Jamaican Government to Provide Free Internet Access in Poor &lt;b&gt;...&lt;/b&gt; Jamaica #39;s government on Tuesday announced a US\$5 million (Jamaican \$308 million) plan to provide free Internet access in poor communities across the island.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：b@10:2.2378 | b@13:1.8439 | 39@16:1.6719。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 48. test:565 | World → Business

预测置信度 0.9555；真实类概率 0.0273；前两类概率差 0.9281。
分词数 27；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

India's Tata makes powerful debut Shares  in Indian software services giant Tata Consultancy close 16 higher on their market debut, raising \$1.2bn for the company.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tata@12:1.4891 | consultancy@13:0.7465 | software@9:0.7114。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 49. test:568 | Sci/Tech → Business

预测置信度 0.5394；真实类概率 0.4570；前两类概率差 0.0824。
分词数 27；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

EU to probe Microsoft-Time Warner buy The decision is a setback for the two companies and their plan to acquire ContentGuard, a digital rights management firm.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：rights@24:0.6579 | eu@0:0.6115 | probe@2:0.5945。
能把预测改为真实类的单词遮挡数：15。仅表示局部敏感性，不代表已证明因果原因。

## 50. test:574 | World → Sci/Tech

预测置信度 0.5288；真实类概率 0.0431；前两类概率差 0.1085。
分词数 58；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Bryant Prosecutors Say Some Data Tainted DENVER - Crucial DNA evidence tested by defense experts in the Kobe Bryant sexual assault case might have been contaminated, prosecutors said in a court filing released Wednesday, just two days before jury selection is to begin.    Prosecutors said they had found contamination in DNA "control" samples intended to ensure testing was accurate...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：dna@8:0.6840 | dna@49:0.4903 | data@4:0.4207。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 51. test:582 | Business → Sci/Tech

预测置信度 0.8972；真实类概率 0.1021；前两类概率差 0.7951。
分词数 35；未知词比例 0.00%；特征：商业与科技边界。

MOM 2005 Released to Manufacturing Microsoft on Wednesday announced the release to manufacturing of Microsoft Operations Manager (MOM) 2005 and MOM 2005 Workgroup Edition, a new edition that the company previously called MOM 2005 Express.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：manager@16:0.4823 | microsoft@14:0.3011 | of@13:0.2491。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 52. test:600 | Business → World

预测置信度 0.9957；真实类概率 0.0041；前两类概率差 0.9916。
分词数 42；未知词比例 4.76%；特征：世界与商业边界；高置信错误>=0.9。

Belarus Bank Denies Money Laundering Charge A bank in Belarus has denied US charges that it laundered money for former Iraqi leader Saddam Hussein. Infobank, in a statement, said it has strictly followed international agreements related to the fight against illegal transactions.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：saddam@22:3.3903 | iraqi@20:3.3609 | leader@21:2.0453。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 53. test:636 | Sci/Tech → Business

预测置信度 0.4999；真实类概率 0.4995；前两类概率差 0.0004。
分词数 32；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Report: Intel Logs Big Gains In Flash Market Intel #39;s share of the booming flash market jumped 40.8 percent in the second quarter, according to market-research firm iSuppli Corp.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@9:1.0624 | s@10:0.4328 | gains@4:0.3502。
能把预测改为真实类的单词遮挡数：26。仅表示局部敏感性，不代表已证明因果原因。

## 54. test:642 | Sci/Tech → World

预测置信度 0.7243；真实类概率 0.2742；前两类概率差 0.4500。
分词数 46；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

U.N. Urges Funds to Curb African Locusts (AP) AP - With swarms of locusts threatening crops in a number of African countries, a U.N. agency appealed for an additional  #36;70 million in assistance Thursday to prevent the upsurge from becoming a full-scale plague.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ap@8:1.9120 | funds@3:1.7564 | ap@9:1.7436。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 55. test:643 | Business → World

预测置信度 0.9970；真实类概率 0.0000；前两类概率差 0.9945。
分词数 23；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

Nepal blockade 'blow to tourism' Nepal tour operators say tourists cancelled millions of  dollars of bookings due to the rebel blockade of Kathmandu.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：nepal@5:2.8952 | tour@6:1.3710 | tourism@4:1.0534。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 56. test:650 | World → Business

预测置信度 0.3720；真实类概率 0.3322；前两类概率差 0.0398。
分词数 51；未知词比例 3.92%；特征：世界与商业边界；前两类接近:概率差<0.2。

Spears' Fiance to Star in Her New Video NEW YORK - Britney Spears' former backup dancer and current fiance Kevin Federline can add another title to his resume: co-star.    On Wednesday, a Jive Records publicist confirmed Federline is featured in Spears' upcoming "My Prerogative" video, set to debut in mid-September...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：co@27:1.1004 | resume@26:0.5840 | my@42:0.4814。
能把预测改为真实类的单词遮挡数：13。仅表示局部敏感性，不代表已证明因果原因。

## 57. test:654 | Sci/Tech → World

预测置信度 0.6188；真实类概率 0.3783；前两类概率差 0.2405。
分词数 43；未知词比例 0.00%；特征：需结合语义人工复核。

Olympics: High-Flying Holm Aims to Defy Science (Reuters) Reuters - Sweden's gold medal-winning high\jumper Stefan Holm reckons he can leap even higher but\scientists say he and other athletes were already close to the\limit of what they can achieve.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：medal@13:1.4787 | say@27:1.1083 | winning@14:0.9477。
能把预测改为真实类的单词遮挡数：7。仅表示局部敏感性，不代表已证明因果原因。

## 58. test:655 | World → Business

预测置信度 0.5823；真实类概率 0.2254；前两类概率差 0.3569。
分词数 44；未知词比例 0.00%；特征：世界与商业边界。

Japan Won't Have U.S. Beef Anytime Soon (Reuters) Reuters - Japan's lucrative market for U.S.\beef, ruptured by mad cow disease worries, is likely to remain\closed for the rest of this year, U.S. meat industry officials\said on Thursday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：industry@39:1.1161 | meat@38:0.7100 | worries@24:0.6892。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 59. test:664 | Sci/Tech → Business

预测置信度 0.9341；真实类概率 0.0656；前两类概率差 0.8686。
分词数 24；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

TiVo loss widens SAN FRANCISCO (CBS.MW) - TiVo said its second-quarter loss widened from a year earlier on higher customer acquisition costs. Free!

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：mw@6:2.0849 | cbs@5:1.5215 | francisco@4:0.6739。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 60. test:676 | World → Sports

预测置信度 0.9982；真实类概率 0.0017；前两类概率差 0.9965。
分词数 24；未知词比例 0.00%；特征：高置信错误>=0.9。

US edge out Brazil for gold The United States beat Brazil 2-1 in extra time to win the women's Olympic football tournament.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：olympic@21:4.4584 | football@22:4.0729 | women@19:1.3559。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 61. test:680 | Sci/Tech → Business

预测置信度 0.7341；真实类概率 0.2561；前两类概率差 0.4780。
分词数 36；未知词比例 0.00%；特征：商业与科技边界。

Govt. to Test New Air Passenger Screening Program The US government unveiled plans on Thursday for a revised computer-based program using personal information to identify airline passengers who may pose a threat to air travel.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：personal@22:0.7545 | air@4:0.7462 | us@9:0.7026。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 62. test:685 | Business → Sci/Tech

预测置信度 0.7353；真实类概率 0.2639；前两类概率差 0.4714。
分词数 42；未知词比例 0.00%；特征：商业与科技边界。

PeopleSoft customers reassured Oracle Corp. President Charles Phillips on Monday said PeopleSoft Inc. customers have become more comfortable with the prospect of a merger between the two software firms even as the proposed transaction awaits a critical ruling from a Delaware court.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：inc@12:0.6836 | peoplesoft@11:0.5551 | software@27:0.3901。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 63. test:687 | Business → World

预测置信度 0.9018；真实类概率 0.0535；前两类概率差 0.8483。
分词数 39；未知词比例 5.13%；特征：世界与商业边界；高置信错误>=0.9。

Union leaders held under ESMA on Day 6 of strike New Delhi, August 26: The sixth day of the truckers strike on Thursday saw 12 more truckers being arrested under the Essential Services Maintenance Act (ESMA)in the Capital.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：essential@31:2.3661 | act@34:0.8599 | under@29:0.5223。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 64. test:705 | Sports → World

预测置信度 0.8286；真实类概率 0.1665；前两类概率差 0.6620。
分词数 65；未知词比例 9.23%；特征：需结合语义人工复核。

A great catch? Lobsters How does he like lobster? Boiled, steamed, broiled, baked, grilled? Newburg? Bahar Uttam prefers his with a capital L -- Lobsters -- and sees them frolicking on a tennis court rather than laid out on a plate. In Uttam's mind lurks a tasty dish for the town's sporting crowd, one that could satisfy the five-year hunger of tennis junkies, a ...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tennis@30:2.8748 | court@31:1.9308 | rather@32:1.5062。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 65. test:707 | Business → Sports

预测置信度 0.7765；真实类概率 0.1000；前两类概率差 0.6764。
分词数 39；未知词比例 5.13%；特征：需结合语义人工复核。

Dominicans' Swift Step Into Crisis SANTO DOMINGO, Dominican Republic -- When Sandro Batista smashed his banana truck into a tree in April, leaving him with two hideously shattered legs and a broken arm, his orthopedic surgeon sent his sister shopping.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：republic@8:0.7766 | his@32:0.6599 | dominican@7:0.5443。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 66. test:714 | Sports → World

预测置信度 0.6024；真实类概率 0.1164；前两类概率差 0.3233。
分词数 32；未知词比例 0.00%；特征：需结合语义人工复核。

CSKA sponsor rejects criticism RUSSIAN oil giant Sibneft today rejected any suggestion of a conflict of interest existing between Chelsea and CSKA Moscow who are due to meet in the Champions League.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：oil@5:3.4371 | giant@6:2.8732 | criticism@3:1.1412。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 67. test:719 | World → Business

预测置信度 0.9962；真实类概率 0.0024；前两类概率差 0.9938。
分词数 31；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

US economic growth slips to 2.8 Annual US economic growth fell to 2.8 in the second quarter of 2004, marking a slowdown from the 3 estimated a month ago.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：economic@9:1.0481 | annual@7:0.7925 | growth@10:0.6484。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 68. test:727 | World → Business

预测置信度 0.7510；真实类概率 0.1870；前两类概率差 0.5640。
分词数 48；未知词比例 0.00%；特征：世界与商业边界。

Japanese Utility Plans IPO in October (AP) AP - Electric Power Development Co., a former state-run utility, said Friday it is planning an initial public offering on the Tokyo Stock Exchange in October, a deal that could be the country's biggest new stock listing in six years.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：october@5:1.1417 | stock@29:1.0447 | exchange@30:1.0148。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 69. test:744 | Business → Sci/Tech

预测置信度 0.9343；真实类概率 0.0651；前两类概率差 0.8692。
分词数 52；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

HP to tempt holiday shoppers with sights and sounds The computer-hardware giant, best known for products such as PCs and printers, on Friday laid out its plan to become a brand-name in consumer electronics products such as flat-screen TVs, music players and the devices that move content between them.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：screen@40:0.6812 | hp@0:0.6059 | tvs@41:0.5013。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 70. test:747 | World → Sports

预测置信度 0.9994；真实类概率 0.0003；前两类概率差 0.9991。
分词数 34；未知词比例 2.94%；特征：高置信错误>=0.9。

Argentina Beats U.S. Men's Basketball Team Argentina defeated the United States team of National Basketball Association stars 89-81 here Friday in the Olympic semi-finals, dethroning the three-time defending champions.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：basketball@16:4.9520 | association@17:4.1682 | stars@18:1.0302。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 71. test:762 | Business → Sci/Tech

预测置信度 0.8065；真实类概率 0.1932；前两类概率差 0.6133。
分词数 45；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Siemens Says Cellphone Flaw May Hurt Users and Its Profit Siemens, the world #39;s fourth-largest maker of mobile phones, said Friday that a software flaw that can create a piercing ring in its newest phone models might hurt earnings in its handset division.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：cellphone@2:0.7322 | siemens@0:0.6812 | flaw@3:0.6051。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 72. test:819 | World → Business

预测置信度 0.9394；真实类概率 0.0216；前两类概率差 0.9005。
分词数 34；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Terror is below radar in Russia It took 2 days for Russia #39;s security service to announce what virtually everyone else believed from the moment two domestic passenger airlines plunged to earth simultaneously 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：airlines@29:3.1693 | 39@12:1.8079 | plunged@30:1.3837。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 73. test:833 | World → Sports

预测置信度 0.5672；真实类概率 0.2839；前两类概率差 0.2832。
分词数 35；未知词比例 2.86%；特征：需结合语义人工复核。

Conn. Man, 70, Oldest to Swim Channel LONDON - A retired Connecticut pilot has become the oldest person to swim the English Channel. George Brunstad, 70, left Dover, England, Saturday morning heading for the French Coast...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：connecticut@10:1.1001 | retired@9:0.8260 | pilot@11:0.6740。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 74. test:839 | Sci/Tech → Business

预测置信度 0.9986；真实类概率 0.0003；前两类概率差 0.9975。
分词数 47；未知词比例 2.13%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Our mobile margins will fall: Telstra TELSTRA chief financial officer John Stanhope has admitted Telstra #39;s margins in its \$4.5 billion a year mobile phone business will shrink this year in the face of increased price competition and the growing cost of acquiring new customers.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：telstra@6:3.0446 | telstra@5:2.0923 | financial@8:1.7878。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 75. test:855 | Sports → Business

预测置信度 0.3809；真实类概率 0.0778；前两类概率差 0.1064。
分词数 36；未知词比例 0.00%；特征：前两类接近:概率差<0.2；含HTML实体或编码痕迹。

A  #39;new Greece #39; beams after success of Games As Greeks get a boost, it remains unclear if success will mean higher stature in Europe. By Peter Ford  Staff writer of The Christian Science Monitor.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：higher@22:1.6196 | stature@23:0.9652 | europe@25:0.5573。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 76. test:877 | Business → Sci/Tech

预测置信度 0.7236；真实类概率 0.2757；前两类概率差 0.4479。
分词数 26；未知词比例 0.00%；特征：商业与科技边界。

For Now, Unwired Means Unlisted. That May Change. In October, most major cellphone carriers plan to start compiling a publicly accessible listing of wireless phone numbers.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：wireless@23:0.4214 | phone@24:0.0888 | means@3:0.0398。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 77. test:881 | Business → World

预测置信度 0.4709；真实类概率 0.3013；前两类概率差 0.1697。
分词数 37；未知词比例 5.41%；特征：世界与商业边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Scaffold collapse survivors improving One of the men who survived Friday #39;s fatal scaffold collapse is in guarded condition at Detroit Receiving Hospital and the two other survivors were released on Sunday, a hospital spokeswoman said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：survivors@2:1.1480 | collapse@1:1.0155 | sunday@32:0.3537。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 78. test:887 | Business → Sci/Tech

预测置信度 0.9384；真实类概率 0.0615；前两类概率差 0.8769。
分词数 40；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

On TV -- from the Internet  SAN MATEO, Calif. -- The promise of Internet-based video has long been hamstrung by copyright and piracy worries, slow dial-up connections, technical challenges, and consumer disdain for watching blotchy videos on their home computers.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：copyright@19:0.2023 | dial@24:0.1465 | internet@4:0.1303。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 79. test:892 | Business → Sci/Tech

预测置信度 0.9817；真实类概率 0.0168；前两类概率差 0.9650。
分词数 21；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Intel in new chip breakthrough Intel creates a more powerful memory chip without increasing its size, confounding the firm's critics.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：memory@10:0.7358 | chip@11:0.5881 | chip@3:0.4538。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 80. test:912 | Sci/Tech → Sports

预测置信度 0.9998；真实类概率 0.0000；前两类概率差 0.9996。
分词数 37；未知词比例 0.00%；特征：高置信错误>=0.9。

Bryant Makes First Appearance at Trial (AP) AP - NBA star Kobe Bryant arrived at his sexual assault trial Monday as attorneys in the case who spent the weekend poring over questionnaires prepared to question potential jurors individually.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：nba@8:3.4614 | kobe@10:2.7941 | ap@7:2.1910。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 81. test:922 | Business → World

预测置信度 0.7812；真实类概率 0.2088；前两类概率差 0.5724。
分词数 52；未知词比例 0.00%；特征：世界与商业边界。

Stocks Dip on Consumer Income Report News (AP) AP - An unsettling report on consumer incomes set off a spate of profit-taking on Wall Street Monday as investors worried that a tepid economy would erode companies' third-quarter earnings. Another drop in oil prices failed to shake the gloom from the market.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ap@8:2.8477 | ap@7:2.5410 | stocks@0:1.6081。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 82. test:927 | Sci/Tech → Business

预测置信度 0.6099；真实类概率 0.3181；前两类概率差 0.2918。
分词数 19；未知词比例 0.00%；特征：商业与科技边界；短文本<=20词。

Survey: IT spending to grow modestly next year CIO confidence is up in third quarter, according to Forrester poll.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：confidence@9:1.1699 | cio@8:0.6908 | year@7:0.4769。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 83. test:930 | World → Business

预测置信度 0.7221；真实类概率 0.2768；前两类概率差 0.4453。
分词数 37；未知词比例 0.00%；特征：世界与商业边界；含HTML实体或编码痕迹。

Iraqi oil exports slump: report NEAR daily attacks on pipelines and pumping stations had pushed down Iraq #39;s oil exports to their lowest point in nearly a year, Britain #39;s Financial Times newspaper reported today.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@30:1.3264 | financial@32:0.8669 | exports@2:0.8107。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 84. test:933 | Sci/Tech → Business

预测置信度 0.5278；真实类概率 0.3179；前两类概率差 0.2099。
分词数 31；未知词比例 0.00%；特征：商业与科技边界。

Orion Debuts Cluster Workstation Orion Multisystems, a new company founded by former Transmeta (Quote, Chart) executives, debuted a family of workstations Monday that think and act like a cluster of servers.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：quote@13:0.9307 | former@11:0.7392 | executives@15:0.6916。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 85. test:942 | World → Business

预测置信度 0.9773；真实类概率 0.0029；前两类概率差 0.9575。
分词数 41；未知词比例 2.44%；特征：世界与商业边界；高置信错误>=0.9。

Japan should outsource more The Japanese information services industry clocked up sales of 13,703.9 billion yen in fiscal 2001, according to a report on selected service industries for 2001 released by the Ministry of Economy, Trade and Industry (METI).

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：economy@36:1.2846 | trade@37:0.9667 | industry@8:0.6440。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 86. test:951 | Sci/Tech → Sports

预测置信度 0.4252；真实类概率 0.2134；前两类概率差 0.2118。
分词数 21；未知词比例 9.52%；特征：需结合语义人工复核。

Hall of Shame   Hall of Fame We spotlight people and products that pester us...and the heroes saving us from annoyances.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：the@15:0.8327 | heroes@16:0.7824 | hall@3:0.3501。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 87. test:967 | World → Sports

预测置信度 0.9978；真实类概率 0.0021；前两类概率差 0.9957。
分词数 62；未知词比例 0.00%；特征：高置信错误>=0.9。

Maddux Wins No. 302, Baker Wins No. 1,000 Greg Maddux pitched the Chicago Cubs into the lead in the NL wild-card race and gave Dusty Baker a win to remember. Maddux threw seven shutout innings for his 302nd career win, Baker got his 1,000th victory as a manager and Chicago beat the Montreal Expos 5-2 on Monday night...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：expos@56:0.8735 | for@37:0.8415 | montreal@55:0.7046。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 88. test:1004 | Sci/Tech → World

预测置信度 0.5873；真实类概率 0.4095；前两类概率差 0.1778。
分词数 35；未知词比例 11.43%；特征：前两类接近:概率差<0.2；未知词比例>=10%。

Old Rumors of Gay Sex Prove Powerful on Web Va. GOP members chose Del. Thelma Drake (Norfolk) to replace Rep. Edward L. Schrock after he resigned amidst allegations Schrock indulged in or solicited gay sex.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：gay@3:0.8090 | va@9:0.6321 | after@23:0.3258。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 89. test:1011 | Sci/Tech → Business

预测置信度 0.4170；真实类概率 0.2439；前两类概率差 0.0779。
分词数 39；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

China's Lenovo in talks with 'major IT firm' for acquisition (AFP) AFP - China's largest manufacturer of personal computers Lenovo Group said it is in negotiations with a major information technology company, believed to be US-based IBM.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：manufacturer@16:1.4709 | largest@15:0.9550 | group@21:0.8900。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 90. test:1019 | Sci/Tech → World

预测置信度 0.9709；真实类概率 0.0112；前两类概率差 0.9545。
分词数 38；未知词比例 0.00%；特征：高置信错误>=0.9。

China Reports Births of Two Giant Pandas (AP) AP - For pandas, it's practically a baby boom. Two giant pandas were born this week, and mothers and cubs were doing fine, the official Xinhua News Agency reported Wednesday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ap@7:1.3685 | ap@8:1.0498 | cubs@27:0.9893。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 91. test:1043 | Sci/Tech → World

预测置信度 0.6966；真实类概率 0.3021；前两类概率差 0.3944。
分词数 43；未知词比例 0.00%；特征：需结合语义人工复核。

Strong Hurricane Roars Over Bahamas Toward Florida (Reuters) Reuters - Hurricane Frances battered the\southeastern Bahamas islands with 140 mph winds on Wednesday as\it roared toward the United States and put millions of people\on alert along Florida's heavily populated east coast.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：bahamas@14:1.0176 | mph@18:0.5248 | winds@19:0.4637。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 92. test:1051 | Business → Sci/Tech

预测置信度 0.9847；真实类概率 0.0135；前两类概率差 0.9712。
分词数 26；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Software Service Aims to Outfox Caller ID A new computerized service enables customers to create phony outbound phone numbers in order to mask their telephone identities.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：id@6:0.8445 | caller@5:0.7382 | new@8:0.3302。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 93. test:1062 | Business → Sci/Tech

预测置信度 0.8447；真实类概率 0.1125；前两类概率差 0.7321。
分词数 36；未知词比例 0.00%；特征：商业与科技边界。

Red Hat replaces CFO Red Hat on Thursday named Charles Peters Jr. as executive vice president and chief financial officer. Peters replaces Kevin Thompson, who unexpectedly announced his resignation in June, a few days before the 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：cfo@3:2.5035 | replaces@2:1.2230 | and@16:0.6789。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 94. test:1074 | Sci/Tech → Business

预测置信度 0.9121；真实类概率 0.0830；前两类概率差 0.8292。
分词数 25；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Appeals court faults Oracle in shareholder suit Judges send case back to lower court to sort out allegations of improper bookkeeping and "suspicious" stock sales.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：stock@23:2.0496 | sales@24:1.5857 | shareholder@5:0.6813。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 95. test:1080 | World → Sports

预测置信度 0.9547；真实类概率 0.0399；前两类概率差 0.9148。
分词数 49；未知词比例 0.00%；特征：高置信错误>=0.9。

Davenport Advances at U.S. Open NEW YORK - Lindsay Davenport's summer of success stayed on course Thursday when the fifth-seeded former U.S. Open champion defeated Arantxa Parra Santonja 6-4, 6-2 and advanced to the third round of the season's final Grand Slam event...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：season@43:1.5934 | open@25:1.2508 | champion@26:1.0895。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 96. test:1084 | Business → World

预测置信度 0.8895；真实类概率 0.1088；前两类概率差 0.7807。
分词数 44；未知词比例 0.00%；特征：世界与商业边界。

Megawati kicks off 36th ASEAN economic meeting JAKARTA (Agencies): President Megawati Soekarnoputri opened high-level economic talks between members of the Association of Southeast Asian Nations (ASEAN) on Friday with a warning to ASEAN leaders that they must stay the course on their agreed 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：president@9:1.0813 | jakarta@7:1.0558 | megawati@10:0.6027。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 97. test:1087 | Sci/Tech → Business

预测置信度 0.9007；真实类概率 0.0933；前两类概率差 0.8074。
分词数 44；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Semiconductor Manufacturing to Boost Capacity by Half (Update2) Semiconductor Manufacturing International Corp., China #39;s biggest supplier of made-to-order chips, said its factory capacity will rise by more than half in the second half as the company brings more plants on line.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：update2@7:1.2611 | 39@13:1.1529 | half@6:0.7269。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 98. test:1098 | Sci/Tech → Sports

预测置信度 0.9940；真实类概率 0.0033；前两类概率差 0.9907。
分词数 22；未知词比例 0.00%；特征：高置信错误>=0.9。

The Bahamas - the real medal winner of the Athens Olympics A different way of calculating the medal standings brings some interesting results.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：medal@4:2.1871 | winner@5:2.1080 | real@3:1.2812。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 99. test:1101 | Business → Sci/Tech

预测置信度 0.8314；真实类概率 0.1103；前两类概率差 0.7210。
分词数 20；未知词比例 5.00%；特征：商业与科技边界；短文本<=20词。

Del Monte Needs 9Lives The leading private and branded food and pet products marketer is spending to revamp its image.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：pet@11:1.7200 | products@12:0.8153 | revamp@17:0.0775。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 100. test:1110 | Business → World

预测置信度 0.9756；真实类概率 0.0236；前两类概率差 0.9520。
分词数 45；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9；含HTML实体或编码痕迹。

EU foreign ministers hope to break deadlock over ASEM summit The European Union said Friday it  quot;hoped to reach a conclusion quot; at a meeting of foreign ministers on the participation of military-ruled Myanmar in an upcoming summit of Asian and European nations.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：military@33:1.4296 | summit@39:0.5395 | myanmar@35:0.3170。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 101. test:1124 | Business → Sci/Tech

预测置信度 0.7670；真实类概率 0.2317；前两类概率差 0.5353。
分词数 40；未知词比例 0.00%；特征：商业与科技边界。

Judge: Geico can sue Google, Overture over ads A federal judge in Virginia has ruled that a trademark infringement suit filed by the Government Employees Insurance Co. (GEICO) against Internet search giants Google Inc. and Overture Services Inc. can proceed.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：internet@29:0.4618 | infringement@18:0.3808 | google@4:0.3460。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 102. test:1168 | World → Business

预测置信度 0.9051；真实类概率 0.0736；前两类概率差 0.8315。
分词数 54；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9；含HTML实体或编码痕迹。

ASEAN moves closer to single market with  #39;road map #39;, global trade &lt;b&gt;...&lt;/b&gt; JAKARTA : ASEAN finance ministers ended a meeting which saw Southeast Asia edge closer to a Europe-style single market, laying out a  quot;road map quot; for integration and opening doors to wider global trade.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：finance@21:2.8355 | ministers@22:0.9938 | b@17:0.7435。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 103. test:1197 | Business → World

预测置信度 0.8352；真实类概率 0.0362；前两类概率差 0.7090。
分词数 32；未知词比例 3.12%；特征：世界与商业边界。

World briefs LONDON - A man wielding a machete and a knife attacked two security guards at the building housing the headquarters of the British domestic intelligence service MI5 on Friday, police said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：intelligence@25:1.2100 | british@23:0.8479 | security@13:0.3957。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 104. test:1204 | Business → World

预测置信度 0.7216；真实类概率 0.2454；前两类概率差 0.4761。
分词数 33；未知词比例 3.03%；特征：世界与商业边界。

Labor situation deserves honest talk For a moment last week, President Bush escaped the White House spin chamber and was the plainspoken man much of the nation came to like four years ago.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：bush@11:0.7328 | president@10:0.6072 | white@14:0.4078。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 105. test:1252 | Business → Sci/Tech

预测置信度 0.5616；真实类概率 0.4068；前两类概率差 0.1548。
分词数 34；未知词比例 2.94%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Retailers Looking to Move Plasma TV's (AP) AP - Hanging stockings by the chimney with care? Retailers hope that St. Nicholas soon will be there  #151; to hang a 42-inch plasma-screen TV.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：inch@30:1.3307 | ap@8:1.1122 | screen@32:1.1011。
能把预测改为真实类的单词遮挡数：5。仅表示局部敏感性，不代表已证明因果原因。

## 106. test:1269 | Sci/Tech → World

预测置信度 0.9991；真实类概率 0.0001；前两类概率差 0.9986。
分词数 38；未知词比例 0.00%；特征：高置信错误>=0.9；含HTML实体或编码痕迹。

Philippines mourns dead in Russian school siege The Philippines Saturday expressed quot;deepest sympathy quot; to the families of the dead in the Russian school siege on Friday, in which 322 people were killed when Russian troops stormed 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：philippines@8:1.5041 | saturday@9:1.2468 | philippines@0:0.7888。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 107. test:1280 | Sci/Tech → Business

预测置信度 0.7070；真实类概率 0.2919；前两类概率差 0.4151。
分词数 40；未知词比例 0.00%；特征：商业与科技边界。

Dell cuts prices on many corporate products Dell on Monday said it had cut prices by as much as fifth for a range of products aimed at US corporate customers, as the computer maker passed along savings from cheaper components.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：us@27:0.9323 | corporate@28:0.9037 | cuts@1:0.7681。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 108. test:1289 | Business → Sci/Tech

预测置信度 0.4880；真实类概率 0.3230；前两类概率差 0.1650。
分词数 22；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

Hurricane loss 'less than feared' Hurricane Frances could cause \$3-6bn in insured losses in the US, less than experts first predicted.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：experts@19:0.9368 | first@20:0.4467 | predicted@21:0.2875。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 109. test:1292 | Sci/Tech → Business

预测置信度 0.7936；真实类概率 0.1931；前两类概率差 0.6005。
分词数 29；未知词比例 0.00%；特征：商业与科技边界。

Working Long Hours? Take a Massage Break, Courtesy of Your Boss Companies across the country are offering yoga and meditation classes to help employees relax, reduce stress and recharge.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：boss@10:0.8139 | break@6:0.5034 | and@18:0.4599。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 110. test:1296 | Business → World

预测置信度 0.8742；真实类概率 0.0479；前两类概率差 0.8251。
分词数 41；未知词比例 2.44%；特征：世界与商业边界；含HTML实体或编码痕迹。

Israel to close Erez industrial zone before March Israel would start liquidating the Erez industrial zone in the northern Gaza Strip before launching the first stage of the disengagement plan in March 2005,local newspaper Ha #39;aretz reported on Tuesday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：israel@8:1.2772 | gaza@19:0.9045 | march@7:0.7849。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 111. test:1307 | Sci/Tech → World

预测置信度 0.9135；真实类概率 0.0323；前两类概率差 0.8597。
分词数 26；未知词比例 0.00%；特征：高置信错误>=0.9。

Tribe challenges American origins Some of the earliest settlers of America may have been from Australia, southern Asia, and the Pacific, not northern Asia, research suggests.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：asia@23:1.3033 | research@24:1.1013 | australia@15:1.0790。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 112. test:1317 | Sports → World

预测置信度 0.7996；真实类概率 0.0012；前两类概率差 0.6559。
分词数 36；未知词比例 0.00%；特征：需结合语义人工复核。

Florida deaths blamed on Hurricane Frances State and local officials Tuesday said nine people have died in Florida because of Hurricane Frances. The following describes those deaths: - A 15-year-old grandson and a former son 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：deaths@26:0.9096 | deaths@1:0.9064 | said@11:0.7978。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 113. test:1340 | Sports → Business

预测置信度 0.5054；真实类概率 0.4028；前两类概率差 0.1026。
分词数 49；未知词比例 0.00%；特征：前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Study: Athletic success doesn #39;t pay off in donations Success in big-time sports has little, if any, effect on a college #39;s alumni donations or the academic quality of its applicants, according to a study made under the direction of the Knight Commission on Intercollegiate Athletics.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：study@0:0.9089 | commission@45:0.8321 | study@37:0.6827。
能把预测改为真实类的单词遮挡数：10。仅表示局部敏感性，不代表已证明因果原因。

## 114. test:1343 | Sci/Tech → Business

预测置信度 0.5797；真实类概率 0.4119；前两类概率差 0.1678。
分词数 44；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

Matsushita Unveils DVD Recorders, Eyes Higher Share  TOKYO (Reuters) - Panasonic brand products maker Matsushita  Electric Industrial unveiled five new DVD recorders on  Wednesday and said it was aiming to boost its share of the  domestic market to over 40 percent from around 35 percent.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tokyo@7:1.5756 | higher@5:1.4251 | reuters@8:1.4076。
能把预测改为真实类的单词遮挡数：8。仅表示局部敏感性，不代表已证明因果原因。

## 115. test:1361 | Business → Sci/Tech

预测置信度 0.7129；真实类概率 0.2836；前两类概率差 0.4292。
分词数 35；未知词比例 2.86%；特征：商业与科技边界。

Movies in a snap: Netflix and TiVo discuss downloads Bee Staff Writer. The high-tech ground is shifting underfoot again, amid rumblings of a new Silicon Valley alliance that would let owners of TiVo Inc.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tech@14:0.6563 | again@19:0.4034 | tivo@6:0.3616。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 116. test:1364 | Sci/Tech → Business

预测置信度 0.8632；真实类概率 0.1278；前两类概率差 0.7354。
分词数 39；未知词比例 2.56%；特征：商业与科技边界；含HTML实体或编码痕迹。

Hyundai signs deal for China truck plant Hyundai Motor Co. said yesterday that it has signed an agreement with a Chinese company, Jianghuai Automobile Corp., to build a commercial vehicle and engine plant in China #39;s Anhui province.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：co@9:1.0064 | yesterday@11:0.8562 | motor@8:0.7958。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 117. test:1375 | Sci/Tech → Business

预测置信度 0.4097；真实类概率 0.4066；前两类概率差 0.0031。
分词数 30；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

Motorola Aims to Sharpen Design Edge In a 26th-floor office suite overlooking Lake Michigan, some 40 industrial designers, mechanical engineers and specialists in fields ranging from anthropology to musicology 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：40@16:1.1866 | industrial@17:1.1189 | a@7:0.6344。
能把预测改为真实类的单词遮挡数：25。仅表示局部敏感性，不代表已证明因果原因。

## 118. test:1377 | Sci/Tech → World

预测置信度 0.8350；真实类概率 0.0359；前两类概率差 0.7126。
分词数 63；未知词比例 0.00%；特征：需结合语义人工复核。

Groups Offers Beer for Blood Donations (AP) AP - Some in Michigan who roll up their sleeves to donate blood will get a racetrack T-shirt, hat and pin. Sponsors in San Diego have given away whale-watching trips. On Wednesday, the Cleveland Regional Transit Authority handed out vouchers for a pint of any beverage, including beer, in exchange for a pint of blood.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ap@6:1.4205 | beer@2:1.2955 | ap@7:1.2731。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 119. test:1388 | Business → Sci/Tech

预测置信度 0.6128；真实类概率 0.3719；前两类概率差 0.2409。
分词数 49；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Ex-WorldCom CEO Wants Witness Immunity (Reuters) Reuters - Lawyers for former WorldCom  Chief\Executive Bernard Ebbers are seeking immunity for two witnesses\who they believe could clear their client of fraud charges\related to the company's  #36;11 billion accounting scandal,\according to court papers filed on Wednesday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：reuters@7:1.0313 | ceo@2:0.8557 | reuters@6:0.7954。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 120. test:1421 | World → Sci/Tech

预测置信度 0.6500；真实类概率 0.2770；前两类概率差 0.3730。
分词数 43；未知词比例 0.00%；特征：需结合语义人工复核。

Groups Petition U.S. on China Policies (AP) AP - A group of industry, farm and labor groups, seeking to put pressure on the Bush administration before the presidential election, petitioned the government on Thursday to file an unfair trade practices case against China.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：trade@38:1.5458 | unfair@37:1.4832 | practices@39:1.4161。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 121. test:1447 | Sci/Tech → Business

预测置信度 0.7181；真实类概率 0.0688；前两类概率差 0.5072。
分词数 38；未知词比例 0.00%；特征：商业与科技边界。

Florida Starts To Recover in the Wake of Hurricane Frances President Bush will travel to Florida Wednesday to survey damage from Hurricane Frances. He sent a letter to Congress asking for \$2 billion to help with recovery efforts.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：president@10:0.9006 | bush@11:0.8666 | wednesday@16:0.6347。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 122. test:1466 | World → Sports

预测置信度 0.7495；真实类概率 0.2331；前两类概率差 0.5164。
分词数 41；未知词比例 0.00%；特征：需结合语义人工复核。

Colts Lead Pats Early in Third Quarter FOXBORO, Mass. - Peyton Manning reached the 25,000-yard passing mark faster than anyone but Dan Marino, and the Indianapolis Colts shredded the New England Patriots for a 17-13 halftime lead Thursday night...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：patriots@32:1.4436 | colts@27:0.8270 | england@31:0.5183。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 123. test:1477 | World → Business

预测置信度 0.5199；真实类概率 0.3612；前两类概率差 0.1587。
分词数 41；未知词比例 2.44%；特征：世界与商业边界；前两类接近:概率差<0.2。

Grenada In Crisis - Friday 10, September-2004 DESPAIR is setting in among the 80 000 homeless Grenadians who, ravaged and traumatised by the damage done to them by Hurricane Ivan, exist each day with no food, no water and no hope.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：food@35:0.4985 | no@36:0.4854 | no@34:0.4653。
能把预测改为真实类的单词遮挡数：5。仅表示局部敏感性，不代表已证明因果原因。

## 124. test:1494 | World → Sci/Tech

预测置信度 0.9743；真实类概率 0.0157；前两类概率差 0.9586。
分词数 25；未知词比例 0.00%；特征：高置信错误>=0.9。

Telescope snaps distant 'planet' The first direct image of a planet circling another star may have been obtained by a US-European team of astronomers.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：telescope@0:2.8790 | snaps@1:1.1776 | astronomers@24:0.8897。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 125. test:1510 | Sci/Tech → Business

预测置信度 0.5470；真实类概率 0.4479；前两类概率差 0.0991。
分词数 41；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Firms announce video antipiracy technology This fourth priority #39;s main focus has been improving or obtaining CRM and ERP software for the past year and a half. NDS, STMicroelectronics and Thomson said Friday that they will develop new encryption technology 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@8:1.3362 | s@9:0.9584 | main@10:0.7320。
能把预测改为真实类的单词遮挡数：17。仅表示局部敏感性，不代表已证明因果原因。

## 126. test:1527 | Business → Sci/Tech

预测置信度 0.4307；真实类概率 0.4301；前两类概率差 0.0006。
分词数 51；未知词比例 1.96%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Storms Seem to Cure Floridians of Hurricane Amnesia The state #39;s East Coast hadn #39;t been hit by a hurricane since 1999. That, and the fact that Florida hasn #39;t had its historic share of such storms in recent decades, has led to some complacency about their effects.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：effects@50:0.3750 | recent@41:0.3468 | storms@0:0.3281。
能把预测改为真实类的单词遮挡数：9。仅表示局部敏感性，不代表已证明因果原因。

## 127. test:1531 | Business → World

预测置信度 0.4791；真实类概率 0.4629；前两类概率差 0.0162。
分词数 38；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

Stocks in a rut According to the FTSE World Index Japan has been best performer of the major markets with a 6 per cent rise in dollar terms while Germany, down 7.7 per cent, was the worst.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：index@9:1.0535 | japan@10:0.9814 | was@35:0.5913。
能把预测改为真实类的单词遮挡数：12。仅表示局部敏感性，不代表已证明因果原因。

## 128. test:1533 | World → Sports

预测置信度 0.8054；真实类概率 0.1932；前两类概率差 0.6122。
分词数 29；未知词比例 0.00%；特征：需结合语义人工复核。

Collingwood anchors England (AFP) AFP - Paul Collingwood's unbeaten 80 took England to 299 for seven against Zimbabwe in their opening Champions Trophy Pool D match at Edgbaston here.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：champions@21:2.8388 | opening@20:1.8755 | trophy@22:1.2620。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 129. test:1541 | Sci/Tech → Business

预测置信度 0.4797；真实类概率 0.2991；前两类概率差 0.1806。
分词数 26；未知词比例 3.85%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Tough to predict a hurricane landfall this season #39;s busy season of landfalling Atlantic hurricanes has seen a few less-than-perfect calls by tropical 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@8:1.4974 | s@9:0.6317 | few@19:0.5521。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 130. test:1548 | Business → World

预测置信度 0.7182；真实类概率 0.2565；前两类概率差 0.4617。
分词数 53；未知词比例 0.00%；特征：世界与商业边界。

Post-Olympic Greece tightens purse, sells family silver to fill budget holes (AFP) AFP - Squeezed by a swelling public deficit and debt following last month's costly Athens Olympics, the Greek government said it would cut defence spending and boost revenue by 1.5 billion euros (1.84 billion dollars) in privatisation receipts.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：afp@13:1.5773 | olympics@28:0.6987 | afp@12:0.6867。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 131. test:1552 | Business → Sci/Tech

预测置信度 0.4617；真实类概率 0.1269；前两类概率差 0.0507。
分词数 25；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

Restoring an Original At Charles Schwab, executives plan a return to the firm's original mission of serving mom-and-pop, buy-and-hold investors.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：mission@15:1.5097 | original@14:0.8813 | and@22:0.4356。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 132. test:1599 | World → Sports

预测置信度 0.8445；真实类概率 0.1503；前两类概率差 0.6942。
分词数 41；未知词比例 9.76%；特征：需结合语义人工复核。

Two gored to death in Spanish bull-run Two Spanish men were gored to death by fighting bulls yesterday during the bull-run at the local fiestas in Ampuero, a town 30 miles east of the northern port city of Santander.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：yesterday@18:1.3077 | run@7:0.6257 | bulls@17:0.5156。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 133. test:1603 | Business → Sci/Tech

预测置信度 0.9410；真实类概率 0.0413；前两类概率差 0.8997。
分词数 26；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Let a Thousand Ideas Flower: China Is a New Hotbed of Research In recent years, hundreds of multinational companies have set up research laboratories in China.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ideas@3:2.3610 | flower@4:1.5561 | china@5:0.1977。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 134. test:1609 | Sci/Tech → Business

预测置信度 0.5856；真实类概率 0.3675；前两类概率差 0.2181。
分词数 32；未知词比例 3.12%；特征：商业与科技边界。

Bullies move online Singapore - More complaints of cyberbullying are emerging from youngsters in Singapore than any other country except the United States, an international safety group said in a report on Monday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：group@25:0.9725 | safety@24:0.7513 | international@23:0.5212。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 135. test:1617 | World → Sports

预测置信度 0.8148；真实类概率 0.1609；前两类概率差 0.6539。
分词数 49；未知词比例 0.00%；特征：需结合语义人工复核。

At Last, Success on the Road for Lions The Detroit Lions went three full seasons without winning an away game, setting an NFL record for road futility. They ended that ignominious streak Sunday in their first opportunity of the season, beating the Chicago Bears 20-16 at Soldier Field...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：the@38:0.4444 | without@15:0.4442 | season@39:0.4352。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 136. test:1658 | World → Sci/Tech

预测置信度 0.5164；真实类概率 0.0455；前两类概率差 0.0791。
分词数 48；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

FDA Approves Lens Implant to Sharpen Sight WASHINGTON - There's a new option for people who suffer from extreme nearsightedness, whose world loses its crisp edge just a few inches from their noses. The first implantable lens for nearsightedness was approved Monday by the Food and Drug Administration...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：fda@0:2.4314 | approves@1:1.3644 | lens@2:0.7569。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 137. test:1662 | Business → World

预测置信度 0.6404；真实类概率 0.2999；前两类概率差 0.3406。
分词数 32；未知词比例 0.00%；特征：世界与商业边界。

Sony-Led Group to Acquire MGM for \$3B LOS ANGELES Sept. 13, 2004 - A consortium led by Sony Corp. has agreed in principle to acquire famed Hollywood studio Metro-Goldwyn-Mayer Inc.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：los@8:2.7376 | 3b@7:2.3504 | angeles@9:0.7395。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 138. test:1668 | Business → World

预测置信度 0.9807；真实类概率 0.0186；前两类概率差 0.9621。
分词数 39；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

EU increases pressure for rights in Myanmar EU foreign ministers agreed Monday to tighten sanctions against Myanmar if it does not improve its human rights record by Oct. 8, when an EU meeting with Asian countries starts in Vietnam.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：myanmar@6:1.7477 | eu@7:0.8759 | human@23:0.4537。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 139. test:1689 | Sci/Tech → Business

预测置信度 0.7433；真实类概率 0.2565；前两类概率差 0.4869。
分词数 37；未知词比例 0.00%；特征：商业与科技边界。

Sun trims fourth-quarter earnings by \$12 million Sun Microsystems Inc. trimmed its fourth quarter and full-year 2004 results this week, to account for final accounting of asset retirement obligations and its settlement with Microsoft Corp.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：asset@28:1.3807 | retirement@29:1.2577 | accounting@26:0.8287。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 140. test:1691 | World → Business

预测置信度 0.7295；真实类概率 0.2588；前两类概率差 0.4707。
分词数 40；未知词比例 0.00%；特征：世界与商业边界。

German investor confidence slumped in September BERLIN - German investor confidence dropped sharply in September, a key economic indicator released Tuesday showed amid concerns about the impact of high oil prices on consumer demand and the outlook for the global economy.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：prices@29:0.7696 | consumer@31:0.7575 | economic@16:0.6327。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 141. test:1742 | World → Sci/Tech

预测置信度 0.9131；真实类概率 0.0371；前两类概率差 0.8760。
分词数 44；未知词比例 2.27%；特征：高置信错误>=0.9；含HTML实体或编码痕迹。

LETTER FROM EUROPE The All-Too-Human Hitler, on Your Big Screen The release of a major movie about Hitler is, by definition, a remarkable event in Germany, especially if it portrays one of history #39;s great monsters as a human being, given 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@35:0.7031 | your@9:0.6654 | screen@11:0.5202。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 142. test:1743 | Sci/Tech → Business

预测置信度 0.7810；真实类概率 0.1946；前两类概率差 0.5864。
分词数 42；未知词比例 0.00%；特征：商业与科技边界。

Sony Set to Exert Influence on Discs As the leader of the group that plans to buy Metro-Goldwyn-Mayer, Sony is poised to gain considerable power in its fight to set the format for the next generation of digital video discs.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：goldwyn@18:2.4196 | buy@16:1.5346 | metro@17:1.5225。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 143. test:1755 | World → Sci/Tech

预测置信度 0.8640；真实类概率 0.0272；前两类概率差 0.7721。
分词数 42；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

Same-sex divorce rules still hazy Now that an Ontario couple has been given Canada #39;s first same-sex divorce, experts are divided over just how easy it will be for gays and lesbians in other provinces to end their marriages.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@15:0.6773 | experts@21:0.3707 | sex@19:0.2962。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 144. test:1770 | Business → Sci/Tech

预测置信度 0.7902；真实类概率 0.2057；前两类概率差 0.5845。
分词数 36；未知词比例 2.78%；特征：商业与科技边界。

Study: 400K Fewer Tech Jobs Since 2001 The US information tech sector lost 403,300 jobs between March 2001 and this past April, and the market for tech workers remains bleak, according to a new report.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tech@27:1.0124 | tech@10:0.4507 | tech@3:0.4464。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 145. test:1774 | Sci/Tech → World

预测置信度 0.6272；真实类概率 0.0328；前两类概率差 0.2875。
分词数 24；未知词比例 0.00%；特征：需结合语义人工复核。

Slowing population 'lacks funds' Rich countries are giving only half the amount they promised to help to slow world population growth, the UN says.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：un@22:1.9553 | funds@3:1.6641 | says@23:1.3582。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 146. test:1781 | Sci/Tech → World

预测置信度 0.9962；真实类概率 0.0020；前两类概率差 0.9942。
分词数 22；未知词比例 4.55%；特征：高置信错误>=0.9。

'Cities in crisis' leaders warn World leaders warn that rapid urbanisation will become one of the biggest challenges of the 21st Century.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：leaders@6:2.9729 | leaders@3:2.8710 | warn@4:1.2140。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 147. test:1790 | Business → Sci/Tech

预测置信度 0.9196；真实类概率 0.0803；前两类概率差 0.8393。
分词数 32；未知词比例 3.12%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

HP Wins Defense Contract HP (Quote, Chart) was awarded a \$290 million, 10-year outsourcing contract with the Defense Logistics Agency #39;s (DLA) Enterprise Data Center (EDC) program, officials announced Wednesday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：hp@4:0.9408 | announced@30:0.2077 | hp@0:0.1670。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 148. test:1791 | World → Sci/Tech

预测置信度 0.5746；真实类概率 0.1740；前两类概率差 0.3251。
分词数 40；未知词比例 0.00%；特征：需结合语义人工复核。

World Population to Rise to 8.9 Billion Although world families are getting smaller in many regions, the 50 poorest countries are expected to triple in size to 1.7 billion people by 2050, posing many challenges for world countries.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：size@26:1.0955 | although@8:1.0443 | world@9:0.6140。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 149. test:1798 | Sports → World

预测置信度 0.8712；真实类概率 0.0387；前两类概率差 0.8168。
分词数 44；未知词比例 2.27%；特征：需结合语义人工复核。

GM Plans to Use Woods More Creatively (AP) AP - General Motors Corp. is thrilled that Tiger Woods will promote Buick for the next five years, but GM chairman Rick Wagoner says the automaker could make better use of the world's best-known golfer.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：motors@10:1.9832 | corp@11:1.1893 | general@9:1.1209。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 150. test:1811 | Sci/Tech → Business

预测置信度 0.5072；真实类概率 0.4904；前两类概率差 0.0169。
分词数 33；未知词比例 3.03%；特征：商业与科技边界；前两类接近:概率差<0.2。

Midtier ERP Vendors Can Capitalize On Oracle Antitrust Verdict The door is open for Oracle to win its bid for PeopleSoft, and for midmarket ERP vendors to increase their business. By Elena Malykhina.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：bid@18:0.7489 | antitrust@7:0.5462 | peoplesoft@20:0.4457。
能把预测改为真实类的单词遮挡数：23。仅表示局部敏感性，不代表已证明因果原因。

## 151. test:1823 | Business → Sci/Tech

预测置信度 0.9837；真实类概率 0.0154；前两类概率差 0.9683。
分词数 37；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Infineon to Pay a Fine in the Fixing Of Chip Prices Federal prosecutors announced on Wednesday that they had cracked a global cartel that had illegally fixed prices of memory chips in personal computers and servers for 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：memory@29:1.7042 | illegally@25:1.6838 | chips@30:1.0768。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 152. test:1835 | World → Sci/Tech

预测置信度 0.5492；真实类概率 0.4422；前两类概率差 0.1070。
分词数 46；未知词比例 2.17%；特征：前两类接近:概率差<0.2。

Mexico Migrant Smugglers Turning to Sea (AP) AP - Migrant smugglers are skirting heightened security along the border by using small boats to shuttle people from the under-supervised Baja coast into Southern California marinas and harbors, already jammed with legal commercial ships and pleasure boat traffic.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：commercial@40:0.9059 | ships@41:0.7300 | using@18:0.2619。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 153. test:1840 | Sports → Business

预测置信度 0.6549；真实类概率 0.1112；前两类概率差 0.5058。
分词数 19；未知词比例 0.00%；特征：短文本<=20词。

Icing call Out of money, out of patience, out of time, and for the foreseeable future, out of business.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：money@4:0.6041 | business@18:0.5028 | patience@7:0.2207。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 154. test:1842 | Business → World

预测置信度 0.5097；真实类概率 0.4773；前两类概率差 0.0324。
分词数 42；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

Senate panel opposes overtime rules  A Senate committee voted yesterday to scuttle new rules that critics say would deny overtime pay to millions of workers, as Democrats won the latest round in their election-year bout with President Bush over the issue.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：democrats@26:0.6796 | president@37:0.3488 | say@16:0.2936。
能把预测改为真实类的单词遮挡数：11。仅表示局部敏感性，不代表已证明因果原因。

## 155. test:1845 | Business → Sci/Tech

预测置信度 0.6753；真实类概率 0.3235；前两类概率差 0.3518。
分词数 30；未知词比例 0.00%；特征：商业与科技边界。

Infineon admits conspiracy in DRAM cartel GIANT MEMORY company Infineon will plead guilty to price fixing of DRAM chips and will pay \$160 million in fines to the US government.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：memory@7:0.7400 | chips@18:0.2789 | dram@17:0.0696。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 156. test:1870 | Business → World

预测置信度 0.4983；真实类概率 0.3386；前两类概率差 0.1597。
分词数 20；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2；短文本<=20词。

Keep It in the Family The IRS is gunning for your inherited IRA. Follow these steps to avoid costly penalties.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ira@12:2.3275 | these@14:1.7219 | follow@13:0.5281。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 157. test:1893 | Sci/Tech → Business

预测置信度 0.8666；真实类概率 0.1319；前两类概率差 0.7346。
分词数 51；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Texas Instruments Plans Buyback (Reuters) Reuters - Texas Instruments Inc., the\largest maker of chips for cellular phones, on Thursday said it\plans to buy back  #36;1 billion in stock and boost its quarterly\dividend by more than 17 percent, becoming the latest\technology company to return extra cash to investors.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：dividend@34:1.3230 | quarterly@33:1.1058 | company@44:0.6195。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 158. test:1961 | Business → Sci/Tech

预测置信度 0.7211；真实类概率 0.1253；前两类概率差 0.5958。
分词数 26；未知词比例 0.00%；特征：商业与科技边界。

Boxer Begs Bush to Back Bum Bill Members of California's congressional team make one last effort to look good for the tech industry back home.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tech@22:1.1551 | begs@1:0.2884 | bush@2:0.1240。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 159. test:1974 | Business → Sports

预测置信度 0.6971；真实类概率 0.1025；前两类概率差 0.5405。
分词数 33；未知词比例 0.00%；特征：需结合语义人工复核。

Pen can pick some bike U-locks That U-shaped bike lock that you thought was so secure may be easy pickings for thieves who have nothing more sophisticated than a Bic pen.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：easy@20:1.7176 | pickings@21:0.7668 | be@19:0.7060。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 160. test:1976 | World → Sports

预测置信度 0.7854；真实类概率 0.1928；前两类概率差 0.5927。
分词数 15；未知词比例 6.67%；特征：短文本<=20词。

Show lights up Paralympics The XII Paralympics begins in Athens, after a spectacular opening ceremony.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：athens@9:1.1858 | after@10:0.5928 | opening@13:0.3421。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 161. test:2017 | Business → World

预测置信度 0.4393；真实类概率 0.3161；前两类概率差 0.1232。
分词数 32；未知词比例 3.12%；特征：世界与商业边界；前两类接近:概率差<0.2。

Florida, Alabama pick up the pieces after Ivan People in Florida and Alabama have started to clean up after hurricane Ivan - the third such pummelling for Florida alone in just five weeks.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ivan@7:0.4306 | people@8:0.4265 | pieces@5:0.2023。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 162. test:2028 | World → Sports

预测置信度 0.7354；真实类概率 0.2577；前两类概率差 0.4777。
分词数 28；未知词比例 0.00%；特征：需结合语义人工复核。

Ryder Cup: Europe close on victory Another good day at Oakland Hills sees Europe move 11-5 clear of the USA going into Sunday's Ryder Cup singles.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：hills@11:1.1943 | at@9:0.6620 | sunday@23:0.6575。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 163. test:2035 | Business → Sci/Tech

预测置信度 0.6775；真实类概率 0.3136；前两类概率差 0.3639。
分词数 49；未知词比例 2.04%；特征：商业与科技边界。

SAN FRANCISCO Mission District cyclist blew whistle on flawed lock The triumph last week of the Bic pen over expensive, state-of-the-art steel locks has panicked the bicycling community, and churned Internet rumor mills about how much the lock manufacturer knew and when the company knew it.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：mission@2:2.1843 | internet@33:2.1555 | francisco@1:1.2153。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 164. test:2036 | Sports → Business

预测置信度 0.3765；真实类概率 0.3345；前两类概率差 0.0420。
分词数 42；未知词比例 0.00%；特征：前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Pitchers finally getting job done? At least it #39;s a start This is a mirage or a sight to behold. This is something you can #39;t trust with your own eyes, or maybe what you #39;re watching is real.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：your@30:1.2939 | own@31:0.8730 | re@38:0.3560。
能把预测改为真实类的单词遮挡数：12。仅表示局部敏感性，不代表已证明因果原因。

## 165. test:2046 | Business → World

预测置信度 0.4328；真实类概率 0.2100；前两类概率差 0.2228。
分词数 33；未知词比例 3.03%；特征：世界与商业边界。

Malls setting curfews for unchaperoned teens COLUMBUS, Ohio -- It's 10 on a Friday night, and all 15-year-old Sylvia Fallon wants is to hang out with her friends at the mall.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：teens@5:1.4887 | columbus@6:0.9059 | old@19:0.2367。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 166. test:2053 | World → Business

预测置信度 0.9280；真实类概率 0.0617；前两类概率差 0.8663。
分词数 39；未知词比例 2.56%；特征：世界与商业边界；高置信错误>=0.9。

EU transport chief hails Alitalia accord (AFP) AFP - EU transport and energy commissioner Loyola de Palacio hailed the accord reached between Alitalia management and staff on a major restructuring plan aimed at keeping the struggling airline in the air.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：alitalia@21:2.5365 | management@22:1.9776 | between@20:0.7537。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 167. test:2062 | Business → Sci/Tech

预测置信度 0.9974；真实类概率 0.0025；前两类概率差 0.9949。
分词数 36；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

VoIP becomes new option Jackson is one of the first to take advantage of Time Warner Cable #39;s new venture into Voice over Internet Provider (VoIP) telephone service here and she says it works great.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：voip@26:1.4339 | telephone@27:0.9608 | provider@25:0.6466。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 168. test:2088 | World → Sci/Tech

预测置信度 0.6393；真实类概率 0.2964；前两类概率差 0.3429。
分词数 25；未知词比例 4.00%；特征：需结合语义人工复核。

Bush video awarded Turner Prize Artist Jeremy Deller wins this year's Turner Prize for a film about US President George Bush's home town.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：video@1:2.1655 | awarded@2:0.5607 | turner@3:0.5384。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 169. test:2094 | Sci/Tech → World

预测置信度 0.6786；真实类概率 0.3208；前两类概率差 0.3578。
分词数 25；未知词比例 4.00%；特征：需结合语义人工复核。

The battle for DR Congo's wildlife As donors pledge \$40m to save DR Congo's wildlife, life in Virunga Park remains a battle ground.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：congo@4:0.6986 | donors@8:0.6208 | 40m@10:0.3313。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 170. test:2101 | Sci/Tech → Business

预测置信度 0.4106；真实类概率 0.2605；前两类概率差 0.0948。
分词数 59；未知词比例 1.69%；特征：商业与科技边界；前两类接近:概率差<0.2。

'Cure' a 4-Letter Word for Cancer Doctors At a time when more people are cured of cancer than ever before, fewer doctors seem willing to say so. They call the cancer undetectable, or in remission. They tell patients they can quit seeing cancer specialists. They quote statistics and say chances are slim that the disease will come back.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：statistics@47:2.5777 | quote@46:1.7756 | specialists@44:0.4860。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 171. test:2105 | World → Business

预测置信度 0.7778；真实类概率 0.0319；前两类概率差 0.5911。
分词数 49；未知词比例 2.04%；特征：世界与商业边界；含HTML实体或编码痕迹。

Malaysia expects to resume poultry exports to Singapore soon By Channel NewsAsia #39;s Malaysia Correspondent Melissa Goh. KUALA LUMPUR : Malaysia expects to resume export of poultry and eggs from two states to Singapore by the end of this month but only after meeting conditions set by the island.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@12:2.8117 | exports@5:1.2404 | channel@10:0.7366。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 172. test:2115 | Sci/Tech → Business

预测置信度 0.5894；真实类概率 0.3721；前两类概率差 0.2172。
分词数 31；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Viruses keep on growing Most IT Managers won #39;t question the importance of security, but this priority has been sliding between the third and fourth most important focus for companies.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@8:0.6913 | most@4:0.6631 | managers@6:0.5958。
能把预测改为真实类的单词遮挡数：5。仅表示局部敏感性，不代表已证明因果原因。

## 173. test:2120 | Business → Sci/Tech

预测置信度 0.9640；真实类概率 0.0358；前两类概率差 0.9282。
分词数 29；未知词比例 3.45%；特征：商业与科技边界；高置信错误>=0.9。

Rogers Wireless Whistles and Fido Responds Its official. Microcell Telecommunications Fido wireless service will be the new dog in Rogers Wireless Communications Canadian kennel, and that puppy wasnt cheap.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：communications@21:1.1206 | telecommunications@9:0.6837 | wireless@20:0.4522。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 174. test:2122 | Sci/Tech → Business

预测置信度 0.9741；真实类概率 0.0218；前两类概率差 0.9524。
分词数 19；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；短文本<=20词。

Hyperion targets broader base New Essbase 7X is intended to draw customers beyond Hyperion's usual corporate-finance crowd.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：finance@17:3.0589 | corporate@16:2.3059 | usual@15:0.7417。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 175. test:2124 | Business → Sci/Tech

预测置信度 0.8392；真实类概率 0.1607；前两类概率差 0.6785。
分词数 31；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

AOL pushes into Internet shopping Looking for new ways to boost its revenue, America Online is launching an online shopping service that won #39;t require an AOL account to access.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：internet@3:0.5322 | online@18:0.4750 | pushes@1:0.0985。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 176. test:2126 | Sci/Tech → World

预测置信度 0.9689；真实类概率 0.0244；前两类概率差 0.9445。
分词数 42；未知词比例 0.00%；特征：高置信错误>=0.9。

Bush Scraps Most U.S. Sanctions on Libya (Reuters) Reuters - President Bush on Monday formally\ended the U.S. trade embargo on Libya to reward it for giving\up weapons of mass destruction but left in place U.S.\terrorism-related sanctions.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：terrorism@39:1.3622 | president@10:1.2508 | bush@11:0.8244。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 177. test:2145 | Sci/Tech → Business

预测置信度 0.5908；真实类概率 0.4087；前两类概率差 0.1821。
分词数 39；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

A  #39;Plan B #39; for PeopleSoft customers com September 20, 2004, 6:13 PM PT. This fourth priority #39;s main focus has been improving or obtaining CRM and ERP software for the past year and a half.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@19:1.3444 | s@20:0.9872 | september@9:0.8916。
能把预测改为真实类的单词遮挡数：12。仅表示局部敏感性，不代表已证明因果原因。

## 178. test:2168 | Business → Sci/Tech

预测置信度 0.6093；真实类概率 0.3874；前两类概率差 0.2219。
分词数 46；未知词比例 2.17%；特征：商业与科技边界。

Clouds darken PeopleSoft conference SAN FRANCISCO -- PeopleSoft Inc. is trying to create a party-like atmosphere at its annual customer conference, but this week's gathering may feel more like a wake with rival Oracle Corp.'s \$7.7 billion takeover bid looming larger than ever.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：peoplesoft@6:0.5374 | inc@7:0.1623 | francisco@5:0.1495。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 179. test:2169 | Business → Sci/Tech

预测置信度 0.9978；真实类概率 0.0016；前两类概率差 0.9962。
分词数 50；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Ask Jeeves retools search engine in bid to catch Google, Yahoo SAN FRANCISCO -- Hoping to emerge from the shadow of its more popular rivals, Ask Jeeves Inc. is adding new tools for visitors to save and organize links to Web pages they find through the company's online search engine.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：s@46:0.8328 | yahoo@10:0.6031 | jeeves@25:0.4565。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 180. test:2173 | World → Sports

预测置信度 0.8147；真实类概率 0.0382；前两类概率差 0.6720。
分词数 22；未知词比例 0.00%；特征：需结合语义人工复核。

India seeks new TV bids The Indian Board re-opens the bidding for TV rights after Australian threaten to cancel their tour.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：board@7:1.7386 | tour@21:0.9813 | re@8:0.8712。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 181. test:2191 | Sci/Tech → World

预测置信度 0.7478；真实类概率 0.2442；前两类概率差 0.5036。
分词数 41；未知词比例 0.00%；特征：需结合语义人工复核。

Noah's Ark Quest Dead in Water -- Was It a Stunt? In April a Christian activist announced a summer 2004 expedition to search for Noah's ark. The quest didn't happen, and now critics are questioning the project's credibility.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：dead@4:0.8934 | christian@14:0.6251 | for@23:0.5179。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 182. test:2198 | Business → World

预测置信度 0.5484；真实类概率 0.3671；前两类概率差 0.1813。
分词数 28；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

Jury calls WTC attack two events Silverstein had hoped the 11-member jury would determine that the language of the insurance policy treated the attacks as two occurrences.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：events@5:0.5864 | attack@3:0.4830 | two@4:0.4622。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 183. test:2207 | Business → Sci/Tech

预测置信度 0.7844；真实类概率 0.2156；前两类概率差 0.5688。
分词数 35；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

PeopleSoft CEO Conway maintains defiant tone SEPTEMBER 21, 2004 (IDG NEWS SERVICE) - With 15,000 attendees at PeopleSoft Inc. #39;s Connect 2004 user show waiting to hear how the company would handle Oracle Corp.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：show@24:0.3598 | ceo@1:0.3130 | peoplesoft@0:0.2680。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 184. test:2219 | World → Sci/Tech

预测置信度 0.9828；真实类概率 0.0171；前两类概率差 0.9657。
分词数 43；未知词比例 0.00%；特征：高置信错误>=0.9；含HTML实体或编码痕迹。

Senate Panel Gives NASA Extra Money (AP) AP - NASA would get  #36;16.4 billion next year under a bill a Senate committee approved Tuesday, reversing a decision by House lawmakers to cut the space agency's budget below this year's levels.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：nasa@3:1.1838 | budget@37:0.9792 | nasa@8:0.9428。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 185. test:2233 | Business → Sci/Tech

预测置信度 0.6312；真实类概率 0.3379；前两类概率差 0.2933。
分词数 22；未知词比例 4.55%；特征：商业与科技边界。

Guilty Plea Seen in Computer Associates Case Steven Woghin, the former general counsel of Computer Associates, will plead guilty to criminal charges.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：computer@4:0.1938 | will@16:0.0510 | criminal@20:0.0110。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 186. test:2234 | Business → World

预测置信度 0.5404；真实类概率 0.0242；前两类概率差 0.1050。
分词数 35；未知词比例 8.57%；特征：世界与商业边界；前两类接近:概率差<0.2。

Spread of GM grass raises fears of crossbreeding Pollen from a genetically modified grass was found 21 kilometres from where it was planted, scientists reported in a study published Tuesday, raising fears of transgenic crossbreeding.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：scientists@23:3.1739 | reported@24:1.2160 | raises@4:0.4067。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 187. test:2247 | World → Business

预测置信度 0.6736；真实类概率 0.2566；前两类概率差 0.4170。
分词数 52；未知词比例 0.00%；特征：世界与商业边界。

Asia to outperform this year, lower growth seen in 2005: ADB (AFP) AFP - Developing Asia is set to outperform this year with higher-than-expected growth of 7.0 percent despite high oil prices but it will slow in 2005 in tandem with the developed world, the Asian Development Bank (ADB) said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：2005@9:0.7748 | growth@6:0.6856 | bank@49:0.6518。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 188. test:2253 | Business → Sci/Tech

预测置信度 0.5833；真实类概率 0.4001；前两类概率差 0.1832。
分词数 28；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

Vodafone targets Japan with 3G offensive Vodafone has unveiled plans for 10 new third-generation handsets for Christmas to help shore up its struggling Japanese unit. Vodafone VOD.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：handsets@15:0.7037 | generation@14:0.6285 | unveiled@8:0.5759。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 189. test:2267 | Sports → Sci/Tech

预测置信度 0.5224；真实类概率 0.3532；前两类概率差 0.1692。
分词数 35；未知词比例 0.00%；特征：前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Olympic traffic measures needed at Paralympics: experts Experts recommend that the traffic control measures taken during last month #39;s Olympic Summer Games and the current Paralympics should be kept in Athens permanently, as they 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：experts@7:4.6714 | experts@6:4.3566 | paralympics@5:0.7622。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 190. test:2296 | Business → Sci/Tech

预测置信度 0.7925；真实类概率 0.2032；前两类概率差 0.5893。
分词数 40；未知词比例 0.00%；特征：商业与科技边界。

PeopleSofts big bash See you next year in Las Vegas , proclaimed a marquee at the PeopleSoft user conference in San Francisco in late September. It was one of many not-so-subtle attempts by the company to reassure its customers 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：user@16:0.9953 | peoplesoft@15:0.5143 | subtle@31:0.0549。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 191. test:2306 | World → Business

预测置信度 0.9238；真实类概率 0.0757；前两类概率差 0.8481。
分词数 32；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

Deal in Congress to Keep Tax Cuts, Widening Deficit Republican and Democratic leaders agreed to extend \$150 billion worth of tax cuts sought by President Bush without trying to pay for them.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tax@20:0.5564 | tax@5:0.5399 | billion@17:0.4986。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 192. test:2333 | Business → Sci/Tech

预测置信度 0.9801；真实类概率 0.0185；前两类概率差 0.9615。
分词数 18；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；短文本<=20词。

Rumours surround Google browser The search giant Google is rumoured to be working on its own web browser.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：browser@17:0.7622 | web@16:0.7594 | browser@3:0.7071。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 193. test:2343 | Business → Sci/Tech

预测置信度 0.7850；真实类概率 0.2131；前两类概率差 0.5720。
分词数 20；未知词比例 5.00%；特征：商业与科技边界；短文本<=20词。

PeopleSoft Plays Defense The business software maker inks a deal with IBM, but it isn't likely to dissuade Oracle.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：t@15:0.4341 | software@5:0.2365 | it@13:0.2120。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 194. test:2355 | Sci/Tech → Sports

预测置信度 0.6188；真实类概率 0.1924；前两类概率差 0.4264。
分词数 33；未知词比例 3.03%；特征：需结合语义人工复核。

Dinosaur May Have Been Stealth Hunter (AP) AP - The strike would have come out of nowhere: One second the fish was swimming placidly, no danger in sight, a moment later it was lunch.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ap@7:1.3308 | ap@6:1.0032 | the@18:0.6430。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 195. test:2357 | Sports → World

预测置信度 0.6619；真实类概率 0.3138；前两类概率差 0.3481。
分词数 36；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

Mass. court denies new trial for convict BOSTON -- The state appeals court on Thursday declined to allow a new trial for a father convicted of beating a man to death at their sons #39; hockey practice.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：mass@0:1.7588 | denies@2:1.6686 | court@1:1.5313。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 196. test:2397 | Sci/Tech → World

预测置信度 0.5236；真实类概率 0.4182；前两类概率差 0.1053。
分词数 38；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Islands press Govt to reverse phone call decision Diplomats from a number of islands in the South Pacific are reported to be pressing the Government to reverse a decision to block all phone calls made to the islands.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：decision@7:0.6438 | press@1:0.6377 | diplomats@8:0.6147。
能把预测改为真实类的单词遮挡数：6。仅表示局部敏感性，不代表已证明因果原因。

## 197. test:2400 | World → Sci/Tech

预测置信度 0.6878；真实类概率 0.2702；前两类概率差 0.4176。
分词数 46；未知词比例 0.00%；特征：需结合语义人工复核。

Dogs said to smell cancer signs  LONDON -- It has long been suspected that man's best friend has a special ability to sense when something is wrong with us. Now, the first experiment to verify that scientifically has demonstrated that dogs are able to smell cancer.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：able@42:0.4483 | something@24:0.2564 | smell@44:0.1706。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 198. test:2417 | Sci/Tech → World

预测置信度 0.5063；真实类概率 0.4674；前两类概率差 0.0389。
分词数 19；未知词比例 5.26%；特征：前两类接近:概率差<0.2；短文本<=20词。

Baby for ovary transplant woman A Belgian cancer patient made infertile by chemotherapy has given birth following revolutionary treatment.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：for@1:0.4906 | belgian@6:0.3455 | revolutionary@17:0.3451。
能把预测改为真实类的单词遮挡数：11。仅表示局部敏感性，不代表已证明因果原因。

## 199. test:2422 | Sci/Tech → World

预测置信度 0.6138；真实类概率 0.3837；前两类概率差 0.2300。
分词数 18；未知词比例 0.00%；特征：短文本<=20词。

Group Questions E-Voting Security Black Box Voting hopes to halt the use of Diebold's voting machines.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：box@6:2.6165 | voting@7:1.8134 | hopes@8:1.6677。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 200. test:2427 | Business → World

预测置信度 0.7911；真实类概率 0.1833；前两类概率差 0.6078。
分词数 38；未知词比例 2.63%；特征：世界与商业边界。

Strikes at London airports London - A 48-hour strike by aircraft refuellers at London Heathrow airport got under way on Friday, with baggage handlers at Gatwick airport also preparing to walk out, threatening a weekend of travel disruptions.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：walk@30:1.5400 | threatening@32:1.0609 | heathrow@14:0.5251。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 201. test:2428 | Sci/Tech → World

预测置信度 0.5517；真实类概率 0.4400；前两类概率差 0.1118。
分词数 26；未知词比例 3.85%；特征：前两类接近:概率差<0.2。

Security firm justifies virus writer's job SecurePoint says the alleged Sasser author was "just an immature boy with mindless intent" who wants to make amends.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：author@12:0.9441 | was@13:0.8557 | alleged@10:0.8085。
能把预测改为真实类的单词遮挡数：8。仅表示局部敏感性，不代表已证明因果原因。

## 202. test:2435 | Sci/Tech → Business

预测置信度 0.7585；真实类概率 0.2375；前两类概率差 0.5210。
分词数 22；未知词比例 0.00%；特征：商业与科技边界。

Airbus drops out of Microsoft appeal Aircraft builder withdraws its request to intervene in Microsoft's antitrust appeal; Boeing also forgoes intervention.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：antitrust@16:1.3099 | boeing@18:1.2923 | appeal@17:1.0257。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 203. test:2438 | Sci/Tech → World

预测置信度 0.8268；真实类概率 0.1615；前两类概率差 0.6653。
分词数 37；未知词比例 10.81%；特征：未知词比例>=10%。

Mom Hugs 'Miracle' Baby After Ovarian Transplant (Reuters) Reuters - Ouarda Touirat, her day-old baby\daughter nestling in her arms, said Friday she had never lost\hope that she could conceive after cancer treatment left her\infertile.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：friday@21:1.5859 | arms@19:1.4853 | her@18:0.9355。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 204. test:2442 | Sports → World

预测置信度 0.6965；真实类概率 0.0766；前两类概率差 0.5195。
分词数 50；未知词比例 0.00%；特征：需结合语义人工复核。

Calvin Murphy removed as Rockets broadcaster Murphy will go to trial Nov. 4 on charges he molested his daughters, a state district judge said Tuesday. Murphy is charged with three counts of indecency with a child and three counts of aggravated sexual assault, punishable by up to life in prison.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：judge@22:0.9999 | district@21:0.5263 | tuesday@24:0.4662。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 205. test:2446 | Sci/Tech → World

预测置信度 0.5485；真实类概率 0.4426；前两类概率差 0.1059。
分词数 37；未知词比例 5.41%；特征：前两类接近:概率差<0.2。

Locusts Encroach on West African Rice-Growing Area (Reuters) Reuters - West Africa's worst locust plague for 15\years has encroached on one of the region's largest\rice-growing areas, authorities in Mali said on Friday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：african@4:0.9973 | rice@5:0.4921 | s@12:0.4453。
能把预测改为真实类的单词遮挡数：8。仅表示局部敏感性，不代表已证明因果原因。

## 206. test:2448 | Business → World

预测置信度 0.6375；真实类概率 0.3147；前两类概率差 0.3228。
分词数 38；未知词比例 0.00%；特征：世界与商业边界；含HTML实体或编码痕迹。

Rivals Ocean Spray, Northland make peace Cranberry juice rivals Ocean Spray and Northland have ended their legal battle and agreed to join forces. The companies said Friday that Ocean Spray will take over its smaller rival #39;s 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：peace@5:1.7437 | ocean@9:0.4606 | rivals@8:0.3692。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 207. test:2449 | World → Sci/Tech

预测置信度 0.3952；真实类概率 0.2133；前两类概率差 0.0038。
分词数 71；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Calif. OKs World's Toughest Smog Rules LOS ANGELES - California air regulators Friday unanimously approved the world's most stringent rules to reduce auto emissions that contribute to global warming - a move that could affect car and truck buyers from coast to coast.    Under the regulations, the auto industry must cut exhaust from cars and light trucks by 25 percent and from larger trucks and sport utility vehicles by 18 percent...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：warming@29:0.9196 | auto@47:0.6031 | industry@48:0.5063。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 208. test:2451 | Business → Sci/Tech

预测置信度 0.7507；真实类概率 0.2472；前两类概率差 0.5034。
分词数 47；未知词比例 0.00%；特征：商业与科技边界。

CA, Partners Move On As Kumar Faces Charges Concern over the fate of former Computer Associates International chairman and CEO Sanjay Kumar accompanied the collective sigh of relief felt by CA partners last week when federal prosecutors settled a two-year-old accounting fraud investigation with the 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：computer@14:0.7999 | ca@30:0.4875 | faces@6:0.1934。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 209. test:2468 | World → Sports

预测置信度 0.8794；真实类概率 0.1098；前两类概率差 0.7697。
分词数 67；未知词比例 0.00%；特征：需结合语义人工复核。

Dodgers Nip Giants 3-2 in Crucial Series SAN FRANCISCO - Shawn Green can sit out Saturday knowing he was a huge help to the Dodgers during their crucial series against San Francisco. Green hit a two-run homer in Los Angeles' 3-2 victory over the Giants on Friday night, a day before the first baseman will miss a game to observe the Jewish holiday Yom Kippur...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：victory@43:0.4463 | series@28:0.3977 | green@32:0.3959。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 210. test:2491 | World → Sci/Tech

预测置信度 0.9554；真实类概率 0.0332；前两类概率差 0.9223。
分词数 69；未知词比例 0.00%；特征：高置信错误>=0.9。

Men, Women More Different Than Thought CHICAGO - Beyond the tired cliches and sperm-and-egg basics taught in grade school science class, researchers are discovering that men and women are even more different than anyone realized.    It turns out that major illnesses like heart disease and lung cancer are influenced by gender and that perhaps treatments for women ought to be slightly different from the approach used for men...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：science@20:1.6173 | school@19:0.8976 | discovering@24:0.2874。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 211. test:2496 | Sports → Business

预测置信度 0.5352；真实类概率 0.0871；前两类概率差 0.3444。
分词数 31；未知词比例 0.00%；特征：需结合语义人工复核。

Robby Gordon Planning to Proceed With Caution Robby Gordon plans to join the oil spills, the tire chunks, the sharp pieces of debris and the other typical racetrack hazards on Sunday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：oil@13:1.7389 | plans@9:0.9385 | join@11:0.5158。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 212. test:2502 | Sports → World

预测置信度 0.7824；真实类概率 0.1045；前两类概率差 0.6779。
分词数 41；未知词比例 2.44%；特征：需结合语义人工复核。

Cricket swings to Calypso once again From the time you touch down in the British Isles, you get an overwhelming sense of grey. The skies are almost always leaden, the clothes people wear are generally either black or neutral shades guaranteed 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：cricket@0:1.0520 | people@31:0.7322 | are@33:0.5027。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 213. test:2521 | Sci/Tech → World

预测置信度 0.9397；真实类概率 0.0602；前两类概率差 0.8795。
分词数 49；未知词比例 0.00%；特征：高置信错误>=0.9。

Soldiers' War Blogs Detail Life in Iraq Iraq war blogs are as varied as the soldiers who write them. Some sites feature practical news, war pictures and advice. Some are overtly political, with more slanting to the right than to the left. Some question the war, some cheer it.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：iraq@6:3.1703 | iraq@7:2.7651 | in@5:0.7085。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 214. test:2566 | Business → World

预测置信度 0.6748；真实类概率 0.1619；前两类概率差 0.5129。
分词数 47；未知词比例 0.00%；特征：世界与商业边界。

A wandering Congress trips over the US Constitution That is the one-word message of advice that citizens wanted to send to members of Congress at the end of last week. Both the House of Representatives and the Senate looked as if they are having trouble seizing 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：senate@38:0.9105 | representatives@35:0.8486 | as@40:0.2140。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 215. test:2574 | Business → Sci/Tech

预测置信度 0.8385；真实类概率 0.1614；前两类概率差 0.6771。
分词数 48；未知词比例 2.08%；特征：商业与科技边界；含HTML实体或编码痕迹。

Adobe updates RAW plug-in with digital negative format Adobe has updated Photoshop #39;s support for digital cameras #39; RAW image formats. The new plug-in adds to the number of camera models supported and includes a utility for converting images into the DNG, digital negative format.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：cameras@18:0.5225 | digital@17:0.3844 | camera@32:0.3190。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 216. test:2577 | Sci/Tech → Business

预测置信度 0.8321；真实类概率 0.1513；前两类概率差 0.6807。
分词数 25；未知词比例 0.00%；特征：商业与科技边界。

Plan B Proposes Its Own Alternatives Donnie Downs, president and chief executive of Plan B Technologies Inc., said the company itself is a "plan B."

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：executive@11:1.1112 | chief@10:0.8424 | said@17:0.7636。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 217. test:2579 | Sports → Business

预测置信度 0.7020；真实类概率 0.0141；前两类概率差 0.4235。
分词数 47；未知词比例 2.13%；特征：含HTML实体或编码痕迹。

SC to hear Zee petition tommorrow Five judges of the top court will hear a petition filed by Zee Telefilms on Tuesday. A three-judge panel of the Supreme Court said a five-judge bench would hear the dispute that threatens the rights of India #39;s 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：court@29:0.7656 | supreme@28:0.7577 | said@30:0.5616。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 218. test:2591 | World → Sports

预测置信度 0.9960；真实类概率 0.0039；前两类概率差 0.9921。
分词数 73；未知词比例 0.00%；特征：高置信错误>=0.9。

Sports Court Hears Hamm Gold Medal Appeal LAUSANNE, Switzerland - Paul Hamm appeared before the sports world's highest court Monday to argue why he should he keep his Olympic gymnastics gold medal.    The Court of Arbitration for Sport convened to hear the appeal from a South Korean gymnast who believes he was unfairly deprived of the gold in the men's all-around event in Athens last month because of a scoring error...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：sports@14:1.0757 | gymnastics@29:0.8930 | olympic@28:0.7009。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 219. test:2607 | World → Sci/Tech

预测置信度 0.8134；真实类概率 0.0991；前两类概率差 0.7143。
分词数 29；未知词比例 3.45%；特征：需结合语义人工复核。

Holiday Stamps to Be Issued in Oct. (AP) AP - Holiday postage stamps celebrating Christmas, Hanukkah and Kwanzaa will be issued next month, the U.S. Postal Service announced Monday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：service@26:0.5491 | announced@27:0.3265 | holiday@9:0.3243。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 220. test:2610 | Business → Sci/Tech

预测置信度 0.7657；真实类概率 0.2342；前两类概率差 0.5314。
分词数 41；未知词比例 2.44%；特征：商业与科技边界；含HTML实体或编码痕迹。

Dell, AOL team up in schools initiative ROUND ROCK, Texas -- Dell Inc. and America Online Inc. announced a partnership Monday to provide 5,000 low-income students with free refurbished personal computers and a year #39;s worth of Internet access.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：inc@15:0.4259 | round@7:0.4166 | dell@0:0.3449。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 221. test:2612 | Sci/Tech → World

预测置信度 0.5453；真实类概率 0.2567；前两类概率差 0.2886。
分词数 51；未知词比例 1.96%；特征：含HTML实体或编码痕迹。

Gold Indian Coin Expected to Fetch  #36;27,000 (Reuters) Reuters - An Indian gold coin which is nearly\1,900 years old and shows one of the earliest depictions of\Buddha is to be sold at auction where it is expected to fetch\up to 15,000 pounds ( #36;27,000).

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：gold@13:0.7718 | indian@12:0.7560 | 1@18:0.2807。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 222. test:2613 | World → Business

预测置信度 0.9919；真实类概率 0.0053；前两类概率差 0.9866。
分词数 27；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

Embattled Mortgage Giant Agrees to Meet New Standards Fannie Mae agreed to keep more cash on hand while it corrects accounting problems, a U.S. regulator said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：fannie@8:1.7857 | mae@9:1.1403 | regulator@25:0.5230。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 223. test:2656 | World → Sports

预测置信度 0.9998；真实类概率 0.0001；前两类概率差 0.9997。
分词数 24；未知词比例 0.00%；特征：高置信错误>=0.9。

Cowboys Defeat Redskins 21-18 LANDOVER, Md. - Bill Parcells celebrated the touchdown with a big smile and his fist thrust high in the air...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：redskins@2:4.2489 | 21@3:1.5227 | defeat@1:0.8779。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 224. test:2660 | Sci/Tech → Business

预测置信度 0.9033；真实类概率 0.0007；前两类概率差 0.8073。
分词数 37；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Gas prices up 5 cents after Hurricane Ivan CAMARILLO, Calif. - Gas prices jumped more than 5 cents a gallon in the past two weeks, largely because of supply problems related to Hurricane Ivan, an industry analyst said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：gas@10:1.3304 | prices@11:1.1992 | jumped@12:1.0688。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 225. test:2670 | World → Business

预测置信度 0.9580；真实类概率 0.0409；前两类概率差 0.9171。
分词数 46；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Nigerian oil flows despite rebel threat-companies Oil should continue to flow from Nigeria, the world #39;s seventh largest exporter, despite a rebel threat to attack foreign oil workers in an  quot;all-out war quot; due to start on Friday, multinational energy companies said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@16:1.6446 | companies@44:1.3490 | energy@43:1.3416。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 226. test:2694 | Sci/Tech → Business

预测置信度 0.7462；真实类概率 0.2314；前两类概率差 0.5148。
分词数 38；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Virgin Starts (70) Mile-High Club With the misery that has plagued the airline industry recently, the last place you #39;d expect to see some inspiring -- heck, potentially rule-breaking -- thinking would be from an airline entrepreneur.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：airline@13:1.1795 | industry@14:0.9044 | 39@20:0.8597。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 227. test:2710 | Sci/Tech → Business

预测置信度 0.6854；真实类概率 0.3121；前两类概率差 0.3734。
分词数 50；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Cendant Near Deal to Buy Orbitz for  #36;1.2 Bln-Source (Reuters) Reuters - Travel and real estate company\Cendant Corp.  is close to an agreement to buy online\travel site Orbitz Inc.  for about  #36;1.2 billion in\cash, a source close to the talks said on Tuesday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：1@8:1.0866 | 2@9:0.9057 | bln@10:0.8057。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 228. test:2718 | Business → Sci/Tech

预测置信度 0.9646；真实类概率 0.0353；前两类概率差 0.9294。
分词数 42；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Amazon sues spammers for misleading consumers SEATTLE -- Amazon.com has filed three lawsuits in King County Superior Court against unidentified defendants who allegedly forged e-mails and Web sites to fool consumers into thinking they are doing business with the Internet retailer.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：spammers@2:1.5740 | web@27:0.7455 | sues@1:0.6564。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 229. test:2738 | World → Sports

预测置信度 0.6136；真实类概率 0.3681；前两类概率差 0.2455。
分词数 68；未知词比例 0.00%；特征：需结合语义人工复核。

Official: MLB to Move Expos to Washington WASHINGTON - Major League Baseball will announce Wednesday that Washington will be the new home of the Montreal Expos, bringing the national pastime back to the nation's capital for the first time in 33 years, The Associated Press has learned.    A city official, speaking on condition of anonymity, said Washington has been notified by Major League Baseball of the impending announcement...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：expos@24:1.3797 | montreal@23:1.0253 | will@11:0.7007。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 230. test:2750 | Business → Sci/Tech

预测置信度 0.6903；真实类概率 0.2050；前两类概率差 0.4853。
分词数 34；未知词比例 5.88%；特征：商业与科技边界。

New \$50 bill designed to counter counterfeits WASHINGTON - The green is still there, but with touches of blue, red and yellow. A stylized image of the Stars and Stripes now waves in the background.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：waves@30:0.7413 | now@29:0.2101 | stars@26:0.1125。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 231. test:2752 | Business → Sci/Tech

预测置信度 0.9738；真实类概率 0.0261；前两类概率差 0.9478。
分词数 31；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

BlueGene sneaks past Earth Simulator The Earth Simulator, an NEC supercomputer, is surpassed, at last. IBM announced yesterday that its Blue Gene/L supercomputer had achieved a sustained performance of 36.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：supercomputer@10:1.2320 | nec@9:1.1656 | earth@6:0.2905。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 232. test:2758 | World → Sports

预测置信度 0.5577；真实类概率 0.4410；前两类概率差 0.1167。
分词数 22；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Cricket: Dubai global academy The International Cricket Council are to open a global cricket academy designed to improve standards of lesser nations.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：cricket@6:1.5291 | the@4:1.3528 | international@5:1.0679。
能把预测改为真实类的单词遮挡数：5。仅表示局部敏感性，不代表已证明因果原因。

## 233. test:2778 | Sci/Tech → Business

预测置信度 0.6564；真实类概率 0.3430；前两类概率差 0.3134。
分词数 31；未知词比例 0.00%；特征：商业与科技边界。

Travelzoo Shares Rise as Offering Rumor Fades (Reuters) Reuters - Shares of Internet travel site\Travelzoo Inc.  rose nearly 4 percent on Wednesday as\market rumors of a secondary stock offering faded.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：rose@16:1.0980 | shares@9:0.7736 | inc@15:0.6346。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 234. test:2805 | Sci/Tech → Business

预测置信度 0.8384；真实类概率 0.1256；前两类概率差 0.7128。
分词数 38；未知词比例 0.00%；特征：商业与科技边界。

I.B.M. Agrees to Settle Part of Giant Pension Case I.B.M. said that it had agreed to pay \$320 million to its employees to settle in part a class-action lawsuit over its pension plan.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：giant@8:0.8914 | pension@9:0.5545 | pay@20:0.3882。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 235. test:2806 | Sci/Tech → Business

预测置信度 0.8533；真实类概率 0.0968；前两类概率差 0.7565。
分词数 55；未知词比例 0.00%；特征：商业与科技边界。

Immunity in Ebbers Case Opposed in U.S. Filing NEW YORK, Sept. 29 -- Federal prosecutors told a judge in a filing late Tuesday night that they have evidence that former WorldCom Inc. chief executive Bernard J. Ebbers knew company officials had improperly tinkered with the telecommunications firm's accounting to boost its publicly reported profits.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：york@10:0.8277 | profits@54:0.7874 | federal@13:0.5183。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 236. test:2822 | World → Business

预测置信度 0.9406；真实类概率 0.0242；前两类概率差 0.9063。
分词数 43；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Poor? Who #39;s poor? Poverty is down The proportion of people living on less than \$1 a day decreased from 40 to 21 per cent of the global population between 1981 and 2001, says the World Bank #39;s latest annual report.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：bank@37:1.9843 | 39@38:1.8297 | world@36:0.9520。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 237. test:2828 | Business → Sci/Tech

预测置信度 0.9230；真实类概率 0.0766；前两类概率差 0.8464。
分词数 32；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

IBM Claims Its BlueGene Supercomputer Is the Fastest IBM Corp. on Wednesday said it has developed the world #39;s fastest computer - a 16,000-processor version of its BlueGene/L supercomputer.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：version@26:1.3616 | processor@25:0.5992 | l@30:0.2147。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 238. test:2833 | Sci/Tech → World

预测置信度 0.8502；真实类概率 0.1220；前两类概率差 0.7282。
分词数 39；未知词比例 7.69%；特征：需结合语义人工复核。

Man arrested for fatally stabbing elderly parents SAITAMA -- A middle-aged man who fatally stabbed his parents has been arrested, police said. Hideo Nakajima, an unemployed man from Soka, Saitama Prefecture, apparently called police shortly before 8 pm, Wednesday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：his@15:1.0919 | stabbed@14:0.7420 | man@11:0.5560。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 239. test:2847 | World → Business

预测置信度 0.6959；真实类概率 0.2897；前两类概率差 0.4062。
分词数 52；未知词比例 0.00%；特征：世界与商业边界。

Tough Talks Ahead After EU Is Criticized Efforts to forge the world's largest free trade zone between the European Union and South America's Mercosur economic bloc are unlikely to be concluded by an Oct. 31 deadline, the EU said Thursday, with both sides declaring each other's trade offers insufficient.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：economic@26:1.4693 | trade@49:0.6669 | mercosur@25:0.5228。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 240. test:2848 | Sci/Tech → Business

预测置信度 0.9448；真实类概率 0.0531；前两类概率差 0.8916。
分词数 30；未知词比例 3.33%；特征：商业与科技边界；高置信错误>=0.9。

Pharma Groups Work on EPC Issues Sept. 30, 2004Reacting to calls from pharmaceutical retailers, distributors and manufacturers, EPCglobal has added a new action group to specifically study the pharmaceutical industry 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：retailers@13:3.1998 | pharmaceutical@12:1.0248 | distributors@14:0.9525。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 241. test:2850 | Sci/Tech → Business

预测置信度 0.6290；真实类概率 0.3693；前两类概率差 0.2597。
分词数 34；未知词比例 0.00%；特征：商业与科技边界。

Net firms: Don't tax VoIP The Spanish-American War is over and a "temporary" tax created to pay for it should not be extended to Internet phone calls, industry groups tell the IRS

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tax@15:1.9695 | temporary@14:1.1385 | tax@4:0.8268。
能把预测改为真实类的单词遮挡数：5。仅表示局部敏感性，不代表已证明因果原因。

## 242. test:2856 | Sci/Tech → Business

预测置信度 0.7657；真实类概率 0.2303；前两类概率差 0.5355。
分词数 42；未知词比例 0.00%；特征：商业与科技边界。

August Chip Sales Growth Slows on High Inventory  SAN FRANCISCO (Reuters) - Global semiconductor sales growth  slowed to 1 percent in August as electronics makers reacted to  growing inventories in Asia by limiting orders of chips, an  industry trade group said on Thursday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：francisco@9:0.8184 | on@5:0.6224 | high@6:0.6112。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 243. test:2857 | Business → Sci/Tech

预测置信度 0.8097；真实类概率 0.0831；前两类概率差 0.7266。
分词数 21；未知词比例 4.76%；特征：商业与科技边界。

Hasbro's No Conehead Its Saturday Night Live version of "Trivial Pursuit" is good strategy for staying ahead of age compression.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：version@8:1.7992 | live@7:0.5961 | trivial@10:0.1755。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 244. test:2868 | Sci/Tech → Business

预测置信度 0.6467；真实类概率 0.3533；前两类概率差 0.2934。
分词数 43；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

EBay Expands PayPal Buyer Protection Up to \$1,000 PayPal, eBay Inc. #39;s (EBAY.O: Quote, Profile, Research) online payment service, will expand its US buyer protection program to cover up to \$1,000 for qualified transactions, the company said on Thursday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@12:1.6727 | quote@16:1.3292 | research@18:0.7868。
能把预测改为真实类的单词遮挡数：6。仅表示局部敏感性，不代表已证明因果原因。

## 245. test:2879 | Sci/Tech → Business

预测置信度 0.8946；真实类概率 0.1053；前两类概率差 0.7893。
分词数 64；未知词比例 3.12%；特征：商业与科技边界。

Opportunity Rings (Forbes.com) Forbes.com - This past summer 25,000 consumers, aged 18 to 24, received short text messages on their cell phones alerting them to numbers on 225 million bottle caps of Snapple iced tea, pink lemonade and the like. People holding a winning number, announced by text message and traditional media, landed overseas trips and walk-on parts on TV shows.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：forbes@4:2.6282 | forbes@2:2.4767 | rings@1:0.6783。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 246. test:2887 | Sports → World

预测置信度 0.9337；真实类概率 0.0625；前两类概率差 0.8712。
分词数 32；未知词比例 6.25%；特征：高置信错误>=0.9。

Singer: Minaya returns home NEW YORK -- Omar Minaya stood behind a small lectern in a danky room in the bowels of Shea Stadium, and allowed his life to flash before his eyes.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：singer@0:2.9029 | york@5:2.4643 | home@3:1.2374。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 247. test:2913 | Sci/Tech → Sports

预测置信度 0.5990；真实类概率 0.2572；前两类概率差 0.3418。
分词数 19；未知词比例 0.00%；特征：短文本<=20词。

Dare you fight the possessed tomatoes? Quirky, stick-figure "Kingdom of Loathing" shows continued promise of independent game-writing.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：figure@8:0.8474 | continued@13:0.6420 | the@3:0.5221。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 248. test:2919 | Sci/Tech → Business

预测置信度 0.9542；真实类概率 0.0223；前两类概率差 0.9307。
分词数 49；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

EU Accuses Microsoft of Paternal View Microsoft Corp. said Friday that small companies and their customers would suffer most if it is forced to remove its digital media software from Windows, while the European Union accused it of being "paternalistic" in trying to decide what's best for everyone.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：union@34:1.6923 | accused@35:1.3824 | corp@7:0.9659。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 249. test:2932 | Business → Sci/Tech

预测置信度 0.7065；真实类概率 0.2343；前两类概率差 0.4722。
分词数 38；未知词比例 5.26%；特征：商业与科技边界。

Siemens in 2.69bn deal with BBC German industrial giant Siemens has signed a 2.69bn contract to deliver technology services around the world to the BBC, a deal that will see it acquire the broadcasters technology subsidiary.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：technology@36:0.6771 | subsidiary@37:0.4809 | siemens@10:0.4682。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 250. test:2952 | Business → Sci/Tech

预测置信度 0.4466；真实类概率 0.4236；前两类概率差 0.0230。
分词数 22；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

Fortune's 100 Most Doomed? Your company made it to Fortune's 100 Fastest Growing Companies list. Is that a good thing?

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：fastest@13:0.6107 | list@16:0.2375 | doomed@4:0.0119。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 251. test:2976 | World → Sci/Tech

预测置信度 0.8158；真实类概率 0.1838；前两类概率差 0.6321。
分词数 39；未知词比例 0.00%；特征：需结合语义人工复核。

Bangkok animal trade talks open The rules controlling the trade in many at-risk wildlife species may change at a Bangkok meeting starting on Saturday. The 166 member states of the Convention on International Trade in Endangered Species of 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：animal@1:0.3908 | trade@2:0.2565 | endangered@36:0.2032。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 252. test:3001 | Business → Sci/Tech

预测置信度 0.7311；真实类概率 0.2664；前两类概率差 0.4647。
分词数 36；未知词比例 2.78%；特征：商业与科技边界；含HTML实体或编码痕迹。

Corporate Krueger haunts PeopleSoft A few weeks ago the then-CEO of PeopleSoft, Craig Conway, posed the following question to attendees at a technology conference:  quot;Have you ever had a bad dream that never ended?

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：technology@23:0.8475 | conference@24:0.4186 | have@26:0.0976。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 253. test:3027 | Sci/Tech → Business

预测置信度 0.7008；真实类概率 0.2880；前两类概率差 0.4129。
分词数 33；未知词比例 0.00%；特征：商业与科技边界。

The C.E.O. Vanishes, and Other Mysteries Why did PeopleSoft, in the midst of a takeover fight with Oracle, fire its chief executive and president? Who knows? And that's a problem.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：executive@23:1.0384 | chief@22:0.7562 | o@3:0.7074。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 254. test:3035 | Business → Sci/Tech

预测置信度 0.8697；真实类概率 0.1293；前两类概率差 0.7403。
分词数 36；未知词比例 0.00%；特征：商业与科技边界。

Lucent's history a case study in wild rides If you've ever wondered what ignited America's late-1990s obsession with telecom and tech stocks, you could well argue it all started with Lucent Technologies .

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tech@24:0.8210 | study@5:0.4049 | you@26:0.2727。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 255. test:3044 | World → Business

预测置信度 0.6720；真实类概率 0.3142；前两类概率差 0.3578。
分词数 28；未知词比例 0.00%；特征：世界与商业边界。

Brown calls for Labour unity Chancellor Gordon Brown has sought to quell speculation over who should run the Labour Party and turned the attack on the opposition Conservatives.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：chancellor@5:2.5989 | gordon@6:1.1651 | the@17:1.0869。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 256. test:3049 | Sports → World

预测置信度 0.7453；真实类概率 0.2477；前两类概率差 0.4976。
分词数 32；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

Flu sidelines Clemens on Sunday Roger Clemens was scratched from his start on Sunday after spending most of the overnight hours battling a stomach virus. Clemens #39; blood pressure was slightly elevated 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：virus@24:2.5211 | flu@0:0.7071 | stomach@23:0.5092。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 257. test:3052 | Business → World

预测置信度 0.4894；真实类概率 0.4188；前两类概率差 0.0707。
分词数 39；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Ahold to Sell Spain Operations to Permira (AP) AP - The Dutch supermarket retailer Ahold, seeking to streamline global operations and reduce debt, said Sunday it will sell its holdings in Spain to Permira Funds for about  #36;849 million.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ap@8:3.5968 | ap@7:2.8799 | spain@3:0.4745。
能把预测改为真实类的单词遮挡数：9。仅表示局部敏感性，不代表已证明因果原因。

## 258. test:3057 | Sci/Tech → World

预测置信度 0.5661；真实类概率 0.4289；前两类概率差 0.1372。
分词数 39；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Mobile phone network reaches last of China's ethnic minorities (AFP) AFP - China has brought its mobile phone network to the last of its ethnic minority regions previously cut off from communication with the outside world, state media reported.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：afp@11:2.1088 | afp@10:1.9064 | s@7:0.8766。
能把预测改为真实类的单词遮挡数：9。仅表示局部敏感性，不代表已证明因果原因。

## 259. test:3060 | Sci/Tech → Business

预测置信度 0.8273；真实类概率 0.0730；前两类概率差 0.7543。
分词数 33；未知词比例 0.00%；特征：商业与科技边界。

You have mail, always, with a BlackBerry Washington lawyer William Wilhelm knows from experience that not everybody loves his BlackBerry as much as he does. The girlfriend was fed up with a relationship 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：lawyer@8:1.1674 | william@9:1.0172 | washington@7:0.7193。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 260. test:3062 | World → Business

预测置信度 0.7577；真实类概率 0.2393；前两类概率差 0.5184。
分词数 40；未知词比例 0.00%；特征：世界与商业边界。

Nikkei Opens Higher (Reuters) Reuters - The Nikkei average rose 1.37 percent at\the opening on Monday as a recovery in U.S. stocks encouraged\investors to seek bargains among lagging issues, including\Canon Inc. and other high-tech issues.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：stocks@23:0.6584 | to@26:0.4790 | rose@8:0.4481。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 261. test:3063 | World → Sports

预测置信度 0.8330；真实类概率 0.1668；前两类概率差 0.6662。
分词数 19；未知词比例 0.00%；特征：短文本<=20词。

US football: Patriots' historic win New England win a record-tying 18th straight game - plus an NFL round-up.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：nfl@16:1.4452 | round@17:1.4409 | patriots@2:0.3743。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 262. test:3076 | Business → Sci/Tech

预测置信度 0.6508；真实类概率 0.3470；前两类概率差 0.3038。
分词数 51；未知词比例 3.92%；特征：商业与科技边界；含HTML实体或编码痕迹。

SUSAN TOMPOR: Stores turn paper into e-checks I picked up my 6-year-old son from school last week, and we drove to Wal-Mart to see the future for paper checks. We grabbed a few of life #39;s staples: some Legos, a pack of 3x5 cards to create 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：e@6:1.4489 | i@8:0.3722 | checks@7:0.3635。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 263. test:3077 | Business → Sports

预测置信度 0.9765；真实类概率 0.0134；前两类概率差 0.9631。
分词数 34；未知词比例 0.00%；特征：高置信错误>=0.9。

Brewers buyer expected to step out of the shadows Monday MILWAUKEE - Paul Attanasio says the story of his brother buying a baseball team is like a script straight out of Hollywood. He should know.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：baseball@21:2.0127 | team@22:1.0088 | monday@9:0.5725。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 264. test:3091 | Sci/Tech → Sports

预测置信度 0.9991；真实类概率 0.0007；前两类概率差 0.9984。
分词数 33；未知词比例 0.00%；特征：高置信错误>=0.9。

Fable; Nascar 2005: Chase For The Cup Fable comes with a big reputation behind it -- it was developed by Peter Molyneux, creator of such involved, engrossing games as Populous and Black and White.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：cup@6:2.9971 | nascar@1:2.7161 | chase@3:1.6922。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 265. test:3115 | Business → Sci/Tech

预测置信度 0.7694；真实类概率 0.2288；前两类概率差 0.5406。
分词数 37；未知词比例 0.00%；特征：商业与科技边界。

SBC links e-mail, voice messages, fax SBC on Monday announced a new service that integrates voice messages, faxes and e-mails into a single mailbox that can be accessed from anywhere by phone or the Internet.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：e@2:1.9808 | mail@3:1.0488 | voice@4:0.4362。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 266. test:3116 | Sci/Tech → Business

预测置信度 0.8646；真实类概率 0.0910；前两类概率差 0.7736。
分词数 33；未知词比例 6.06%；特征：商业与科技边界；含HTML实体或编码痕迹。

OPM Delving Deeper Into Employees #39; Backgrounds which sets hiring and employment standards for the government -- is reviewing its employees to ensure that they are suitable for jobs involving the  quot;public trust.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：employment@11:0.6891 | hiring@9:0.5902 | employees@4:0.5601。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 267. test:3130 | Business → Sci/Tech

预测置信度 0.6927；真实类概率 0.2817；前两类概率差 0.4110。
分词数 23；未知词比例 0.00%；特征：商业与科技边界。

Taking Advantage of the Terminally Stupid Would you pay \$4 for something that, at best, is worth a dime? Concord Communications shareholders would.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：communications@20:1.6814 | shareholders@21:0.4439 | for@10:0.1356。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 268. test:3141 | Sci/Tech → Business

预测置信度 0.8165；真实类概率 0.1818；前两类概率差 0.6347。
分词数 54；未知词比例 1.85%；特征：商业与科技边界；含HTML实体或编码痕迹。

It #39;s Time for Tech Firms to Bet on Growth Industry leaders have been offering too few innovations and too many marginal upgradesat not-so-marginal prices. There #39;s a joke going around that our lives have become so boring that we #39;ve taken up watching people play cards on TV.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：growth@10:1.2377 | 39@29:0.8648 | prices@27:0.6452。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 269. test:3146 | Sci/Tech → Business

预测置信度 0.7544；真实类概率 0.2339；前两类概率差 0.5206。
分词数 41；未知词比例 0.00%；特征：商业与科技边界。

Judge Challenges EU Position on Microsoft (Reuters) Reuters - A top European Union judge\challenged the EU executive's reasoning in its antitrust court\battle with Microsoft Corp. Friday, questioning why it opposed\the U.S. software giant's setting industry standards.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：union@11:0.9523 | corp@26:0.4338 | battle@23:0.4025。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 270. test:3155 | Sci/Tech → Business

预测置信度 0.9657；真实类概率 0.0083；前两类概率差 0.9397。
分词数 22；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

PeopleSoft down on testimony, forecast Investors react to a disappointing earnings projection and to testimony that dampens hopes of negotiations with Oracle.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：investors@5:3.6630 | forecast@4:2.2828 | testimony@3:1.1025。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 271. test:3156 | Business → Sci/Tech

预测置信度 0.9763；真实类概率 0.0180；前两类概率差 0.9583。
分词数 37；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

New Siebel Chief Outlines Chapter 2 For CRM Vendor After 10 years of focusing on product development and delivery, CEO Michael Lawrie says Siebel had to recognize that technology is only one part of the CRM equation.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：technology@28:0.4617 | siebel@23:0.4122 | outlines@3:0.3014。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 272. test:3157 | World → Sci/Tech

预测置信度 0.8351；真实类概率 0.1645；前两类概率差 0.6706。
分词数 44；未知词比例 0.00%；特征：需结合语义人工复核。

Gordon Cooper, NASA Mercury Pioneer, Dies LOS ANGELES - Gordon Cooper, who was the youngest and perhaps cockiest member of the original Mercury astronauts and set the space endurance record that helped clear the way for the first moon landing, has died. He was 77...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：nasa@2:2.4626 | cooper@1:0.3235 | space@26:0.2876。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 273. test:3163 | World → Business

预测置信度 0.8747；真实类概率 0.1215；前两类概率差 0.7532。
分词数 51；未知词比例 0.00%；特征：世界与商业边界。

U.S. Seeks Reconciliation with Oil-Rich Venezuela  SAO PAULO, Brazil (Reuters) - The United States said on  Monday it will seek better ties with oil-rich Venezuela in the  clearest sign since President Hugo Chavez won a recall  referendum in August that Washington is looking for  reconciliation with the firebrand populist.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：looking@44:0.8318 | washington@42:0.7588 | recall@37:0.6254。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 274. test:3170 | Business → Sci/Tech

预测置信度 0.7833；真实类概率 0.2070；前两类概率差 0.5763。
分词数 45；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Feds kick off digital TV consumer campaign WASHINGTON - It #39;s one of the biggest technical changes in television since color TV: the digital transition. And because many Americans remain in the dark about it, federal regulators began an education campaign Monday to enlighten them.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：digital@23:0.4039 | digital@3:0.3059 | campaign@6:0.2042。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 275. test:3178 | Business → World

预测置信度 0.9071；真实类概率 0.0318；前两类概率差 0.8460。
分词数 47；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

SEC considering civil action over 3 AIG press releases American International Group Inc. said it has been informed by the Securities and Exchange Commission that it could face a civil action over three of the company's press releases, two of which came out in recent weeks.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：s@36:1.2435 | press@37:1.0882 | releases@38:0.9762。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 276. test:3180 | Sci/Tech → World

预测置信度 0.5914；真实类概率 0.4045；前两类概率差 0.1868。
分词数 42；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Russia May Ratify Kyoto Protocol in Oct. -- Minister (Reuters) Reuters - The Russian government expects\parliament to ratify the Kyoto Protocol this month in a move\allowing the long-delayed climate change treaty to come into\force worldwide, a senior minister said Monday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：parliament@14:0.7657 | move@24:0.5788 | allowing@25:0.5532。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 277. test:3183 | Business → Sci/Tech

预测置信度 0.7862；真实类概率 0.1778；前两类概率差 0.6083。
分词数 27；未知词比例 3.70%；特征：商业与科技边界。

webcrawler: A9.com is cool NOW heres something else thats off the mind. Theres no more need to make mental or computer notes while searching the Internet.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：computer@21:0.9467 | internet@26:0.2203 | the@25:0.2061。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 278. test:3186 | World → Sports

预测置信度 0.9451；真实类概率 0.0537；前两类概率差 0.8913。
分词数 23；未知词比例 0.00%；特征：高置信错误>=0.9。

Tennis: Night final for Aus Open The centenary Australian Open will be the first Grand Slam event to stage its final at night.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：event@16:0.7612 | slam@15:0.5553 | open@9:0.5262。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 279. test:3217 | Sci/Tech → Business

预测置信度 0.7001；真实类概率 0.2868；前两类概率差 0.4133。
分词数 25；未知词比例 0.00%；特征：商业与科技边界。

Is PeopleSoft waiting for the right price? A company board member testifies in trial that a sale would be possible if Oracle ups its offer.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：board@9:1.0333 | member@10:0.7392 | that@14:0.5497。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 280. test:3264 | Business → Sci/Tech

预测置信度 0.8558；真实类概率 0.1431；前两类概率差 0.7127。
分词数 35；未知词比例 2.86%；特征：商业与科技边界。

CA aquires computer security firm Computer Associates International Inc., as promised, is back in the acquisition game, scooping up its second computer security company in as many months with an agreement to buy Netegrity Inc.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：game@16:0.8466 | ca@0:0.6409 | security@3:0.5939。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 281. test:3265 | Sci/Tech → Sports

预测置信度 0.9641；真实类概率 0.0181；前两类概率差 0.9460。
分词数 20；未知词比例 0.00%；特征：高置信错误>=0.9；短文本<=20词。

How to take the perfect penalty A sports psychologist says how footballers should prepare themselves for the high-pressure penalties.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：sports@7:4.5739 | psychologist@8:1.1610 | penalty@5:1.0531。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 282. test:3269 | Business → World

预测置信度 0.6861；真实类概率 0.3081；前两类概率差 0.3780。
分词数 43；未知词比例 0.00%；特征：世界与商业边界；含HTML实体或编码痕迹。

Pacific Oil Link Is Best for Russia, Ambassador Says (Update1) Russia, the world #39;s second-biggest oil exporter, will benefit most from a Siberian crude oil pipeline to the Pacific rather than to China as energy resources are needed to develop the 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ambassador@7:3.2825 | russia@6:0.9624 | says@8:0.8185。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 283. test:3303 | World → Business

预测置信度 0.5465；真实类概率 0.3952；前两类概率差 0.1513。
分词数 69；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

Stern to Join Sirius Satellite Radio NEW YORK - Howard Stern has long had two words for the Federal Communications Commission - and in 15 months, he can finally utter them on the air.    The self-proclaimed "King of All Media," perhaps the most influential radio voice of the last 20 years, is shifting his salacious act to satellite radio and freeing himself from the increasingly harsh glare of federal regulators...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：sirius@3:0.7708 | satellite@4:0.6397 | federal@17:0.3524。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 284. test:3306 | World → Sci/Tech

预测置信度 0.9680；真实类概率 0.0320；前两类概率差 0.9360。
分词数 43；未知词比例 0.00%；特征：高置信错误>=0.9。

Ex-Bush Official on Cybersecurity Returns (AP) AP - Howard Schmidt, a highly regarded technology executive who was former special adviser to President Bush for cybersecurity, is returning to work with the Homeland Security Department on efforts to protect the nation's computer networks.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：cybersecurity@24:1.6265 | returning@26:0.5299 | technology@13:0.4307。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 285. test:3312 | World → Business

预测置信度 0.9341；真实类概率 0.0297；前两类概率差 0.9045。
分词数 30；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

Howard Stern Says He Plans to Jump to Satellite Radio After heavy F.C.C. fines, Howard Stern expects to deliver "my show my way" in the mostly unregulated medium.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：satellite@8:1.5221 | stern@17:0.9889 | radio@9:0.8305。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 286. test:3334 | Business → Sci/Tech

预测置信度 0.9961；真实类概率 0.0039；前两类概率差 0.9921。
分词数 36；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

34 tech firms sued for alleged LCD patent theft Honeywell has issued lawsuits against 34 companies, including Dell, Apple, Sony and Toshiba alleging LCD panels used in their products infringe a 1992 patent the company holds.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：lcd@6:0.5408 | apple@18:0.5369 | tech@1:0.2924。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 287. test:3354 | Business → Sci/Tech

预测置信度 0.9722；真实类概率 0.0276；前两类概率差 0.9445。
分词数 28；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Nintendo to Unveil Handheld Upgrade Facing its biggest threat ever from the arrival of Sony Corp. in the portable video-game machine market, Japanese game-maker Nintendo Co.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：facing@5:0.7320 | game@24:0.6132 | game@20:0.4748。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 288. test:3384 | World → Business

预测置信度 0.7329；真实类概率 0.1479；前两类概率差 0.5850。
分词数 82；未知词比例 0.00%；特征：世界与商业边界。

Employment Picture Expected to Improve NEW YORK - A rash of job cuts - more than 10,000 layoffs just this week from a handful of companies - has created some gloom on the jobs front. But Friday's release of jobs data for September was expected to show a steady unemployment rate and creation between about 50,000 to 250,000 new jobs, though uncertainties such as the effects of last month's hurricanes kept the estimates all over the map, said Wachovia Corp...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：hurricanes@71:1.0383 | data@39:0.9865 | month@69:0.8188。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 289. test:3406 | Business → Sci/Tech

预测置信度 0.5966；真实类概率 0.4014；前两类概率差 0.1951。
分词数 46；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Advanced Micro Devices meets reduced forecast for third quarter SAN FRANCISCO - Advanced Micro Devices Inc. reported a third-quarter profit from a loss a year-earlier on today, but sales fell from the second quarter in line with the chip maker #39;s recently reduced outlook.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：devices@13:0.3819 | francisco@10:0.2946 | chip@39:0.1828。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 290. test:3409 | Business → Sci/Tech

预测置信度 0.4358；真实类概率 0.4300；前两类概率差 0.0057。
分词数 35；未知词比例 2.86%；特征：商业与科技边界；前两类接近:概率差<0.2。

Skyboxes May Reach A Limit Verizon Communications Inc. would seem to be a prime candidate to snap up a luxury suite at the \$440 million ballpark being planned for Washington's Major League Baseball team.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：communications@6:0.7137 | baseball@33:0.2771 | s@30:0.2537。
能把预测改为真实类的单词遮挡数：5。仅表示局部敏感性，不代表已证明因果原因。

## 291. test:3419 | Business → World

预测置信度 0.5538；真实类概率 0.1696；前两类概率差 0.2821。
分词数 29；未知词比例 3.45%；特征：世界与商业边界。

Aisin finishes deal for Michigan land HANDY TOWNSHIP -- A Japanese auto supplier said Thursday it completed the purchase of about 750 acres of Michigan land for a proving ground.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：land@5:0.7399 | handy@6:0.3946 | japanese@9:0.2346。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 292. test:3422 | Business → World

预测置信度 0.9407；真实类概率 0.0007；前两类概率差 0.8826。
分词数 46；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

Woman's death probed Public health officials are investigating why a 38-year-old woman died two weeks after undergoing gastric bypass surgery at Saint Anne's Hospital in Fall River. The hospital has stopped offering the surgery during the state probe and an internal review.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：woman@14:1.0420 | death@2:0.9387 | old@13:0.7802。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 293. test:3423 | Business → Sci/Tech

预测置信度 0.7725；真实类概率 0.2017；前两类概率差 0.5708。
分词数 42；未知词比例 0.00%；特征：商业与科技边界。

Danaher to Make Offer for Linx Printing Danaher Corp., a maker of Sears Craftsman tools and environmental testing products, said Wednesday that it plans to make a cash tender offer to purchase Linx Printing Technologies PLC for \$158 million, including transaction costs.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：environmental@16:2.0438 | testing@17:1.2634 | products@18:0.6048。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 294. test:3455 | Business → Sci/Tech

预测置信度 0.9594；真实类概率 0.0404；前两类概率差 0.9190。
分词数 28；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Sun settles Kodak patent suit Sun Microsystems says it will pay Kodak \$92 million to settle a high-profile patent suit involving Sun #39;s Java programming technology.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：java@25:2.3047 | programming@26:2.0608 | sun@5:0.6687。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 295. test:3465 | Business → World

预测置信度 0.7346；真实类概率 0.1421；前两类概率差 0.5926。
分词数 44；未知词比例 0.00%；特征：世界与商业边界。

Lego, Carrefour in French Price-Fix Probe (AP) AP - French competition authorities are investigating Danish toy maker Lego Systems AS and supermarket retailer Carrefour SA as part of a probe into alleged price fixing in the French toy market in 2002 and early 2003.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ap@8:3.7954 | ap@7:2.7636 | french@9:0.9843。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 296. test:3495 | Business → Sci/Tech

预测置信度 0.5729；真实类概率 0.4185；前两类概率差 0.1544。
分词数 41；未知词比例 4.88%；特征：商业与科技边界；前两类接近:概率差<0.2。

Trading blows When a can of worms is opened, all manner of slimy things crawl out. So it was when the US government fired the first shots in a fusillade against the European Union - by complaining to the World Trade Organisation 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：worms@6:2.8436 | of@5:0.4428 | opened@8:0.3297。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 297. test:3538 | Business → Sci/Tech

预测置信度 0.6337；真实类概率 0.0141；前两类概率差 0.2823。
分词数 33；未知词比例 0.00%；特征：商业与科技边界。

American Economist Expected to Win Nobel (AP) AP - Americans have dominated the annual Nobel Memorial Prize in Economic Sciences five years running, and it may not surprise Nobel watchers if the trend continues.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ap@6:2.1449 | ap@7:1.8619 | nobel@5:0.9624。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 298. test:3546 | World → Sci/Tech

预测置信度 0.5614；真实类概率 0.0629；前两类概率差 0.1856。
分词数 93；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Study: Few Americans Buy Drugs Online NEW YORK - Only 4 percent of Americans have ever used the Internet to buy prescription drugs - and even fewer do so through foreign pharmacies - despite Web sites maintained by a handful of states to help citizens import medicines more cheaply from Canada, a new study finds.    A majority - 62 percent - believe drugs bought online are less safe than those purchased from a local pharmacy, accepting the federal government's stated concerns in opposing drug imports, the Pew Internet and American Life Project said in a report Sunday...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：web@31:1.2107 | sites@32:0.9693 | study@50:0.3875。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 299. test:3548 | Business → Sci/Tech

预测置信度 0.5417；真实类概率 0.1007；前两类概率差 0.1849。
分词数 26；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

New pension 'would help millions' Britain's pension system could easily be replaced by a new payment that would make millions better off, a report says.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：could@9:0.7241 | system@8:0.4471 | s@6:0.2608。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 300. test:3555 | World → Business

预测置信度 0.6351；真实类概率 0.3571；前两类概率差 0.2780。
分词数 54；未知词比例 0.00%；特征：世界与商业边界。

Senate Resolves Corporate Tax Bill Delay WASHINGTON - The Senate late Sunday resolved a dispute delaying passage of a sweeping corporate tax bill and two spending bills for disaster relief and homeland security, clearing the way for senators to adjourn Monday to hit the campaign trail.    The agreement removed parliamentary roadblocks thrown up by Sen...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：and@29:0.4310 | the@45:0.3326 | tax@3:0.3025。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 301. test:3556 | Business → Sci/Tech

预测置信度 0.5704；真实类概率 0.4140；前两类概率差 0.1563。
分词数 50；未知词比例 2.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

Complex Brings Work, Shops Close to Home Tucked on a side street, just a block from the cars and trucks that whiz along Rockville Pike, sits a new complex of 404 luxury apartments, renovated restaurants and stores that some planners and developers are calling the optimum in compact urban redevelopment.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：compact@47:1.4616 | urban@48:0.5855 | and@35:0.4812。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 302. test:3561 | World → Business

预测置信度 0.6319；真实类概率 0.0061；前两类概率差 0.2700。
分词数 25；未知词比例 0.00%；特征：世界与商业边界。

Cellphone Industry Hits Snag as It Woos Untapped Market The mobile phone industry is turning its attention to the last untapped demographic - people over 65.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：cellphone@0:1.9736 | industry@1:1.6053 | it@5:0.8189。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 303. test:3563 | World → Sports

预测置信度 0.9831；真实类概率 0.0167；前两类概率差 0.9664。
分词数 33；未知词比例 0.00%；特征：高置信错误>=0.9。

Ken Caminiti, 1996 NL MVP, Dies at Age 41 NEW YORK - Ken Caminiti, the 1996 National League MVP who later admitted using steroids during his major league career, died Sunday. He was 41...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：mvp@17:0.6339 | league@16:0.6293 | 1996@14:0.4904。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 304. test:3570 | World → Sports

预测置信度 0.9964；真实类概率 0.0036；前两类概率差 0.9928。
分词数 22；未知词比例 0.00%；特征：高置信错误>=0.9。

Legendary all-rounder Miller dies Keith Miller, arguably Australia's greatest  all-rounder in Test cricket, has died in Melbourne aged 84.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：keith@5:2.2219 | miller@6:1.8168 | has@16:1.5659。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 305. test:3576 | Business → Sci/Tech

预测置信度 0.6361；真实类概率 0.3520；前两类概率差 0.2841。
分词数 35；未知词比例 2.86%；特征：商业与科技边界；含HTML实体或编码痕迹。

Intel defeats AMD in court AMD #39;s attempt to persuade the US court to sanction the release of over 60,000 pages of Intel documentation to a European Commission anti-trust enquiry has failed.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：amd@2:0.3419 | amd@5:0.2269 | intel@24:0.2085。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 306. test:3580 | Business → Sci/Tech

预测置信度 0.8640；真实类概率 0.1118；前两类概率差 0.7521。
分词数 32；未知词比例 0.00%；特征：商业与科技边界。

T-Online returns to Deutsche Telekom mothership German incumbent telco Deutsche Telekom announced over the weekend it is to begin taking its internet division, T-Online, back entirely within the mother corporation.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：internet@22:0.9768 | online@25:0.4886 | t@24:0.4289。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 307. test:3590 | World → Sci/Tech

预测置信度 0.9346；真实类概率 0.0405；前两类概率差 0.8942。
分词数 36；未知词比例 0.00%；特征：高置信错误>=0.9。

Finnish Watchdog Raps TV Game Operators (Reuters) Reuters - Finland's consumer watchdog said on\Monday it had reprimanded broadcasters for causing children to\run up huge mobile phone bills with interactive television game\and chat programs.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：mobile@26:1.4329 | phone@27:1.4008 | consumer@10:0.5184。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 308. test:3604 | World → Sports

预测置信度 0.8183；真实类概率 0.0783；前两类概率差 0.7400。
分词数 43；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

World ; Bigley: I want to live a simple life, the final plea World News, The nearly five-minute tape was released two days after Bigley #39;s family said it had the proof that the 62-year-old engineer from Liverpool was killed.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@25:2.3278 | final@10:0.9814 | the@9:0.8891。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 309. test:3617 | Business → Sci/Tech

预测置信度 0.9968；真实类概率 0.0031；前两类概率差 0.9937。
分词数 50；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Linux: Paris weighs a shift to open-source camp PARIS The open-source computer system known as Linux won a tough battle over Microsoft earlier this year when the city of Munich decided to change the operating software of 14,000 government computers, despite the personal intervention of Steve Ballmer 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：computer@13:0.9031 | system@14:0.5367 | source@12:0.4944。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 310. test:3627 | World → Sci/Tech

预测置信度 0.8752；真实类概率 0.0332；前两类概率差 0.7836。
分词数 45；未知词比例 0.00%；特征：需结合语义人工复核。

SKorea's Samsung to invest 24 billion dollars in new chip lines (AFP) AFP - South Korea's Samsung Electronics Co., the world's largest memory chipmaker, said it would invest some 24 billion dollars in building new chip production lines over the next six years.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：memory@24:0.5868 | chip@37:0.3560 | chipmaker@25:0.2983。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 311. test:3638 | World → Sports

预测置信度 0.5648；真实类概率 0.2166；前两类概率差 0.3482。
分词数 22；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

Highlights of What Congress Has Done (AP) AP - Highlights of what Congress has done  #151; and has not done  #151; this year.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：what@10:0.4935 | done@5:0.4182 | highlights@8:0.3449。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 312. test:3643 | Sci/Tech → World

预测置信度 0.9948；真实类概率 0.0045；前两类概率差 0.9903。
分词数 40；未知词比例 0.00%；特征：高置信错误>=0.9。

Kenyan Laureate Urges Rich Nations to Ratify Kyoto (Reuters) Reuters - Kenya's Nobel Peace Prize winner,\Wangari Maathai, on Monday urged wealthy nations to ratify the\Kyoto protocol on climate change to ease the burden of\pollution on poor countries.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：wangari@16:3.3652 | winner@15:2.0596 | maathai@17:1.6156。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 313. test:3664 | Sci/Tech → Business

预测置信度 0.8216；真实类概率 0.1777；前两类概率差 0.6439。
分词数 40；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Oracle vs. PeopleSoft: Lies and Lying CEOs Who Tell Them PeopleSoft #39;s board knew that CEO Craig Conway had erred in his comments, so it filed a corrected version of the meeting transcript with the Securities and Exchange Commission.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@11:1.7146 | board@13:1.2763 | a@27:0.7165。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 314. test:3671 | Business → Sci/Tech

预测置信度 0.9917；真实类概率 0.0082；前两类概率差 0.9835。
分词数 41；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Microsoft Launches New Media Center PC Microsoft Corp. MSFT.O on Tuesday unveiled a new version of its Windows XP Media Center, adding features such as instant messaging and high-definition television to a personal computer designed for the living room.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：version@15:0.6171 | messaging@27:0.5532 | microsoft@0:0.4136。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 315. test:3672 | Business → Sci/Tech

预测置信度 0.9791；真实类概率 0.0196；前两类概率差 0.9595。
分词数 41；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Rumors Suggest Photo Ability To Be Added to iPod  quot;Apple has invested heavily in technology to edit pictures. Not having a portable device to show them seemed an obvious oversight that would be corrected once the price of the displays 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ipod@8:0.8003 | apple@10:0.8000 | photo@2:0.2462。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 316. test:3675 | Sci/Tech → Business

预测置信度 0.9908；真实类概率 0.0074；前两类概率差 0.9834。
分词数 47；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

DreamWorks Animation IPO Set at 29M Shares Underwriters for DreamWorks Animation SKG Inc., producer of the blockbuster "Shrek" movies, Tuesday set the terms of the company's pending initial public offering at 29 million common shares, with an estimated price range of \$23 to \$25 a share.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：skg@11:1.1900 | dreamworks@9:1.0456 | inc@12:0.9476。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 317. test:3683 | World → Business

预测置信度 0.5465；真实类概率 0.4363；前两类概率差 0.1102。
分词数 23；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

Australia: Wallets trump war A majority of Australians oppose the Iraq war, but they turned out to be more concerned about the economy.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：trump@2:3.9610 | wallets@1:1.5439 | the@9:1.2037。
能把预测改为真实类的单词遮挡数：6。仅表示局部敏感性，不代表已证明因果原因。

## 318. test:3684 | Business → World

预测置信度 0.3031；真实类概率 0.2610；前两类概率差 0.0068。
分词数 31；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

Lazard adversaries edge closer to a deal Bruce Wasserstein, head of Lazard, could reach an agreement as early as this week with Michel David-Weill, the chairman, extending the deadline for 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：edge@2:0.3627 | reach@13:0.3604 | closer@3:0.3546。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 319. test:3685 | World → Business

预测置信度 0.6199；真实类概率 0.3697；前两类概率差 0.2502。
分词数 45；未知词比例 0.00%；特征：世界与商业边界。

FCC Proposes \$1.2M Indecency Fine for Fox WASHINGTON - Federal regulators proposed a record indecency fine of nearly \$1.2 million Tuesday against Fox Broadcasting Co. for an episode of its reality series "Married by America" that included graphic scenes from bachelor and bachelorette parties...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：regulators@10:1.0955 | and@42:1.0097 | federal@9:0.8044。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 320. test:3688 | World → Sports

预测置信度 0.9784；真实类概率 0.0124；前两类概率差 0.9660。
分词数 32；未知词比例 6.25%；特征：高置信错误>=0.9。

Ljubicic Downs Hanescu at Open De Moselle Top-seeded Ivan Ljubicic of Croatia beat Victor Hanescu of Romania 6-4, 6-4 Tuesday in the first round of the Open de Moselle.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：seeded@8:2.1896 | top@7:1.6843 | open@4:1.2272。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 321. test:3689 | Sci/Tech → Business

预测置信度 0.6188；真实类概率 0.3809；前两类概率差 0.2380。
分词数 24；未知词比例 0.00%；特征：商业与科技边界。

Will your phone become your credit card? Motorola is working with MasterCard to introduce a "lifestyle changing" credit card phone by year's end.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：your@4:0.6581 | credit@5:0.5758 | a@14:0.5496。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 322. test:3702 | Sci/Tech → Business

预测置信度 0.9838；真实类概率 0.0160；前两类概率差 0.9678。
分词数 49；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Intel Posts Higher Profit, Sales Computer-chip maker Intel Corp. said yesterday that earnings for its third quarter were \$1.9 billion -- up 15 percent from the same quarter a year ago -- but the company cautioned that computer-processor demand in the United States is likely to remain low.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：profit@3:2.5596 | sales@4:1.4352 | maker@7:1.0149。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 323. test:3718 | World → Sports

预测置信度 0.9902；真实类概率 0.0040；前两类概率差 0.9862。
分词数 72；未知词比例 8.33%；特征：高置信错误>=0.9。

'Sherlock' Is Bicycling Across Australia PERTH, Australia - A former British soccer player raising money for a leukemia charity set off Wednesday on a coast-to-coast ride across Australia on a Victorian-era bicycle that is older than the country.    Leukemia survivor Lloyd Scott dressed up as fictional British supersleuth Sherlock Holmes, complete with tweed coat, deerstalker hat and a fake mustache for the 2,700-mile trip from Perth to Sydney...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：player@11:4.7705 | soccer@10:4.2317 | british@9:0.7826。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 324. test:3723 | Business → Sci/Tech

预测置信度 0.6187；真实类概率 0.3688；前两类概率差 0.2499。
分词数 54；未知词比例 3.70%；特征：商业与科技边界；含HTML实体或编码痕迹。

SICK KIDS VS. DISNEY IN  #39;PETER PAN #39; DUSTUP It #39;s a story that would make Peter Pan glad that he never grew up. Walt Disney Co. is caught in a feud with a UK children #39;s hospital over the copyright to JM Barrie #39;s classic novel,  quot;Peter Pan.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：novel@50:1.6386 | copyright@43:1.1660 | classic@49:0.8337。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 325. test:3728 | Business → Sci/Tech

预测置信度 0.7105；真实类概率 0.2878；前两类概率差 0.4227。
分词数 38；未知词比例 0.00%；特征：商业与科技边界。

Excess chips a drag on 3rd-quarter Intel results Intel on Tuesday released third-quarter financial results showing that it continues to struggle to sell a substantial stockpile of computer chips as demand for personal computers remains slow.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：computers@35:1.0260 | remains@36:0.9449 | computer@29:0.5151。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 326. test:3746 | World → Sports

预测置信度 0.6760；真实类概率 0.3239；前两类概率差 0.3521。
分词数 18；未知词比例 0.00%；特征：短文本<=20词。

Football: Azerbaijan 0-1 England Michael Owen heads England's winner in the World Cup qualifier against Azerbaijan.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：cup@14:3.3329 | world@13:1.6155 | winner@10:1.1264。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 327. test:3747 | World → Business

预测置信度 0.9904；真实类概率 0.0023；前两类概率差 0.9831。
分词数 29；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

Ban for former Ahold executives Dutch  retailer Ahold's former chairman and its ex-finance officer are barred from executive posts as part of a US fraud case settlement.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：retailer@6:3.5213 | executives@4:1.1104 | dutch@5:0.9966。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 328. test:3777 | Sci/Tech → World

预测置信度 0.9396；真实类概率 0.0521；前两类概率差 0.8874。
分词数 52；未知词比例 1.92%；特征：高置信错误>=0.9；含HTML实体或编码痕迹。

Thai minister says zoo #39;s illegal orangutans to be moved JAKARTA/BANGKOK (DPA): Thailand, under growing pressure to repatriate some 100 orangutans allegedly smuggled into the country from Indonesia, plans to shift the apes from a private zoo to a safe centre, probably in Chiang Mai, a minister said on Thursday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：thailand@14:2.6372 | under@15:1.5242 | minister@1:1.3528。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 329. test:3784 | World → Business

预测置信度 0.3814；真实类概率 0.2554；前两类概率差 0.0212。
分词数 24；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

New planes fly to battle locusts The United Nations is flying six more aircraft to combat swarms of crop-devouring locusts in west Africa.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：crop@18:2.1539 | devouring@19:1.1365 | in@21:0.6532。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 330. test:3790 | World → Business

预测置信度 0.7266；真实类概率 0.2694；前两类概率差 0.4572。
分词数 43；未知词比例 0.00%；特征：世界与商业边界；含HTML实体或编码痕迹。

Oil exports flow as strike woes ease A general strike in Nigeria, which has raised fears over oil supply from the world #39;s seventh-largest exporter, will likely end its first phase on Thursday  quot;all going well quot;, union leaders said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@22:1.5726 | exports@1:0.8243 | seventh@24:0.5656。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 331. test:3796 | Business → Sci/Tech

预测置信度 0.5888；真实类概率 0.3999；前两类概率差 0.1889。
分词数 40；未知词比例 2.50%；特征：商业与科技边界；前两类接近:概率差<0.2。

Diesels, Hybrids Fated to Wed Two leading technologies used in fuel-efficient vehicles seem destined to unite. Industry experts say joining hybrid motors with diesel engines would result in the greenest mainstream vehicles ever, and the initial tests are promising.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：with@23:0.6764 | technologies@7:0.3553 | experts@18:0.3322。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 332. test:3797 | Business → World

预测置信度 0.8297；真实类概率 0.1406；前两类概率差 0.6891。
分词数 23；未知词比例 0.00%；特征：世界与商业边界。

Transport strike hits Netherlands Public transport grinds to a halt in the Netherlands as workers strike against the government's planned welfare cuts.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：government@18:0.4488 | s@19:0.3472 | hits@2:0.3395。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 333. test:3805 | World → Sports

预测置信度 0.9905；真实类概率 0.0082；前两类概率差 0.9823。
分词数 50；未知词比例 0.00%；特征：高置信错误>=0.9。

Munro, Morris Face Off in NLCS Game 2 ST. LOUIS - The Houston Astros put their hopes in a pitcher untested in the postseason when they give Pete Munro the ball to start Game 2 of the NL Championship series on Thursday, one night after dropping the opener to the St...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：st@8:0.8468 | the@10:0.5023 | game@32:0.5020。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 334. test:3813 | Business → Sci/Tech

预测置信度 0.6350；真实类概率 0.3059；前两类概率差 0.3291。
分词数 37；未知词比例 0.00%；特征：商业与科技边界。

FCC exempts fiber-to-curb from sharing requirements The Federal Communications Commission Thursday voted to allow incumbent telephone carriers from sharing fiber-to-the-curb deployments from competitors, prompting one incumbent to announce an accelerated fiber rollout.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：telephone@17:0.9446 | allow@15:0.4712 | communications@10:0.1422。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 335. test:3856 | World → Business

预测置信度 0.9968；真实类概率 0.0011；前两类概率差 0.9946。
分词数 37；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

September Retail Sales Up by 1.5 Percent WASHINGTON - Shoppers got their buying groove back last month, propelling sales at the nation's retailers by a strong 1.5 percent. It was the best showing since March...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：retailers@23:1.3995 | retail@1:1.1282 | sales@2:0.9282。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 336. test:3882 | World → Business

预测置信度 0.8613；真实类概率 0.0585；前两类概率差 0.7928。
分词数 34；未知词比例 2.94%；特征：世界与商业边界。

For Many Airline Pilots, the Thrill Is Gone While pilots still feel in command in the air, they increasingly are feeling slighted on the ground, as airlines extract salary and benefits concessions from them.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：airlines@26:1.3600 | salary@28:0.5846 | extract@27:0.4374。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 337. test:3887 | Sci/Tech → Business

预测置信度 0.6083；真实类概率 0.3914；前两类概率差 0.2169。
分词数 44；未知词比例 0.00%；特征：商业与科技边界。

Blockbuster Cuts Online Price, Challenges Netflix (Reuters) Reuters - Video chain Blockbuster Inc on\Friday said it would lower the price of its online DVD rentals\to undercut a similar move by Netflix Inc. that sparked a stock\a sell-off of both companies' shares.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：blockbuster@10:1.2050 | friday@13:0.7279 | chain@9:0.6656。
能把预测改为真实类的单词遮挡数：9。仅表示局部敏感性，不代表已证明因果原因。

## 338. test:3888 | Sci/Tech → World

预测置信度 0.7225；真实类概率 0.2763；前两类概率差 0.4462。
分词数 31；未知词比例 0.00%；特征：需结合语义人工复核。

Great White Shark Loses Monitor Tag (AP) AP - A great white shark that was tagged with a data-gathering device in shallow waters off Cape Cod has apparently reclaimed its privacy.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ap@7:1.6258 | ap@6:1.2146 | loses@3:1.0087。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 339. test:3899 | World → Sports

预测置信度 0.9258；真实类概率 0.0713；前两类概率差 0.8545。
分词数 36；未知词比例 0.00%；特征：高置信错误>=0.9。

Warne takes six but India establish handy lead (Reuters) Reuters - World test wicket record holder Shane Warne grabbed six wickets as India established a handy 141-run first innings lead in the second test on Saturday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：lead@7:1.1469 | lead@29:0.9206 | innings@28:0.9075。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 340. test:3900 | World → Sports

预测置信度 0.8797；真实类概率 0.0995；前两类概率差 0.7802。
分词数 20；未知词比例 0.00%；特征：短文本<=20词。

Rugby: Kiwis earn draw New Zealand hold Australia 16-16 in the first game of the 2004 Tri-Nations series.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：kiwis@1:1.4492 | game@13:0.8062 | rugby@0:0.4997。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 341. test:3942 | Sports → World

预测置信度 0.5751；真实类概率 0.4247；前两类概率差 0.1505。
分词数 48；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

UPDATE 2-Cricket-Malik reported for suspect action  Cricket-ICC clears Zimbabwe Cricket Union of racism October 17, 2004 14:05:37 LAHORE, Pakistan, Oct 17 (Reuters) - A special report by an International Cricket Council (ICC) inquiry commission has ruled there is no evidence of racism within the 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：suspect@6:1.0720 | commission@37:0.9674 | inquiry@36:0.8040。
能把预测改为真实类的单词遮挡数：7。仅表示局部敏感性，不代表已证明因果原因。

## 342. test:3949 | Business → Sports

预测置信度 0.5207；真实类概率 0.1999；前两类概率差 0.3208。
分词数 40；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

Florida #39;s prepaid tuition program thriving Already the biggest of its kind in the country, Florida #39;s popular prepaid-tuition program expects to count its millionth customer during a sign-up period that runs Monday through Jan. 31.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：runs@35:2.4523 | monday@36:1.4446 | 39@17:0.6249。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 343. test:3953 | Sci/Tech → Sports

预测置信度 0.8611；真实类概率 0.1171；前两类概率差 0.7440。
分词数 64；未知词比例 3.12%；特征：需结合语义人工复核。

Toughest athlete is female and unknown You probably haven't heard about one of the toughest endurance sports around: the deca-ironman. That's 38 km swimming, immediately followed by an 1800 km bicycle ride and a 420 km run. Currently, the world record stands at about 187 hours, held by a German housewife. Nobody else has ever finished the course below 192 hours.  

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：sports@17:1.4959 | that@22:1.0090 | the@41:0.6401。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 344. test:3968 | Business → Sci/Tech

预测置信度 0.9141；真实类概率 0.0840；前两类概率差 0.8302。
分词数 37；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

US consumers unaware of spyware The findings come in a report from the newly formed Consumer Spyware Initiative, a joint effort by Dell and the non-profit Internet Education Foundation that aims to increase awareness of spyware.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：spyware@16:1.4950 | formed@14:0.3159 | spyware@4:0.2305。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 345. test:3970 | Business → Sci/Tech

预测置信度 0.9958；真实类概率 0.0038；前两类概率差 0.9920。
分词数 42；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Wi-Fi successor is called high-speed hype -- for now SAN FRANCISCO -- At virtually every turn, Intel Corp. executives are heaping praise on an emerging long-range wireless technology known as WiMAX, which can blanket entire cities with high-speed Internet access.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：wimax@31:0.6720 | technology@28:0.3254 | with@37:0.2573。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 346. test:3973 | Sports → Sci/Tech

预测置信度 0.9829；真实类概率 0.0043；前两类概率差 0.9710。
分词数 46；未知词比例 2.17%；特征：高置信错误>=0.9。

Ramirez should be taking it to heart When it comes down to this, when it's worse than you could have possibly imagined, if you are any kind of ballplayer at all, you look within and ask yourself what you can do to make it better.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：yourself@37:3.1869 | what@38:1.2770 | you@39:0.7665。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 347. test:3980 | World → Sports

预测置信度 0.4318；真实类概率 0.3936；前两类概率差 0.0382。
分词数 26；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

An Old Church's New Tilt Inspires Tourists and T-Shirts A humble church has something Germany's glorious Cologne Cathedral cannot match: a leaning tower.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：glorious@18:2.4019 | cologne@19:1.5472 | cathedral@20:0.9001。
能把预测改为真实类的单词遮挡数：7。仅表示局部敏感性，不代表已证明因果原因。

## 348. test:3981 | World → Sci/Tech

预测置信度 0.5253；真实类概率 0.4450；前两类概率差 0.0803。
分词数 39；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Calif. Mental Health Services May Expand (AP) AP - As pressures increase on California's mental health system, its workers and advocates say they are forced to do more with a supply of money that seems to shrink each year.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：system@16:0.7222 | california@12:0.4329 | workers@18:0.3089。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 349. test:3992 | World → Sci/Tech

预测置信度 0.5681；真实类概率 0.1424；前两类概率差 0.2787。
分词数 46；未知词比例 0.00%；特征：需结合语义人工复核。

5 EU ministers back digital passports FLORENCE Interior ministers from the five largest West European countries have agreed to adopt digital fingerprinting on passports, officials here said, but a second day of talks on Monday found them still deadlocked on a plan to create migrant holding 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：digital@4:2.5151 | passports@5:1.7591 | digital@20:0.4606。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 350. test:3998 | Sci/Tech → World

预测置信度 0.8543；真实类概率 0.1450；前两类概率差 0.7092。
分词数 28；未知词比例 0.00%；特征：需结合语义人工复核。

UN 'must ignore cloning ban call' The UK's Royal Society urges the UN to ignore a call by President Bush to ban all forms of human cloning.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：bush@20:1.4328 | president@19:1.3502 | un@0:1.2565。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 351. test:4000 | Business → Sci/Tech

预测置信度 0.9929；真实类概率 0.0067；前两类概率差 0.9862。
分词数 49；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Google puts desktop search privacy up front Google has announced a new desktop search application that enables users to search their e-mail, files, web history, and chats. Perhaps learning from previous mistakes, Google says it has designed the product  quot;from the ground up to respect user privacy.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：privacy@48:0.4408 | user@47:0.3881 | application@14:0.1760。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 352. test:4027 | World → Sports

预测置信度 0.9567；真实类概率 0.0308；前两类概率差 0.9259。
分词数 18；未知词比例 0.00%；特征：高置信错误>=0.9；短文本<=20词。

Tennis: Davenport to play on Lindsay Davenport says she plans to play in the Australian Open next January.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：open@15:1.4994 | australian@14:0.8711 | play@3:0.8499。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 353. test:4029 | World → Sports

预测置信度 0.9952；真实类概率 0.0048；前两类概率差 0.9903。
分词数 41；未知词比例 0.00%；特征：高置信错误>=0.9。

USC, Miami Top BCS Standings, Not Okla. Southern California took the top spot Monday in the season's first Bowl Championship Series standings, and surprisingly Miami is ahead of Oklahoma in a close race for the second spot.    Oklahoma is No...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：bowl@19:1.3200 | season@16:0.9286 | bcs@3:0.8017。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 354. test:4036 | Business → Sci/Tech

预测置信度 0.9231；真实类概率 0.0499；前两类概率差 0.8731。
分词数 31；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

BASS moving headquarters to Florida The Bass Anglers Sportsman Society is moving its headquarters to Central Florida. The bass fishing organization, based in Montgomery since its inception in 1967, announced Monday 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：fishing@19:3.7931 | organization@20:1.3700 | in@27:0.0499。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 355. test:4058 | Sci/Tech → Business

预测置信度 0.7312；真实类概率 0.1955；前两类概率差 0.5357。
分词数 28；未知词比例 3.57%；特征：商业与科技边界。

Regulators Approve Artificial Heart The Food and Drug Administration approved the use of an artificial heart made by SynCardia Systems as a temporary device for people awaiting transplants.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：drug@7:1.0918 | administration@8:0.7424 | regulators@0:0.3912。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 356. test:4065 | Business → World

预测置信度 0.8370；真实类概率 0.1560；前两类概率差 0.6810。
分词数 35；未知词比例 0.00%；特征：世界与商业边界。

GM Protests Spread Across Europe Tens of thousands of General Motors workers across Europe were set to stop working on Tuesday in a sign of solidarity with their German colleagues, who face massive job cuts.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：german@28:0.7892 | europe@4:0.5365 | who@30:0.4366。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 357. test:4088 | World → Sports

预测置信度 0.9129；真实类概率 0.0151；前两类概率差 0.8427。
分词数 29；未知词比例 0.00%；特征：高置信错误>=0.9。

Glazer stake in Man Utd nears 30 US tycoon Malcolm Glazer lifts his stake in Manchester Utd to 28.11, one day after spending 17m on  further share buys.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：manchester@15:3.0800 | stake@13:1.3598 | his@12:0.4542。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 358. test:4097 | Sci/Tech → Business

预测置信度 0.9997；真实类概率 0.0000；前两类概率差 0.9995。
分词数 37；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Greenspan: Debt, home prices not dangerous The record level of debt carried by American households and soaring home prices do not appear to represent serious threats to the US economy, Federal Reserve Chairman Alan Greenspan said Tuesday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：economy@29:2.1601 | reserve@31:2.1474 | us@28:1.5354。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 359. test:4102 | World → Sci/Tech

预测置信度 0.9517；真实类概率 0.0333；前两类概率差 0.9184。
分词数 28；未知词比例 0.00%；特征：高置信错误>=0.9。

Ancient fungus 'revived' in lab Fungus from a deep-sea sediment core that is hundreds of thousands of years old will grow when placed in culture, scientists discover.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：lab@4:0.4764 | culture@25:0.4057 | in@24:0.3113。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 360. test:4114 | Sci/Tech → World

预测置信度 0.6454；真实类概率 0.3546；前两类概率差 0.2909。
分词数 57；未知词比例 0.00%；特征：需结合语义人工复核。

Chirac: Europe Can Do More in Science Race (AP) AP - A European laboratory that was the birthplace of the World Wide Web and home of Nobel prize-winning developments in understanding the origins of the universe celebrated its 50th birthday Tuesday. But French President Jacques Chirac warned that despite those illustrious achievements, European scientists are falling behind.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：french@42:1.7248 | president@43:1.5317 | ap@8:1.3867。
能把预测改为真实类的单词遮挡数：5。仅表示局部敏感性，不代表已证明因果原因。

## 361. test:4137 | World → Sports

预测置信度 0.9518；真实类概率 0.0471；前两类概率差 0.9047。
分词数 20；未知词比例 0.00%；特征：高置信错误>=0.9；短文本<=20词。

F1: British Grand Prix ruled out Jackie Stewart rejects Bernie Ecclestone's claims that the British Grand Prix is dead.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：prix@3:1.9636 | ruled@4:1.3726 | bernie@9:0.5319。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 362. test:4138 | Business → Sci/Tech

预测置信度 0.5707；真实类概率 0.4266；前两类概率差 0.1441。
分词数 62；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Web-based kidney match raises ethics questions A Colorado man who placed a  quot;transplant wanted quot; ad on a Massachusetts-based Internet site is expected today to receive a kidney donated by a total stranger who simply wanted to do  quot;something big. quot; The transaction marks the first time an organ transplant has been brokered by a commercial web company.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：web@0:0.3172 | web@60:0.2296 | commercial@59:0.1511。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 363. test:4148 | Sci/Tech → Business

预测置信度 0.8522；真实类概率 0.1465；前两类概率差 0.7058。
分词数 42；未知词比例 0.00%；特征：商业与科技边界。

Motorola Quarterly Earnings Rise Motorola Inc., the world's No. 2 maker of cell phones, on Tuesday said its quarterly profit\more than tripled, as sales rose 26 percent, driven in part by a host of new handset models and cost controls.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：earnings@2:0.7860 | the@6:0.7668 | quarterly@1:0.5817。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 364. test:4241 | Business → Sci/Tech

预测置信度 0.5116；真实类概率 0.3182；前两类概率差 0.1934。
分词数 49；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Alaska #39;s summer tourism pegged at 1.4 million visitors The number of summer visitors to Alaska rose from the year before, prompting the president of the Alaska Travel Industry Association to say tourism appeared to be back on track since leveling off after the 2001 terrorist attacks.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tourism@34:0.7220 | at@6:0.2376 | alaska@28:0.2275。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 365. test:4273 | Sports → World

预测置信度 0.4294；真实类概率 0.0289；前两类概率差 0.1029。
分词数 50；未知词比例 2.00%；特征：前两类接近:概率差<0.2；含HTML实体或编码痕迹。

America #39;s curse There is an all but unanswerable case for asserting that the biggest story out of the United States this week has nothing to do with the presidential election, has no connection with the flu vaccine shortage and that it does not involve a gay bishop either 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：election@31:1.4273 | presidential@30:1.2815 | gay@47:1.0623。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 366. test:4275 | Business → World

预测置信度 0.9373；真实类概率 0.0381；前两类概率差 0.8992。
分词数 52；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Erdogan Believes European Council #39;s Decision Will Be A Milestone PARIS - Turkish PM Recep Tayyip Erdogan expressed belief on Thursday that the decision that the European Council would make on December 17th (on whether and when to open negotiations with Turkey) would be a milestone for not only Turkey-(EU) relations 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：pm@13:0.9418 | turkish@12:0.7662 | turkey@41:0.7265。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 367. test:4300 | Sports → Business

预测置信度 0.7577；真实类概率 0.1786；前两类概率差 0.5791。
分词数 37；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

City Series-ly wounded With the Yanks out of the World Series, the city #39;s economy loses out on at least \$40 million, according to studies by the controller #39;s office and other city agencies.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：economy@16:4.6158 | loses@17:2.5975 | 40@22:0.3248。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 368. test:4319 | Sci/Tech → Business

预测置信度 0.9480；真实类概率 0.0382；前两类概率差 0.9098。
分词数 28；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Avis blames IT for multimillion-dollar loss The car rental company takes a major hit because of problems with IT, including high costs associated with an ERP project.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：rental@9:1.6751 | dollar@5:1.1933 | loss@6:0.6052。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 369. test:4323 | Sci/Tech → Business

预测置信度 0.7375；真实类概率 0.2618；前两类概率差 0.4757。
分词数 38；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Amazon.com net sales jump 29; Google reports \$52M in net income OCTOBER 22, 2004 (IDG NEWS SERVICE) - Amazon.com Inc. fell a penny short of analysts #39; per-share earnings expectations, while reporting net sales of \$1.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：income@11:0.6694 | jump@4:0.6431 | fell@21:0.6211。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 370. test:4359 | Business → Sci/Tech

预测置信度 0.7654；真实类概率 0.1660；前两类概率差 0.5994。
分词数 54；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Google #39;s New PC Search Tool Poses Risks NEW YORK Oct. 18, 2004 - People who use public or workplace computers for e-mail, instant messaging and Web searching have a new privacy risk to worry about: Google #39;s free new tool that indexes a PC #39;s contents for quickly locating data.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：messaging@25:0.5063 | e@22:0.4037 | instant@24:0.3961。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 371. test:4396 | World → Business

预测置信度 0.5061；真实类概率 0.0940；前两类概率差 0.1087。
分词数 24；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Revolving Door  &lt;em&gt; IN&lt;/em&gt;&lt;br&gt;   Aylwin B. Lewis,  president of Yum Brands, as chief executive of Kmart.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：brands@18:1.2724 | executive@21:1.0246 | gt@11:0.8745。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 372. test:4441 | Sci/Tech → Business

预测置信度 0.9549；真实类概率 0.0451；前两类概率差 0.9098。
分词数 34；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Approval Expected for Big Cellphone Deal Federal regulators will formally approve Cingular Wireless #39;s \$41 billion purchase of AT amp;T Wireless today, company officials briefed on the matter said over the weekend.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：amp@20:1.1900 | 39@13:1.1792 | cingular@11:0.9787。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 373. test:4451 | Sci/Tech → Business

预测置信度 0.9870；真实类概率 0.0130；前两类概率差 0.9741。
分词数 37；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Regulators Let Cingular Buy AT amp;T Wireless The \$41 billion merger between Cingular Wireless LLC and AT amp;T Wireless Services Inc. won approval from the Federal Communications Commission yesterday, according to federal sources close to 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：buy@3:1.3612 | amp@5:1.2731 | yesterday@30:0.8612。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 374. test:4481 | World → Sci/Tech

预测置信度 0.8822；真实类概率 0.0529；前两类概率差 0.8175。
分词数 38；未知词比例 0.00%；特征：需结合语义人工复核。

Hynix's 3Q Profit More Than Triples (AP) AP - South Korea's Hynix Semiconductor Inc. said Monday its third-quarter net profit more than tripled from same period last year thanks to steady global prices for memory chips.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：memory@36:2.4259 | chips@37:1.8049 | inc@14:0.4222。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 375. test:4501 | Business → Sci/Tech

预测置信度 0.7479；真实类概率 0.2519；前两类概率差 0.4960。
分词数 28；未知词比例 0.00%；特征：商业与科技边界。

Classmates agrees to \$100M buyout United Online Inc., a California-based provider of low-cost Internet subscription services, has agreed to buy Internet networking company Classmates Online Inc.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：networking@23:0.5300 | internet@22:0.4850 | online@6:0.3696。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 376. test:4508 | Business → Sci/Tech

预测置信度 0.9397；真实类概率 0.0578；前两类概率差 0.8819。
分词数 42；未知词比例 2.38%；特征：商业与科技边界；高置信错误>=0.9。

Spyware opponents win another battle The Federal Trade Commission won an important victory last week in its fight to protect consumers from spyware, the software that tracks unsuspecting Web surfers, bombards them with advertisements and sometimes even steal login information and passwords.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：web@28:0.9609 | spyware@22:0.6593 | surfers@29:0.5179。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 377. test:4520 | World → Sci/Tech

预测置信度 0.7486；真实类概率 0.1676；前两类概率差 0.5809。
分词数 41；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

Broadcaster Donates  #36;325,000 to GOP (AP) AP - One of the state's biggest broadcasters has given 13 Republican county committees  #36;325,000 worth of free air time to promote candidates on its radio and television stations throughout California.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：throughout@39:1.1449 | california@40:0.8128 | county@20:0.6472。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 378. test:4540 | Sports → World

预测置信度 0.9851；真实类概率 0.0129；前两类概率差 0.9722。
分词数 44；未知词比例 2.27%；特征：高置信错误>=0.9。

Miss Peru takes Miss World crown Twenty-year-old Miss Peru has been crowned Miss World in a southern Chinese resort town, as China looks to become the regular host of an event that would have once been deemed heretical by its Communist leaders.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：peru@10:0.9164 | old@8:0.5639 | communist@42:0.3637。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 379. test:4549 | World → Sports

预测置信度 0.9883；真实类概率 0.0116；前两类概率差 0.9767。
分词数 34；未知词比例 0.00%；特征：高置信错误>=0.9。

Australia 362-7 v India, third test - close (Reuters) Reuters - Australia were 362 for seven wickets at the close of play on the first day of their third cricket test against India on Tuesday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：cricket@28:3.0910 | third@27:1.3365 | their@26:1.2179。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 380. test:4550 | Sci/Tech → Business

预测置信度 0.6057；真实类概率 0.2498；前两类概率差 0.3559。
分词数 60；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Lockheed Profit Jumps on IT, Jet Demand &lt;p&gt;\&lt;/p&gt;&lt;p&gt; NEW YORK (Reuters) - No. 1 U.S. defense contractor Lockheed\Martin Corp. &lt;LMT.N&gt; reported a 41 percent rise in quarterly\profit on Tuesday, beating Wall Street forecasts, as demand\soared for its combat aircraft and information technology\services.&lt;/p&gt;

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：street@44:1.2877 | forecasts@45:1.1670 | reuters@18:1.0988。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 381. test:4564 | Sci/Tech → Business

预测置信度 0.9557；真实类概率 0.0430；前两类概率差 0.9127。
分词数 42；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

E.U. Regulators Approve Oracle's PeopleSoft Bid European Union antitrust regulators on Tuesday cleared Oracle Corp.'s hostile \$7.7 billion bid for rival business software maker PeopleSoft Inc., removing one of the last major hurdles to the contested takeover proposal.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：union@9:2.2686 | regulators@11:1.6298 | bid@7:1.4351。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 382. test:4571 | Business → Sci/Tech

预测置信度 0.9988；真实类概率 0.0012；前两类概率差 0.9975。
分词数 38；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Microsoft Readies Next Business IM Server A little over a year after introducing the first version of Office Live Communications Server, Microsoft says it plans to release the next version of its enterprise instant messaging software, in December.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：server@20:0.5958 | instant@33:0.4603 | communications@19:0.3787。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 383. test:4580 | Business → Sci/Tech

预测置信度 0.9948；真实类概率 0.0050；前两类概率差 0.9898。
分词数 42；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

FaceTime, IMlogic Back Live Communications Server 2005 Hard on the heels of Microsoft announcing that it #39;s taken Live Communications Server 2005 gold, instant messaging management software vendors IMlogic and FaceTime on Tuesday both touted their support for the communication product.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：messaging@25:0.8353 | instant@24:0.6228 | management@26:0.3296。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 384. test:4584 | Sci/Tech → Business

预测置信度 0.6387；真实类概率 0.3303；前两类概率差 0.3084。
分词数 25；未知词比例 0.00%；特征：商业与科技边界。

Broadcom taps ex-Philips executive as CEO Scott McGregor, former head of Royal Philips Electronics' semiconductor division, will replace Alan Ross, who plans to retire.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：executive@4:1.5996 | mcgregor@8:0.7360 | former@9:0.6898。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 385. test:4588 | Sci/Tech → Business

预测置信度 0.5234；真实类概率 0.4753；前两类概率差 0.0481。
分词数 41；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

IBM Unveils Security Intel Service, Notes Big Jump In Attacks IBM has launched a new intelligence service to give enterprises a monthly report showing the big picture of security attacks and other business threats, the Armonk, NY-based giant said Tuesday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ny@36:2.6288 | giant@38:2.5111 | based@37:1.5807。
能把预测改为真实类的单词遮挡数：18。仅表示局部敏感性，不代表已证明因果原因。

## 386. test:4591 | Business → Sci/Tech

预测置信度 0.7185；真实类概率 0.2810；前两类概率差 0.4375。
分词数 40；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Cingular Closes  #36;41 Bln ATT Wireless Deal (Reuters) Reuters - Cingular Wireless on Tuesday closed\its  #36;41 billion cash purchase of AT T Wireless Services Inc.\, creating the biggest U.S. mobile service with more\than 46 million customers.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：reuters@9:0.8828 | t@23:0.6639 | at@22:0.5082。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 387. test:4648 | Sci/Tech → World

预测置信度 0.8126；真实类概率 0.1107；前两类概率差 0.7019。
分词数 36；未知词比例 0.00%；特征：需结合语义人工复核。

Singapore Telecom ties up with Malaysia's TIME dotcom (AFP) AFP - Singapore Telecommunications (SingTel) said it has entered into an agreement with Malaysia's TIME dotCom to link their corporate customers through private leased line circuits.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：afp@10:2.0618 | singapore@11:1.7054 | afp@9:1.5997。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 388. test:4650 | World → Business

预测置信度 0.6612；真实类概率 0.3173；前两类概率差 0.3439。
分词数 50；未知词比例 0.00%；特征：世界与商业边界。

BHP Billiton, Alcoa sell Integris Metals for 359 million pounds (AFP) AFP - Anglo-Australian mining giant BHP Billiton and Alcoa, the world's largest aluminium producer, have agreed to sell their metal services joint venture Integris Metals for 660 million dollars (359 million pounds) including debt, a joint statement said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：venture@34:1.5277 | joint@33:1.2598 | million@8:0.8201。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 389. test:4677 | World → Sci/Tech

预测置信度 0.9905；真实类概率 0.0041；前两类概率差 0.9851。
分词数 47；未知词比例 2.13%；特征：高置信错误>=0.9。

Black Market in British Treasure Sold on EBay (Reuters) Reuters - Pieces of Britain's past, including a\second-century silver ring and a 500-year-old Tudor trade\weight, are among artifacts being peddled daily on the Internet\to the alarm of experts at the British Museum.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ebay@7:1.4622 | internet@37:0.8219 | experts@42:0.2791。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 390. test:4681 | Business → Sci/Tech

预测置信度 0.5344；真实类概率 0.4526；前两类概率差 0.0817。
分词数 38；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

Report finds handheld device market in continued decline The worldwide market for handheld devices saw its third successive quarter of year-over-year decline in the third quarter of 2004, according to a new report released by IDC.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：devices@13:0.3133 | finds@1:0.2988 | idc@37:0.2124。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 391. test:4684 | Business → World

预测置信度 0.9127；真实类概率 0.0334；前两类概率差 0.8625。
分词数 33；未知词比例 3.03%；特征：世界与商业边界；高置信错误>=0.9。

Faces From The 1929 Crash NEW YORK - The people who will forever be associated with the Great Crash of 1929 were all white, male and wealthy, but their occupations and ethics varied considerably.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：york@6:0.8541 | crash@17:0.8105 | crash@4:0.7369。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 392. test:4687 | Business → Sci/Tech

预测置信度 0.8708；真实类概率 0.1239；前两类概率差 0.7469。
分词数 17；未知词比例 0.00%；特征：商业与科技边界；短文本<=20词。

Will Tellabs Push Its Luck? Perhaps the optical network supplier should call off its merger with AFC.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：network@8:1.7629 | optical@7:1.4279 | its@13:0.2214。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 393. test:4689 | Business → Sci/Tech

预测置信度 0.9776；真实类概率 0.0221；前两类概率差 0.9555。
分词数 37；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Yahoo Debuts Mobile Search SAN FRANCISCO -- Yahoo (Quote, Chart) expanded its search empire to the mobile arena with the launch of some additional services. The company was one of the original content providers for mobile devices running 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：yahoo@6:0.6831 | mobile@15:0.3657 | content@31:0.3374。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 394. test:4691 | Business → Sci/Tech

预测置信度 0.9714；真实类概率 0.0280；前两类概率差 0.9434。
分词数 41；未知词比例 2.44%；特征：商业与科技边界；高置信错误>=0.9。

Lexmark Loss Good for Consumers Lexmark's loss in court on Tuesday may mean that consumer electronics companies won't try to use the Digital Millenium Copyright Act as an all-purpose competition shield anymore, consumer advocates say. By Katie Dean.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：act@27:1.1038 | copyright@26:0.9784 | digital@24:0.3667。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 395. test:4720 | World → Sci/Tech

预测置信度 0.9756；真实类概率 0.0024；前两类概率差 0.9538。
分词数 36；未知词比例 0.00%；特征：高置信错误>=0.9。

Stability Control Systems Can Save Lives (AP) AP - Stability control systems could save up to 7,000 lives each year if they were standard equipment on all vehicles, according to a study by the insurance industry.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：stability@8:0.5996 | systems@10:0.4891 | study@31:0.3274。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 396. test:4764 | World → Business

预测置信度 0.5947；真实类概率 0.0964；前两类概率差 0.3913。
分词数 36；未知词比例 2.78%；特征：世界与商业边界；含HTML实体或编码痕迹。

Remark on Homosexuality Delays Seating of European Panel The European Union #39;s normally yawn-inducing institutions raised eyebrows on Wednesday when a spat over comments about homosexuality made by an Italian bureaucrat led to the 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@11:3.2469 | institutions@16:2.0549 | union@10:1.1496。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 397. test:4766 | Business → Sci/Tech

预测置信度 0.5265；真实类概率 0.2918；前两类概率差 0.2348。
分词数 55；未知词比例 10.91%；特征：商业与科技边界；未知词比例>=10%；含HTML实体或编码痕迹。

Ryanair agrees to repay 4M in an escrow account for the Walloon &lt;b&gt;...&lt;/b&gt; vueling writes  quot;Ryanair confirmed it had written to the Walloon authorities and agreed to repay 4M in an escrow account until Ryanairs appeal is heard and the European Courts make a definitive decision on this matter.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：writes@19:0.7149 | lt@15:0.1757 | courts@47:0.1590。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 398. test:4773 | Business → Sci/Tech

预测置信度 0.8458；真实类概率 0.1538；前两类概率差 0.6920。
分词数 46；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

AOL Files Lawsuit Against IM  #39;Spim #39; America Online Inc. said Thursday it had filed a federal lawsuit accusing numerous unnamed defendants of violating federal and state laws by sending bulk messages known as  quot;spim quot; to instant message accounts and Internet chat rooms.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：internet@43:0.9505 | instant@39:0.7437 | message@40:0.6486。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 399. test:4783 | Business → Sci/Tech

预测置信度 0.9938；真实类概率 0.0061；前两类概率差 0.9877。
分词数 45；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

AOL, E-Mail Companies Sue Spammers The nation #39;s largest e-mail providers today filed a new round of lawsuits against Internet spammers allegedly responsible for shoveling millions of junk e-mail messages into computer users #39; in-boxes and their instant messaging screens.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：internet@22:1.1274 | spammers@23:0.6940 | instant@42:0.5270。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 400. test:4789 | Sci/Tech → Business

预测置信度 0.7896；真实类概率 0.2045；前两类概率差 0.5851。
分词数 47；未知词比例 0.00%；特征：商业与科技边界。

Gateway Reports Smaller Quarterly Loss Gateway Inc. reported a narrowed net loss in the first quarter as it continues to restructure its operations and integrate its acquisition of eMachines. Still, the personal computer and electronics company posted a tiny operating profit -- its first in nearly three years.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：profit@40:1.0819 | loss@4:0.5164 | a@8:0.3948。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 401. test:4815 | Sci/Tech → Sports

预测置信度 0.9345；真实类概率 0.0581；前两类概率差 0.8764。
分词数 28；未知词比例 0.00%；特征：高置信错误>=0.9。

Blame player, not game It was like nothing youd ever exercised your thumbs to before. You could do whatever you wanted, whenever you wanted. The game seemed endless.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：player@1:2.8143 | blame@0:1.9591 | not@2:1.5828。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 402. test:4824 | Business → Sports

预测置信度 0.9164；真实类概率 0.0538；前两类概率差 0.8625。
分词数 35；未知词比例 2.86%；特征：高置信错误>=0.9；含HTML实体或编码痕迹。

Sign off, then sign in  G. Michael Caggiano Jr. lies awake at night thinking about bank signs. He ponders them during breakfast, while brushing his teeth, and  quot;constantly quot; during the day, he says.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：sign@3:1.1616 | he@17:0.9116 | then@2:0.8659。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 403. test:4825 | Sports → Sci/Tech

预测置信度 0.5637；真实类概率 0.3448；前两类概率差 0.2190。
分词数 41；未知词比例 0.00%；特征：需结合语义人工复核。

Not quite high Tech Virginia Tech just couldn't seem to get going. There were turnovers. There were botched plays. There were missed opportunities. Then, in the last 5 1/2 minutes, Bryan Randall and the Hokies turned it all around.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：t@8:1.0446 | tech@5:0.8338 | couldn@7:0.6490。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 404. test:4854 | Sports → Sci/Tech

预测置信度 0.5755；真实类概率 0.0198；前两类概率差 0.2544。
分词数 41；未知词比例 0.00%；特征：需结合语义人工复核。

Times to Scrap Broadsheet Edition The Times is to scrap its broadsheet edition and go tabloid from Monday, it was confirmed today. The decision was made after a trial run of the compact edition proved a success, said editor Robert Thomson.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：compact@32:1.4783 | robert@39:0.7256 | editor@38:0.6814。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 405. test:4862 | Business → Sci/Tech

预测置信度 0.8804；真实类概率 0.1183；前两类概率差 0.7621。
分词数 15；未知词比例 6.67%；特征：商业与科技边界；短文本<=20词。

AOL's Viral Marketing America Online will now provide gratis antivirus protection to its subscribers.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：antivirus@10:0.6017 | online@5:0.4788 | provide@8:0.1909。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 406. test:4880 | World → Business

预测置信度 0.6886；真实类概率 0.2366；前两类概率差 0.4520。
分词数 27；未知词比例 0.00%；特征：世界与商业边界；含HTML实体或编码痕迹。

Danish group #39;s gift criticized A Danish group has caused controversy in Colombia by publicly donating money to the country #39;s largest Marxist guerrilla organization.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@21:1.4419 | 39@2:1.3490 | money@17:0.9696。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 407. test:4900 | World → Sports

预测置信度 0.5810；真实类概率 0.3889；前两类概率差 0.1922。
分词数 34；未知词比例 5.88%；特征：前两类接近:概率差<0.2。

THE UNFOLDING UNIFORM Pakistan is inherently unstable. Dealing with them is like playing with matches in a forest. - Larry Pressler. That statement from Larry Pressler, made during his recent visit to India, coincided with 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：playing@12:0.6495 | his@27:0.5608 | larry@18:0.4747。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 408. test:4902 | Business → Sci/Tech

预测置信度 0.6398；真实类概率 0.0594；前两类概率差 0.3404。
分词数 30；未知词比例 6.67%；特征：商业与科技边界。

FasTrak Toll Bridge Discounts End Monday About 70,000 motorists signed up for FasTrak, the electronic toll collection system, since July 1, when tolls went up from \$2 to \$3.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：collection@17:1.3075 | system@18:0.7970 | electronic@15:0.5302。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 409. test:4921 | Sci/Tech → World

预测置信度 0.5778；真实类概率 0.3105；前两类概率差 0.2673。
分词数 25；未知词比例 8.00%；特征：需结合语义人工复核。

The Great Vegetarian Scam Ive written before about my struggle to remain a vegetarian on Tuesday - when I abjure meat for religious reasons -hile travelling.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：religious@21:1.5314 | reasons@22:0.9961 | about@7:0.2289。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 410. test:4929 | Business → Sports

预测置信度 0.7487；真实类概率 0.1740；前两类概率差 0.5747。
分词数 44；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

Key Australia-US FTA deadline passes A key deadline to bring Australia #39;s Free Trade Agreement with the United States into force has expired. But the Australian Government is still confident the deal will come into effect next year, as Louise Willis reports.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：willis@42:2.3627 | 39@12:0.9152 | louise@41:0.7967。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 411. test:4940 | Business → Sci/Tech

预测置信度 0.9449；真实类概率 0.0261；前两类概率差 0.9188。
分词数 36；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Med school move delayed to 2007 The MSU College of Human Medicine won #39;t be relocated to Grand Rapids until at least 2007, and could cost only half as much as university officials originally estimated.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：human@10:2.1279 | medicine@11:1.3696 | grand@18:0.1973。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 412. test:4952 | Business → World

预测置信度 0.7251；真实类概率 0.2617；前两类概率差 0.4634。
分词数 37；未知词比例 2.70%；特征：世界与商业边界。

Singapore govt extends third-party war risk insurance SINGAPORE : The government is extending third-party war risk insurance cover to the Civil Aviation Authority of Singapore and SATS Security Services, a unit of the Singapore Airlines group.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：government@10:0.7757 | security@28:0.5748 | party@4:0.3567。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 413. test:4999 | Business → Sci/Tech

预测置信度 0.5856；真实类概率 0.3982；前两类概率差 0.1874。
分词数 46；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Profit Plunges at International Game Tech International Game Technology, the world #39;s biggest maker of slot machines, Tuesday said said profit for its latest quarter fell 50 percent from a year ago due to a charge for early redemption of debt and a tax adjustment.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tech@5:1.8059 | game@7:1.3882 | technology@8:0.5229。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 414. test:5006 | Sci/Tech → Business

预测置信度 0.5878；真实类概率 0.4120；前两类概率差 0.1758。
分词数 34；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

PalmOne to play with Windows Mobile? Rumors of Treo #39;s using a Microsoft operating system have been circulating for more than three years. Now an investment bank reports that PalmOne will use a 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@9:1.8981 | bank@27:1.8642 | investment@26:1.3778。
能把预测改为真实类的单词遮挡数：10。仅表示局部敏感性，不代表已证明因果原因。

## 415. test:5020 | Business → Sci/Tech

预测置信度 0.5266；真实类概率 0.4690；前两类概率差 0.0576。
分词数 42；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

AOL Is Said to Plan 700 Layoffs America Online, the country #39;s leading Internet service, is preparing to lay off as many as 700 of its 13,000 employees in the United States, according to an executive knowledgeable about its plans.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：internet@14:0.5846 | layoffs@6:0.2173 | plan@4:0.0236。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 416. test:5045 | Sci/Tech → Sports

预测置信度 0.5310；真实类概率 0.1148；前两类概率差 0.2538。
分词数 34；未知词比例 2.94%；特征：含HTML实体或编码痕迹。

Gateway Can Party Like It #39;s 1999 Those were heady days, they were, back in 1999. The bull market was still roaring. We hadn #39;t yet heard of hanging or dimpled chads.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@5:1.4631 | 39@25:0.5956 | we@23:0.5775。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 417. test:5067 | Business → World

预测置信度 0.9247；真实类概率 0.0468；前两类概率差 0.8779。
分词数 33；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

Quick end to US election crucial US President George W. Bush is on the verge of a re-election victory, but Democratic challenger John Kerry is not conceding defeat, at least not now.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：kerry@24:1.4945 | john@23:1.4778 | defeat@28:0.3713。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 418. test:5107 | World → Business

预测置信度 0.5935；真实类概率 0.3435；前两类概率差 0.2501。
分词数 44；未知词比例 0.00%；特征：世界与商业边界；含HTML实体或编码痕迹。

New EU Executive Chief Announces Revamped Team The incoming head of the European Union #39;s executive body has announced changes to his group of commissioners and says he is ready to go to the European Parliament to seek its approval of his team.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@14:2.1206 | union@13:1.2427 | executive@16:1.0274。
能把预测改为真实类的单词遮挡数：8。仅表示局部敏感性，不代表已证明因果原因。

## 419. test:5115 | Sci/Tech → World

预测置信度 0.3476；真实类概率 0.3203；前两类概率差 0.0156。
分词数 43；未知词比例 0.00%；特征：前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Calif. Voters Back  #36;3 Billion Stem Cell Measure (Reuters) Reuters - A controversial California ballot\measure that would fund a decade of stem cell research with  #36;3\billion in state money was headed for a resounding victory on\Wednesday, initial returns showed.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：voters@1:1.9312 | calif@0:1.6651 | back@2:0.8790。
能把预测改为真实类的单词遮挡数：25。仅表示局部敏感性，不代表已证明因果原因。

## 420. test:5127 | Sci/Tech → World

预测置信度 0.9723；真实类概率 0.0162；前两类概率差 0.9562。
分词数 38；未知词比例 0.00%；特征：高置信错误>=0.9。

Another homicide in Holland  It is a sad day.      In what seems to be another politically inspired homicide in Holland, Dutch filmmaker, and controversial columnist Theo van Gogh was brutally murdered in the streets of Amsterdam this morning.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：filmmaker@21:2.6074 | dutch@20:1.8997 | controversial@23:0.9224。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 421. test:5128 | World → Sports

预测置信度 0.9996；真实类概率 0.0004；前两类概率差 0.9993。
分词数 27；未知词比例 7.41%；特征：高置信错误>=0.9。

Argentina Basketball Coach Magnano Quits Ruben Magnano, who coached Argentina to the Olympic basketball gold medal in Athens, resigned Thursday to accept a coaching job in Italy.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：basketball@1:1.8266 | coach@2:1.6630 | basketball@13:1.4204。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 422. test:5129 | Business → Sci/Tech

预测置信度 0.9955；真实类概率 0.0043；前两类概率差 0.9912。
分词数 134；未知词比例 2.24%；特征：商业与科技边界；高置信错误>=0.9。

Product Previews palmOneUpgrades Treo With Faster Chip, Better Display\With more than 600,000 units shipped, the Treo 600 is one of the big smartphone success stories. Last week, palmOne introduced the follow-on Treo 650 with a higher resolution 320-by-320-pixel TFT screen, which the company claims increases the visible area of the display and makes pictures and documents much clearer. The 650 also carries a removable battery; 32MB of flash memory, and a faster 312MHz, Intel XScale processor. Improved multimedia features include a built-in MP3 player, a digital camera with improved low-light capabilities, as well as video capture and playback functionality. Products are expected to ship by years end from some carriers who will add their own services, and will be priced at about \$499.\ Treo 650, palmOne

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：camera@93:0.5106 | digital@92:0.5069 | mp3@89:0.4380。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 423. test:5134 | Sci/Tech → World

预测置信度 0.6489；真实类概率 0.0695；前两类概率差 0.4074。
分词数 23；未知词比例 0.00%；特征：需结合语义人工复核。

10 O'Clock News goes interactive BBC One's 10 O'Clock News is launching the first interactive news television bulletin on Tuesday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：bbc@6:1.7127 | s@8:0.6459 | interactive@5:0.3265。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 424. test:5142 | World → Business

预测置信度 0.4877；真实类概率 0.4713；前两类概率差 0.0164。
分词数 50；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

Japan Airlines Sees Profit on Int'l Travel (AP) AP - Japan Airlines Corp. said Friday that it returned to profitability in first half of the fiscal year as international travel picked up from a decline a year ago caused by the war in Iraq and the SARS outbreak in Asia.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：airlines@1:2.1463 | profit@3:2.0727 | airlines@11:1.6856。
能把预测改为真实类的单词遮挡数：22。仅表示局部敏感性，不代表已证明因果原因。

## 425. test:5145 | Sci/Tech → World

预测置信度 0.9750；真实类概率 0.0118；前两类概率差 0.9619。
分词数 32；未知词比例 0.00%；特征：高置信错误>=0.9。

Serial HIV Assault Verdict Expected Mon. (AP) AP - A verdict will be announced Monday in the trial of a man charged with intentionally exposing 17 women to HIV, a county judge said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：hiv@1:2.5215 | assault@2:1.7659 | ap@7:1.7351。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 426. test:5151 | Sci/Tech → Business

预测置信度 0.4142；真实类概率 0.2342；前两类概率差 0.0920。
分词数 55；未知词比例 3.64%；特征：商业与科技边界；前两类接近:概率差<0.2。

Contradiction in Terms : How to make beer It's been around for thousands of years. It has been worshiped, reviled, banned, and made the cornerstone of economies. It has helped us celebrate, weep, relax, and get laid. And now we're going to make some. A pint, a glass, an ale, a lager, a beer.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：beer@6:0.6192 | us@30:0.5633 | to@4:0.4334。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 427. test:5152 | Sci/Tech → World

预测置信度 0.8772；真实类概率 0.0895；前两类概率差 0.7877。
分词数 45；未知词比例 2.22%；特征：需结合语义人工复核。

Hope Fades for Saving 2 Boys Stuck in Mexico Cave (Reuters) Reuters - Hopes of rescuing two small boys\trapped for five days in a jungle cave faded fast on Friday\after contact was lost with the brothers and as the cavern\flooded in overnight rains.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：friday@29:1.0226 | was@32:0.8166 | after@30:0.6745。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 428. test:5164 | World → Sci/Tech

预测置信度 0.6989；真实类概率 0.2700；前两类概率差 0.4289。
分词数 49；未知词比例 4.08%；特征：需结合语义人工复核。

Atomic Power Station Halted in Russia, No Radiation  MOSCOW (Reuters) - One reactor at a Russian nuclear power  station was closed down after a malfunction, but there was no  leak of radiation at the site near the city of Saratov on the  Volga river, Russian news agencies reported on Friday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：radiation@7:1.2627 | radiation@30:0.8326 | one@10:0.4586。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 429. test:5265 | Sci/Tech → Business

预测置信度 0.8680；真实类概率 0.1313；前两类概率差 0.7367。
分词数 32；未知词比例 3.12%；特征：商业与科技边界。

Travelocity Says Speed Is the Ticket For Growth Sam Gilliand, the chief executive of Travelocity, talks about the online travel industry, the Cendant-Orbitz merger and the woes of the airline industry.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：merger@24:1.1322 | cendant@22:0.9312 | the@17:0.8628。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 430. test:5285 | Business → Sci/Tech

预测置信度 0.8088；真实类概率 0.1685；前两类概率差 0.6402。
分词数 34；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Study raises stent doubts Heart patients aren #39;t more likely to live long term after getting the artery-opening tubes called stents, according to a study released yesterday by researchers at Duke University.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：researchers@30:1.1684 | duke@32:0.8309 | university@33:0.5527。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 431. test:5291 | World → Sci/Tech

预测置信度 0.7160；真实类概率 0.2771；前两类概率差 0.4389。
分词数 43；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

Website posts video of suicide attack against British troops A video purportedly showing a suicide attack against British troops last week was posted on an Islamic website. Soldiers from Britain #39;s Black Watch regiment were manning a vehicle checkpoint south of Baghdad 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：website@0:2.1987 | posts@1:1.6096 | video@2:1.3260。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 432. test:5293 | Sci/Tech → Business

预测置信度 0.7908；真实类概率 0.2072；前两类概率差 0.5836。
分词数 36；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Flat-screen TV But the booming demand isn #39;t proving profitable for the companies that make the high-resolution video panels. For electronics retailers, it will be the holiday season of the flat-screen TV.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：retailers@24:1.3979 | demand@6:0.8928 | 39@8:0.7346。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 433. test:5295 | Business → World

预测置信度 0.6567；真实类概率 0.3363；前两类概率差 0.3203。
分词数 39；未知词比例 0.00%；特征：世界与商业边界；含HTML实体或编码痕迹。

PM welcomes EU partnership Prime Minister Manmohan Singh arrived in the Hague last night to participate in the India-European summit.  quot;In recognition of Indias growing stature and influence, the EU has proposed a strategic partnership with India.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：welcomes@1:0.8723 | prime@4:0.6810 | european@19:0.6484。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 434. test:5305 | Sci/Tech → Business

预测置信度 0.8206；真实类概率 0.1788；前两类概率差 0.6418。
分词数 30；未知词比例 0.00%；特征：商业与科技边界。

Microsoft settles antitrust cases with Novell, CCIA Microsoft Corp on Monday announced antitrust settlements with Novell Inc. and the Computer and Communications Industry Association (CCIA), ending years of legal wrangling.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：settlements@13:1.6536 | antitrust@12:1.4420 | monday@10:0.8666。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 435. test:5308 | Business → Sci/Tech

预测置信度 0.7034；真实类概率 0.2292；前两类概率差 0.4742。
分词数 30；未知词比例 0.00%；特征：商业与科技边界。

Alternative Energy: Ready or not? Even with a boost from higher oil prices and growing concern about global warming, the payoff on most alternative energy technologies seems a ways off.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：warming@18:2.5924 | global@17:0.4249 | alternative@23:0.1641。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 436. test:5312 | Sci/Tech → Business

预测置信度 0.6007；真实类概率 0.3959；前两类概率差 0.2049。
分词数 18；未知词比例 0.00%；特征：商业与科技边界；短文本<=20词。

Microsoft Makes Another Antitrust Deal Software giant settles with Novell and the CCIA, ending years of legal wrangling.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：deal@4:1.2737 | antitrust@3:1.1876 | giant@6:0.6901。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 437. test:5316 | Business → Sci/Tech

预测置信度 0.5667；真实类概率 0.4331；前两类概率差 0.1336。
分词数 31；未知词比例 3.23%；特征：商业与科技边界；前两类接近:概率差<0.2。

Phoney eBay bidders fined EIGHT eBay sellers were ordered to pay nearly \$US90,000 (\$118,000) in restitution and fines after admitting they had bid on products to inflate the prices.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：they@22:0.2728 | fined@3:0.2462 | on@25:0.1930。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 438. test:5321 | Business → Sci/Tech

预测置信度 0.5324；真实类概率 0.4666；前两类概率差 0.0658。
分词数 35；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

Microsoft Settles Novell Antitrust Suit (Reuters) Reuters - Microsoft Corp.  said\on Monday it agreed to settle antitrust lawsuits with Novell\Inc.  and an industry trade group, marking the end of a\decade-long antitrust battle.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：reuters@6:1.2213 | reuters@5:0.5635 | microsoft@0:0.2851。
能把预测改为真实类的单词遮挡数：7。仅表示局部敏感性，不代表已证明因果原因。

## 439. test:5322 | Sci/Tech → World

预测置信度 0.5389；真实类概率 0.4553；前两类概率差 0.0836。
分词数 20；未知词比例 5.00%；特征：前两类接近:概率差<0.2；短文本<=20词。

Cellphones outstrip landlines in India (AFP) AFP - Mobile phone users have outstripped traditional landline connections in India, the government announced.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：afp@5:1.7776 | afp@6:1.4537 | india@4:1.1643。
能把预测改为真实类的单词遮挡数：8。仅表示局部敏感性，不代表已证明因果原因。

## 440. test:5324 | Sci/Tech → Business

预测置信度 0.5532；真实类概率 0.2923；前两类概率差 0.2610。
分词数 60；未知词比例 1.67%；特征：商业与科技边界。

Conversion Rates Between PPC (Paid) and Organic (Free) Results Conversion Rates Between PPC (Paid) and Organic (Free) Results\\In a thread over at Cre8asite Forums named Organic vs Paid traffic ROI?, there is a discussion going on about the different conversion rates and ROI seen between the pay per click traffic (paid traffic) and organic traffic (free traffic). I have ...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：vs@27:0.5202 | paid@28:0.4169 | pay@47:0.4078。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 441. test:5325 | Sci/Tech → Business

预测置信度 0.7444；真实类概率 0.2554；前两类概率差 0.4890。
分词数 43；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

IBM #39;s eServer Blue Gene For Sale IBM #39;s five-year, \$100 million Blue Gene project on Monday bore commercial fruit as the Armonk, NY-based computer maker announced it was offering the supercomputer to anyone who has at least \$1.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ny@26:1.5730 | 39@9:0.9314 | maker@29:0.6228。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 442. test:5337 | World → Sci/Tech

预测置信度 0.6406；真实类概率 0.1023；前两类概率差 0.3836。
分词数 35；未知词比例 11.43%；特征：未知词比例>=10%。

Colombia Accuses Cos. of Illegal Imports The Colombian government has filed a lawsuit accusing Pernod Ricard SA, Diageo PLC and Seagram Export Sales Co. of illegally importing spirits via Colombian companies that launder drug money.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：via@28:3.4880 | sales@22:0.7259 | companies@30:0.7206。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 443. test:5339 | Sci/Tech → World

预测置信度 0.6023；真实类概率 0.3954；前两类概率差 0.2070。
分词数 37；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

Postal Service to Use Motorola Devices (AP) AP - Motorola Israel Ltd. said Monday it will provide the U.S. Postal Service with new hand-held scanning devices under a three-year deal worth about  #36;300 million.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：israel@9:2.5174 | ap@6:2.2997 | ap@7:1.1995。
能把预测改为真实类的单词遮挡数：6。仅表示局部敏感性，不代表已证明因果原因。

## 444. test:5353 | Business → World

预测置信度 0.6008；真实类概率 0.3643；前两类概率差 0.2365。
分词数 42；未知词比例 0.00%；特征：世界与商业边界。

German Finance Professionals Grow Sharply (AP) AP - German finance professionals grew sharply more pessimistic about the country's economic growth outlook, fearing that the euro's record highs against the U.S. dollar will weigh on exports, a monthly survey showed Tuesday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ap@6:3.5243 | ap@5:2.7247 | professionals@2:0.7234。
能把预测改为真实类的单词遮挡数：5。仅表示局部敏感性，不代表已证明因果原因。

## 445. test:5376 | Sci/Tech → Sports

预测置信度 0.4416；真实类概率 0.0346；前两类概率差 0.0767。
分词数 40；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Supreme Court Asked To Hear File-Sharing Arguments The file-sharing legal battle has moved to the Supreme Court, with a group composed of labor unions, sports leagues and state attorneys general asking for a hearing on a claim brought 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：sports@26:5.5977 | unions@25:1.6706 | labor@24:0.9619。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 446. test:5379 | World → Business

预测置信度 0.9278；真实类概率 0.0532；前两类概率差 0.8746。
分词数 42；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Cocoa prices down but Ivorian exports still blocked World cocoa prices were down on Tuesday but off the day #39;s lows as exports remained on hold after mob violence and military clashes in Ivory Coast, the key global supplier, traders said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：prices@10:1.6016 | cocoa@9:1.2222 | and@30:1.2195。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 447. test:5384 | World → Sci/Tech

预测置信度 0.3843；真实类概率 0.2674；前两类概率差 0.1169。
分词数 33；未知词比例 12.12%；特征：前两类接近:概率差<0.2；未知词比例>=10%；含HTML实体或编码痕迹。

The Bag of Aeolus  quot;Aeolus was keeper of the winds. He gave a bag of evil winds to Odysseus, instructing him to keep it closed while a good breeze wafted him home.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：of@15:0.5284 | evil@16:0.3075 | to@18:0.2262。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 448. test:5402 | Sci/Tech → World

预测置信度 0.8571；真实类概率 0.1402；前两类概率差 0.7169。
分词数 25；未知词比例 0.00%；特征：需结合语义人工复核。

Fusion reactor decision must wait Six nations planning to build the world's biggest nuclear fusion reactor fail to agree where to site the facility.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：nuclear@14:0.9568 | six@5:0.6366 | nations@6:0.5683。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 449. test:5410 | Sci/Tech → Business

预测置信度 0.9467；真实类概率 0.0527；前两类概率差 0.8940。
分词数 24；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

PeopleSoft revises third-quarter profit Oracle target adds \$2.6 million to bottom line after tax adjustment related to ex-CEO's severance package.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tax@15:1.2571 | profit@4:1.2310 | 6@9:1.0346。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 450. test:5431 | Business → Sci/Tech

预测置信度 0.8294；真实类概率 0.1704；前两类概率差 0.6590。
分词数 20；未知词比例 0.00%；特征：商业与科技边界；短文本<=20词。

Vodafone begins 3G service Vodafone launches its third-generation services for mobile phones, offering video calls, music downloads and games.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：music@16:0.2552 | mobile@11:0.2482 | phones@12:0.2307。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 451. test:5444 | World → Business

预测置信度 0.5110；真实类概率 0.4834；前两类概率差 0.0277。
分词数 59；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

India will never become an international liability: Manmohan Singh &lt;b&gt;...&lt;/b&gt; India News  gt; The Hague: The Indian Prime Minister, Dr Manmohan Singh, has said that despite three changes in government in the past 14 years since the economic reforms were introduced in the country, there has been no roll back in the reforms programme.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：economic@42:1.5018 | b@10:1.0301 | b@13:0.9301。
能把预测改为真实类的单词遮挡数：26。仅表示局部敏感性，不代表已证明因果原因。

## 452. test:5467 | Sports → Sci/Tech

预测置信度 0.9030；真实类概率 0.0826；前两类概率差 0.8204。
分词数 30；未知词比例 6.67%；特征：高置信错误>=0.9。

Andreas Herzog Retires From Pro Soccer (AP) AP - Los Angeles Galaxy midfielder Andreas Herzog, who played for Austria in the 1990 and 1998 World Cups, retired from professional soccer Wednesday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：andreas@12:3.3674 | midfielder@11:0.7132 | galaxy@10:0.5102。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 453. test:5479 | Business → Sci/Tech

预测置信度 0.9678；真实类概率 0.0321；前两类概率差 0.9357。
分词数 48；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Halo 2 scores record sales of \$125 million in first 24 hours Halo 2 broke entertainment retail records in its first 24 hours. Microsoft Game Studios said that the video game sold through 2.4 million stores in the US and Canada raking in \$125 million in sales.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：halo@0:0.2612 | game@24:0.2522 | game@30:0.2463。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 454. test:5532 | Business → Sci/Tech

预测置信度 0.9939；真实类概率 0.0060；前两类概率差 0.9880。
分词数 23；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Prized Fossil Just a Rock? With positive and negative results, it remains to be seen what type of Fossil this company really is.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：fossil@1:1.3255 | fossil@18:0.6125 | prized@0:0.5700。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 455. test:5537 | Sci/Tech → World

预测置信度 0.7421；真实类概率 0.2274；前两类概率差 0.5148。
分词数 47；未知词比例 2.13%；特征：含HTML实体或编码痕迹。

Hit TV series 24 goes from small screen to smaller screen (AFP) AFP - The hit US television show  quot;24 quot; is going from the small screen to the smaller after 20th Century Fox and Vodaphone struck a groundbreaking deal to distribute the drama on mobile telephones.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：afp@11:1.8167 | afp@12:1.7331 | small@6:0.3651。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 456. test:5559 | Business → Sci/Tech

预测置信度 0.6829；真实类概率 0.2771；前两类概率差 0.4057。
分词数 46；未知词比例 2.17%；特征：商业与科技边界；含HTML实体或编码痕迹。

Intel dauphin Otellini becomes king Intel #39;s board has given the go ahead for the long anticipated shift in power from current CEO Craig Barrett to current President Paul Otellini Come May 18, Otellini will take over the chipmaker and become its fifth ever CEO.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：becomes@3:0.9159 | intel@5:0.8438 | intel@0:0.1667。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 457. test:5592 | Business → World

预测置信度 0.6641；真实类概率 0.3345；前两类概率差 0.3296。
分词数 41；未知词比例 0.00%；特征：世界与商业边界。

France joins Germany, Japan in economic slide (AFP) AFP - The French economy hit a rough patch in the third quarter, throwing the government's full-year growth target into question amid signs of an economic slowdown in the 12-nation eurozone.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：afp@7:2.0529 | afp@8:1.9584 | germany@2:1.2735。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 458. test:5597 | World → Sci/Tech

预测置信度 0.5706；真实类概率 0.1495；前两类概率差 0.2908。
分词数 41；未知词比例 0.00%；特征：需结合语义人工复核。

BSkyB sees profits rise after strong subscriber growth (AFP) AFP - British satellite broadcaster BSkyB said profit rose by 16 percent in the first quarter as the group enjoyed strong subscriber growth in the run-up to the key Christmas trading period.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：satellite@11:0.9427 | enjoyed@27:0.2868 | subscriber@29:0.2672。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 459. test:5602 | Business → World

预测置信度 0.9766；真实类概率 0.0045；前两类概率差 0.9606。
分词数 24；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

Donors seek clarity on PA finances Donors to the Palestinians are asking  whether the change of leadership can let more light into Palestinian finances.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：palestinian@22:2.9413 | palestinians@9:1.0726 | light@20:0.9546。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 460. test:5625 | Sci/Tech → World

预测置信度 0.5589；真实类概率 0.4209；前两类概率差 0.1380。
分词数 40；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Coalition asks US Congress to kill copyright bill WASHINGTON - A coalition of technology and advocacy groups on Friday asked the U.S. Senate to kill copyright legislation that might result in jail time for people who trade copyrighted files online.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：kill@5:0.9634 | bill@7:0.7510 | congress@3:0.7297。
能把预测改为真实类的单词遮挡数：11。仅表示局部敏感性，不代表已证明因果原因。

## 461. test:5634 | Sci/Tech → World

预测置信度 0.5502；真实类概率 0.2478；前两类概率差 0.3024。
分词数 30；未知词比例 6.67%；特征：需结合语义人工复核。

Court ruling has fat cats purring THE future of horseracing in Britain was thrown into confusion this week as a result of a judgment by the European Court of Justice.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：european@26:0.6483 | court@27:0.6341 | in@10:0.2975。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 462. test:5656 | Sports → World

预测置信度 0.6164；真实类概率 0.0822；前两类概率差 0.3993。
分词数 37；未知词比例 2.70%；特征：含HTML实体或编码痕迹。

Don King Productions Presents:  quot;Battle For Supremacy quot; On Saturday November 13th, ten misfits, nomads and upstarts seek to wage war or settle the score at the famed Madison Square Garden in New York, New York.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：york@34:1.3159 | war@21:0.7262 | new@33:0.7083。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 463. test:5659 | Sci/Tech → Sports

预测置信度 0.4803；真实类概率 0.4209；前两类概率差 0.0595。
分词数 34；未知词比例 2.94%；特征：前两类接近:概率差<0.2。

This week in game news They risked hypothermia and fought off the effects of sleep deprivation so they could be among the first to achieve their quest in the wee hours of the morning.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：the@11:0.6480 | of@13:0.5876 | their@25:0.5395。
能把预测改为真实类的单词遮挡数：17。仅表示局部敏感性，不代表已证明因果原因。

## 464. test:5666 | Business → World

预测置信度 0.7180；真实类概率 0.2794；前两类概率差 0.4385。
分词数 34；未知词比例 0.00%；特征：世界与商业边界。

Indian PM pledges to protect poor from oil-driven inflation NEW DELHI : Indian Prime Minister Manmohan Singh pledged to try to shield the poor by keeping down prices of essential goods amid rising inflation.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：essential@29:1.7880 | amid@31:0.6541 | indian@0:0.3243。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 465. test:5674 | Business → Sports

预测置信度 0.4561；真实类概率 0.1750；前两类概率差 0.2312。
分词数 26；未知词比例 0.00%；特征：需结合语义人工复核。

Will Hutton There were two stories last week that will have world-shaping implications. The first was in a Paris hospital and a compound in Ramallah.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：stories@5:0.3301 | last@6:0.3158 | was@16:0.2764。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 466. test:5683 | Sci/Tech → World

预测置信度 0.6465；真实类概率 0.0812；前两类概率差 0.4023。
分词数 33；未知词比例 0.00%；特征：需结合语义人工复核。

Final Round in Cable-ISP Fight The U.S. Supreme Court has agreed to hear whether cable operators must give access to their lines to third-party ISPs. Michael Grebb reports from Washington.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：hear@14:1.3988 | agreed@12:1.0572 | court@10:1.0447。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 467. test:5685 | World → Business

预测置信度 0.9542；真实类概率 0.0239；前两类概率差 0.9303。
分词数 24；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

Safety Group Closely Echoes Rail Industry Documents show that the nation's most influential rail-safety group is tightly bound to the railroad industry.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：safety@15:1.0630 | industry@5:0.9373 | rail@14:0.7667。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 468. test:5690 | Business → Sci/Tech

预测置信度 0.8496；真实类概率 0.1441；前两类概率差 0.7055。
分词数 30；未知词比例 0.00%；特征：商业与科技边界。

Where have all the people gone? While media and political attention is on the threat of outsourcing, the reality is that outsourcing is a sideshow in a much larger event.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：outsourcing@21:0.4749 | outsourcing@16:0.1039 | is@22:0.0875。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 469. test:5692 | Sports → Business

预测置信度 0.9398；真实类概率 0.0424；前两类概率差 0.8974。
分词数 28；未知词比例 0.00%；特征：高置信错误>=0.9；含HTML实体或编码痕迹。

Boston archbishop reveals anguish of closings BOSTON Boston #39;s Archbishop is telling catholics that the church #39;s financial footing is  quot;much worse than people realize.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：boston@6:1.1225 | financial@19:1.0291 | footing@20:0.6007。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 470. test:5740 | World → Business

预测置信度 0.9479；真实类概率 0.0002；前两类概率差 0.8961。
分词数 44；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

Dow Jones Agrees to Buy MarketWatch in \$519 Million Deal Dow Jones   Company, the publisher of The Wall Street Journal, has agreed to buy MarketWatch, the parent company of the financial news Web site CBS MarketWatch, for approximately \$519 million, the companies said today.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：cbs@34:1.1638 | web@32:1.0691 | marketwatch@35:0.9109。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 471. test:5748 | Business → Sci/Tech

预测置信度 0.6335；真实类概率 0.3602；前两类概率差 0.2734。
分词数 27；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Microsoft signs two Indian deals The announcement came as Microsoft chief executive Steve Ballmer opened the group #39;s new Indian headquarters in the city of Hyderabad.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ballmer@13:0.8452 | opened@14:0.8364 | steve@12:0.4642。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 472. test:5797 | World → Sci/Tech

预测置信度 0.7070；真实类概率 0.2096；前两类概率差 0.4975。
分词数 35；未知词比例 0.00%；特征：需结合语义人工复核。

Microsoft open new software development unit in India (AFP) AFP - Microsoft said it will join with India's second-largest software firm, Infosys Technologies, to provide software and consulting to manufacturing, banking and automobile companies.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：software@3:0.5648 | software@20:0.4511 | firm@21:0.3111。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 473. test:5813 | Business → Sci/Tech

预测置信度 0.5293；真实类概率 0.4703；前两类概率差 0.0591。
分词数 68；未知词比例 2.94%；特征：商业与科技边界；前两类接近:概率差<0.2。

ScanSoft to acquire 3 software firms ScanSoft Inc. said it plans three acquisitions. The company will acquire Phonetic Systems Ltd., a provider of automated directory assistance and voice-based programs, for \$35 million in cash, and an additional consideration of up to \$35 million, based on the achievement of performance targets and the potential vesting of a warrant to buy 750,000 common shares. ART Advanced Recognition Technologies ...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：software@4:0.8986 | 3@3:0.1751 | of@22:0.1596。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 474. test:5830 | Business → Sci/Tech

预测置信度 0.6045；真实类概率 0.3502；前两类概率差 0.2542。
分词数 40；未知词比例 2.50%；特征：商业与科技边界；含HTML实体或编码痕迹。

Microsoft to hire hundreds in India Microsoft on Tuesday announced its decision to localise Windows and Office software in 14 Indian languages over the next 12 months and that the company would hire  #39;hundreds #39; in India this year.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：microsoft@0:0.3355 | software@17:0.2252 | windows@14:0.1338。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 475. test:5841 | Sports → Business

预测置信度 0.7069；真实类概率 0.0123；前两类概率差 0.4627。
分词数 33；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

INSIDE INFO: Man Utd shares drop MAN UNITED #39;S share price has fallen by just over 2.5, less than expected after the resignation of Malcolm Glazer #39;s bankers JP Morgan.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：drop@5:2.4810 | shares@4:1.6037 | utd@3:1.1200。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 476. test:5845 | Sci/Tech → Business

预测置信度 0.6858；真实类概率 0.1515；前两类概率差 0.5231。
分词数 39；未知词比例 0.00%；特征：商业与科技边界。

Oil Company on Trial in Madagascar Over Pollution (Reuters) Reuters - The operator of Madagascar's\privatized oil refinery went on trial on Tuesday, accused of\polluting the environment around the Indian Ocean island's main\international port, officials said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：refinery@17:2.2764 | oil@16:2.1786 | tuesday@22:1.1575。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 477. test:5862 | Business → Sci/Tech

预测置信度 0.8652；真实类概率 0.0859；前两类概率差 0.7793。
分词数 24；未知词比例 0.00%；特征：商业与科技边界。

You Say Sell, I Say Potato Disgruntled shareholders file suit to force talks with Oracle while PeopleSoft's two largest shareholders agree to disagree.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：s@17:1.3907 | file@8:0.7533 | suit@9:0.4178。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 478. test:5884 | World → Business

预测置信度 0.8998；真实类概率 0.0665；前两类概率差 0.8334。
分词数 21；未知词比例 0.00%；特征：世界与商业边界。

Argentina gets China investment China is to invest nearly \$20bn (11bn) in Argentina over the next 10 years, Argentine officials say.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：investment@3:1.7740 | invest@7:0.7296 | to@6:0.5869。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 479. test:5886 | World → Business

预测置信度 0.9934；真实类概率 0.0061；前两类概率差 0.9872。
分词数 22；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

Producer Price Surge Fuels Inflation Fears Producer prices surged 1.7 percent in October, their sharpest monthly increase in nearly 15 years.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：producer@6:2.0230 | price@1:0.7757 | prices@7:0.6442。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 480. test:5900 | Business → World

预测置信度 0.9571；真实类概率 0.0068；前两类概率差 0.9211。
分词数 33；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

China, Argentina sign 5 cooperation documents China and Argentina signed five agreements in Buenos Aires Tuesday that will allow them to expand cooperation in the areas of trade, space, education, tourism and railways.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：cooperation@4:1.7148 | sign@2:1.4539 | argentina@1:1.0139。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 481. test:5902 | Sci/Tech → World

预测置信度 0.6363；真实类概率 0.1763；前两类概率差 0.4600。
分词数 27；未知词比例 7.41%；特征：含HTML实体或编码痕迹。

Press review 0850CET--The seizure of fake Nike sportswear by the Customs Department was one of the main stories on Wednesday #39;s newspapers. L-Orizzont published 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：fake@6:0.6942 | main@17:0.6688 | on@19:0.4122。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 482. test:5916 | World → Business

预测置信度 0.6152；真实类概率 0.3831；前两类概率差 0.2321。
分词数 38；未知词比例 0.00%；特征：世界与商业边界。

ConocoPhillips boosts LUKoil stake to 10 percent (AFP) AFP - US oil major ConocoPhillips has boosted its stake in Russia's second-largest oil producer LUKoil to 10 percent, giving Conoco at least one representative on LUkoil's board.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：stake@3:1.5846 | lukoil@2:1.2016 | boosts@1:0.7554。
能把预测改为真实类的单词遮挡数：5。仅表示局部敏感性，不代表已证明因果原因。

## 483. test:5935 | World → Sci/Tech

预测置信度 0.9951；真实类概率 0.0026；前两类概率差 0.9925。
分词数 32；未知词比例 6.25%；特征：高置信错误>=0.9。

Swedes beam poetry into outer space (Reuters) Reuters - Swedish poets have broadcast their work into outer space by radio to give alien life forms -- if they exist -- a taste\of earthling literature.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：space@5:0.9360 | reuters@6:0.7056 | swedish@8:0.4960。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 484. test:5956 | World → Business

预测置信度 0.5668；真实类概率 0.3998；前两类概率差 0.1670。
分词数 39；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

APEC Ministers Urge New Effort on Trade Talks Pacific Rim trading nations said on Wednesday they should pool their influence to energize talks to free up world trade. As trade and foreign ministers from the 21-member Asia-Pacific 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：trade@27:1.1852 | trading@10:0.4405 | world@26:0.4376。
能把预测改为真实类的单词遮挡数：6。仅表示局部敏感性，不代表已证明因果原因。

## 485. test:5973 | World → Sci/Tech

预测置信度 0.8942；真实类概率 0.1006；前两类概率差 0.7936。
分词数 38；未知词比例 5.26%；特征：需结合语义人工复核。

Nursery rhymes more violent than TV (Reuters) Reuters - Children's nursery rhymes contain 10 times more violence than television shows broadcast before the\9 p.m. "watershed" after which more adult content can be shown, research has said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：content@31:2.8528 | can@32:1.2701 | adult@30:0.8315。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 486. test:5981 | World → Business

预测置信度 0.9421；真实类概率 0.0331；前两类概率差 0.9089。
分词数 36；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

India desperate for jobs, infrastructure despite economic boom (AFP) AFP - Despite India's economic boom in software and outsourcing services, economists have warned the government needs more reforms to create jobs in manufacturing to cut poverty.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：outsourcing@18:2.4662 | economists@20:2.3977 | services@19:1.4661。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 487. test:6006 | Business → World

预测置信度 0.6859；真实类概率 0.3026；前两类概率差 0.3832。
分词数 35；未知词比例 0.00%；特征：世界与商业边界；含HTML实体或编码痕迹。

Russia #39;s Putin Defends Reforms, Worries About Clans Russian President Vladimir Putin said on Thursday he had no plans to grab more power or change the constitution when reforming Russia #39;s government structure.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：president@10:0.8070 | putin@12:0.6423 | vladimir@11:0.5398。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 488. test:6022 | Business → Sci/Tech

预测置信度 0.6611；真实类概率 0.3389；前两类概率差 0.3222。
分词数 32；未知词比例 0.00%；特征：商业与科技边界。

SBC and Yahoo! extend pact to offer Internet service SAN ANTONIO SBC Communications and Yahoo are expanding their high-speed Internet service partnership to link video, wireless phone, Internet and other services.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：video@25:0.3839 | wireless@26:0.3134 | partnership@22:0.2711。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 489. test:6028 | Business → World

预测置信度 0.7507；真实类概率 0.0201；前两类概率差 0.5215。
分词数 41；未知词比例 0.00%；特征：世界与商业边界。

Suspect Animal Tested for Mad Cow Disease  WASHINGTON (Reuters) - Government scientists are chasing a  possible new case of mad cow disease in the United States, with  final results on a suspicious slaughtered animal expected in  coming days, officials said on Thursday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：scientists@10:1.6098 | government@9:0.8225 | suspect@0:0.6425。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 490. test:6035 | Sci/Tech → Business

预测置信度 0.6000；真实类概率 0.3992；前两类概率差 0.2008。
分词数 36；未知词比例 0.00%；特征：商业与科技边界。

Epiphany looks to beef up call center CRM software maker Epiphany Inc. this week is rolling out new analytical software, including two new products and vertical-specific bundles aimed at the communications and retail finance industries.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：finance@34:1.8111 | industries@35:1.4542 | two@21:0.5489。
能把预测改为真实类的单词遮挡数：5。仅表示局部敏感性，不代表已证明因果原因。

## 491. test:6043 | Business → World

预测置信度 0.5370；真实类概率 0.3748；前两类概率差 0.1622。
分词数 54；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

US May Have New Case of Mad Cow Disease  WASHINGTON (Reuters) - A final test is likely to confirm a  second U.S. case of mad cow disease, experts said on Thursday,  though they see a small possibility the animal, which tested  "inconclusive" in two preliminary tests, could be given a clean  bill of health.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：s@21:0.7276 | u@20:0.3274 | disease@26:0.2972。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 492. test:6044 | World → Sci/Tech

预测置信度 0.4646；真实类概率 0.3414；前两类概率差 0.1232。
分词数 39；未知词比例 2.56%；特征：前两类接近:概率差<0.2。

Police Chief Backs Using Force Against Intruders Britains top police officer today called for an urgent updating of the law to protect householders who use force to defend their homes against criminals - even if it involves killing the intruder.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：officer@10:0.7129 | using@3:0.4906 | called@12:0.3859。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 493. test:6058 | World → Business

预测置信度 0.8995；真实类概率 0.0779；前两类概率差 0.8217。
分词数 38；未知词比例 0.00%；特征：世界与商业边界。

A Bit of Wall St. on the Tigris The 150 brokers and traders on the Iraq Stock Exchange are not waiting for the war to end, buying and selling orders a few hundred yards away from the fighting.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：stock@16:2.2555 | exchange@17:1.9085 | buying@26:0.8597。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 494. test:6067 | Business → Sci/Tech

预测置信度 0.5962；真实类概率 0.1151；前两类概率差 0.3076。
分词数 48；未知词比例 0.00%；特征：商业与科技边界。

Aussies battle EU over cheese, champagne AP - The United States and Australia have prevailed in an interim ruling by World Trade Organisation (WTO) in a dispute over the protection given by the European Union to its regional goods such as Champagne wine and Feta cheese, trade officials said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ap@6:2.7893 | cheese@4:2.7735 | cheese@44:0.4841。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 495. test:6068 | Sci/Tech → Business

预测置信度 0.8086；真实类概率 0.1404；前两类概率差 0.6682。
分词数 76；未知词比例 2.63%；特征：商业与科技边界。

A Fair Tax Some say a "fair tax" that removes the need to file tax returns from the vast majority of the citizenry is a national sales tax.  This doesn't seem to be very fair to people trying to feed, house and clothe themselves and seems to subsidize large land holders (Bush's favorite constituency).  There is a tax that lives up to the promises broken by Bush's proposal for a national sales tax.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：doesn@29:0.6843 | and@45:0.5111 | tax@27:0.4878。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 496. test:6082 | Sci/Tech → Business

预测置信度 0.5556；真实类概率 0.4329；前两类概率差 0.1227。
分词数 28；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

PeopleSoft Chief Threatens to Sue Over Oracle Statements PeopleSoft's chief executive accused Oracle of spreading misleading information about his stock sales and threatened to sue for defamation.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：sales@21:1.5064 | stock@20:1.4052 | chief@10:1.0403。
能把预测改为真实类的单词遮挡数：6。仅表示局部敏感性，不代表已证明因果原因。

## 497. test:6084 | Business → Sci/Tech

预测置信度 0.8640；真实类概率 0.1357；前两类概率差 0.7283。
分词数 39；未知词比例 0.00%；特征：商业与科技边界。

Yahoo and SBC extend partnership and plan new services Yahoo and SBC Communications have agreed to collaborate to extend some of the online services and content they currently provide to PC users to mobile phones and home entertainment devices.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：users@31:0.5853 | pc@30:0.5253 | online@22:0.4451。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 498. test:6100 | Business → Sci/Tech

预测置信度 0.9853；真实类概率 0.0004；前两类概率差 0.9710。
分词数 19；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；短文本<=20词。

Lazarus-like virus hits computers A new computer virus is catching people out by coming back from the dead.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：virus@2:2.5361 | virus@8:1.7226 | hits@3:1.0755。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 499. test:6114 | World → Sci/Tech

预测置信度 0.6348；真实类概率 0.3631；前两类概率差 0.2717。
分词数 28；未知词比例 0.00%；特征：需结合语义人工复核。

UN deadlock defeats cloning ban The United Nations has shelved efforts to draft a treaty banning the cloning of human embryos in a setback for the Bush administration.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：cloning@3:1.1500 | embryos@20:0.6620 | cloning@17:0.4828。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 500. test:6115 | Sci/Tech → Business

预测置信度 0.4749；真实类概率 0.3262；前两类概率差 0.1486。
分词数 39；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

Congress Sends 'Net Access Ban to White House The U.S. Congress on Friday reinstated a ban on Internet access taxes after the House of Representatives agreed to extend it for another three years rather than make it permanent.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：taxes@20:1.8240 | agreed@26:1.0241 | on@12:0.7892。
能把预测改为真实类的单词遮挡数：11。仅表示局部敏感性，不代表已证明因果原因。

## 501. test:6150 | World → Sports

预测置信度 0.9891；真实类概率 0.0074；前两类概率差 0.9817。
分词数 15；未知词比例 6.67%；特征：高置信错误>=0.9；短文本<=20词。

England humble Sprinboks Charlie Hodgson scores 27 points as England overwhelm the Springboks at Twickenham.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：points@7:3.7005 | 27@6:1.1787 | scores@5:0.8324。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 502. test:6161 | Business → World

预测置信度 0.6472；真实类概率 0.2850；前两类概率差 0.3622。
分词数 34；未知词比例 0.00%；特征：世界与商业边界；含HTML实体或编码痕迹。

Senators Want Boeing Deal Investigated Leaders of the Senate Armed Services Committee asked the Defense Department on Friday to have its inspector general #39;s office investigate the Air Force #39;s effort to 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：armed@9:3.0286 | senate@8:2.3261 | services@10:0.6066。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 503. test:6185 | Business → Sports

预测置信度 0.9284；真实类概率 0.0622；前两类概率差 0.8662。
分词数 49；未知词比例 0.00%；特征：高置信错误>=0.9；含HTML实体或编码痕迹。

Special to ESPN.com It #39;s the age old question:  quot;What do you give to the man who #39;s been everything? quot;. Only time will tell whether Phil Knight #39;s retirement will be as long-lived as so many players he paid to endorse Nike.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：players@43:2.6862 | he@44:1.3789 | 39@32:0.5765。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 504. test:6208 | Business → Sci/Tech

预测置信度 0.6671；真实类概率 0.3249；前两类概率差 0.3421。
分词数 30；未知词比例 0.00%；特征：商业与科技边界。

Google creators in share sell-off Google founders Larry Page and Sergey Brin have announced plans to sell millions of shares in the web search company they launched in 1998.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：web@23:0.4907 | google@6:0.0898 | they@26:0.0759。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 505. test:6220 | Sci/Tech → Business

预测置信度 0.5689；真实类概率 0.4304；前两类概率差 0.1385。
分词数 42；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

NVIDIA and Intel sign broad cross-license and chipset license &lt;b&gt;...&lt;/b&gt;  quot;NVIDIA and Intel Corporation announced that the companies have signed a broad, multi-year patent cross-license agreement spanning multiple product lines and product generations.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：b@14:1.4029 | b@11:1.1642 | corporation@20:0.8091。
能把预测改为真实类的单词遮挡数：19。仅表示局部敏感性，不代表已证明因果原因。

## 506. test:6222 | Business → Sci/Tech

预测置信度 0.6292；真实类概率 0.3688；前两类概率差 0.2603。
分词数 53；未知词比例 0.00%；特征：商业与科技边界。

HGS Picks Watkins as New Chief Executive  Human Genome Sciences Inc. plans to announce today that it has hired a 20-year product development veteran from Abbott Laboratories Inc. as chief executive. H. Thomas Watkins, 51, will face the challenge of completing the Rockville company's makeover from gene hunter to drug marketer.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：human@7:2.5312 | genome@8:1.9107 | s@45:0.7952。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 507. test:6226 | Business → Sci/Tech

预测置信度 0.6571；真实类概率 0.3385；前两类概率差 0.3185。
分词数 25；未知词比例 0.00%；特征：商业与科技边界。

Google targets software giant  SEATTLE -- Not too long ago, Google Inc. seemed little more than a pesky insect to Microsoft Corp.'s 800-pound gorilla.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：google@9:0.3828 | pound@23:0.2167 | gorilla@24:0.1725。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 508. test:6234 | Business → World

预测置信度 0.4290；真实类概率 0.3987；前两类概率差 0.0303。
分词数 35；未知词比例 2.86%；特征：世界与商业边界；前两类接近:概率差<0.2。

Amtrak Infrastructure On Brink, DOT Warns The national passenger rail service risks a "major point of failure" if infrastructure needs remain unaddressed, the U.S. Department of Transportation warned in a scathing report made public.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：passenger@8:1.2260 | s@24:1.0549 | national@7:0.3709。
能把预测改为真实类的单词遮挡数：5。仅表示局部敏感性，不代表已证明因果原因。

## 509. test:6241 | Business → Sci/Tech

预测置信度 0.6757；真实类概率 0.3001；前两类概率差 0.3755。
分词数 28；未知词比例 3.57%；特征：商业与科技边界。

CAT and AstraZeneca enter \$175m collaboration AstraZeneca intends to invest over 120m in Cambridge Antibody Technology (CAT) through an innovative five-year research collaboration and a 75m equity 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：technology@15:2.3911 | cat@16:1.8058 | through@17:0.5325。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 510. test:6247 | Sci/Tech → Business

预测置信度 0.9965；真实类概率 0.0026；前两类概率差 0.9940。
分词数 40；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Before-the-Bell: GenCorp Falls 5.6 Pct. (Reuters) Reuters - Shares of GenCorp Inc.  fell 5.6\percent before the opening bell on Monday after investment fund\Steel Partners withdrew its proposal to acquire the aerospace\and real estate company.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：investment@25:1.7061 | steel@27:1.3989 | fund@26:1.3981。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 511. test:6260 | Sci/Tech → Business

预测置信度 0.8110；真实类概率 0.1835；前两类概率差 0.6274。
分词数 29；未知词比例 0.00%；特征：商业与科技边界。

Thomson joins takeover bid for ContentGuard Thomson joined Microsoft and Time Warner on Monday in trying to take control of U.S. digital rights management (DRM) company ContentGuard Holdings.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：thomson@6:1.4715 | joined@7:1.2318 | bid@3:1.1835。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 512. test:6262 | Sci/Tech → Business

预测置信度 0.8912；真实类概率 0.1083；前两类概率差 0.7829。
分词数 56；未知词比例 0.00%；特征：商业与科技边界。

Google Founders Selling Off Stock Google Founders Selling Off Stock\\Is this a sign that Google stack is overpriced? Or does it just mean that since there is so much interest in Google and its shares right now that the founders decided to sell off a big part of their holdings with the search engine. Dow ...

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：stock@4:0.7468 | is@10:0.7031 | stock@9:0.6501。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 513. test:6266 | World → Business

预测置信度 0.6922；真实类概率 0.2868；前两类概率差 0.4053。
分词数 35；未知词比例 0.00%；特征：世界与商业边界；含HTML实体或编码痕迹。

Ivory Coast violence deals economic blow Burned, looted shops dot the commercial capital. European airlines have suspended flights. And only a few ships remain in what was one of West Africa #39;s busiest ports.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：economic@4:1.5772 | deals@3:1.2526 | airlines@14:0.8654。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 514. test:6267 | Business → Sports

预测置信度 0.8232；真实类概率 0.0109；前两类概率差 0.6615。
分词数 30；未知词比例 0.00%；特征：需结合语义人工复核。

Banks seek court ruling over F1 Three banks go to the High Court in London seeking a ruling which could lead to Bernie Ecclestone losing control of Formula One racing.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：formula@27:2.8948 | racing@29:1.7936 | one@28:1.1144。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 515. test:6276 | Business → Sci/Tech

预测置信度 0.9741；真实类概率 0.0239；前两类概率差 0.9502。
分词数 30；未知词比例 3.33%；特征：商业与科技边界；高置信错误>=0.9。

Federal CISOs Rank Patch Management As Biggest Obstacle Survey by Intelligent Decisions indicates that patch management leaves less time for chief information security officers to work on improving overall security.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：security@22:0.9715 | information@21:0.7431 | officers@23:0.4909。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 516. test:6278 | Sci/Tech → Business

预测置信度 0.9045；真实类概率 0.0954；前两类概率差 0.8091。
分词数 39；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Update: PeopleSoft board won't negotiate Oracle takeover PeopleSoft executives said over the weekend that they won't discuss a sale to Oracle at a price of \$24 per share but would consider an offer at a higher price.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：board@2:1.1512 | takeover@7:1.1174 | update@0:0.8145。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 517. test:6293 | Business → Sci/Tech

预测置信度 0.5420；真实类概率 0.3540；前两类概率差 0.1880。
分词数 50；未知词比例 6.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

The Handbag? Total Knockoff. The Price Tag? All Too Real. It is as much a rite of the New York holiday season as sidewalk Santas or crowded Fifth Avenue sidewalks: the proliferation of hawkers selling counterfeit products like the fake Fendi handbag, the replica Rolex watch and the pirated DVD.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：pirated@48:1.3535 | dvd@49:1.2583 | too@8:0.2115。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 518. test:6319 | Sports → Sci/Tech

预测置信度 0.5061；真实类概率 0.2547；前两类概率差 0.2514。
分词数 34；未知词比例 2.94%；特征：需结合语义人工复核。

Arrowhead: It still is pointing the way In comparison to its contemporaries it could be termed a modern marvel, an example of how to do things right when everyone else was doing things wrong.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：marvel@18:1.6331 | modern@17:0.4036 | example@20:0.3508。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 519. test:6325 | Sci/Tech → World

预测置信度 0.5780；真实类概率 0.3670；前两类概率差 0.2109。
分词数 28；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

JFK killing fades in intensity WASHINGTON: The 41st anniversary of President John F Kennedy #39;s assassination passed on November 22 - a lot more quietly than earlier ones.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：president@10:0.7790 | washington@5:0.6228 | 41st@7:0.4882。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 520. test:6327 | World → Sci/Tech

预测置信度 0.7558；真实类概率 0.1434；前两类概率差 0.6124。
分词数 41；未知词比例 0.00%；特征：需结合语义人工复核。

EasyGroup close to launching low-cost mobile phone service (AFP) AFP - EasyGroup, the holding company of no-frills British airline easyJet, is close to striking a deal to launch a low-cost mobile telephone service in Britain, the Financial Times reported.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：mobile@32:0.9214 | telephone@33:0.8723 | cost@31:0.2965。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 521. test:6344 | Sci/Tech → Business

预测置信度 0.7122；真实类概率 0.2693；前两类概率差 0.4428。
分词数 22；未知词比例 0.00%；特征：商业与科技边界。

Elderly 'need digital TV funds' Vulnerable groups such as the elderly should be helped to buy digital TV equipment, a report says.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：funds@4:2.4995 | groups@6:0.5411 | such@7:0.5083。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 522. test:6438 | Business → Sci/Tech

预测置信度 0.3837；真实类概率 0.1980；前两类概率差 0.0012。
分词数 46；未知词比例 2.17%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Four Hurricanes Hurting Florida Economy (AP) AP - Normally at this time of the year, labor contractor Jose Luis Avalos would be assembling a crew of workers who could each earn  #36;1,500 to  #36;2,000 a week in the area's abundant citrus groves.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ap@6:0.9707 | ap@5:0.9282 | normally@7:0.6400。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 523. test:6462 | Business → Sci/Tech

预测置信度 0.4772；真实类概率 0.3736；前两类概率差 0.1036。
分词数 35；未知词比例 2.86%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Land Rover aims new model at US Land Rover will launch a sports tourer next year in a what is likely to be a test of British carmakers #39; ability to compete in the US.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：sports@12:0.1435 | british@26:0.0729 | rover@1:0.0643。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 524. test:6500 | Sci/Tech → World

预测置信度 0.9687；真实类概率 0.0284；前两类概率差 0.9403。
分词数 54；未知词比例 1.85%；特征：高置信错误>=0.9。

The Shockwaves of Sumatra The Indian Ocean earthquake of December 2004 produced     a shockwave that created tsunamis all across the Indian Ocean. The tsunamis hammered nearby Indonesia and struck as far as     the coast of East Africa. The death toll has climbed over 100,000 and continues to grow.    It also created social shockwaves.  

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：indonesia@26:0.9160 | death@38:0.5849 | africa@36:0.5030。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 525. test:6512 | World → Sci/Tech

预测置信度 0.5339；真实类概率 0.2306；前两类概率差 0.3006。
分词数 35；未知词比例 5.71%；特征：含HTML实体或编码痕迹。

SAY NEIGHBORS #39; WEAPONS LEAVE THEM VULNERABLE Electrical engineering student Roozbeh Rahimi reflects a common sentiment among Iranians when he expresses hope that this famous tourist city will gain fame soon for its nuclear technology.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：engineering@8:0.4957 | vulnerable@6:0.4846 | electrical@7:0.3331。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 526. test:6516 | World → Sci/Tech

预测置信度 0.7812；真实类概率 0.1346；前两类概率差 0.6466。
分词数 46；未知词比例 0.00%；特征：需结合语义人工复核。

FDA OKs Scientist Publishing Vioxx Data (AP) AP - The Food and Drug Administration has given a whistle-blower scientist permission to publish data indicating that as many as 139,000 people had heart attacks that may be linked to Vioxx, the scientist's lawyer said Monday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：data@5:0.7842 | scientist@2:0.4911 | fda@0:0.4586。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 527. test:6542 | Business → Sci/Tech

预测置信度 0.6017；真实类概率 0.3696；前两类概率差 0.2321。
分词数 38；未知词比例 0.00%；特征：商业与科技边界。

Discovery Channel Tests Power of Licensing By rushing more than 700 products under the American Chopper brand as part of a new in-house licensing program, the cable channel is relying more heavily on licensing to market shows.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：licensing@5:0.4250 | licensing@24:0.2810 | licensing@34:0.2220。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 528. test:6555 | Business → World

预测置信度 0.5321；真实类概率 0.4624；前两类概率差 0.0697。
分词数 41；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

Iraq to spend \$1 billion to expand oil production Iraq is planning to spend more than \$1 billion in 2005 to boost its oil production capacity by about 15 percent to 3.25 million barrels a day, an Iraqi official said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：iraqi@38:2.4134 | official@39:1.3467 | iraq@9:0.8176。
能把预测改为真实类的单词遮挡数：5。仅表示局部敏感性，不代表已证明因果原因。

## 529. test:6565 | Business → Sci/Tech

预测置信度 0.7102；真实类概率 0.2895；前两类概率差 0.4207。
分词数 37；未知词比例 2.70%；特征：商业与科技边界；含HTML实体或编码痕迹。

EasyMobile launch set for March Denmark #39;s leading telecoms operator TDC says it will launch a low-budget mobile telephone operator dubbed  quot;easyMobile quot; with mobile network operator T-Mobile in Britain in March 2005.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：network@28:0.7552 | telephone@20:0.5200 | t@30:0.2108。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 530. test:6566 | Business → World

预测置信度 0.4045；真实类概率 0.3965；前两类概率差 0.0080。
分词数 34；未知词比例 5.88%；特征：世界与商业边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

More buyers choose artificial Renee McDonald remembers the Christmas trees of her youth: spindly, fake and out of a box. They were hard to put up, and they just didn #39;t smell right.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：fake@14:1.0048 | youth@12:0.6880 | her@11:0.5351。
能把预测改为真实类的单词遮挡数：10。仅表示局部敏感性，不代表已证明因果原因。

## 531. test:6568 | Sci/Tech → Business

预测置信度 0.5618；真实类概率 0.3393；前两类概率差 0.2225。
分词数 35；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

SEO #39;s Multiplying Effect on Paid Inclusion Paid inclusion (PI) has always been a hot potato. It #39;s not quite SEO (define) and not quite search advertising. No one wants to touch it.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@18:0.8113 | no@29:0.6600 | and@24:0.5339。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 532. test:6574 | Business → Sci/Tech

预测置信度 0.9868；真实类概率 0.0122；前两类概率差 0.9746。
分词数 107；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Is this the end of IT as we know it? Halsey Minor, CEO of hosted integration provider grand central Communications, has a powerful message for IT: In four years, ... basically the whole notion of enterprise application software is going to be dead. He believes application functionality will instead be available as hosted, pay-per-use services delivered by companies such as Salesforce.com. Putting his money where his mouth is, Minor has recently launched a \$50 million venture capital fund with his own money to fuel on-demand startups. For its part, Grand Central will handle data and process integration between enterprises and multiple on-demand services.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：application@35:0.9371 | enterprise@34:0.5970 | application@44:0.2020。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 533. test:6576 | World → Sci/Tech

预测置信度 0.9935；真实类概率 0.0058；前两类概率差 0.9877。
分词数 43；未知词比例 0.00%；特征：高置信错误>=0.9。

Toshiba claims Hollywood backing in war for next DVD standard (AFP) AFP - Toshiba said four major Hollywood studios had thrown their crucial weight behind High Definition DVD (HD-DVD), one of two disc formats contending to be the standard in next-generation DVDs.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：dvd@26:2.6467 | hd@27:1.4193 | dvd@28:1.2197。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 534. test:6582 | Business → Sci/Tech

预测置信度 0.8370；真实类概率 0.1556；前两类概率差 0.6814。
分词数 39；未知词比例 10.26%；特征：商业与科技边界；未知词比例>=10%。

Telekom Austria taps the Bulgarian market Telekom Austria, Austrias largest telecoms operator, obtained access to the relatively underdeveloped East European mobile services market by winning the right to purchase the Bulgarian mobile operator MobilTel for 1.6billion (\$2.12billion).

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：austria@1:0.7922 | taps@2:0.6180 | mobile@20:0.4758。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 535. test:6592 | Business → Sci/Tech

预测置信度 0.9999；真实类概率 0.0001；前两类概率差 0.9998。
分词数 45；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Sony, IBM, Toshiba Give Details of 'Cell' Chip (Reuters) Reuters - IBM , Sony Corp. (6758.T) and\Toshiba Corp. (6502.T) on Monday revealed their plans for the\powerful new "Cell" processor the three are jointly producing\to run next-generation computers, game consoles and\televisions.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：game@41:1.5742 | computers@40:1.1375 | reuters@9:0.9669。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 536. test:6614 | Sci/Tech → Business

预测置信度 0.5963；真实类概率 0.3945；前两类概率差 0.2018。
分词数 38；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

 #39;Breakthrough #39; on hydrogen fuel US scientists had made a breakthrough in their quest to make low-cost hydrogen, a technology key to finding new sources of energy to end US dependence on foreign oil, they said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：oil@35:1.0922 | us@31:1.0205 | us@6:0.7648。
能把预测改为真实类的单词遮挡数：7。仅表示局部敏感性，不代表已证明因果原因。

## 537. test:6623 | Business → Sci/Tech

预测置信度 0.4836；真实类概率 0.1702；前两类概率差 0.1512。
分词数 71；未知词比例 7.04%；特征：商业与科技边界；前两类接近:概率差<0.2。

With work, Dana-Farber learns from '94 mistakes Nurse Teresa Mazeika has known the woman knitting in the blue reclining chair for months. But she asks Carolyn Harlow her name and birthday anyway, as she approaches with chemotherapy for Harlow's blood cancer. Mazeika, a 17-year nursing veteran at Dana-Farber Cancer Institute, isn't taking any chances that she is about to give the drug to the wrong patient.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：s@40:0.7610 | birthday@31:0.2502 | farber@3:0.2477。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 538. test:6669 | World → Business

预测置信度 0.8267；真实类概率 0.1701；前两类概率差 0.6566。
分词数 32；未知词比例 0.00%；特征：世界与商业边界。

Panel Urges N.Y. to Pay \$14 Billion More for City Schools Court-appointed referees recommended the state pay an additional \$14 billion over four years to improve New York City schools.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：pay@18:0.8381 | billion@7:0.5366 | state@17:0.4903。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 539. test:6682 | World → Sci/Tech

预测置信度 0.6967；真实类概率 0.2807；前两类概率差 0.4160。
分词数 36；未知词比例 0.00%；特征：需结合语义人工复核。

EPA May Conduct Human Tests for Chemicals (AP) AP - In setting limits on chemicals in food and water, the Environmental Protection Agency may rely on industry tests that expose people to poisons and raise ethical questions.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：environmental@19:0.9409 | industry@25:0.4059 | and@32:0.3654。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 540. test:6698 | World → Sports

预测置信度 0.9594；真实类概率 0.0380；前两类概率差 0.9214。
分词数 70；未知词比例 4.29%；特征：高置信错误>=0.9。

Terms of Endearment   Seems that the Bush administration, unlike previous White Houses, is not necessarily averse to allowing its ambassadors to have second tours. For example, word is that    John     Thomas "Tom    " Schieffer , the Texas oilman who brought    President Bush  into the Texas Rangers baseball club partnership and who is now ambassador to Australia, is to hang out in the Pacific a while longer, this time as ambassador to Japan.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：baseball@44:4.2390 | rangers@43:2.4906 | club@45:2.0482。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 541. test:6710 | World → Sci/Tech

预测置信度 0.6069；真实类概率 0.3118；前两类概率差 0.2951。
分词数 23；未知词比例 4.35%；特征：需结合语义人工复核。

Murdoch novel reveals Alzheimer's The last novel by the author Iris Murdoch reveals the first signs of Alzheimer's disease, experts say.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：novel@1:0.9516 | reveals@2:0.6946 | murdoch@0:0.5214。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 542. test:6711 | Business → Sci/Tech

预测置信度 0.9941；真实类概率 0.0016；前两类概率差 0.9899。
分词数 36；未知词比例 8.33%；特征：商业与科技边界；高置信错误>=0.9。

Local group joins suit to de-list endangered species Bob Briggs wifes family has owned about 1,000 acres of redwood forest off Waddell Creek since 1913. He doesnt clearcut, and logs about once a decade.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：species@8:4.3574 | endangered@7:1.1311 | joins@2:0.1727。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 543. test:6718 | World → Sci/Tech

预测置信度 0.9992；真实类概率 0.0001；前两类概率差 0.9986。
分词数 22；未知词比例 0.00%；特征：高置信错误>=0.9。

Why 2004 was the year of the blog A US dictionary publisher declares "blog" as one of the words of the year.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：blog@13:5.6229 | publisher@11:2.1798 | declares@12:1.2287。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 544. test:6734 | World → Business

预测置信度 0.9863；真实类概率 0.0090；前两类概率差 0.9773。
分词数 36；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Turkey eyes \$15 billion investment years ANKARA: Turkey is hoping to attract \$15 billion of foreign investment between 2005 and 2007 through reforms designed to overhaul its economy and ease the country #39;s entry into 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：investment@16:1.7233 | 39@32:0.9991 | 2005@18:0.7343。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 545. test:6746 | Sports → World

预测置信度 0.6312；真实类概率 0.3530；前两类概率差 0.2782。
分词数 43；未知词比例 0.00%；特征：需结合语义人工复核。

Judge Declines to Dismiss Steroid Case (AP) AP - A judge declined to dismiss charges against four men accused of distributing steroids to top athletes amid accusations that prosecutors illegally searched a nutritional supplement lab and the house and car of Barry Bonds' trainer.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：lab@33:0.9368 | illegally@28:0.8074 | house@36:0.6624。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 546. test:6748 | Business → Sci/Tech

预测置信度 0.9891；真实类概率 0.0104；前两类概率差 0.9787。
分词数 40；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Intel planning Centrino-like brand for desktops Intel is preparing a marketing strategy that will brand desktop PCs with a similar label that made its Centrino notebook technology a household name, according to sources familiar with the company's plans.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：desktop@16:1.9002 | pcs@17:1.8545 | s@38:0.6312。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 547. test:6766 | World → Business

预测置信度 0.6621；真实类概率 0.3262；前两类概率差 0.3359。
分词数 46；未知词比例 2.17%；特征：世界与商业边界。

India's low-cost airline eyes business travel (AFP) AFP - India's pioneer low-cost carrier Air Deccan plans to raise 50 million dollars in private equity by shedding a 26 percent stake and also aims to enter the corporate business jet segment, its chairman said.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：corporate@39:0.9924 | business@40:0.8278 | s@11:0.7571。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 548. test:6794 | World → Sci/Tech

预测置信度 0.8074；真实类概率 0.0072；前两类概率差 0.6935。
分词数 42；未知词比例 4.76%；特征：含HTML实体或编码痕迹。

HAYLEY MICK: Hayley Mick is a journalist currently based in Vancouver. She has broadcast experience with CBC Radio #39;s Quirks and Quarks and has reported for the Vancouver Sun, CBC Online, and the Canadian Press #39;s Ontario and Vancouver bureaus.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：journalist@6:1.0143 | currently@7:0.9701 | sun@29:0.8052。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 549. test:6796 | Business → World

预测置信度 0.3996；真实类概率 0.3891；前两类概率差 0.0105。
分词数 39；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

Setback for asbestos settlement at ABB ABB said it was aware of the ruling, but remained confident that a settlement would be reached. ABB is naturally surprised and disappointed at todays decision, but remains confident that it can resolve.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ruling@13:0.4298 | confident@16:0.2659 | the@12:0.1422。
能把预测改为真实类的单词遮挡数：10。仅表示局部敏感性，不代表已证明因果原因。

## 550. test:6805 | World → Sports

预测置信度 0.4001；真实类概率 0.3760；前两类概率差 0.0241。
分词数 24；未知词比例 8.33%；特征：前两类接近:概率差<0.2。

Eureka! Has Australia found its 'defining moment'? Friday is the 150th anniversary of Eureka Day. For some Australians, it's their Boston Tea Party.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：boston@21:1.9295 | tea@22:1.6524 | their@20:1.4511。
能把预测改为真实类的单词遮挡数：9。仅表示局部敏感性，不代表已证明因果原因。

## 551. test:6830 | Sports → World

预测置信度 0.5628；真实类概率 0.0607；前两类概率差 0.2674。
分词数 34；未知词比例 5.88%；特征：含HTML实体或编码痕迹。

Conte goes on TV and names names As the bassist for the pop-funk band Tower of Power, Victor Conte laid down a song #39;s backbone by playing a predetermined series of notes.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：band@14:1.7942 | tower@15:0.9627 | song@23:0.6327。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 552. test:6847 | Business → Sci/Tech

预测置信度 0.7253；真实类概率 0.2740；前两类概率差 0.4513。
分词数 41；未知词比例 0.00%；特征：商业与科技边界。

IBM Quitting Computer Business An era will come to an end when IBM sells off its computer manufacturing business, according to The New York Times. A Chinese company seems the likely buyer and the deal should fetch upward of \$2 billion.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：computer@2:0.9430 | ibm@0:0.8415 | quitting@1:0.2402。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 553. test:6849 | Business → Sci/Tech

预测置信度 0.8189；真实类概率 0.1806；前两类概率差 0.6383。
分词数 43；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

Two top Nokia executives resign HELSINKI: Nokia said the respected head of its networks unit had resigned and another top networks official left in the second major departure of top management in two weeks at the world #39;s largest mobile phone maker.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：nokia@2:0.9754 | nokia@6:0.1988 | executives@3:0.1885。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 554. test:6870 | Sci/Tech → Business

预测置信度 0.5885；真实类概率 0.3683；前两类概率差 0.2202。
分词数 34；未知词比例 0.00%；特征：商业与科技边界。

Bush Signs Internet Access Tax Ban State and local governments will be barred from taxing connections that link people to the Internet for the next three years under legislation signed Friday by President Bush.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tax@4:2.4356 | access@3:0.6725 | friday@30:0.6415。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 555. test:6877 | Business → Sci/Tech

预测置信度 0.7390；真实类概率 0.2609；前两类概率差 0.4781。
分词数 49；未知词比例 0.00%；特征：商业与科技边界；含HTML实体或编码痕迹。

IBM  #39;to sell PC business #39; IBM is reportedly in talks to sell its personal computer business. It would mark the end of an era for the company that brought the computer into the mainstream when it began selling its desktop PC to corporations and consumers in 1981.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：pc@42:1.6438 | desktop@41:1.4222 | end@22:0.2122。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 556. test:6887 | Business → Sci/Tech

预测置信度 0.5305；真实类概率 0.4692；前两类概率差 0.0614。
分词数 36；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

IBM reported to be exiting PC business IBM #39;s possible exit from the personal-computer business would be the latest move in what amounts to a long goodbye from a field it pioneered and revolutionized.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：ibm@0:0.2207 | the@13:0.1167 | field@31:0.0132。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 557. test:6891 | World → Sci/Tech

预测置信度 0.6519；真实类概率 0.3455；前两类概率差 0.3064。
分词数 39；未知词比例 0.00%；特征：需结合语义人工复核。

Villagers flee clashes, huddle in forests  GOMA, Congo -- Thousands of civilians have fled their homes after clashes in the east of Democratic Republic of Congo, the United Nations said yesterday, although it was unclear who was behind the violence.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：forests@5:4.5341 | goma@6:0.7066 | of@9:0.2733。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 558. test:6893 | Business → World

预测置信度 0.9878；真实类概率 0.0113；前两类概率差 0.9765。
分词数 21；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9。

Germans plan mass welfare rallies Nationwide protests are set to take place in Germany as cuts in unemployment benefit take effect.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：germans@0:3.3514 | plan@1:1.9214 | mass@2:1.1635。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 559. test:6914 | World → Business

预测置信度 0.8051；真实类概率 0.0934；前两类概率差 0.7098。
分词数 23；未知词比例 0.00%；特征：世界与商业边界。

BBC 'must keep up' BBC boss Mark Thompson says the corporation must keep up with change, after announcing nearly 3,000 job cuts.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：corporation@10:3.8849 | must@11:0.7788 | up@3:0.5707。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 560. test:6919 | World → Sci/Tech

预测置信度 0.4287；真实类概率 0.3696；前两类概率差 0.0591。
分词数 39；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Court Hears Interstate Wine Sales Case (AP) AP - The Supreme Court considered Tuesday whether state alcoholic beverage regulations put in place 70 years ago, after Prohibition was lifted, should remain the law of the land in the Internet age.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：internet@37:1.8541 | regulations@17:0.3691 | age@38:0.3063。
能把预测改为真实类的单词遮挡数：5。仅表示局部敏感性，不代表已证明因果原因。

## 561. test:6931 | Business → Sci/Tech

预测置信度 0.6561；真实类概率 0.3276；前两类概率差 0.3285。
分词数 53；未知词比例 0.00%；特征：商业与科技边界。

Bipartisan Panel Seeks Greenhouse Gas Limits A bipartisan commission that includes energy industry executives, environmentalists and academics will issue a report Wednesday that calls on the nation to adopt mandatory limits on greenhouse gas emissions linked to global warming, set stricter fuel economy standards and promote nuclear power, renewable energy and oil exploration.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：warming@38:1.6258 | renewable@48:0.5286 | nuclear@46:0.5278。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 562. test:6936 | Sci/Tech → Business

预测置信度 0.5575；真实类概率 0.3520；前两类概率差 0.2055。
分词数 58；未知词比例 0.00%；特征：商业与科技边界。

China's Lenovo to buy IBM's PC business TOKYO - China's Lenovo Group Ltd. signed a definitive agreement on Wednesday to acquire IBM Corp.'s personal computing division. Lenovo will pay US\$1.25 billion in cash for the business, which is expected to transform it into the world's number three PC maker, the companies announced.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：lenovo@29:1.7969 | division@28:1.4214 | pay@31:1.3833。
能把预测改为真实类的单词遮挡数：7。仅表示局部敏感性，不代表已证明因果原因。

## 563. test:6938 | Business → Sci/Tech

预测置信度 0.5483；真实类概率 0.4311；前两类概率差 0.1172。
分词数 32；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Automakers sue California over emissions FRESNO, Calif. -- Automobile manufacturers sued on Tuesday to block the world #39;s toughest vehicle emissions standards, adopted by California regulators in September to cut greenhouse gases.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：standards@21:1.1620 | emissions@20:0.4089 | vehicle@19:0.1986。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 564. test:6951 | Sci/Tech → World

预测置信度 0.7854；真实类概率 0.1101；前两类概率差 0.6753。
分词数 25；未知词比例 0.00%；特征：需结合语义人工复核。

Hawks Evicted From New York City Perch (AP) AP - Pale Male the city hawk was evicted from his nest, and the flap has already begun.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：york@4:2.6093 | ap@7:1.8312 | city@5:1.7351。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 565. test:6959 | Business → Sports

预测置信度 0.5981；真实类概率 0.2845；前两类概率差 0.3135。
分词数 27；未知词比例 0.00%；特征：需结合语义人工复核。

Virgin dips its toe into the Pacific SIR Richard Branson did not disappoint with his stunts yesterday, flying into Sydney to promote his international airline Virgin Atlantic.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：his@22:0.6447 | yesterday@16:0.4062 | his@14:0.3914。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 566. test:6965 | World → Business

预测置信度 0.5221；真实类概率 0.3040；前两类概率差 0.2181。
分词数 33；未知词比例 0.00%；特征：世界与商业边界。

Justices hear cases on shipping wine (USATODAY.com) USATODAY.com - States that block direct shipments of wine to consumers from out-of-state wineries faced skeptical comments from Supreme Court justices on Tuesday.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：wine@5:1.3321 | shipping@4:1.2875 | consumers@18:0.6094。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 567. test:6973 | World → Business

预测置信度 0.8312；真实类概率 0.0342；前两类概率差 0.6969。
分词数 31；未知词比例 0.00%；特征：世界与商业边界。

Schwarzenegger Vows to Defend Emissions Law Toyota, General Motors and seven other automakers filed suit to block California's new greenhouse gas regulation, which was approved by the state in September.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：automakers@12:1.3301 | motors@8:0.9291 | filed@13:0.9255。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 568. test:6980 | Business → Sports

预测置信度 0.6694；真实类概率 0.1880；前两类概率差 0.4814。
分词数 39；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

Virgin wishing for Melbourne Sir Richard said yesterday Melbourne was on his wish list, with flights to London possibly through Hong Kong or Bangkok. The British billionaire landed in Sydney yesterday aboard Virgin Atlantic #39;s inaugural Australian flight.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：39@34:0.8704 | with@14:0.7563 | wish@12:0.6607。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 569. test:6992 | Sci/Tech → Business

预测置信度 0.8547；真实类概率 0.1433；前两类概率差 0.7113。
分词数 36；未知词比例 0.00%；特征：商业与科技边界。

Nortel to file restated results next year Nortel Networks said today that after months of trying to untangle faulty financial results, it won't file its 2003 and first-half 2004 results until early next year.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：financial@19:1.6743 | faulty@18:0.6728 | results@20:0.6646。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 570. test:7013 | Business → Sci/Tech

预测置信度 0.9375；真实类概率 0.0595；前两类概率差 0.8780。
分词数 38；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Ellison: Data Hubs Could #39;ve Prevented 9/11 SAN FRANCISCO -- Oracle CEO Larry Ellison is convinced that had the intelligence community used a unified database from Oracle, the terrorist attacks on 9/11 would never have happened.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：community@21:0.8641 | intelligence@20:0.7938 | oracle@11:0.5016。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 571. test:7017 | World → Sci/Tech

预测置信度 0.5987；真实类概率 0.3708；前两类概率差 0.2279。
分词数 22；未知词比例 0.00%；特征：需结合语义人工复核。

English 'world language' forecast A third of people on the planet will be learning English in the next decade, \says a report.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：planet@10:0.8629 | will@11:0.5572 | language@2:0.1256。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 572. test:7030 | Business → World

预测置信度 0.6751；真实类概率 0.0801；前两类概率差 0.5504。
分词数 53；未知词比例 9.43%；特征：世界与商业边界；含HTML实体或编码痕迹。

Without Batting An Eyelash : A very French welcome for a new &lt;b&gt;...&lt;/b&gt; THAT night, it seemed as if three or four parties were going on at once in Cosmo Manille. Wrong, palanggas. Actually, there were five in Makati alone, and one of them had a stream of traffic 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：parties@26:0.6468 | welcome@7:0.5397 | four@25:0.4778。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 573. test:7031 | Sci/Tech → World

预测置信度 0.8580；真实类概率 0.0242；前两类概率差 0.7403。
分词数 34；未知词比例 14.71%；特征：未知词比例>=10%。

Large Gambian Rats Worry Fla. Officials (AP) AP - The Florida Keys, already dealing with invasive exotics from melaleuca to iguanas, have added another to the list of unwanted newcomers: the African Gambian pouch rat.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：fla@4:4.1978 | ap@7:1.8151 | ap@6:1.3375。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 574. test:7051 | Business → Sci/Tech

预测置信度 0.7629；真实类概率 0.2327；前两类概率差 0.5302。
分词数 43；未知词比例 2.33%；特征：商业与科技边界；含HTML实体或编码痕迹。

Amazon #39;s UK DVD Rentals Might Presage War with Netflix Analysts said Amazon #39;s launch of the DVD rental service in the UK might be to test its approach and streamline the logistically difficult process of handling DVDs through the mail.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：process@36:0.6999 | difficult@35:0.3253 | dvd@4:0.2098。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 575. test:7061 | Business → Sports

预测置信度 0.3321；真实类概率 0.2303；前两类概率差 0.0068。
分词数 30；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Opel to cut payroll by 9,500 Opel gets by without layoffs. Readers taking in these and similar headlines earlier this week were well advised to read the fine print.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：taking@13:1.1998 | readers@12:0.6747 | layoffs@11:0.4196。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 576. test:7068 | Sci/Tech → Business

预测置信度 0.9646；真实类概率 0.0353；前两类概率差 0.9293。
分词数 23；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Nextel, Sprint Talk Merger Nextel Communications Inc. and Sprint Corp. are negotiating a possible merger, according to a source familiar with the discussions.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：merger@3:1.8855 | inc@6:0.9072 | sprint@1:0.8847。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 577. test:7081 | Business → World

预测置信度 0.4312；真实类概率 0.3459；前两类概率差 0.0853。
分词数 44；未知词比例 4.55%；特征：世界与商业边界；前两类接近:概率差<0.2。

Japan's comics retool the art Animation in America once meant Mickey Mouse and Winnie the Pooh. These days, it's just as likely to mean Japanese fighting cyborgs, doe-eyed schoolgirls, and sinister monsters -- thanks in large part to people like John Ledford.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：these@17:0.3321 | in@7:0.2575 | japanese@26:0.1946。
能把预测改为真实类的单词遮挡数：2。仅表示局部敏感性，不代表已证明因果原因。

## 578. test:7089 | Sci/Tech → World

预测置信度 0.4522；真实类概率 0.3547；前两类概率差 0.0976。
分词数 43；未知词比例 4.65%；特征：前两类接近:概率差<0.2；含HTML实体或编码痕迹。

Lonely whale #39;s song remains a mystery A lone whale with a voice unlike any other has been wandering the Pacific for the past 12 years. Marine biologist Mary Ann Daher of Woods Hole Oceanographic Institution in Massachusetts, US, and her colleagues 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：woods@33:1.5991 | song@4:1.1943 | remains@5:0.8397。
能把预测改为真实类的单词遮挡数：8。仅表示局部敏感性，不代表已证明因果原因。

## 579. test:7108 | Business → World

预测置信度 0.5314；真实类概率 0.3811；前两类概率差 0.1503。
分词数 20；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2；短文本<=20词。

Cardinal Picks a Lilly Cardinal Health's deal with Lilly suggests the new fee-for-service model is gaining traction.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：s@6:1.1585 | suggests@10:0.8656 | lilly@9:0.6090。
能把预测改为真实类的单词遮挡数：3。仅表示局部敏感性，不代表已证明因果原因。

## 580. test:7122 | Sci/Tech → Business

预测置信度 0.4953；真实类概率 0.4293；前两类概率差 0.0659。
分词数 37；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

US Supreme Court to Decide Grokster Case The US Supreme Court on Friday agreed to consider whether Internet file-trading networks should be held responsible when their users copy music, movies and other protected works without permission.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：consider@15:1.5306 | friday@12:1.3941 | agreed@13:1.3916。
能把预测改为真实类的单词遮挡数：23。仅表示局部敏感性，不代表已证明因果原因。

## 581. test:7132 | World → Sci/Tech

预测置信度 0.6825；真实类概率 0.1339；前两类概率差 0.4997。
分词数 40；未知词比例 0.00%；特征：含HTML实体或编码痕迹。

Plant a tree at Easter urges Nobel laureate world to plant trees at Easter as a symbol of renewal and to protect the planet. planted, quot; Maathai told Reuters Television in Oslo, where she received the 2004 Nobel Peace Prize.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：plant@10:0.8081 | trees@11:0.4706 | planet@23:0.3225。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 582. test:7148 | Sci/Tech → Business

预测置信度 0.9834；真实类概率 0.0160；前两类概率差 0.9674。
分词数 36；未知词比例 2.78%；特征：商业与科技边界；高置信错误>=0.9。

Sources: Sprint, Nextel closing in on \$36B deal Sprint Corp. is in advanced talks to buy Nextel Communications Inc. for more than \$36 billion in a mostly stock deal, sources familiar with the situation said today.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：buy@15:1.7528 | talks@13:0.9122 | a@25:0.6538。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 583. test:7164 | Sports → Business

预测置信度 0.9325；真实类概率 0.0445；前两类概率差 0.8880。
分词数 38；未知词比例 0.00%；特征：高置信错误>=0.9；含HTML实体或编码痕迹。

Cuts offered, issue remains tax or cap The union #39;s proposal to end the lockout, made Thursday at the league #39;s Canadian headquarters, calls for a tax that would penalize -- and perhaps deter -- high-end payrolls.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：tax@4:3.5629 | remains@3:1.5686 | tax@28:0.6600。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 584. test:7228 | Business → World

预测置信度 0.9948；真实类概率 0.0038；前两类概率差 0.9910。
分词数 31；未知词比例 0.00%；特征：世界与商业边界；高置信错误>=0.9；含HTML实体或编码痕迹。

Indonesian diplomats asked to help improve RI #39;s bad image JAKARTA (Antara): President Susilo Yudhoyono asked Indonesian diplomats on Monday to help the government improve Indonesia #39;s bad image.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：indonesian@17:1.4114 | susilo@14:1.1895 | president@13:0.8511。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 585. test:7238 | World → Sports

预测置信度 0.8539；真实类概率 0.1354；前两类概率差 0.7186。
分词数 19；未知词比例 0.00%；特征：短文本<=20词。

Bangladesh boss slams detractors Bangladesh's coach says they still deserve Test status after their 30th defeat, to India.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：coach@6:2.0131 | their@14:0.4076 | defeat@16:0.3794。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 586. test:7239 | World → Sci/Tech

预测置信度 0.8049；真实类概率 0.0404；前两类概率差 0.6501。
分词数 24；未知词比例 0.00%；特征：需结合语义人工复核。

Week's delay for Delta launcher Boeing's new heavy-lift Delta 4 rocket must wait a further week before making its maiden flight.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：rocket@13:1.6566 | delta@11:0.6328 | 4@12:0.4713。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 587. test:7262 | Sci/Tech → World

预测置信度 0.7746；真实类概率 0.0832；前两类概率差 0.6915。
分词数 24；未知词比例 12.50%；特征：未知词比例>=10%。

Travel Column: Australia Through Aboriginal Eyes This week's TravelWatch column profiles Anangu Tours, an Aborigine-owned tour company in Australia's Red Center.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：eyes@5:1.3548 | australia@2:0.8706 | aboriginal@4:0.7242。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 588. test:7278 | Sports → Business

预测置信度 0.5233；真实类概率 0.3420；前两类概率差 0.1813。
分词数 40；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

Report Says N.H.L. Will Reject Proposal The N.H.L. appears poised to reject a proposal made by the players union, which included a 24 percent reduction in pay and other concessions but not a hard salary cap.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：pay@30:1.0084 | union@22:0.7968 | reduction@28:0.5643。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 589. test:7290 | Business → Sci/Tech

预测置信度 0.7813；真实类概率 0.2079；前两类概率差 0.5733。
分词数 30；未知词比例 0.00%；特征：商业与科技边界。

Symantec Said to Be in Talks for Veritas Symantec, which produces the Norton line of computer products, is in talks to acquire Veritas Software, a maker of data backup programs.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：computer@15:0.3404 | products@16:0.2682 | symantec@0:0.1328。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 590. test:7305 | Sci/Tech → Business

预测置信度 0.6717；真实类概率 0.0975；前两类概率差 0.4518。
分词数 29；未知词比例 3.45%；特征：商业与科技边界。

Take Two Torts and Call Me in the Morning The friction that sometimes strains the patient-doctor relationship when lawyers seek medical care is at an all-time high.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：medical@21:1.7550 | care@22:1.0229 | that@11:0.7613。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 591. test:7325 | Sci/Tech → Business

预测置信度 0.5945；真实类概率 0.4021；前两类概率差 0.1923。
分词数 51；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2。

Worldwide PC Market Seen Doubling by 2010  NEW YORK (Reuters) - The number of personal computers  worldwide is expected to double to about 1.3 billion by 2010,  driven by explosive growth in emerging markets such as China,  Russia and India, according to a report released on Tuesday by  Forrester Research Inc.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：york@8:1.4636 | reuters@9:1.3289 | the@10:0.8353。
能把预测改为真实类的单词遮挡数：6。仅表示局部敏感性，不代表已证明因果原因。

## 592. test:7326 | Sports → Sci/Tech

预测置信度 0.5790；真实类概率 0.3925；前两类概率差 0.1865。
分词数 30；未知词比例 0.00%；特征：前两类接近:概率差<0.2。

EA Signs Five-Year Exclusive NFL Deal Electronic Arts announced an exclusive licensing relationships with the National Football League and PLAYERS INC to develop, publish and distribute interactive football games.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：electronic@7:2.5285 | arts@8:2.1691 | inc@21:1.1380。
能把预测改为真实类的单词遮挡数：5。仅表示局部敏感性，不代表已证明因果原因。

## 593. test:7369 | Business → World

预测置信度 0.8402；真实类概率 0.0819；前两类概率差 0.7583。
分词数 58；未知词比例 0.00%；特征：世界与商业边界。

China succeeds in cooling economy, but 2005 likely to prove just as tough (AFP) AFP - China can claim some success in the battle to cool its roaring economy in 2004 with a series of macro policies helping prevent another boom-bust cycle, but much remains to be done if Beijing is to avoid increasing wrangles with trade partners.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：afp@14:2.7538 | afp@13:2.3119 | china@15:0.5921。
能把预测改为真实类的单词遮挡数：1。仅表示局部敏感性，不代表已证明因果原因。

## 594. test:7413 | Business → World

预测置信度 0.8349；真实类概率 0.1601；前两类概率差 0.6747。
分词数 28；未知词比例 0.00%；特征：世界与商业边界。

Bush Pledges Strong-Dollar Policy President Bush meets with Italian Prime Minister Silvio Berlusconi in the Oval Office of the White House, Wednesday, Dec. 15, 2004, in Washington.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：silvio@12:1.0843 | bush@6:1.0263 | berlusconi@13:0.7944。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 595. test:7418 | Sci/Tech → Business

预测置信度 0.8136；真实类概率 0.1248；前两类概率差 0.6888。
分词数 46；未知词比例 2.17%；特征：商业与科技边界。

MicroStrategy Turnover Draws Analyst Scrutiny MicroStrategy Inc. said yesterday that president and chief financial officer Eric F. Brown had resigned and that founder Michael J. Saylor would again hold the company's top three jobs, prompting some analysts to raise concerns about the company's stock.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：yesterday@8:0.9129 | said@7:0.6896 | financial@13:0.6346。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 596. test:7426 | Sci/Tech → World

预测置信度 0.4780；真实类概率 0.4481；前两类概率差 0.0299。
分词数 75；未知词比例 1.33%；特征：前两类接近:概率差<0.2。

R.I.P. Gary Webb -- Unembedded Reporter The finest journalist ever to get fired for telling the truth is dead at age 49. The official cause of death on the death certificate will be suicide. But, as we shall see, he had much help getting to that point. The story of the life and death of Gary Webb says much about the state of American politics and what passes as "journalism" in today's America. 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：dead@19:0.4963 | death@30:0.4495 | american@64:0.3948。
能把预测改为真实类的单词遮挡数：39。仅表示局部敏感性，不代表已证明因果原因。

## 597. test:7440 | Sci/Tech → World

预测置信度 0.9455；真实类概率 0.0172；前两类概率差 0.9200。
分词数 17；未知词比例 0.00%；特征：高置信错误>=0.9；短文本<=20词。

A Distraction as a Deadline Approaches As the holidays approach, Christmas spirit is a bargain-hunting essential.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：hunting@15:3.5180 | essential@16:2.5106 | bargain@14:1.8552。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 598. test:7470 | Business → Sci/Tech

预测置信度 0.9308；真实类概率 0.0577；前两类概率差 0.8731。
分词数 28；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Broadband charges set to tumble The cost of broadband internet access is likely to fall after Ofcom ordered British Telecom to cut the amount it charges internet providers.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：british@18:0.3935 | broadband@0:0.3301 | broadband@8:0.3039。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 599. test:7476 | World → Sci/Tech

预测置信度 0.5996；真实类概率 0.3974；前两类概率差 0.2022。
分词数 30；未知词比例 6.67%；特征：需结合语义人工复核。

Britons still prefer fish n'chips (AFP) AFP - Traditional fish-and-chips along with cherished pub grub remain the dishes of choice for Britons outstripping Chinese or Indian take-aways.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：fish@3:1.8666 | prefer@2:0.9453 | fish@9:0.6071。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。

## 600. test:7492 | Business → Sci/Tech

预测置信度 0.9814；真实类概率 0.0115；前两类概率差 0.9699。
分词数 41；未知词比例 4.88%；特征：商业与科技边界；高置信错误>=0.9；含HTML实体或编码痕迹。

FCC Mulls Airborne Mobile Phone Use Although there may have been technical limitations at the time the cell phone ban was established, according to IDC #39;s Shiv Bakhshi, it is unclear why the ban has remained in place, given that 

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：idc@24:0.7976 | cell@17:0.4346 | phone@4:0.1842。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 601. test:7522 | Sci/Tech → Business

预测置信度 0.5286；真实类概率 0.4583；前两类概率差 0.0703。
分词数 16；未知词比例 0.00%；特征：商业与科技边界；前两类接近:概率差<0.2；短文本<=20词。

Panasonic Races to Meet Plasma Demand Company is expanding production to deliver more flat-panel TVs.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：demand@5:1.0067 | company@6:0.6774 | production@9:0.4932。
能把预测改为真实类的单词遮挡数：11。仅表示局部敏感性，不代表已证明因果原因。

## 602. test:7539 | World → Sci/Tech

预测置信度 0.9915；真实类概率 0.0041；前两类概率差 0.9872。
分词数 30；未知词比例 0.00%；特征：高置信错误>=0.9。

Mars water tops science honours The discovery that salty, acidic water once flowed across the surface of Mars has topped a list of the 10 key scientific advances of 2004.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：water@1:0.6010 | science@3:0.3896 | mars@0:0.3784。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 603. test:7542 | Sci/Tech → Business

预测置信度 0.9060；真实类概率 0.0872；前两类概率差 0.8188。
分词数 34；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

Boeing casts eyes on live TV over Connexion service The Boeing Co. is planning to add live television to its Connexion by Boeing service during 2005, a company executive said in a recent interview.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：co@11:0.8377 | boeing@10:0.7280 | over@6:0.6057。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 604. test:7564 | Business → World

预测置信度 0.5853；真实类概率 0.4145；前两类概率差 0.1708。
分词数 47；未知词比例 0.00%；特征：世界与商业边界；前两类接近:概率差<0.2。

Russia shrugs off US court freeze on oil giant Yukos auction MOSCOW (AFP) - Russia forged ahead with the weekend auction of the core asset of crippled oil giant Yukos despite a disputed US court order barring the sale, with state-controlled gas giant Gazprom entering the bidding.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：afp@12:2.4671 | russia@13:0.9378 | giant@8:0.8000。
能把预测改为真实类的单词遮挡数：6。仅表示局部敏感性，不代表已证明因果原因。

## 605. test:7567 | Sci/Tech → Business

预测置信度 0.9027；真实类概率 0.0972；前两类概率差 0.8055。
分词数 26；未知词比例 0.00%；特征：商业与科技边界；高置信错误>=0.9。

This week in merger news This week saw three merger deals worth about \$60 billion--including one that ranks as the largest software merger in history.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：deals@10:1.0546 | merger@9:1.0057 | billion@14:0.6447。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 606. test:7585 | World → Business

预测置信度 0.9607；真实类概率 0.0049；前两类概率差 0.9264。
分词数 29；未知词比例 3.45%；特征：世界与商业边界；高置信错误>=0.9。

Pricey Drug Trials Turn Up Few New Blockbusters The \$500 billion drug industry is stumbling badly in its core business of finding new medicines, while aggressively marketing existing drugs.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：marketing@26:1.2821 | aggressively@25:0.7031 | industry@12:0.6913。
能把预测改为真实类的单词遮挡数：0。仅表示局部敏感性，不代表已证明因果原因。

## 607. test:7589 | Sports → World

预测置信度 0.6022；真实类概率 0.2211；前两类概率差 0.3811。
分词数 36；未知词比例 0.00%；特征：需结合语义人工复核。

The Newest Hope ; Marriage of Necessity Just Might Work Out NEW YORK - The TV lights were on, the cameras rolled and the symphony of cameras flashing in his face blinded Pedro Martinez - but not for long.

单词遮挡敏感项（词@0起始位置:错误类相对真实类 logit 差的降幅）：hope@2:1.8435 | newest@1:1.6793 | york@11:1.2323。
能把预测改为真实类的单词遮挡数：4。仅表示局部敏感性，不代表已证明因果原因。
