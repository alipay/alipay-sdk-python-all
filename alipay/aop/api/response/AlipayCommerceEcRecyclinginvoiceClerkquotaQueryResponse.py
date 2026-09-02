#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcRecyclinginvoiceClerkquotaQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcRecyclinginvoiceClerkquotaQueryResponse, self).__init__()
        self._calculate_time = None
        self._company_clerk_id = None
        self._locked_amount = None
        self._quota_type = None
        self._remain_amount = None
        self._total_amount = None

    @property
    def calculate_time(self):
        return self._calculate_time

    @calculate_time.setter
    def calculate_time(self, value):
        self._calculate_time = value
    @property
    def company_clerk_id(self):
        return self._company_clerk_id

    @company_clerk_id.setter
    def company_clerk_id(self, value):
        self._company_clerk_id = value
    @property
    def locked_amount(self):
        return self._locked_amount

    @locked_amount.setter
    def locked_amount(self, value):
        self._locked_amount = value
    @property
    def quota_type(self):
        return self._quota_type

    @quota_type.setter
    def quota_type(self, value):
        self._quota_type = value
    @property
    def remain_amount(self):
        return self._remain_amount

    @remain_amount.setter
    def remain_amount(self, value):
        self._remain_amount = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcRecyclinginvoiceClerkquotaQueryResponse, self).parse_response_content(response_content)
        if 'calculate_time' in response:
            self.calculate_time = response['calculate_time']
        if 'company_clerk_id' in response:
            self.company_clerk_id = response['company_clerk_id']
        if 'locked_amount' in response:
            self.locked_amount = response['locked_amount']
        if 'quota_type' in response:
            self.quota_type = response['quota_type']
        if 'remain_amount' in response:
            self.remain_amount = response['remain_amount']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
