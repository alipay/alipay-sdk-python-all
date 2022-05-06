#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantMrchsurplmorderPointQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantMrchsurplmorderPointQueryResponse, self).__init__()
        self._point = None

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantMrchsurplmorderPointQueryResponse, self).parse_response_content(response_content)
        if 'point' in response:
            self.point = response['point']
