#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundBailCollectionFinishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundBailCollectionFinishResponse, self).__init__()
        self._biz_error = None
        self._collection_no = None
        self._extra_param = None
        self._out_collection_no = None
        self._product_code = None
        self._result_code = None

    @property
    def biz_error(self):
        return self._biz_error

    @biz_error.setter
    def biz_error(self, value):
        self._biz_error = value
    @property
    def collection_no(self):
        return self._collection_no

    @collection_no.setter
    def collection_no(self, value):
        self._collection_no = value
    @property
    def extra_param(self):
        return self._extra_param

    @extra_param.setter
    def extra_param(self, value):
        self._extra_param = value
    @property
    def out_collection_no(self):
        return self._out_collection_no

    @out_collection_no.setter
    def out_collection_no(self, value):
        self._out_collection_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundBailCollectionFinishResponse, self).parse_response_content(response_content)
        if 'biz_error' in response:
            self.biz_error = response['biz_error']
        if 'collection_no' in response:
            self.collection_no = response['collection_no']
        if 'extra_param' in response:
            self.extra_param = response['extra_param']
        if 'out_collection_no' in response:
            self.out_collection_no = response['out_collection_no']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'result_code' in response:
            self.result_code = response['result_code']
