#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SignContentBodyResponse import SignContentBodyResponse


class AlipayOpenMiniInnercontentSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnercontentSignResponse, self).__init__()
        self._cert_json = None
        self._sign_content_list = None
        self._sign_json = None

    @property
    def cert_json(self):
        return self._cert_json

    @cert_json.setter
    def cert_json(self, value):
        self._cert_json = value
    @property
    def sign_content_list(self):
        return self._sign_content_list

    @sign_content_list.setter
    def sign_content_list(self, value):
        if isinstance(value, list):
            self._sign_content_list = list()
            for i in value:
                if isinstance(i, SignContentBodyResponse):
                    self._sign_content_list.append(i)
                else:
                    self._sign_content_list.append(SignContentBodyResponse.from_alipay_dict(i))
    @property
    def sign_json(self):
        return self._sign_json

    @sign_json.setter
    def sign_json(self, value):
        self._sign_json = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnercontentSignResponse, self).parse_response_content(response_content)
        if 'cert_json' in response:
            self.cert_json = response['cert_json']
        if 'sign_content_list' in response:
            self.sign_content_list = response['sign_content_list']
        if 'sign_json' in response:
            self.sign_json = response['sign_json']
