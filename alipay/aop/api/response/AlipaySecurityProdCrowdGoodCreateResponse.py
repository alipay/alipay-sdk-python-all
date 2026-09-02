#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdCrowdGoodCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdCrowdGoodCreateResponse, self).__init__()
        self._good_id = None

    @property
    def good_id(self):
        return self._good_id

    @good_id.setter
    def good_id(self, value):
        self._good_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdCrowdGoodCreateResponse, self).parse_response_content(response_content)
        if 'good_id' in response:
            self.good_id = response['good_id']
