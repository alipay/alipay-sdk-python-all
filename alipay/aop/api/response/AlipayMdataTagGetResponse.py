#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMdataTagGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMdataTagGetResponse, self).__init__()
        self._tag_values = None

    @property
    def tag_values(self):
        return self._tag_values

    @tag_values.setter
    def tag_values(self, value):
        self._tag_values = value

    def parse_response_content(self, response_content):
        response = super(AlipayMdataTagGetResponse, self).parse_response_content(response_content)
        if 'tag_values' in response:
            self.tag_values = response['tag_values']
