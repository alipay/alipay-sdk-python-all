#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsDataDsbImageUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsDataDsbImageUploadResponse, self).__init__()
        self._image_path = None

    @property
    def image_path(self):
        return self._image_path

    @image_path.setter
    def image_path(self, value):
        self._image_path = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsDataDsbImageUploadResponse, self).parse_response_content(response_content)
        if 'image_path' in response:
            self.image_path = response['image_path']
