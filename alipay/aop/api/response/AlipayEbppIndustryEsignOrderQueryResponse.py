#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryEsignOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryEsignOrderQueryResponse, self).__init__()
        self._ability_code = None
        self._completed_time = None
        self._enterprise_no = None
        self._estimated_price = None
        self._order_no = None
        self._out_biz_no = None
        self._product_no = None
        self._status = None
        self._use_time = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def completed_time(self):
        return self._completed_time

    @completed_time.setter
    def completed_time(self, value):
        self._completed_time = value
    @property
    def enterprise_no(self):
        return self._enterprise_no

    @enterprise_no.setter
    def enterprise_no(self, value):
        self._enterprise_no = value
    @property
    def estimated_price(self):
        return self._estimated_price

    @estimated_price.setter
    def estimated_price(self, value):
        self._estimated_price = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_no(self):
        return self._product_no

    @product_no.setter
    def product_no(self, value):
        self._product_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def use_time(self):
        return self._use_time

    @use_time.setter
    def use_time(self, value):
        self._use_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryEsignOrderQueryResponse, self).parse_response_content(response_content)
        if 'ability_code' in response:
            self.ability_code = response['ability_code']
        if 'completed_time' in response:
            self.completed_time = response['completed_time']
        if 'enterprise_no' in response:
            self.enterprise_no = response['enterprise_no']
        if 'estimated_price' in response:
            self.estimated_price = response['estimated_price']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'product_no' in response:
            self.product_no = response['product_no']
        if 'status' in response:
            self.status = response['status']
        if 'use_time' in response:
            self.use_time = response['use_time']
