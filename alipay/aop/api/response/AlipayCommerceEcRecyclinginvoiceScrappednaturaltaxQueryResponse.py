#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.NatrualPersonInvoiceAmountMonthly import NatrualPersonInvoiceAmountMonthly
from alipay.aop.api.domain.RecyclingScrappedTaxCalcItem import RecyclingScrappedTaxCalcItem


class AlipayCommerceEcRecyclinginvoiceScrappednaturaltaxQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceScrappednaturaltaxQueryResponse, self).__init__()
        self._individual_tax_accumulated_amount_current_year = None
        self._interrupt = None
        self._invoice_amount_list = None
        self._paid_individual_tax_amount_current_year = None
        self._scrapped_tax_calc_item_list = None
        self._wait_pay_general_invoice_1 = None
        self._wait_pay_general_invoice_edu_amount = None
        self._wait_pay_special_invoice_1 = None
        self._wait_pay_special_invoice_3 = None

    @property
    def individual_tax_accumulated_amount_current_year(self):
        return self._individual_tax_accumulated_amount_current_year

    @individual_tax_accumulated_amount_current_year.setter
    def individual_tax_accumulated_amount_current_year(self, value):
        self._individual_tax_accumulated_amount_current_year = value
    @property
    def interrupt(self):
        return self._interrupt

    @interrupt.setter
    def interrupt(self, value):
        self._interrupt = value
    @property
    def invoice_amount_list(self):
        return self._invoice_amount_list

    @invoice_amount_list.setter
    def invoice_amount_list(self, value):
        if isinstance(value, list):
            self._invoice_amount_list = list()
            for i in value:
                if isinstance(i, NatrualPersonInvoiceAmountMonthly):
                    self._invoice_amount_list.append(i)
                else:
                    self._invoice_amount_list.append(NatrualPersonInvoiceAmountMonthly.from_alipay_dict(i))
    @property
    def paid_individual_tax_amount_current_year(self):
        return self._paid_individual_tax_amount_current_year

    @paid_individual_tax_amount_current_year.setter
    def paid_individual_tax_amount_current_year(self, value):
        self._paid_individual_tax_amount_current_year = value
    @property
    def scrapped_tax_calc_item_list(self):
        return self._scrapped_tax_calc_item_list

    @scrapped_tax_calc_item_list.setter
    def scrapped_tax_calc_item_list(self, value):
        if isinstance(value, list):
            self._scrapped_tax_calc_item_list = list()
            for i in value:
                if isinstance(i, RecyclingScrappedTaxCalcItem):
                    self._scrapped_tax_calc_item_list.append(i)
                else:
                    self._scrapped_tax_calc_item_list.append(RecyclingScrappedTaxCalcItem.from_alipay_dict(i))
    @property
    def wait_pay_general_invoice_1(self):
        return self._wait_pay_general_invoice_1

    @wait_pay_general_invoice_1.setter
    def wait_pay_general_invoice_1(self, value):
        self._wait_pay_general_invoice_1 = value
    @property
    def wait_pay_general_invoice_edu_amount(self):
        return self._wait_pay_general_invoice_edu_amount

    @wait_pay_general_invoice_edu_amount.setter
    def wait_pay_general_invoice_edu_amount(self, value):
        self._wait_pay_general_invoice_edu_amount = value
    @property
    def wait_pay_special_invoice_1(self):
        return self._wait_pay_special_invoice_1

    @wait_pay_special_invoice_1.setter
    def wait_pay_special_invoice_1(self, value):
        self._wait_pay_special_invoice_1 = value
    @property
    def wait_pay_special_invoice_3(self):
        return self._wait_pay_special_invoice_3

    @wait_pay_special_invoice_3.setter
    def wait_pay_special_invoice_3(self, value):
        self._wait_pay_special_invoice_3 = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceScrappednaturaltaxQueryResponse, self).parse_response_content(response_content)
        if 'individual_tax_accumulated_amount_current_year' in response:
            self.individual_tax_accumulated_amount_current_year = response['individual_tax_accumulated_amount_current_year']
        if 'interrupt' in response:
            self.interrupt = response['interrupt']
        if 'invoice_amount_list' in response:
            self.invoice_amount_list = response['invoice_amount_list']
        if 'paid_individual_tax_amount_current_year' in response:
            self.paid_individual_tax_amount_current_year = response['paid_individual_tax_amount_current_year']
        if 'scrapped_tax_calc_item_list' in response:
            self.scrapped_tax_calc_item_list = response['scrapped_tax_calc_item_list']
        if 'wait_pay_general_invoice_1' in response:
            self.wait_pay_general_invoice_1 = response['wait_pay_general_invoice_1']
        if 'wait_pay_general_invoice_edu_amount' in response:
            self.wait_pay_general_invoice_edu_amount = response['wait_pay_general_invoice_edu_amount']
        if 'wait_pay_special_invoice_1' in response:
            self.wait_pay_special_invoice_1 = response['wait_pay_special_invoice_1']
        if 'wait_pay_special_invoice_3' in response:
            self.wait_pay_special_invoice_3 = response['wait_pay_special_invoice_3']
