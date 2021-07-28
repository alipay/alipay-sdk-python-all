#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneContentCommunityAlivemsgNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneContentCommunityAlivemsgNotifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AntfortuneContentCommunityAlivemsgNotifyResponse, self).parse_response_content(response_content)
