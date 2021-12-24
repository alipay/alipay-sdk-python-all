#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundBailOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundBailOrderQueryResponse, self).__init__()
        self._auth_no = None
        self._biz_error = None
        self._fund_entrust_type = None
        self._gmt_create = None
        self._gmt_modified = None
        self._order_status = None
        self._order_title = None
        self._out_order_no = None
        self._product_code = None
        self._rest_amount = None
        self._result_code = None
        self._result_message = None
        self._scene_code = None

    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
    @property
    def biz_error(self):
        return self._biz_error

    @biz_error.setter
    def biz_error(self, value):
        self._biz_error = value
    @property
    def fund_entrust_type(self):
        return self._fund_entrust_type

    @fund_entrust_type.setter
    def fund_entrust_type(self, value):
        self._fund_entrust_type = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def rest_amount(self):
        return self._rest_amount

    @rest_amount.setter
    def rest_amount(self, value):
        self._rest_amount = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_message(self):
        return self._result_message

    @result_message.setter
    def result_message(self, value):
        self._result_message = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundBailOrderQueryResponse, self).parse_response_content(response_content)
        if 'auth_no' in response:
            self.auth_no = response['auth_no']
        if 'biz_error' in response:
            self.biz_error = response['biz_error']
        if 'fund_entrust_type' in response:
            self.fund_entrust_type = response['fund_entrust_type']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'order_title' in response:
            self.order_title = response['order_title']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'rest_amount' in response:
            self.rest_amount = response['rest_amount']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_message' in response:
            self.result_message = response['result_message']
        if 'scene_code' in response:
            self.scene_code = response['scene_code']
