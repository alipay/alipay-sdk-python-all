#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcoRenthouseOtherAmount import EcoRenthouseOtherAmount


class EcoDisRenthousepayTypeList(object):

    def __init__(self):
        self._foregift_amount = None
        self._lease_term = None
        self._other_amount = None
        self._pay_type = None
        self._room_amount = None
        self._service_amount = None
        self._service_type = None

    @property
    def foregift_amount(self):
        return self._foregift_amount

    @foregift_amount.setter
    def foregift_amount(self, value):
        self._foregift_amount = value
    @property
    def lease_term(self):
        return self._lease_term

    @lease_term.setter
    def lease_term(self, value):
        self._lease_term = value
    @property
    def other_amount(self):
        return self._other_amount

    @other_amount.setter
    def other_amount(self, value):
        if isinstance(value, list):
            self._other_amount = list()
            for i in value:
                if isinstance(i, EcoRenthouseOtherAmount):
                    self._other_amount.append(i)
                else:
                    self._other_amount.append(EcoRenthouseOtherAmount.from_alipay_dict(i))
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def room_amount(self):
        return self._room_amount

    @room_amount.setter
    def room_amount(self, value):
        self._room_amount = value
    @property
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, value):
        self._service_amount = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.foregift_amount:
            if hasattr(self.foregift_amount, 'to_alipay_dict'):
                params['foregift_amount'] = self.foregift_amount.to_alipay_dict()
            else:
                params['foregift_amount'] = self.foregift_amount
        if self.lease_term:
            if hasattr(self.lease_term, 'to_alipay_dict'):
                params['lease_term'] = self.lease_term.to_alipay_dict()
            else:
                params['lease_term'] = self.lease_term
        if self.other_amount:
            if isinstance(self.other_amount, list):
                for i in range(0, len(self.other_amount)):
                    element = self.other_amount[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_amount[i] = element.to_alipay_dict()
            if hasattr(self.other_amount, 'to_alipay_dict'):
                params['other_amount'] = self.other_amount.to_alipay_dict()
            else:
                params['other_amount'] = self.other_amount
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.room_amount:
            if hasattr(self.room_amount, 'to_alipay_dict'):
                params['room_amount'] = self.room_amount.to_alipay_dict()
            else:
                params['room_amount'] = self.room_amount
        if self.service_amount:
            if hasattr(self.service_amount, 'to_alipay_dict'):
                params['service_amount'] = self.service_amount.to_alipay_dict()
            else:
                params['service_amount'] = self.service_amount
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcoDisRenthousepayTypeList()
        if 'foregift_amount' in d:
            o.foregift_amount = d['foregift_amount']
        if 'lease_term' in d:
            o.lease_term = d['lease_term']
        if 'other_amount' in d:
            o.other_amount = d['other_amount']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'room_amount' in d:
            o.room_amount = d['room_amount']
        if 'service_amount' in d:
            o.service_amount = d['service_amount']
        if 'service_type' in d:
            o.service_type = d['service_type']
        return o


