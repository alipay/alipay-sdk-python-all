#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceIssueruleCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceIssueruleCreateResponse, self).__init__()
        self._issue_rule_id = None

    @property
    def issue_rule_id(self):
        return self._issue_rule_id

    @issue_rule_id.setter
    def issue_rule_id(self, value):
        self._issue_rule_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceIssueruleCreateResponse, self).parse_response_content(response_content)
        if 'issue_rule_id' in response:
            self.issue_rule_id = response['issue_rule_id']
