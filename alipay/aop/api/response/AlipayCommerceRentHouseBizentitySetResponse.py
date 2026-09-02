#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentHouseBizentitySetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentHouseBizentitySetResponse, self).__init__()
        self._feature_id = None

    @property
    def feature_id(self):
        return self._feature_id

    @feature_id.setter
    def feature_id(self, value):
        self._feature_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentHouseBizentitySetResponse, self).parse_response_content(response_content)
        if 'feature_id' in response:
            self.feature_id = response['feature_id']
