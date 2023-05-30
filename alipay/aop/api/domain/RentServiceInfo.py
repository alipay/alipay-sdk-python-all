#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ParticipantInfoDTO import ParticipantInfoDTO
from alipay.aop.api.domain.ParticipantInfoDTO import ParticipantInfoDTO


class RentServiceInfo(object):

    def __init__(self):
        self._capital_principal = None
        self._invite_principal = None
        self._repayment_amount = None
        self._repayment_end_time = None
        self._repayment_period = None
        self._repayment_period_type = None

    @property
    def capital_principal(self):
        return self._capital_principal

    @capital_principal.setter
    def capital_principal(self, value):
        if isinstance(value, ParticipantInfoDTO):
            self._capital_principal = value
        else:
            self._capital_principal = ParticipantInfoDTO.from_alipay_dict(value)
    @property
    def invite_principal(self):
        return self._invite_principal

    @invite_principal.setter
    def invite_principal(self, value):
        if isinstance(value, ParticipantInfoDTO):
            self._invite_principal = value
        else:
            self._invite_principal = ParticipantInfoDTO.from_alipay_dict(value)
    @property
    def repayment_amount(self):
        return self._repayment_amount

    @repayment_amount.setter
    def repayment_amount(self, value):
        self._repayment_amount = value
    @property
    def repayment_end_time(self):
        return self._repayment_end_time

    @repayment_end_time.setter
    def repayment_end_time(self, value):
        self._repayment_end_time = value
    @property
    def repayment_period(self):
        return self._repayment_period

    @repayment_period.setter
    def repayment_period(self, value):
        self._repayment_period = value
    @property
    def repayment_period_type(self):
        return self._repayment_period_type

    @repayment_period_type.setter
    def repayment_period_type(self, value):
        self._repayment_period_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.capital_principal:
            if hasattr(self.capital_principal, 'to_alipay_dict'):
                params['capital_principal'] = self.capital_principal.to_alipay_dict()
            else:
                params['capital_principal'] = self.capital_principal
        if self.invite_principal:
            if hasattr(self.invite_principal, 'to_alipay_dict'):
                params['invite_principal'] = self.invite_principal.to_alipay_dict()
            else:
                params['invite_principal'] = self.invite_principal
        if self.repayment_amount:
            if hasattr(self.repayment_amount, 'to_alipay_dict'):
                params['repayment_amount'] = self.repayment_amount.to_alipay_dict()
            else:
                params['repayment_amount'] = self.repayment_amount
        if self.repayment_end_time:
            if hasattr(self.repayment_end_time, 'to_alipay_dict'):
                params['repayment_end_time'] = self.repayment_end_time.to_alipay_dict()
            else:
                params['repayment_end_time'] = self.repayment_end_time
        if self.repayment_period:
            if hasattr(self.repayment_period, 'to_alipay_dict'):
                params['repayment_period'] = self.repayment_period.to_alipay_dict()
            else:
                params['repayment_period'] = self.repayment_period
        if self.repayment_period_type:
            if hasattr(self.repayment_period_type, 'to_alipay_dict'):
                params['repayment_period_type'] = self.repayment_period_type.to_alipay_dict()
            else:
                params['repayment_period_type'] = self.repayment_period_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentServiceInfo()
        if 'capital_principal' in d:
            o.capital_principal = d['capital_principal']
        if 'invite_principal' in d:
            o.invite_principal = d['invite_principal']
        if 'repayment_amount' in d:
            o.repayment_amount = d['repayment_amount']
        if 'repayment_end_time' in d:
            o.repayment_end_time = d['repayment_end_time']
        if 'repayment_period' in d:
            o.repayment_period = d['repayment_period']
        if 'repayment_period_type' in d:
            o.repayment_period_type = d['repayment_period_type']
        return o


