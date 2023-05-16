#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiTradeBencftestRefuseResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeBencftestRefuseResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(KoubeiTradeBencftestRefuseResponse, self).parse_response_content(response_content)
