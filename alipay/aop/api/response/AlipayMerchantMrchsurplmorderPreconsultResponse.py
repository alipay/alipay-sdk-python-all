#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantMrchsurplmorderPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantMrchsurplmorderPreconsultResponse, self).__init__()
        self._allowed = None
        self._reason_code = None
        self._reason_desc = None

    @property
    def allowed(self):
        return self._allowed

    @allowed.setter
    def allowed(self, value):
        self._allowed = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def reason_desc(self):
        return self._reason_desc

    @reason_desc.setter
    def reason_desc(self, value):
        self._reason_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantMrchsurplmorderPreconsultResponse, self).parse_response_content(response_content)
        if 'allowed' in response:
            self.allowed = response['allowed']
        if 'reason_code' in response:
            self.reason_code = response['reason_code']
        if 'reason_desc' in response:
            self.reason_desc = response['reason_desc']
