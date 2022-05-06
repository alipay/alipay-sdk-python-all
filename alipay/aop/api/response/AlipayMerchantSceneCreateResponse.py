#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantSceneCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantSceneCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMerchantSceneCreateResponse, self).parse_response_content(response_content)
