#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChipDTO import ChipDTO


class AntfortuneStockPokerChipSendResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockPokerChipSendResponse, self).__init__()
        self._chip = None

    @property
    def chip(self):
        return self._chip

    @chip.setter
    def chip(self, value):
        if isinstance(value, ChipDTO):
            self._chip = value
        else:
            self._chip = ChipDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockPokerChipSendResponse, self).parse_response_content(response_content)
        if 'chip' in response:
            self.chip = response['chip']
