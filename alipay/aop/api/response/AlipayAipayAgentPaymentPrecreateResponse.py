#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAipayAgentPaymentPrecreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayAgentPaymentPrecreateResponse, self).__init__()
        self._amt_pre_pay_id = None
        self._qr_code_url = None

    @property
    def amt_pre_pay_id(self):
        return self._amt_pre_pay_id

    @amt_pre_pay_id.setter
    def amt_pre_pay_id(self, value):
        self._amt_pre_pay_id = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayAgentPaymentPrecreateResponse, self).parse_response_content(response_content)
        if 'amt_pre_pay_id' in response:
            self.amt_pre_pay_id = response['amt_pre_pay_id']
        if 'qr_code_url' in response:
            self.qr_code_url = response['qr_code_url']
