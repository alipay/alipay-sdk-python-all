#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniAmpeQrcodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeQrcodeCreateResponse, self).__init__()
        self._qrcode_img_url = None

    @property
    def qrcode_img_url(self):
        return self._qrcode_img_url

    @qrcode_img_url.setter
    def qrcode_img_url(self, value):
        self._qrcode_img_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeQrcodeCreateResponse, self).parse_response_content(response_content)
        if 'qrcode_img_url' in response:
            self.qrcode_img_url = response['qrcode_img_url']
