#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiCvRsXytileGetResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiCvRsXytileGetResponse, self).__init__()
        self._image = None

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiCvRsXytileGetResponse, self).parse_response_content(response_content)
        if 'image' in response:
            self.image = response['image']
