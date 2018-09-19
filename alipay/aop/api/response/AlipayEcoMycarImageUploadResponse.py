#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarImageUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarImageUploadResponse, self).__init__()
        self._img_id = None
        self._img_url = None

    @property
    def img_id(self):
        return self._img_id

    @img_id.setter
    def img_id(self, value):
        self._img_id = value
    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarImageUploadResponse, self).parse_response_content(response_content)
        if 'img_id' in response:
            self.img_id = response['img_id']
        if 'img_url' in response:
            self.img_url = response['img_url']
