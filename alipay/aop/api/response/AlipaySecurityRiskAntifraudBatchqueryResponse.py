#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskAntifraudBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskAntifraudBatchqueryResponse, self).__init__()
        self._company_relation_list = None
        self._staff_company_relation_list = None

    @property
    def company_relation_list(self):
        return self._company_relation_list

    @company_relation_list.setter
    def company_relation_list(self, value):
        if isinstance(value, list):
            self._company_relation_list = list()
            for i in value:
                self._company_relation_list.append(i)
    @property
    def staff_company_relation_list(self):
        return self._staff_company_relation_list

    @staff_company_relation_list.setter
    def staff_company_relation_list(self, value):
        if isinstance(value, list):
            self._staff_company_relation_list = list()
            for i in value:
                self._staff_company_relation_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskAntifraudBatchqueryResponse, self).parse_response_content(response_content)
        if 'company_relation_list' in response:
            self.company_relation_list = response['company_relation_list']
        if 'staff_company_relation_list' in response:
            self.staff_company_relation_list = response['staff_company_relation_list']
