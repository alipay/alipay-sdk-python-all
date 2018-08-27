#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFaceMatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFaceMatchResponse, self).__init__()
        self._biz_unique_no = None

    @property
    def biz_unique_no(self):
        return self._biz_unique_no

    @biz_unique_no.setter
    def biz_unique_no(self, value):
        self._biz_unique_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFaceMatchResponse, self).parse_response_content(response_content)
        if 'biz_unique_no' in response:
            self.biz_unique_no = response['biz_unique_no']
