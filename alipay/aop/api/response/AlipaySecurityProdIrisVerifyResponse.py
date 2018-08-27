#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdIrisVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdIrisVerifyResponse, self).__init__()
        self._biz_token = None
        self._ext_info = None
        self._iris_id = None
        self._person_id = None
        self._status = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def iris_id(self):
        return self._iris_id

    @iris_id.setter
    def iris_id(self, value):
        self._iris_id = value
    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        self._person_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdIrisVerifyResponse, self).parse_response_content(response_content)
        if 'biz_token' in response:
            self.biz_token = response['biz_token']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'iris_id' in response:
            self.iris_id = response['iris_id']
        if 'person_id' in response:
            self.person_id = response['person_id']
        if 'status' in response:
            self.status = response['status']
