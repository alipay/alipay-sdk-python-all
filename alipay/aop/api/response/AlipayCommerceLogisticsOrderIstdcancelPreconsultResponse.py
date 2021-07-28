#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsOrderIstdcancelPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsOrderIstdcancelPreconsultResponse, self).__init__()
        self._allow_cancel = None

    @property
    def allow_cancel(self):
        return self._allow_cancel

    @allow_cancel.setter
    def allow_cancel(self, value):
        self._allow_cancel = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsOrderIstdcancelPreconsultResponse, self).parse_response_content(response_content)
        if 'allow_cancel' in response:
            self.allow_cancel = response['allow_cancel']
