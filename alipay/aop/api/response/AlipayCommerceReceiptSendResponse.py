#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EnvironmentInfo import EnvironmentInfo
from alipay.aop.api.domain.GreenOrderReceiptSendInfo import GreenOrderReceiptSendInfo


class AlipayCommerceReceiptSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceReceiptSendResponse, self).__init__()
        self._order_goods_list = None
        self._order_list = None

    @property
    def order_goods_list(self):
        return self._order_goods_list

    @order_goods_list.setter
    def order_goods_list(self, value):
        if isinstance(value, list):
            self._order_goods_list = list()
            for i in value:
                if isinstance(i, EnvironmentInfo):
                    self._order_goods_list.append(i)
                else:
                    self._order_goods_list.append(EnvironmentInfo.from_alipay_dict(i))
    @property
    def order_list(self):
        return self._order_list

    @order_list.setter
    def order_list(self, value):
        if isinstance(value, list):
            self._order_list = list()
            for i in value:
                if isinstance(i, GreenOrderReceiptSendInfo):
                    self._order_list.append(i)
                else:
                    self._order_list.append(GreenOrderReceiptSendInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceReceiptSendResponse, self).parse_response_content(response_content)
        if 'order_goods_list' in response:
            self.order_goods_list = response['order_goods_list']
        if 'order_list' in response:
            self.order_list = response['order_list']
