#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IotIdentityFaceOutEventApiResponse import IotIdentityFaceOutEventApiResponse


class AlipayOpenIotvspOrguserfaceoutQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotvspOrguserfaceoutQueryResponse, self).__init__()
        self._code = None
        self._data = None
        self._message = None
        self._success = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, IotIdentityFaceOutEventApiResponse):
            self._data = value
        else:
            self._data = IotIdentityFaceOutEventApiResponse.from_alipay_dict(value)
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotvspOrguserfaceoutQueryResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'data' in response:
            self.data = response['data']
        if 'message' in response:
            self.message = response['message']
        if 'success' in response:
            self.success = response['success']
