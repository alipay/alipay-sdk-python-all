#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineMaterialImageDownloadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMaterialImageDownloadResponse, self).__init__()
        self._image_urls = None

    @property
    def image_urls(self):
        return self._image_urls

    @image_urls.setter
    def image_urls(self, value):
        if isinstance(value, list):
            self._image_urls = list()
            for i in value:
                self._image_urls.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMaterialImageDownloadResponse, self).parse_response_content(response_content)
        if 'image_urls' in response:
            self.image_urls = response['image_urls']
