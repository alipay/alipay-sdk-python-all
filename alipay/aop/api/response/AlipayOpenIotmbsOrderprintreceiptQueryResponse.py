#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LightPosOrderSku import LightPosOrderSku


class AlipayOpenIotmbsOrderprintreceiptQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotmbsOrderprintreceiptQueryResponse, self).__init__()
        self._pay_channel = None
        self._pay_time = None
        self._price = None
        self._real_price = None
        self._sku_list = None
        self._status = None

    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def real_price(self):
        return self._real_price

    @real_price.setter
    def real_price(self, value):
        self._real_price = value
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                if isinstance(i, LightPosOrderSku):
                    self._sku_list.append(i)
                else:
                    self._sku_list.append(LightPosOrderSku.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotmbsOrderprintreceiptQueryResponse, self).parse_response_content(response_content)
        if 'pay_channel' in response:
            self.pay_channel = response['pay_channel']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'price' in response:
            self.price = response['price']
        if 'real_price' in response:
            self.real_price = response['real_price']
        if 'sku_list' in response:
            self.sku_list = response['sku_list']
        if 'status' in response:
            self.status = response['status']
