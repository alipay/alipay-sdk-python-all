#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtHrcampuscoreEntrySyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtHrcampuscoreEntrySyncResponse, self).__init__()
        self._form_no = None

    @property
    def form_no(self):
        return self._form_no

    @form_no.setter
    def form_no(self, value):
        self._form_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtHrcampuscoreEntrySyncResponse, self).parse_response_content(response_content)
        if 'form_no' in response:
            self.form_no = response['form_no']
