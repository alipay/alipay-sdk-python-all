#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpCreditunionTppSubscribeResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCreditunionTppSubscribeResponse, self).__init__()
        self._biz_no = None
        self._business_person = None
        self._ent_name = None
        self._merchant_request_id = None
        self._product_code = None
        self._reg_no = None
        self._type = None
        self._uscc = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def business_person(self):
        return self._business_person

    @business_person.setter
    def business_person(self, value):
        self._business_person = value
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def merchant_request_id(self):
        return self._merchant_request_id

    @merchant_request_id.setter
    def merchant_request_id(self, value):
        self._merchant_request_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCreditunionTppSubscribeResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'business_person' in response:
            self.business_person = response['business_person']
        if 'ent_name' in response:
            self.ent_name = response['ent_name']
        if 'merchant_request_id' in response:
            self.merchant_request_id = response['merchant_request_id']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'reg_no' in response:
            self.reg_no = response['reg_no']
        if 'type' in response:
            self.type = response['type']
        if 'uscc' in response:
            self.uscc = response['uscc']
