#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdTemplateFilewebofficeurlGenerateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateFilewebofficeurlGenerateResponse, self).__init__()
        self._access_token = None
        self._file_key = None
        self._refresh_token = None
        self._weboffice_url = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def file_key(self):
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value
    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value
    @property
    def weboffice_url(self):
        return self._weboffice_url

    @weboffice_url.setter
    def weboffice_url(self, value):
        self._weboffice_url = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateFilewebofficeurlGenerateResponse, self).parse_response_content(response_content)
        if 'access_token' in response:
            self.access_token = response['access_token']
        if 'file_key' in response:
            self.file_key = response['file_key']
        if 'refresh_token' in response:
            self.refresh_token = response['refresh_token']
        if 'weboffice_url' in response:
            self.weboffice_url = response['weboffice_url']
