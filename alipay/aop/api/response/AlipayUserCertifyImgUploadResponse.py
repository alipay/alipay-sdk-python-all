#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertifyImgUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyImgUploadResponse, self).__init__()
        self._pic_url = None

    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyImgUploadResponse, self).parse_response_content(response_content)
        if 'pic_url' in response:
            self.pic_url = response['pic_url']
