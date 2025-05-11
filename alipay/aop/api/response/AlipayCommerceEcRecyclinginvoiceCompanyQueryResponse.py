#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CompanyProduct import CompanyProduct


class AlipayCommerceEcRecyclinginvoiceCompanyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceCompanyQueryResponse, self).__init__()
        self._company_id = None
        self._company_name = None
        self._company_product_list = None
        self._company_tax_no = None

    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def company_product_list(self):
        return self._company_product_list

    @company_product_list.setter
    def company_product_list(self, value):
        if isinstance(value, list):
            self._company_product_list = list()
            for i in value:
                if isinstance(i, CompanyProduct):
                    self._company_product_list.append(i)
                else:
                    self._company_product_list.append(CompanyProduct.from_alipay_dict(i))
    @property
    def company_tax_no(self):
        return self._company_tax_no

    @company_tax_no.setter
    def company_tax_no(self, value):
        self._company_tax_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceCompanyQueryResponse, self).parse_response_content(response_content)
        if 'company_id' in response:
            self.company_id = response['company_id']
        if 'company_name' in response:
            self.company_name = response['company_name']
        if 'company_product_list' in response:
            self.company_product_list = response['company_product_list']
        if 'company_tax_no' in response:
            self.company_tax_no = response['company_tax_no']
