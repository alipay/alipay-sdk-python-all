#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExpenseConsumeInfo import ExpenseConsumeInfo


class AlipayEbppInvoiceEnterpriseconsumeConsumeBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEnterpriseconsumeConsumeBatchqueryResponse, self).__init__()
        self._expense_consume_info_list = None

    @property
    def expense_consume_info_list(self):
        return self._expense_consume_info_list

    @expense_consume_info_list.setter
    def expense_consume_info_list(self, value):
        if isinstance(value, list):
            self._expense_consume_info_list = list()
            for i in value:
                if isinstance(i, ExpenseConsumeInfo):
                    self._expense_consume_info_list.append(i)
                else:
                    self._expense_consume_info_list.append(ExpenseConsumeInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEnterpriseconsumeConsumeBatchqueryResponse, self).parse_response_content(response_content)
        if 'expense_consume_info_list' in response:
            self.expense_consume_info_list = response['expense_consume_info_list']
