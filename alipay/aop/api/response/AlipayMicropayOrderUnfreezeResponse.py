#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UnfreezeOrderDetail import UnfreezeOrderDetail


class AlipayMicropayOrderUnfreezeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMicropayOrderUnfreezeResponse, self).__init__()
        self._unfreeze_order_detail = None

    @property
    def unfreeze_order_detail(self):
        return self._unfreeze_order_detail

    @unfreeze_order_detail.setter
    def unfreeze_order_detail(self, value):
        if isinstance(value, UnfreezeOrderDetail):
            self._unfreeze_order_detail = value
        else:
            self._unfreeze_order_detail = UnfreezeOrderDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMicropayOrderUnfreezeResponse, self).parse_response_content(response_content)
        if 'unfreeze_order_detail' in response:
            self.unfreeze_order_detail = response['unfreeze_order_detail']
