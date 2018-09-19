#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingMallTradeBindResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingMallTradeBindResponse, self).__init__()
        self._remark = None

    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingMallTradeBindResponse, self).parse_response_content(response_content)
        if 'remark' in response:
            self.remark = response['remark']
