#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantLogoImageUploadResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantLogoImageUploadResponse, self).__init__()
        self._image_url = None

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantLogoImageUploadResponse, self).parse_response_content(response_content)
        if 'image_url' in response:
            self.image_url = response['image_url']
