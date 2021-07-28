#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotAdvertiserAdModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotAdvertiserAdModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotAdvertiserAdModifyResponse, self).parse_response_content(response_content)
