#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetPromotionApplyCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetPromotionApplyCreateResponse, self).__init__()
        self._apply_no = None
        self._trace_id = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetPromotionApplyCreateResponse, self).parse_response_content(response_content)
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
