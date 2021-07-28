#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayAppTradeArrearSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppTradeArrearSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayPayAppTradeArrearSyncResponse, self).parse_response_content(response_content)
