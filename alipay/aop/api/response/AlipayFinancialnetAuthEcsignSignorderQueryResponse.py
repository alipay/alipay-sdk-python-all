#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthEcsignSignorderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthEcsignSignorderQueryResponse, self).__init__()
        self._ext_info = None
        self._gmt_create = None
        self._gmt_modified = None
        self._order_status = None
        self._sign_order_no = None
        self._sign_product_id = None
        self._solution_code = None
        self._user_id = None
        self._verify_result = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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
    def sign_order_no(self):
        return self._sign_order_no

    @sign_order_no.setter
    def sign_order_no(self, value):
        self._sign_order_no = value
    @property
    def sign_product_id(self):
        return self._sign_product_id

    @sign_product_id.setter
    def sign_product_id(self, value):
        self._sign_product_id = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def verify_result(self):
        return self._verify_result

    @verify_result.setter
    def verify_result(self, value):
        self._verify_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthEcsignSignorderQueryResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'sign_order_no' in response:
            self.sign_order_no = response['sign_order_no']
        if 'sign_product_id' in response:
            self.sign_product_id = response['sign_product_id']
        if 'solution_code' in response:
            self.solution_code = response['solution_code']
        if 'user_id' in response:
            self.user_id = response['user_id']
        if 'verify_result' in response:
            self.verify_result = response['verify_result']
