#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoanapplySmartcountyLoaninfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplySmartcountyLoaninfoQueryResponse, self).__init__()
        self._admited = None
        self._county_area = None
        self._mybank_user = None
        self._show_entrance = None

    @property
    def admited(self):
        return self._admited

    @admited.setter
    def admited(self, value):
        self._admited = value
    @property
    def county_area(self):
        return self._county_area

    @county_area.setter
    def county_area(self, value):
        if isinstance(value, list):
            self._county_area = list()
            for i in value:
                self._county_area.append(i)
    @property
    def mybank_user(self):
        return self._mybank_user

    @mybank_user.setter
    def mybank_user(self, value):
        self._mybank_user = value
    @property
    def show_entrance(self):
        return self._show_entrance

    @show_entrance.setter
    def show_entrance(self, value):
        self._show_entrance = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplySmartcountyLoaninfoQueryResponse, self).parse_response_content(response_content)
        if 'admited' in response:
            self.admited = response['admited']
        if 'county_area' in response:
            self.county_area = response['county_area']
        if 'mybank_user' in response:
            self.mybank_user = response['mybank_user']
        if 'show_entrance' in response:
            self.show_entrance = response['show_entrance']
