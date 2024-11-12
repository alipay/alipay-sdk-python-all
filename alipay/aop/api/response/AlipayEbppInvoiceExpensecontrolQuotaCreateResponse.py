#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInvoiceExpensecontrolQuotaCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceExpensecontrolQuotaCreateResponse, self).__init__()
        self._issue_batch_id = None
        self._quota_id = None

    @property
    def issue_batch_id(self):
        return self._issue_batch_id

    @issue_batch_id.setter
    def issue_batch_id(self, value):
        self._issue_batch_id = value
    @property
    def quota_id(self):
        return self._quota_id

    @quota_id.setter
    def quota_id(self, value):
        self._quota_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceExpensecontrolQuotaCreateResponse, self).parse_response_content(response_content)
        if 'issue_batch_id' in response:
            self.issue_batch_id = response['issue_batch_id']
        if 'quota_id' in response:
            self.quota_id = response['quota_id']
