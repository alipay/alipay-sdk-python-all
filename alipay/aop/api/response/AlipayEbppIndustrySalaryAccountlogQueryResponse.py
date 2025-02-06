#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccountLogListDTO import AccountLogListDTO


class AlipayEbppIndustrySalaryAccountlogQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySalaryAccountlogQueryResponse, self).__init__()
        self._account_log_list = None
        self._page_no = None
        self._page_size = None
        self._sign_xml = None
        self._total = None

    @property
    def account_log_list(self):
        return self._account_log_list

    @account_log_list.setter
    def account_log_list(self, value):
        if isinstance(value, list):
            self._account_log_list = list()
            for i in value:
                if isinstance(i, AccountLogListDTO):
                    self._account_log_list.append(i)
                else:
                    self._account_log_list.append(AccountLogListDTO.from_alipay_dict(i))
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def sign_xml(self):
        return self._sign_xml

    @sign_xml.setter
    def sign_xml(self, value):
        self._sign_xml = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySalaryAccountlogQueryResponse, self).parse_response_content(response_content)
        if 'account_log_list' in response:
            self.account_log_list = response['account_log_list']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'sign_xml' in response:
            self.sign_xml = response['sign_xml']
        if 'total' in response:
            self.total = response['total']
