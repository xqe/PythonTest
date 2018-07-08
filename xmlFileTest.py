# coding=utf-8
import xml.dom.minidom
from SaxParser import MovieHandler

# 打开xml文档
dom = xml.dom.minidom.parse("abc.xml")

# 得到文档元素对象
root = dom.documentElement
print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE

print "----------------"
# 获得子标签
bb = root.getElementsByTagName("maxid")
print len(bb)
bb = bb[0]
print bb.nodeValue
print bb.nodeName

bb = root.getElementsByTagName('maxid')
bb = bb[0]
print bb.nodeName

bb = root.getElementsByTagName('login')
bb = bb[0]
print bb.nodeName

# 创建一个 XMLReader
parser = xml.sax.make_parser()
# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# 重写 ContextHandler
Handler = MovieHandler()
parser.setContentHandler(Handler)

parser.parse("movies.xml")