#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CommerceAppUploadResponseData import CommerceAppUploadResponseData


class AlipayCommerceAppUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAppUploadResponse, self).__init__()
        self._biz_code = None
        self._biz_msg = None
        self._data = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_msg(self):
        return self._biz_msg

    @biz_msg.setter
    def biz_msg(self, value):
        self._biz_msg = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, CommerceAppUploadResponseData):
            self._data = value
        else:
            self._data = CommerceAppUploadResponseData.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAppUploadResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_msg' in response:
            self.biz_msg = response['biz_msg']
        if 'data' in response:
            self.data = response['data']
