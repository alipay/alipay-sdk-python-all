#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalPaymentPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalPaymentPreconsultResponse, self).__init__()
        self._suggestion = None

    @property
    def suggestion(self):
        return self._suggestion

    @suggestion.setter
    def suggestion(self, value):
        self._suggestion = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalPaymentPreconsultResponse, self).parse_response_content(response_content)
        if 'suggestion' in response:
            self.suggestion = response['suggestion']
