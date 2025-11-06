#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CertBillDetail import CertBillDetail


class AlipayOpenMiniBillDailyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniBillDailyQueryResponse, self).__init__()
        self._response = None

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        if isinstance(value, CertBillDetail):
            self._response = value
        else:
            self._response = CertBillDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniBillDailyQueryResponse, self).parse_response_content(response_content)
        if 'response' in response:
            self.response = response['response']
