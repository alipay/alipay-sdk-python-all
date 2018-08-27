#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbAdvertIdentifyResponse import KbAdvertIdentifyResponse


class KoubeiAdvertCommissionAdvertPurchaseResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertCommissionAdvertPurchaseResponse, self).__init__()
        self._identify_codes = None

    @property
    def identify_codes(self):
        return self._identify_codes

    @identify_codes.setter
    def identify_codes(self, value):
        if isinstance(value, list):
            self._identify_codes = list()
            for i in value:
                if isinstance(i, KbAdvertIdentifyResponse):
                    self._identify_codes.append(i)
                else:
                    self._identify_codes.append(KbAdvertIdentifyResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertCommissionAdvertPurchaseResponse, self).parse_response_content(response_content)
        if 'identify_codes' in response:
            self.identify_codes = response['identify_codes']
