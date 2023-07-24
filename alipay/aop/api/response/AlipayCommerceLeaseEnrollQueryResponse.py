#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LeaseEnrollDTO import LeaseEnrollDTO


class AlipayCommerceLeaseEnrollQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLeaseEnrollQueryResponse, self).__init__()
        self._enroll_list = None
        self._page = None
        self._total_count = None

    @property
    def enroll_list(self):
        return self._enroll_list

    @enroll_list.setter
    def enroll_list(self, value):
        if isinstance(value, list):
            self._enroll_list = list()
            for i in value:
                if isinstance(i, LeaseEnrollDTO):
                    self._enroll_list.append(i)
                else:
                    self._enroll_list.append(LeaseEnrollDTO.from_alipay_dict(i))
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLeaseEnrollQueryResponse, self).parse_response_content(response_content)
        if 'enroll_list' in response:
            self.enroll_list = response['enroll_list']
        if 'page' in response:
            self.page = response['page']
        if 'total_count' in response:
            self.total_count = response['total_count']
