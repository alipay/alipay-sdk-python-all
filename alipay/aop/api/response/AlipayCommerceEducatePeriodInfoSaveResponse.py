#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducatePeriodInfoSaveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducatePeriodInfoSaveResponse, self).__init__()
        self._period_id = None

    @property
    def period_id(self):
        return self._period_id

    @period_id.setter
    def period_id(self, value):
        self._period_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducatePeriodInfoSaveResponse, self).parse_response_content(response_content)
        if 'period_id' in response:
            self.period_id = response['period_id']
