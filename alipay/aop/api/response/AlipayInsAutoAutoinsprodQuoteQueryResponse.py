#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsProduct import InsProduct
from alipay.aop.api.domain.Car import Car
from alipay.aop.api.domain.InsProduct import InsProduct


class AlipayInsAutoAutoinsprodQuoteQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsAutoAutoinsprodQuoteQueryResponse, self).__init__()
        self._business_premium = None
        self._business_product = None
        self._car = None
        self._check_code = None
        self._check_code_id = None
        self._check_code_type = None
        self._com_id = None
        self._com_name = None
        self._enquiry_biz_id = None
        self._force_premium = None
        self._force_product = None
        self._quote_biz_id = None
        self._quote_error_code = None
        self._quote_error_msg = None
        self._real_premium = None
        self._reduce_premium = None
        self._total_premium = None

    @property
    def business_premium(self):
        return self._business_premium

    @business_premium.setter
    def business_premium(self, value):
        self._business_premium = value
    @property
    def business_product(self):
        return self._business_product

    @business_product.setter
    def business_product(self, value):
        if isinstance(value, InsProduct):
            self._business_product = value
        else:
            self._business_product = InsProduct.from_alipay_dict(value)
    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, value):
        if isinstance(value, Car):
            self._car = value
        else:
            self._car = Car.from_alipay_dict(value)
    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def check_code_id(self):
        return self._check_code_id

    @check_code_id.setter
    def check_code_id(self, value):
        self._check_code_id = value
    @property
    def check_code_type(self):
        return self._check_code_type

    @check_code_type.setter
    def check_code_type(self, value):
        self._check_code_type = value
    @property
    def com_id(self):
        return self._com_id

    @com_id.setter
    def com_id(self, value):
        self._com_id = value
    @property
    def com_name(self):
        return self._com_name

    @com_name.setter
    def com_name(self, value):
        self._com_name = value
    @property
    def enquiry_biz_id(self):
        return self._enquiry_biz_id

    @enquiry_biz_id.setter
    def enquiry_biz_id(self, value):
        self._enquiry_biz_id = value
    @property
    def force_premium(self):
        return self._force_premium

    @force_premium.setter
    def force_premium(self, value):
        self._force_premium = value
    @property
    def force_product(self):
        return self._force_product

    @force_product.setter
    def force_product(self, value):
        if isinstance(value, InsProduct):
            self._force_product = value
        else:
            self._force_product = InsProduct.from_alipay_dict(value)
    @property
    def quote_biz_id(self):
        return self._quote_biz_id

    @quote_biz_id.setter
    def quote_biz_id(self, value):
        self._quote_biz_id = value
    @property
    def quote_error_code(self):
        return self._quote_error_code

    @quote_error_code.setter
    def quote_error_code(self, value):
        self._quote_error_code = value
    @property
    def quote_error_msg(self):
        return self._quote_error_msg

    @quote_error_msg.setter
    def quote_error_msg(self, value):
        self._quote_error_msg = value
    @property
    def real_premium(self):
        return self._real_premium

    @real_premium.setter
    def real_premium(self, value):
        self._real_premium = value
    @property
    def reduce_premium(self):
        return self._reduce_premium

    @reduce_premium.setter
    def reduce_premium(self, value):
        self._reduce_premium = value
    @property
    def total_premium(self):
        return self._total_premium

    @total_premium.setter
    def total_premium(self, value):
        self._total_premium = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsAutoAutoinsprodQuoteQueryResponse, self).parse_response_content(response_content)
        if 'business_premium' in response:
            self.business_premium = response['business_premium']
        if 'business_product' in response:
            self.business_product = response['business_product']
        if 'car' in response:
            self.car = response['car']
        if 'check_code' in response:
            self.check_code = response['check_code']
        if 'check_code_id' in response:
            self.check_code_id = response['check_code_id']
        if 'check_code_type' in response:
            self.check_code_type = response['check_code_type']
        if 'com_id' in response:
            self.com_id = response['com_id']
        if 'com_name' in response:
            self.com_name = response['com_name']
        if 'enquiry_biz_id' in response:
            self.enquiry_biz_id = response['enquiry_biz_id']
        if 'force_premium' in response:
            self.force_premium = response['force_premium']
        if 'force_product' in response:
            self.force_product = response['force_product']
        if 'quote_biz_id' in response:
            self.quote_biz_id = response['quote_biz_id']
        if 'quote_error_code' in response:
            self.quote_error_code = response['quote_error_code']
        if 'quote_error_msg' in response:
            self.quote_error_msg = response['quote_error_msg']
        if 'real_premium' in response:
            self.real_premium = response['real_premium']
        if 'reduce_premium' in response:
            self.reduce_premium = response['reduce_premium']
        if 'total_premium' in response:
            self.total_premium = response['total_premium']
