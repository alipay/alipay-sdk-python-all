#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppQrcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppQrcodeCreateResponse, self).__init__()
        self._qr_code_url = None
        self._qr_code_url_circle_blue = None
        self._qr_code_url_circle_white = None

    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value
    @property
    def qr_code_url_circle_blue(self):
        return self._qr_code_url_circle_blue

    @qr_code_url_circle_blue.setter
    def qr_code_url_circle_blue(self, value):
        self._qr_code_url_circle_blue = value
    @property
    def qr_code_url_circle_white(self):
        return self._qr_code_url_circle_white

    @qr_code_url_circle_white.setter
    def qr_code_url_circle_white(self, value):
        self._qr_code_url_circle_white = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppQrcodeCreateResponse, self).parse_response_content(response_content)
        if 'qr_code_url' in response:
            self.qr_code_url = response['qr_code_url']
        if 'qr_code_url_circle_blue' in response:
            self.qr_code_url_circle_blue = response['qr_code_url_circle_blue']
        if 'qr_code_url_circle_white' in response:
            self.qr_code_url_circle_white = response['qr_code_url_circle_white']
