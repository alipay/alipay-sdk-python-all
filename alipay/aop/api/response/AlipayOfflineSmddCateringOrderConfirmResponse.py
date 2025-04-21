#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityBean import ActivityBean
from alipay.aop.api.domain.SkuBean import SkuBean


class AlipayOfflineSmddCateringOrderConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineSmddCateringOrderConfirmResponse, self).__init__()
        self._activity_list = None
        self._delivery_fee = None
        self._discount_notice_text = None
        self._discounted_price = None
        self._exception_msg = None
        self._item_total_price = None
        self._original_price = None
        self._package_fee = None
        self._payment_price = None
        self._sku_list = None
        self._total_item = None

    @property
    def activity_list(self):
        return self._activity_list

    @activity_list.setter
    def activity_list(self, value):
        if isinstance(value, list):
            self._activity_list = list()
            for i in value:
                if isinstance(i, ActivityBean):
                    self._activity_list.append(i)
                else:
                    self._activity_list.append(ActivityBean.from_alipay_dict(i))
    @property
    def delivery_fee(self):
        return self._delivery_fee

    @delivery_fee.setter
    def delivery_fee(self, value):
        self._delivery_fee = value
    @property
    def discount_notice_text(self):
        return self._discount_notice_text

    @discount_notice_text.setter
    def discount_notice_text(self, value):
        self._discount_notice_text = value
    @property
    def discounted_price(self):
        return self._discounted_price

    @discounted_price.setter
    def discounted_price(self, value):
        self._discounted_price = value
    @property
    def exception_msg(self):
        return self._exception_msg

    @exception_msg.setter
    def exception_msg(self, value):
        self._exception_msg = value
    @property
    def item_total_price(self):
        return self._item_total_price

    @item_total_price.setter
    def item_total_price(self, value):
        self._item_total_price = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def package_fee(self):
        return self._package_fee

    @package_fee.setter
    def package_fee(self, value):
        self._package_fee = value
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
        response = super(AlipayOfflineSmddCateringOrderConfirmResponse, self).parse_response_content(response_content)
        if 'activity_list' in response:
            self.activity_list = response['activity_list']
        if 'delivery_fee' in response:
            self.delivery_fee = response['delivery_fee']
        if 'discount_notice_text' in response:
            self.discount_notice_text = response['discount_notice_text']
        if 'discounted_price' in response:
            self.discounted_price = response['discounted_price']
        if 'exception_msg' in response:
            self.exception_msg = response['exception_msg']
        if 'item_total_price' in response:
            self.item_total_price = response['item_total_price']
        if 'original_price' in response:
            self.original_price = response['original_price']
        if 'package_fee' in response:
            self.package_fee = response['package_fee']
        if 'payment_price' in response:
            self.payment_price = response['payment_price']
        if 'sku_list' in response:
            self.sku_list = response['sku_list']
        if 'total_item' in response:
            self.total_item = response['total_item']
