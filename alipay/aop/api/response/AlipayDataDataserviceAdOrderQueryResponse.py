#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenOrderDetail import OpenOrderDetail


class AlipayDataDataserviceAdOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdOrderQueryResponse, self).__init__()
        self._order_detail = None

    @property
    def order_detail(self):
        return self._order_detail

    @order_detail.setter
    def order_detail(self, value):
        if isinstance(value, OpenOrderDetail):
            self._order_detail = value
        else:
            self._order_detail = OpenOrderDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdOrderQueryResponse, self).parse_response_content(response_content)
        if 'order_detail' in response:
            self.order_detail = response['order_detail']
