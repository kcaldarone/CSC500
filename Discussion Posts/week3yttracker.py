from fractions import Fraction #used in lines 60-62 & 76-78

#IRL Example 3 - YouTube Tracker
class Video: #challening myself by making an object array
    def __init__(self, title, viewCount, contentType, likeCount, dislikeCount, commentCount, videoLength, avgWatchTime):
        self.title = title
        self.viewCount = viewCount
        self.contentType = contentType
        self.likeCount = likeCount
        self.dislikeCount = dislikeCount
        self.commentCount = commentCount
        self.videoLength = videoLength #videoLength is in seconds
        self.avgWatchTime = avgWatchTime #avgWatchTime is in seconds
#creating base array
videos = []
#adding Video objects (title, viewCount, contentType, likeCount, dislikeCount, commentCount, videoLength, avgWatchTime)
videos[0] = Video('How I Would Remake Garten of Banban 1-3', 300000, 'Essay', 10000, 100, 580, 1958, 1936)
videos[1] = Video('How I Would Remake Garten of Banban 4-6', 424000, 'Essay', 15500, 130, 674, 2759, 2700)
videos[2] = Video('Drawing the Redesigns of Garten of Banban Characters', 190000, 'Art', 5000, 69, 263, 2340, 1353)
videos[3] = Video('FNAF: Into The Pit is FINALLY Here! (Full Game + All Endings)', 391000, 'Gameplay', 14677, 198, 1080, 4100, 4097)
videos[4] = Video('Breaking Poppy Playtime Chapter 3', 793000, 'Gameplay', 27000, 500, 1987, 2420, 2410)
videos[5] = Video('Breaking Down How I Do Character Design', 239000, 'Art', 6666, 111, 555, 2020, 1800)
#starting all counts (is there a way to shorten this? It just feels messy)
count,essayViews,artViews,gameplayViews,essayCount,artCount,gameplayCount,essayComment,artComment,gameplayComment,essayLikes,artLikes,gameplayLikes,essayDislikes,artDislikes,gameplayDislikes,essayVidLen,artVidLen,gameplayVidLen,essayWatchTime,artWatchTime,gameplayWatchTime = 0
while count < len(videos):
    if(videos[count].contentType == 'Essay'):
        essayCount = essayCount + 1
        essayViews = essayViews + videos[count].viewCount
        essayLikes = essayLikes + videos[count].likeCount
        essayDislikes = essayDislikes + videos[count].dislikeCount
        essayComments = essayComments + videos[count].commentCount
        essayVidLen = essayVidLen + videos[count].videoLength
        essayWatchTime = essayWatchTime + videos[count].avgWatchTime
    elif(videos[count].contentType == 'Art'):
        artCount = artCount + 1
        artViews = artViews + videos[count].viewCount
        artLikes = artLikes + videos[count].likeCount
        artDislikes = artDislikes + videos[count].dislikeCount
        artComments = artComments + videos[count].commentCount
        artVidLen = artVidLen + videos[count].videoLength
        artWatchTime = artWatchTime + videos[count].avgWatchTime
    else: #gameplay videos
        gameplayCount = gameplayCount + 1
        gameplayViews = gameplayViews + videos[count].viewCount
        gameplayLikes = gameplayLikes + videos[count].likeCount
        gameplayDislikes = gameplayDislikes + videos[count].dislikeCount
        gameplayComments = gameplayComments + videos[count].commentCount
        gameplayVidLen = gameplayVidLen + videos[count].videoLength
        gameplayWatchTime = gameplayWatchTime + videos[count].avgWatchTime
    count = count + 1
#most views
essayTotal = essayViews/essayCount
artTotal = artViews/artCount
gameplayTotal = gameplayViews/gameplayCount
totalList = [essayTotal,artTotal,gameplayTotal]
totalList.sort
print("The most viewed genre of video you make is " + str(totalList[-1]))

#best like to dislike ratio 
essayLikeDislike = Fraction(essayLikes,essayDislikes)
artLikeDislike = Fraction(artLikes,artDislikes)
gameplayLikeDislike = Fraction(gameplayLikes,gameplayDislikes)
likeDislikeList = [essayLikeDislike,artLikeDislike,gameplayLikeDislike]
likeDislikeList.sort
print("The video genre you post with the best like to dislike ratio is " +str(likeDislikeList[-1]))

#most comments
avgEssayComments = essayComment / essayCount
avgArtComments = artComment / artCount
avgGameplayComments = gameplayComment / gameplayCount
commentList = [avgEssayComments,avgArtComments,avgGameplayComments]
commentList.sort
print("The video genre with the most comments per video you make is " + str(commentList[-1]))

#best avg view time per video
essayAvgViewTime = Fraction(essayWatchTime,essayVidLen)
artAvgViewTime = Fraction(artWatchTime,artVidLen)
gameplayAvgViewTime = Fraction(gameplayWatchTime,gameplayVidLen)
watchTimeList = [essayAvgViewTime,artAvgViewTime,gameplayAvgViewTime]
watchTimeList.sort
print("The genre of video you make with the best average view time per video is " + srt(watchTimeList[-1]))