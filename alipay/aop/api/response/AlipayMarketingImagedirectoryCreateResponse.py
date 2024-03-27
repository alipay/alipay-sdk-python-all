#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingImagedirectoryCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingImagedirectoryCreateResponse, self).__init__()
        self._image_directory_id = None

    @property
    def image_directory_id(self):
        return self._image_directory_id

    @image_directory_id.setter
    def image_directory_id(self, value):
        self._image_directory_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingImagedirectoryCreateResponse, self).parse_response_content(response_content)
        if 'image_directory_id' in response:
            self.image_directory_id = response['image_directory_id']
