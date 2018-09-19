#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingToolMallPointsSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingToolMallPointsSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingToolMallPointsSyncResponse, self).parse_response_content(response_content)
