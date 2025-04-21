#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SkuBean import SkuBean


class AlipayOfflineSmddCustomerCartClearResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineSmddCustomerCartClearResponse, self).__init__()
        self._discount_text = None
        self._discounted_price = None
        self._original_price = None
        self._payment_price = None
        self._sku_list = None
        self._total_item = None

    @property
    def discount_text(self):
        return self._discount_text

    @discount_text.setter
    def discount_text(self, value):
        self._discount_text = value
    @property
    def discounted_price(self):
        return self._discounted_price

    @discounted_price.setter
    def discounted_price(self, value):
        self._discounted_price = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def payment_price(self):
        return self._payment_price

    @payment_price.setter
    def payment_price(self, value):
        self._payment_price = value
    @property
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                if isinstance(i, SkuBean):
                    self._sku_list.append(i)
                else:
                    self._sku_list.append(SkuBean.from_alipay_dict(i))
    @property
    def total_item(self):
        return self._total_item

    @total_item.setter
    def total_item(self, value):
        self._total_item = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineSmddCustomerCartClearResponse, self).parse_response_content(response_content)
        if 'discount_text' in response:
            self.discount_text = response['discount_text']
        if 'discounted_price' in response:
            self.discounted_price = response['discounted_price']
        if 'original_price' in response:
            self.original_price = response['original_price']
        if 'payment_price' in response:
            self.payment_price = response['payment_price']
        if 'sku_list' in response:
            self.sku_list = response['sku_list']
        if 'total_item' in response:
            self.total_item = response['total_item']
