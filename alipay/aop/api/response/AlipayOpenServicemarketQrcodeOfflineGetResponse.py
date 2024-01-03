#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenServicemarketQrcodeOfflineGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenServicemarketQrcodeOfflineGetResponse, self).__init__()
        self._logo = None
        self._qr_code_url = None
        self._sub_title = None
        self._title = None
        self._url = None

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenServicemarketQrcodeOfflineGetResponse, self).parse_response_content(response_content)
        if 'logo' in response:
            self.logo = response['logo']
        if 'qr_code_url' in response:
            self.qr_code_url = response['qr_code_url']
        if 'sub_title' in response:
            self.sub_title = response['sub_title']
        if 'title' in response:
            self.title = response['title']
        if 'url' in response:
            self.url = response['url']
