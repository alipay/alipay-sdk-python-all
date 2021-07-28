#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceExpenserulesProjectruleCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceExpenserulesProjectruleCreateResponse, self).__init__()
        self._project_id = None

    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceExpenserulesProjectruleCreateResponse, self).parse_response_content(response_content)
        if 'project_id' in response:
            self.project_id = response['project_id']
