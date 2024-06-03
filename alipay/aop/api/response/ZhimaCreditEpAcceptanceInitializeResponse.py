#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpAcceptanceInitializeResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpAcceptanceInitializeResponse, self).__init__()
        self._access_token = None
        self._access_url = None
        self._biz_no = None
        self._out_biz_no = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def access_url(self):
        return self._access_url

    @access_url.setter
    def access_url(self, value):
        self._access_url = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpAcceptanceInitializeResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'access_url' in response:
            self.access_url = response['access_url']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
