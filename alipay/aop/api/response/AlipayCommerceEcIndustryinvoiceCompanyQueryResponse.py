#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CompanyProductInfo import CompanyProductInfo
from alipay.aop.api.domain.CompanyInvoiceClerk import CompanyInvoiceClerk


class AlipayCommerceEcIndustryinvoiceCompanyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcIndustryinvoiceCompanyQueryResponse, self).__init__()
        self._company_name = None
        self._company_product_info_list = None
        self._invoice_clerk = None
        self._tax_no = None

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def company_product_info_list(self):
        return self._company_product_info_list

    @company_product_info_list.setter
    def company_product_info_list(self, value):
        if isinstance(value, list):
            self._company_product_info_list = list()
            for i in value:
                if isinstance(i, CompanyProductInfo):
                    self._company_product_info_list.append(i)
                else:
                    self._company_product_info_list.append(CompanyProductInfo.from_alipay_dict(i))
    @property
    def invoice_clerk(self):
        return self._invoice_clerk

    @invoice_clerk.setter
    def invoice_clerk(self, value):
        if isinstance(value, CompanyInvoiceClerk):
            self._invoice_clerk = value
        else:
            self._invoice_clerk = CompanyInvoiceClerk.from_alipay_dict(value)
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcIndustryinvoiceCompanyQueryResponse, self).parse_response_content(response_content)
        if 'company_name' in response:
            self.company_name = response['company_name']
        if 'company_product_info_list' in response:
            self.company_product_info_list = response['company_product_info_list']
        if 'invoice_clerk' in response:
            self.invoice_clerk = response['invoice_clerk']
        if 'tax_no' in response:
            self.tax_no = response['tax_no']
