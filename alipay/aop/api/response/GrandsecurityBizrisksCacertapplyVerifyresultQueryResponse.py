#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ValidateProductInfo import ValidateProductInfo


class GrandsecurityBizrisksCacertapplyVerifyresultQueryResponse(AlipayResponse):

    def __init__(self):
        super(GrandsecurityBizrisksCacertapplyVerifyresultQueryResponse, self).__init__()
        self._error_code = None
        self._error_msg = None
        self._query_success = None
        self._successful_products = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def query_success(self):
        return self._query_success

    @query_success.setter
    def query_success(self, value):
        self._query_success = value
    @property
    def successful_products(self):
        return self._successful_products

    @successful_products.setter
    def successful_products(self, value):
        if isinstance(value, list):
            self._successful_products = list()
            for i in value:
                if isinstance(i, ValidateProductInfo):
                    self._successful_products.append(i)
                else:
                    self._successful_products.append(ValidateProductInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(GrandsecurityBizrisksCacertapplyVerifyresultQueryResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'query_success' in response:
            self.query_success = response['query_success']
        if 'successful_products' in response:
            self.successful_products = response['successful_products']
