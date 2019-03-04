#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AdvanceOrder import AdvanceOrder


class KoubeiMallScanpurchasePreorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMallScanpurchasePreorderQueryResponse, self).__init__()
        self._advance_order = None

    @property
    def advance_order(self):
        return self._advance_order

    @advance_order.setter
    def advance_order(self, value):
        if isinstance(value, AdvanceOrder):
            self._advance_order = value
        else:
            self._advance_order = AdvanceOrder.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMallScanpurchasePreorderQueryResponse, self).parse_response_content(response_content)
        if 'advance_order' in response:
            self.advance_order = response['advance_order']
