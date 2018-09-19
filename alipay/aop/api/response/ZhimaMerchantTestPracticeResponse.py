#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.XXXXsdasdasd import XXXXsdasdasd


class ZhimaMerchantTestPracticeResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantTestPracticeResponse, self).__init__()
        self._dddd = None
        self._sss = None

    @property
    def dddd(self):
        return self._dddd

    @dddd.setter
    def dddd(self, value):
        if isinstance(value, XXXXsdasdasd):
            self._dddd = value
        else:
            self._dddd = XXXXsdasdasd.from_alipay_dict(value)
    @property
    def sss(self):
        return self._sss

    @sss.setter
    def sss(self, value):
        self._sss = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantTestPracticeResponse, self).parse_response_content(response_content)
        if 'dddd' in response:
            self.dddd = response['dddd']
        if 'sss' in response:
            self.sss = response['sss']
