#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccountingEntityInfoDTO import AccountingEntityInfoDTO


class AlipayCommerceEcAccountingentityPageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcAccountingentityPageQueryResponse, self).__init__()
        self._accounting_entity_list = None
        self._current_page = None
        self._total_num = None
        self._total_pages = None

    @property
    def accounting_entity_list(self):
        return self._accounting_entity_list

    @accounting_entity_list.setter
    def accounting_entity_list(self, value):
        if isinstance(value, list):
            self._accounting_entity_list = list()
            for i in value:
                if isinstance(i, AccountingEntityInfoDTO):
                    self._accounting_entity_list.append(i)
                else:
                    self._accounting_entity_list.append(AccountingEntityInfoDTO.from_alipay_dict(i))
    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcAccountingentityPageQueryResponse, self).parse_response_content(response_content)
        if 'accounting_entity_list' in response:
            self.accounting_entity_list = response['accounting_entity_list']
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'total_num' in response:
            self.total_num = response['total_num']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
