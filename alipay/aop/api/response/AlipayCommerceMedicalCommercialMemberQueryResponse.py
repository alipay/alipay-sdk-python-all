#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalCommercialMemberQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommercialMemberQueryResponse, self).__init__()
        self._biz_order_id = None
        self._end_time = None
        self._exist = None
        self._open_id = None
        self._order_id = None
        self._out_product_id = None
        self._start_time = None
        self._user_id = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def exist(self):
        return self._exist

    @exist.setter
    def exist(self, value):
        self._exist = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_product_id(self):
        return self._out_product_id

    @out_product_id.setter
    def out_product_id(self, value):
        self._out_product_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommercialMemberQueryResponse, self).parse_response_content(response_content)
        if 'biz_order_id' in response:
            self.biz_order_id = response['biz_order_id']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'exist' in response:
            self.exist = response['exist']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_product_id' in response:
            self.out_product_id = response['out_product_id']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'user_id' in response:
            self.user_id = response['user_id']
