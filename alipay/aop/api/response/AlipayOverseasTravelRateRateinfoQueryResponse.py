#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ClassRateInfo import ClassRateInfo
from alipay.aop.api.domain.ClassRateInfo import ClassRateInfo


class AlipayOverseasTravelRateRateinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTravelRateRateinfoQueryResponse, self).__init__()
        self._benefit_rate_list = None
        self._contrast_rate = None
        self._contrast_rate_amount = None
        self._currency = None
        self._currency_icon = None
        self._member_rate_list = None
        self._rate_desc = None
        self._rate_source = None
        self._user_benefit_grade = None
        self._user_member_grade = None
        self._user_rate = None
        self._user_rate_amount = None

    @property
    def benefit_rate_list(self):
        return self._benefit_rate_list

    @benefit_rate_list.setter
    def benefit_rate_list(self, value):
        if isinstance(value, list):
            self._benefit_rate_list = list()
            for i in value:
                if isinstance(i, ClassRateInfo):
                    self._benefit_rate_list.append(i)
                else:
                    self._benefit_rate_list.append(ClassRateInfo.from_alipay_dict(i))
    @property
    def contrast_rate(self):
        return self._contrast_rate

    @contrast_rate.setter
    def contrast_rate(self, value):
        self._contrast_rate = value
    @property
    def contrast_rate_amount(self):
        return self._contrast_rate_amount

    @contrast_rate_amount.setter
    def contrast_rate_amount(self, value):
        self._contrast_rate_amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def currency_icon(self):
        return self._currency_icon

    @currency_icon.setter
    def currency_icon(self, value):
        self._currency_icon = value
    @property
    def member_rate_list(self):
        return self._member_rate_list

    @member_rate_list.setter
    def member_rate_list(self, value):
        if isinstance(value, list):
            self._member_rate_list = list()
            for i in value:
                if isinstance(i, ClassRateInfo):
                    self._member_rate_list.append(i)
                else:
                    self._member_rate_list.append(ClassRateInfo.from_alipay_dict(i))
    @property
    def rate_desc(self):
        return self._rate_desc

    @rate_desc.setter
    def rate_desc(self, value):
        self._rate_desc = value
    @property
    def rate_source(self):
        return self._rate_source

    @rate_source.setter
    def rate_source(self, value):
        self._rate_source = value
    @property
    def user_benefit_grade(self):
        return self._user_benefit_grade

    @user_benefit_grade.setter
    def user_benefit_grade(self, value):
        self._user_benefit_grade = value
    @property
    def user_member_grade(self):
        return self._user_member_grade

    @user_member_grade.setter
    def user_member_grade(self, value):
        self._user_member_grade = value
    @property
    def user_rate(self):
        return self._user_rate

    @user_rate.setter
    def user_rate(self, value):
        self._user_rate = value
    @property
    def user_rate_amount(self):
        return self._user_rate_amount

    @user_rate_amount.setter
    def user_rate_amount(self, value):
        self._user_rate_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTravelRateRateinfoQueryResponse, self).parse_response_content(response_content)
        if 'benefit_rate_list' in response:
            self.benefit_rate_list = response['benefit_rate_list']
        if 'contrast_rate' in response:
            self.contrast_rate = response['contrast_rate']
        if 'contrast_rate_amount' in response:
            self.contrast_rate_amount = response['contrast_rate_amount']
        if 'currency' in response:
            self.currency = response['currency']
        if 'currency_icon' in response:
            self.currency_icon = response['currency_icon']
        if 'member_rate_list' in response:
            self.member_rate_list = response['member_rate_list']
        if 'rate_desc' in response:
            self.rate_desc = response['rate_desc']
        if 'rate_source' in response:
            self.rate_source = response['rate_source']
        if 'user_benefit_grade' in response:
            self.user_benefit_grade = response['user_benefit_grade']
        if 'user_member_grade' in response:
            self.user_member_grade = response['user_member_grade']
        if 'user_rate' in response:
            self.user_rate = response['user_rate']
        if 'user_rate_amount' in response:
            self.user_rate_amount = response['user_rate_amount']
