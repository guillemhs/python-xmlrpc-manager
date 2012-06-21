#!/usr/bin/env python

"""
	Small example script that publish post with JPEG image
"""

# import library
import wordpresslib
import xmlrpclib
import datetime

print 'Example of posting.'

url = "http://localhost/wordpress/xmlrpc.php"
#url = "http://www.hottestporn4u.com/"
user = "pornmaster"
password = "pornmasterpiece"

# prepare client object
wp = wordpresslib.WordPressClient(url, user, password)

# select blog id
wp.selectBlog(0)

# upload image for post
# imageSrc = wp.newMediaObject('python.jpg')


# FIXME if imageSrc:
# create post object
post = wordpresslib.WordPressPost()
post.title = 'yui misaki 4 fd1965 mejicano'
post.description = '<div class="hreview-aggregate"><div class="item vcard"><div itemscope itemtype="http://schema.org/VideoObject"><h2 class="fn"><meta itemprop="embedURL" content="http://xhamster.com/xembed.php?video=1265168" /><iframe width="510" height="400" src="http://xhamster.com/xembed.php?video=1265168" frameborder="0" scrolling="no"></iframe><p><span itemprop="name">yui misaki 4 fd1965</span></h2><meta itemprop="duration" content="T10M31S" /><h3>(10m31s)</h3><meta itemprop="thumbnailUrl" content="http://et4.xhamster.com/t/024/1_1264024.jpg" /><p><span itemprop="description">This video is called yui misaki 4 fd1965</span></div></div><span class="rating"><span class="average">8.52</span> out of <span class="best"> 10 </span>based on <span class="votes">3736 </span>votes</span><p><img src="http://et4.xhamster.com/t/024/1_1264024.jpg" alt="yui misaki 4 fd1965"><br></div>'
post.categories  = ['latest updates','sex','fucking']
post.tags = ['porn', 'yui', 'misaki', '4', 'fd1965']
post.date_created = '20120610T00:56:00'

server = xmlrpclib.ServerProxy(url)
result = server.metaWeblog.getRecentPosts(url, user, password, 500)
print result
# do not publish post
wp.newPost(post, True)

print
print 'Posting successfull!'


