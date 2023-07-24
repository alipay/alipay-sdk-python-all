#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MallReceivePrResponseData import MallReceivePrResponseData


class AlipayDigitalmgmtPunchoutPrCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtPunchoutPrCreateResponse, self).__init__()
        self._response_data = None

    @property
    def response_data(self):
        return self._response_data

    @response_data.setter
    def response_data(self, value):
        if isinstance(value, MallReceivePrResponseData):
            self._response_data = value
        else:
            self._response_data = MallReceivePrResponseData.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtPunchoutPrCreateResponse, self).parse_response_content(response_content)
        if 'response_data' in response:
            self.response_data = response['response_data']
