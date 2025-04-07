#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationIotnsphgUserinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationIotnsphgUserinfoQueryResponse, self).__init__()
        self._binded_mobile = None

    @property
    def binded_mobile(self):
        return self._binded_mobile

    @binded_mobile.setter
    def binded_mobile(self, value):
        self._binded_mobile = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationIotnsphgUserinfoQueryResponse, self).parse_response_content(response_content)
        if 'binded_mobile' in response:
            self.binded_mobile = response['binded_mobile']
