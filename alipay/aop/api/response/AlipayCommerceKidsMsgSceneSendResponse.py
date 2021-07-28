#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceKidsMsgSceneSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceKidsMsgSceneSendResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceKidsMsgSceneSendResponse, self).parse_response_content(response_content)
