#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpCodecCreateResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCodecCreateResponse, self).__init__()
        self._codec_img_url = None
        self._token = None

    @property
    def codec_img_url(self):
        return self._codec_img_url

    @codec_img_url.setter
    def codec_img_url(self, value):
        self._codec_img_url = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCodecCreateResponse, self).parse_response_content(response_content)
        if 'codec_img_url' in response:
            self.codec_img_url = response['codec_img_url']
        if 'token' in response:
            self.token = response['token']
