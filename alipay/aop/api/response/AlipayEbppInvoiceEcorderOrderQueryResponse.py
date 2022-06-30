#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EcOrderItem import EcOrderItem
from alipay.aop.api.domain.EcOrderItem import EcOrderItem


class AlipayEbppInvoiceEcorderOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEcorderOrderQueryResponse, self).__init__()
        self._order_info = None
        self._sub_order_list = None

    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, value):
        if isinstance(value, EcOrderItem):
            self._order_info = value
        else:
            self._order_info = EcOrderItem.from_alipay_dict(value)
    @property
    def sub_order_list(self):
        return self._sub_order_list

    @sub_order_list.setter
    def sub_order_list(self, value):
        if isinstance(value, list):
            self._sub_order_list = list()
            for i in value:
                if isinstance(i, EcOrderItem):
                    self._sub_order_list.append(i)
                else:
                    self._sub_order_list.append(EcOrderItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEcorderOrderQueryResponse, self).parse_response_content(response_content)
        if 'order_info' in response:
            self.order_info = response['order_info']
        if 'sub_order_list' in response:
            self.sub_order_list = response['sub_order_list']
