#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalPaymentPreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalPaymentPreconsultResponse, self).__init__()
        self._active_url = None
        self._suggestion = None

    @property
    def active_url(self):
        return self._active_url

    @active_url.setter
    def active_url(self, value):
        self._active_url = value
    @property
    def suggestion(self):
        return self._suggestion

    @suggestion.setter
    def suggestion(self, value):
        self._suggestion = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalPaymentPreconsultResponse, self).parse_response_content(response_content)
        if 'active_url' in response:
            self.active_url = response['active_url']
        if 'suggestion' in response:
            self.suggestion = response['suggestion']
