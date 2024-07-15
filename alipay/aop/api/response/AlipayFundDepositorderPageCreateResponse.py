#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundDepositorderPageCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundDepositorderPageCreateResponse, self).__init__()
        self._biz_scene = None
        self._deposit_link = None
        self._deposit_link_type = None
        self._order_id = None
        self._out_biz_no = None
        self._product_code = None
        self._status = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def deposit_link(self):
        return self._deposit_link

    @deposit_link.setter
    def deposit_link(self, value):
        self._deposit_link = value
    @property
    def deposit_link_type(self):
        return self._deposit_link_type

    @deposit_link_type.setter
    def deposit_link_type(self, value):
        self._deposit_link_type = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundDepositorderPageCreateResponse, self).parse_response_content(response_content)
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'deposit_link' in response:
            self.deposit_link = response['deposit_link']
        if 'deposit_link_type' in response:
            self.deposit_link_type = response['deposit_link_type']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'status' in response:
            self.status = response['status']
