#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechAiCvRsTiffQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechAiCvRsTiffQueryResponse, self).__init__()
        self._tile_result = None

    @property
    def tile_result(self):
        return self._tile_result

    @tile_result.setter
    def tile_result(self, value):
        self._tile_result = value

    def parse_response_content(self, response_content):
        response = super(AnttechAiCvRsTiffQueryResponse, self).parse_response_content(response_content)
        if 'tile_result' in response:
            self.tile_result = response['tile_result']
