#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRetailBusinesslistSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailBusinesslistSaveResponse, self).__init__()
        self._biz_type = None
        self._operate_type = None
        self._response_list = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def response_list(self):
        return self._response_list

    @response_list.setter
    def response_list(self, value):
        self._response_list = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailBusinesslistSaveResponse, self).parse_response_content(response_content)
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'operate_type' in response:
            self.operate_type = response['operate_type']
        if 'response_list' in response:
            self.response_list = response['response_list']
