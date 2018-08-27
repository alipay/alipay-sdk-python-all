#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCognitiveOcrImageclassifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveOcrImageclassifyQueryResponse, self).__init__()
        self._image_type = None

    @property
    def image_type(self):
        return self._image_type

    @image_type.setter
    def image_type(self, value):
        self._image_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveOcrImageclassifyQueryResponse, self).parse_response_content(response_content)
        if 'image_type' in response:
            self.image_type = response['image_type']
