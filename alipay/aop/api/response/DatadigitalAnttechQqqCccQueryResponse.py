#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalAnttechQqqCccQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAnttechQqqCccQueryResponse, self).__init__()
        self._cert_no = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalAnttechQqqCccQueryResponse, self).parse_response_content(response_content)
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
