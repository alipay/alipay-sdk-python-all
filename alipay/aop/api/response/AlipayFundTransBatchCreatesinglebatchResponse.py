#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransBatchCreatesinglebatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransBatchCreatesinglebatchResponse, self).__init__()
        self._batch_no = None
        self._ext_param = None
        self._token = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransBatchCreatesinglebatchResponse, self).parse_response_content(response_content)
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'ext_param' in response:
            self.ext_param = response['ext_param']
        if 'token' in response:
            self.token = response['token']
