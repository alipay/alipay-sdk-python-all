#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarMaintainShopModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarMaintainShopModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarMaintainShopModifyResponse, self).parse_response_content(response_content)
