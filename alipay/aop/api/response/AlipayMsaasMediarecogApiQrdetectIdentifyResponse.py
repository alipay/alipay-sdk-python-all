#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogApiQrdetectIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogApiQrdetectIdentifyResponse, self).__init__()
        self._has_qr = None
        self._list_url = None

    @property
    def has_qr(self):
        return self._has_qr

    @has_qr.setter
    def has_qr(self, value):
        self._has_qr = value
    @property
    def list_url(self):
        return self._list_url

    @list_url.setter
    def list_url(self, value):
        if isinstance(value, list):
            self._list_url = list()
            for i in value:
                self._list_url.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogApiQrdetectIdentifyResponse, self).parse_response_content(response_content)
        if 'has_qr' in response:
            self.has_qr = response['has_qr']
        if 'list_url' in response:
            self.list_url = response['list_url']
