#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingPassShopBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingPassShopBindResponse, self).__init__()
        self._binded = None
        self._total_binded = None

    @property
    def binded(self):
        return self._binded

    @binded.setter
    def binded(self, value):
        self._binded = value
    @property
    def total_binded(self):
        return self._total_binded

    @total_binded.setter
    def total_binded(self, value):
        self._total_binded = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingPassShopBindResponse, self).parse_response_content(response_content)
        if 'binded' in response:
            self.binded = response['binded']
        if 'total_binded' in response:
            self.total_binded = response['total_binded']
