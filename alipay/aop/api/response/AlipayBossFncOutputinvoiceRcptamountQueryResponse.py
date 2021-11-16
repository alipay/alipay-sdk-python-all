#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class AlipayBossFncOutputinvoiceRcptamountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncOutputinvoiceRcptamountQueryResponse, self).__init__()
        self._total_inv_amt = None
        self._total_inved_amt = None
        self._total_link_invoice_amt = None
        self._total_receivable_inv_amt = None
        self._total_receivable_inved_amt = None
        self._total_receivable_link_inv_amt = None
        self._total_writeoff_inv_amt = None
        self._total_writeoff_inved_amt = None
        self._total_writeoff_link_inv_amt = None

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
    @property
    def total_receivable_inv_amt(self):
        return self._total_receivable_inv_amt

    @total_receivable_inv_amt.setter
    def total_receivable_inv_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._total_receivable_inv_amt = value
        else:
            self._total_receivable_inv_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def total_receivable_inved_amt(self):
        return self._total_receivable_inved_amt

    @total_receivable_inved_amt.setter
    def total_receivable_inved_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._total_receivable_inved_amt = value
        else:
            self._total_receivable_inved_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def total_receivable_link_inv_amt(self):
        return self._total_receivable_link_inv_amt

    @total_receivable_link_inv_amt.setter
    def total_receivable_link_inv_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._total_receivable_link_inv_amt = value
        else:
            self._total_receivable_link_inv_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def total_writeoff_inv_amt(self):
        return self._total_writeoff_inv_amt

    @total_writeoff_inv_amt.setter
    def total_writeoff_inv_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._total_writeoff_inv_amt = value
        else:
            self._total_writeoff_inv_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def total_writeoff_inved_amt(self):
        return self._total_writeoff_inved_amt

    @total_writeoff_inved_amt.setter
    def total_writeoff_inved_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._total_writeoff_inved_amt = value
        else:
            self._total_writeoff_inved_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def total_writeoff_link_inv_amt(self):
        return self._total_writeoff_link_inv_amt

    @total_writeoff_link_inv_amt.setter
    def total_writeoff_link_inv_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._total_writeoff_link_inv_amt = value
        else:
            self._total_writeoff_link_inv_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncOutputinvoiceRcptamountQueryResponse, self).parse_response_content(response_content)
        if 'total_inv_amt' in response:
            self.total_inv_amt = response['total_inv_amt']
        if 'total_inved_amt' in response:
            self.total_inved_amt = response['total_inved_amt']
        if 'total_link_invoice_amt' in response:
            self.total_link_invoice_amt = response['total_link_invoice_amt']
        if 'total_receivable_inv_amt' in response:
            self.total_receivable_inv_amt = response['total_receivable_inv_amt']
        if 'total_receivable_inved_amt' in response:
            self.total_receivable_inved_amt = response['total_receivable_inved_amt']
        if 'total_receivable_link_inv_amt' in response:
            self.total_receivable_link_inv_amt = response['total_receivable_link_inv_amt']
        if 'total_writeoff_inv_amt' in response:
            self.total_writeoff_inv_amt = response['total_writeoff_inv_amt']
        if 'total_writeoff_inved_amt' in response:
            self.total_writeoff_inved_amt = response['total_writeoff_inved_amt']
        if 'total_writeoff_link_inv_amt' in response:
            self.total_writeoff_link_inv_amt = response['total_writeoff_link_inv_amt']
