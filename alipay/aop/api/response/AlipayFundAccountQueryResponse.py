#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExtCardInfo import ExtCardInfo


class AlipayFundAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAccountQueryResponse, self).__init__()
        self._available_amount = None
        self._ext_card_info = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def ext_card_info(self):
        return self._ext_card_info

    @ext_card_info.setter
    def ext_card_info(self, value):
        if isinstance(value, ExtCardInfo):
            self._ext_card_info = value
        else:
            self._ext_card_info = ExtCardInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayFundAccountQueryResponse, self).parse_response_content(response_content)
        if 'available_amount' in response:
            self.available_amount = response['available_amount']
        if 'ext_card_info' in response:
            self.ext_card_info = response['ext_card_info']
