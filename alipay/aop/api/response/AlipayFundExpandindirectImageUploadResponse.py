#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundExpandindirectImageUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundExpandindirectImageUploadResponse, self).__init__()
        self._image_id = None

    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundExpandindirectImageUploadResponse, self).parse_response_content(response_content)
        if 'image_id' in response:
            self.image_id = response['image_id']
