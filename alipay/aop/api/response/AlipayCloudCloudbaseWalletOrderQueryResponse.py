#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseWalletOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseWalletOrderQueryResponse, self).__init__()
        self._before_discount_money = None
        self._env_id = None
        self._gmt_create = None
        self._money = None
        self._num = None
        self._order_no = None
        self._order_status = None
        self._order_type = None
        self._product_code = None
        self._product_name = None

    @property
    def before_discount_money(self):
        return self._before_discount_money

    @before_discount_money.setter
    def before_discount_money(self, value):
        self._before_discount_money = value
    @property
    def env_id(self):
        return self._env_id

    @env_id.setter
    def env_id(self, value):
        self._env_id = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseWalletOrderQueryResponse, self).parse_response_content(response_content)
        if 'before_discount_money' in response:
            self.before_discount_money = response['before_discount_money']
        if 'env_id' in response:
            self.env_id = response['env_id']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'money' in response:
            self.money = response['money']
        if 'num' in response:
            self.num = response['num']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'order_type' in response:
            self.order_type = response['order_type']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'product_name' in response:
            self.product_name = response['product_name']
