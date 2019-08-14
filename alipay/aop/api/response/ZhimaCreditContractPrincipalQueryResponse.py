#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditContractPrincipalQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditContractPrincipalQueryResponse, self).__init__()
        self._need_auth = None
        self._url = None

    @property
    def need_auth(self):
        return self._need_auth

    @need_auth.setter
    def need_auth(self, value):
        self._need_auth = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditContractPrincipalQueryResponse, self).parse_response_content(response_content)
        if 'need_auth' in response:
            self.need_auth = response['need_auth']
        if 'url' in response:
            self.url = response['url']
