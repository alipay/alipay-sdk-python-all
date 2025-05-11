#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TaxCategory import TaxCategory


class AlipayCommerceEcRecyclinginvoiceTaxcategoryBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceTaxcategoryBatchqueryResponse, self).__init__()
        self._tax_category_list = None

    @property
    def tax_category_list(self):
        return self._tax_category_list

    @tax_category_list.setter
    def tax_category_list(self, value):
        if isinstance(value, list):
            self._tax_category_list = list()
            for i in value:
                if isinstance(i, TaxCategory):
                    self._tax_category_list.append(i)
                else:
                    self._tax_category_list.append(TaxCategory.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceTaxcategoryBatchqueryResponse, self).parse_response_content(response_content)
        if 'tax_category_list' in response:
            self.tax_category_list = response['tax_category_list']
