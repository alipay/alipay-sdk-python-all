#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OfflineLaborInsurancePolicy import OfflineLaborInsurancePolicy


class AlipayCommerceOfflinelaborInsuranceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOfflinelaborInsuranceQueryResponse, self).__init__()
        self._current_page = None
        self._page_size = None
        self._policys = None
        self._total = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def policys(self):
        return self._policys

    @policys.setter
    def policys(self, value):
        if isinstance(value, list):
            self._policys = list()
            for i in value:
                if isinstance(i, OfflineLaborInsurancePolicy):
                    self._policys.append(i)
                else:
                    self._policys.append(OfflineLaborInsurancePolicy.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOfflinelaborInsuranceQueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'policys' in response:
            self.policys = response['policys']
        if 'total' in response:
            self.total = response['total']
