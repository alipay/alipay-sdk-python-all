#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryRentHousingQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryRentHousingQueryResponse, self).__init__()
        self._acc_amount = None
        self._biz_seq = None
        self._description = None
        self._order_status = None
        self._org_biz_no = None
        self._self_amount = None
        self._subject = None
        self._total_amount = None
        self._trade_no = None

    @property
    def acc_amount(self):
        return self._acc_amount

    @acc_amount.setter
    def acc_amount(self, value):
        self._acc_amount = value
    @property
    def biz_seq(self):
        return self._biz_seq

    @biz_seq.setter
    def biz_seq(self, value):
        self._biz_seq = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def org_biz_no(self):
        return self._org_biz_no

    @org_biz_no.setter
    def org_biz_no(self, value):
        self._org_biz_no = value
    @property
    def self_amount(self):
        return self._self_amount

    @self_amount.setter
    def self_amount(self, value):
        self._self_amount = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryRentHousingQueryResponse, self).parse_response_content(response_content)
        if 'acc_amount' in response:
            self.acc_amount = response['acc_amount']
        if 'biz_seq' in response:
            self.biz_seq = response['biz_seq']
        if 'description' in response:
            self.description = response['description']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'org_biz_no' in response:
            self.org_biz_no = response['org_biz_no']
        if 'self_amount' in response:
            self.self_amount = response['self_amount']
        if 'subject' in response:
            self.subject = response['subject']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
