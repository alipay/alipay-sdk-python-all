#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EsignResult import EsignResult


class AlipayFundTaxbillSignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTaxbillSignQueryResponse, self).__init__()
        self._biz_scene = None
        self._product_code = None
        self._result_list = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def result_list(self):
        return self._result_list

    @result_list.setter
    def result_list(self, value):
        if isinstance(value, list):
            self._result_list = list()
            for i in value:
                if isinstance(i, EsignResult):
                    self._result_list.append(i)
                else:
                    self._result_list.append(EsignResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayFundTaxbillSignQueryResponse, self).parse_response_content(response_content)
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'result_list' in response:
            self.result_list = response['result_list']
