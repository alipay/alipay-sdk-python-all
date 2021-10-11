#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceEnterpriseconsumeEnterpriseopenruleCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEnterpriseconsumeEnterpriseopenruleCreateResponse, self).__init__()
        self._invoice_rule_id = None

    @property
    def invoice_rule_id(self):
        return self._invoice_rule_id

    @invoice_rule_id.setter
    def invoice_rule_id(self, value):
        self._invoice_rule_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEnterpriseconsumeEnterpriseopenruleCreateResponse, self).parse_response_content(response_content)
        if 'invoice_rule_id' in response:
            self.invoice_rule_id = response['invoice_rule_id']
