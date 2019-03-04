#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ArInvoiceReceiptOpenApiResponse import ArInvoiceReceiptOpenApiResponse
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class AlipayBossFncInvoicereceiptBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncInvoicereceiptBatchqueryResponse, self).__init__()
        self._result_set = None
        self._total_inv_amt = None
        self._total_inved_amt = None
        self._total_link_invoice_amt = None

    @property
    def result_set(self):
        return self._result_set

    @result_set.setter
    def result_set(self, value):
        if isinstance(value, list):
            self._result_set = list()
            for i in value:
                if isinstance(i, ArInvoiceReceiptOpenApiResponse):
                    self._result_set.append(i)
                else:
                    self._result_set.append(ArInvoiceReceiptOpenApiResponse.from_alipay_dict(i))
    @property
    def total_inv_amt(self):
        return self._total_inv_amt

    @total_inv_amt.setter
    def total_inv_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._total_inv_amt = value
        else:
            self._total_inv_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def total_inved_amt(self):
        return self._total_inved_amt

    @total_inved_amt.setter
    def total_inved_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._total_inved_amt = value
        else:
            self._total_inved_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def total_link_invoice_amt(self):
        return self._total_link_invoice_amt

    @total_link_invoice_amt.setter
    def total_link_invoice_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._total_link_invoice_amt = value
        else:
            self._total_link_invoice_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncInvoicereceiptBatchqueryResponse, self).parse_response_content(response_content)
        if 'result_set' in response:
            self.result_set = response['result_set']
        if 'total_inv_amt' in response:
            self.total_inv_amt = response['total_inv_amt']
        if 'total_inved_amt' in response:
            self.total_inved_amt = response['total_inved_amt']
        if 'total_link_invoice_amt' in response:
            self.total_link_invoice_amt = response['total_link_invoice_amt']
