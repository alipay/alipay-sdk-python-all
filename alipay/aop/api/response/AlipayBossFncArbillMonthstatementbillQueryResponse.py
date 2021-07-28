#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ArMonthlyStatementBillOpenApiResponse import ArMonthlyStatementBillOpenApiResponse
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class AlipayBossFncArbillMonthstatementbillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncArbillMonthstatementbillQueryResponse, self).__init__()
        self._current_page = None
        self._items_page = None
        self._result_set = None
        self._total_adj_amt = None
        self._total_bill_amt = None
        self._total_inv_amt = None
        self._total_inved_amt = None
        self._total_items = None
        self._total_link_invoice_amt = None
        self._total_pages = None
        self._total_received_amt = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def items_page(self):
        return self._items_page

    @items_page.setter
    def items_page(self, value):
        self._items_page = value
    @property
    def result_set(self):
        return self._result_set

    @result_set.setter
    def result_set(self, value):
        if isinstance(value, list):
            self._result_set = list()
            for i in value:
                if isinstance(i, ArMonthlyStatementBillOpenApiResponse):
                    self._result_set.append(i)
                else:
                    self._result_set.append(ArMonthlyStatementBillOpenApiResponse.from_alipay_dict(i))
    @property
    def total_adj_amt(self):
        return self._total_adj_amt

    @total_adj_amt.setter
    def total_adj_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._total_adj_amt = value
        else:
            self._total_adj_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def total_bill_amt(self):
        return self._total_bill_amt

    @total_bill_amt.setter
    def total_bill_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._total_bill_amt = value
        else:
            self._total_bill_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
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
    def total_items(self):
        return self._total_items

    @total_items.setter
    def total_items(self, value):
        self._total_items = value
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
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value
    @property
    def total_received_amt(self):
        return self._total_received_amt

    @total_received_amt.setter
    def total_received_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._total_received_amt = value
        else:
            self._total_received_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossFncArbillMonthstatementbillQueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'items_page' in response:
            self.items_page = response['items_page']
        if 'result_set' in response:
            self.result_set = response['result_set']
        if 'total_adj_amt' in response:
            self.total_adj_amt = response['total_adj_amt']
        if 'total_bill_amt' in response:
            self.total_bill_amt = response['total_bill_amt']
        if 'total_inv_amt' in response:
            self.total_inv_amt = response['total_inv_amt']
        if 'total_inved_amt' in response:
            self.total_inved_amt = response['total_inved_amt']
        if 'total_items' in response:
            self.total_items = response['total_items']
        if 'total_link_invoice_amt' in response:
            self.total_link_invoice_amt = response['total_link_invoice_amt']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'total_received_amt' in response:
            self.total_received_amt = response['total_received_amt']
