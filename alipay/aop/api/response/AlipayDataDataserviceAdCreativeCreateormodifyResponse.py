#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdCreativeCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdCreativeCreateormodifyResponse, self).__init__()
        self._creative_id = None
        self._creative_outer_id = None

    @property
    def creative_id(self):
        return self._creative_id

    @creative_id.setter
    def creative_id(self, value):
        self._creative_id = value
    @property
    def creative_outer_id(self):
        return self._creative_outer_id

    @creative_outer_id.setter
    def creative_outer_id(self, value):
        self._creative_outer_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdCreativeCreateormodifyResponse, self).parse_response_content(response_content)
        if 'creative_id' in response:
            self.creative_id = response['creative_id']
        if 'creative_outer_id' in response:
            self.creative_outer_id = response['creative_outer_id']
