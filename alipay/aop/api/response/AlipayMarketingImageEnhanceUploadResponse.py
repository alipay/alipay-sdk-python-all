#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingImageEnhanceUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingImageEnhanceUploadResponse, self).__init__()
        self._image_enhanced = None
        self._image_id = None
        self._image_url = None

    @property
    def image_enhanced(self):
        return self._image_enhanced

    @image_enhanced.setter
    def image_enhanced(self, value):
        self._image_enhanced = value
    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingImageEnhanceUploadResponse, self).parse_response_content(response_content)
        if 'image_enhanced' in response:
            self.image_enhanced = response['image_enhanced']
        if 'image_id' in response:
            self.image_id = response['image_id']
        if 'image_url' in response:
            self.image_url = response['image_url']
