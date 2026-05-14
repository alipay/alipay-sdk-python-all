#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsWaybillIntelinoticeConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsWaybillIntelinoticeConsultResponse, self).__init__()
        self._can_intelinotice = None

    @property
    def can_intelinotice(self):
        return self._can_intelinotice

    @can_intelinotice.setter
    def can_intelinotice(self, value):
        self._can_intelinotice = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsWaybillIntelinoticeConsultResponse, self).parse_response_content(response_content)
        if 'can_intelinotice' in response:
            self.can_intelinotice = response['can_intelinotice']
