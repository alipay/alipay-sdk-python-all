#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftBlessBodhileafSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftBlessBodhileafSubmitResponse, self).__init__()
        self._actual_deduct_value = None

    @property
    def actual_deduct_value(self):
        return self._actual_deduct_value

    @actual_deduct_value.setter
    def actual_deduct_value(self, value):
        self._actual_deduct_value = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftBlessBodhileafSubmitResponse, self).parse_response_content(response_content)
        if 'actual_deduct_value' in response:
            self.actual_deduct_value = response['actual_deduct_value']
