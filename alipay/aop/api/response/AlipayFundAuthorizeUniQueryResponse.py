#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAuthorizeUniQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAuthorizeUniQueryResponse, self).__init__()
        self._agreement_no = None
        self._authorize_electronic_receipt = None
        self._biz_scene = None
        self._open_id = None
        self._operate_time = None
        self._out_biz_no = None
        self._personal_product_code = None
        self._product_code = None
        self._status = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def authorize_electronic_receipt(self):
        return self._authorize_electronic_receipt

    @authorize_electronic_receipt.setter
    def authorize_electronic_receipt(self, value):
        self._authorize_electronic_receipt = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def personal_product_code(self):
        return self._personal_product_code

    @personal_product_code.setter
    def personal_product_code(self, value):
        self._personal_product_code = value
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
        response = super(AlipayFundAuthorizeUniQueryResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'authorize_electronic_receipt' in response:
            self.authorize_electronic_receipt = response['authorize_electronic_receipt']
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'operate_time' in response:
            self.operate_time = response['operate_time']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'personal_product_code' in response:
            self.personal_product_code = response['personal_product_code']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'status' in response:
            self.status = response['status']
