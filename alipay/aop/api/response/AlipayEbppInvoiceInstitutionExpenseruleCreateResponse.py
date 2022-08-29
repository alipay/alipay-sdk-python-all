#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceInstitutionExpenseruleCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceInstitutionExpenseruleCreateResponse, self).__init__()
        self._standard_id = None

    @property
    def standard_id(self):
        return self._standard_id

    @standard_id.setter
    def standard_id(self, value):
        self._standard_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceInstitutionExpenseruleCreateResponse, self).parse_response_content(response_content)
        if 'standard_id' in response:
            self.standard_id = response['standard_id']
