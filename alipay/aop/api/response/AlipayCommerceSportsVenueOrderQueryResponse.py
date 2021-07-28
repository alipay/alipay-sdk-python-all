#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ProductGroup import ProductGroup


class AlipayCommerceSportsVenueOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSportsVenueOrderQueryResponse, self).__init__()
        self._create_time = None
        self._desc = None
        self._order_id = None
        self._order_status = None
        self._payment_amount = None
        self._payment_time = None
        self._product_group_list = None
        self._refund_end_time = None
        self._refund_time = None
        self._total_amount = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def payment_time(self):
        return self._payment_time

    @payment_time.setter
    def payment_time(self, value):
        self._payment_time = value
    @property
    def product_group_list(self):
        return self._product_group_list

    @product_group_list.setter
    def product_group_list(self, value):
        if isinstance(value, list):
            self._product_group_list = list()
            for i in value:
                if isinstance(i, ProductGroup):
                    self._product_group_list.append(i)
                else:
                    self._product_group_list.append(ProductGroup.from_alipay_dict(i))
    @property
    def refund_end_time(self):
        return self._refund_end_time

    @refund_end_time.setter
    def refund_end_time(self, value):
        self._refund_end_time = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSportsVenueOrderQueryResponse, self).parse_response_content(response_content)
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'desc' in response:
            self.desc = response['desc']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'payment_amount' in response:
            self.payment_amount = response['payment_amount']
        if 'payment_time' in response:
            self.payment_time = response['payment_time']
        if 'product_group_list' in response:
            self.product_group_list = response['product_group_list']
        if 'refund_end_time' in response:
            self.refund_end_time = response['refund_end_time']
        if 'refund_time' in response:
            self.refund_time = response['refund_time']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
