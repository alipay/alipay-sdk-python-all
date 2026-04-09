#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftUserChainQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftUserChainQueryResponse, self).__init__()
        self._chain_address = None

    @property
    def chain_address(self):
        return self._chain_address

    @chain_address.setter
    def chain_address(self, value):
        self._chain_address = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftUserChainQueryResponse, self).parse_response_content(response_content)
        if 'chain_address' in response:
            self.chain_address = response['chain_address']
