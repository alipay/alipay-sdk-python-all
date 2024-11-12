#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentContractDictVo import RentContractDictVo
from alipay.aop.api.domain.RentContractDictVo import RentContractDictVo


class AlipayCloudCloudpromoContractFormInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoContractFormInitializeResponse, self).__init__()
        self._earliest_start_time = None
        self._furniture_list = None
        self._latest_start_time = None
        self._maximum_deposit_amount = None
        self._maximum_rent_amount = None
        self._maximum_rent_period = None
        self._pay_period_type_list = None
        self._room_type_list = None

    @property
    def earliest_start_time(self):
        return self._earliest_start_time

    @earliest_start_time.setter
    def earliest_start_time(self, value):
        self._earliest_start_time = value
    @property
    def furniture_list(self):
        return self._furniture_list

    @furniture_list.setter
    def furniture_list(self, value):
        if isinstance(value, list):
            self._furniture_list = list()
            for i in value:
                self._furniture_list.append(i)
    @property
    def latest_start_time(self):
        return self._latest_start_time

    @latest_start_time.setter
    def latest_start_time(self, value):
        self._latest_start_time = value
    @property
    def maximum_deposit_amount(self):
        return self._maximum_deposit_amount

    @maximum_deposit_amount.setter
    def maximum_deposit_amount(self, value):
        self._maximum_deposit_amount = value
    @property
    def maximum_rent_amount(self):
        return self._maximum_rent_amount

    @maximum_rent_amount.setter
    def maximum_rent_amount(self, value):
        self._maximum_rent_amount = value
    @property
    def maximum_rent_period(self):
        return self._maximum_rent_period

    @maximum_rent_period.setter
    def maximum_rent_period(self, value):
        self._maximum_rent_period = value
    @property
    def pay_period_type_list(self):
        return self._pay_period_type_list

    @pay_period_type_list.setter
    def pay_period_type_list(self, value):
        if isinstance(value, list):
            self._pay_period_type_list = list()
            for i in value:
                if isinstance(i, RentContractDictVo):
                    self._pay_period_type_list.append(i)
                else:
                    self._pay_period_type_list.append(RentContractDictVo.from_alipay_dict(i))
    @property
    def room_type_list(self):
        return self._room_type_list

    @room_type_list.setter
    def room_type_list(self, value):
        if isinstance(value, list):
            self._room_type_list = list()
            for i in value:
                if isinstance(i, RentContractDictVo):
                    self._room_type_list.append(i)
                else:
                    self._room_type_list.append(RentContractDictVo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoContractFormInitializeResponse, self).parse_response_content(response_content)
        if 'earliest_start_time' in response:
            self.earliest_start_time = response['earliest_start_time']
        if 'furniture_list' in response:
            self.furniture_list = response['furniture_list']
        if 'latest_start_time' in response:
            self.latest_start_time = response['latest_start_time']
        if 'maximum_deposit_amount' in response:
            self.maximum_deposit_amount = response['maximum_deposit_amount']
        if 'maximum_rent_amount' in response:
            self.maximum_rent_amount = response['maximum_rent_amount']
        if 'maximum_rent_period' in response:
            self.maximum_rent_period = response['maximum_rent_period']
        if 'pay_period_type_list' in response:
            self.pay_period_type_list = response['pay_period_type_list']
        if 'room_type_list' in response:
            self.room_type_list = response['room_type_list']
