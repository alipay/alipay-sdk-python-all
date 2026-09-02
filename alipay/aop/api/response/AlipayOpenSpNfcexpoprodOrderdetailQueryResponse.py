#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderDetailOpenApiResponse import OrderDetailOpenApiResponse


class AlipayOpenSpNfcexpoprodOrderdetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNfcexpoprodOrderdetailQueryResponse, self).__init__()
        self._order_detail_list = None
        self._order_type = None

    @property
    def order_detail_list(self):
        return self._order_detail_list

    @order_detail_list.setter
    def order_detail_list(self, value):
        if isinstance(value, list):
            self._order_detail_list = list()
            for i in value:
                if isinstance(i, OrderDetailOpenApiResponse):
                    self._order_detail_list.append(i)
                else:
                    self._order_detail_list.append(OrderDetailOpenApiResponse.from_alipay_dict(i))
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNfcexpoprodOrderdetailQueryResponse, self).parse_response_content(response_content)
        if 'order_detail_list' in response:
            self.order_detail_list = response['order_detail_list']
        if 'order_type' in response:
            self.order_type = response['order_type']
