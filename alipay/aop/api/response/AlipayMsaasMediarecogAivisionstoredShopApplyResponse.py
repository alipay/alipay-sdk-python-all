#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogAivisionstoredShopApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogAivisionstoredShopApplyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogAivisionstoredShopApplyResponse, self).parse_response_content(response_content)
