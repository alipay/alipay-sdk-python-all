#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceYuntaskAgreementSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskAgreementSignResponse, self).__init__()
        self._form_data = None

    @property
    def form_data(self):
        return self._form_data

    @form_data.setter
    def form_data(self, value):
        self._form_data = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskAgreementSignResponse, self).parse_response_content(response_content)
        if 'form_data' in response:
            self.form_data = response['form_data']
