from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage
# Create your views here.

WECHAT_TOKEN = 'zqxt'
AppID = ''
AppSecret = ''
wechat_instance = WechatBasic(token=WECHAT_TOKEN,appid=AppID,appsecret=AppSecret)
def index(request):
	if request.method == 'GET':
		# 检验合法性
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')
    	#return HttpResponse("Hello, world. You're at the polls index.")
    	return HttpResponse(request.GET.get('echostr', ''), content_type="text/plain")

    # 解析本次请求的 XML 数据
    try:
        wechat_instance.parse_data(data=request.body)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')

    # 获取解析好的微信请求信息
    message = wechat_instance.get_message()
 	
 	my_string = "abcdeABCDE"
 	if message.MsgType=="text":
 		context=message.context
    	if context in my_string:
    		response = wechat_instance.response_text(content =('太开心了~您的反馈我们已经收到啦~我们还在成长阶段，希望我们能一起为更懂宝宝而共同努力~'))
    elif message.MsgType=="voice":
    	response = wechat_instance.response_text(content =('太开心了~您的反馈我们已经收到啦~我们还在成长阶段，希望我们能一起为更懂宝宝而共同努力~'))
    else:
    	response = wechat_instance.response_text(content =('请回复1,A-E或其他+原因~'))

    return HttpResponse(response, content_type="application/xml")