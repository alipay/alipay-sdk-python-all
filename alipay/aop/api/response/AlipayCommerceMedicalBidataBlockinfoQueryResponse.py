#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalBidataBlockinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalBidataBlockinfoQueryResponse, self).__init__()
        self._block_content = None
        self._block_type = None

    @property
    def block_content(self):
        return self._block_content

    @block_content.setter
    def block_content(self, value):
        self._block_content = value
    @property
    def block_type(self):
        return self._block_type

    @block_type.setter
    def block_type(self, value):
        self._block_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalBidataBlockinfoQueryResponse, self).parse_response_content(response_content)
        if 'block_content' in response:
            self.block_content = response['block_content']
        if 'block_type' in response:
            self.block_type = response['block_type']
