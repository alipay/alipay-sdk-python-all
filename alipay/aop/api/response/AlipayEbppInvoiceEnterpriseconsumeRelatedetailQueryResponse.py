#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExpenseCtrlConsumeInfo import ExpenseCtrlConsumeInfo


class AlipayEbppInvoiceEnterpriseconsumeRelatedetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEnterpriseconsumeRelatedetailQueryResponse, self).__init__()
        self._expense_ctrl_consume_info = None

    @property
    def expense_ctrl_consume_info(self):
        return self._expense_ctrl_consume_info

    @expense_ctrl_consume_info.setter
    def expense_ctrl_consume_info(self, value):
        if isinstance(value, ExpenseCtrlConsumeInfo):
            self._expense_ctrl_consume_info = value
        else:
            self._expense_ctrl_consume_info = ExpenseCtrlConsumeInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEnterpriseconsumeRelatedetailQueryResponse, self).parse_response_content(response_content)
        if 'expense_ctrl_consume_info' in response:
            self.expense_ctrl_consume_info = response['expense_ctrl_consume_info']
