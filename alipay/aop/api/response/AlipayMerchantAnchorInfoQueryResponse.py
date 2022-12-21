#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantAnchorInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantAnchorInfoQueryResponse, self).__init__()
        self._anchor_id = None

    @property
    def anchor_id(self):
        return self._anchor_id

    @anchor_id.setter
    def anchor_id(self, value):
        self._anchor_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantAnchorInfoQueryResponse, self).parse_response_content(response_content)
        if 'anchor_id' in response:
            self.anchor_id = response['anchor_id']
