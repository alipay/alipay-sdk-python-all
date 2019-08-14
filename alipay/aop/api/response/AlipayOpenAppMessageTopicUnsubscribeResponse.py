#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppMessageTopicUnsubscribeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppMessageTopicUnsubscribeResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppMessageTopicUnsubscribeResponse, self).parse_response_content(response_content)
