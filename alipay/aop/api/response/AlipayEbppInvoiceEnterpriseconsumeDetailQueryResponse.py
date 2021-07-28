#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExpenseConsumeInfo import ExpenseConsumeInfo
from alipay.aop.api.domain.ExpenseInvoiceInfo import ExpenseInvoiceInfo
from alipay.aop.api.domain.ExpenseVoucherInfo import ExpenseVoucherInfo


class AlipayEbppInvoiceEnterpriseconsumeDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceEnterpriseconsumeDetailQueryResponse, self).__init__()
        self._expense_consume_info = None
        self._expense_invoice_info = None
        self._voucher_info = None

    @property
    def expense_consume_info(self):
        return self._expense_consume_info

    @expense_consume_info.setter
    def expense_consume_info(self, value):
        if isinstance(value, ExpenseConsumeInfo):
            self._expense_consume_info = value
        else:
            self._expense_consume_info = ExpenseConsumeInfo.from_alipay_dict(value)
    @property
    def expense_invoice_info(self):
        return self._expense_invoice_info

    @expense_invoice_info.setter
    def expense_invoice_info(self, value):
        if isinstance(value, ExpenseInvoiceInfo):
            self._expense_invoice_info = value
        else:
            self._expense_invoice_info = ExpenseInvoiceInfo.from_alipay_dict(value)
    @property
    def voucher_info(self):
        return self._voucher_info

    @voucher_info.setter
    def voucher_info(self, value):
        if isinstance(value, ExpenseVoucherInfo):
            self._voucher_info = value
        else:
            self._voucher_info = ExpenseVoucherInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceEnterpriseconsumeDetailQueryResponse, self).parse_response_content(response_content)
        if 'expense_consume_info' in response:
            self.expense_consume_info = response['expense_consume_info']
        if 'expense_invoice_info' in response:
            self.expense_invoice_info = response['expense_invoice_info']
        if 'voucher_info' in response:
            self.voucher_info = response['voucher_info']
