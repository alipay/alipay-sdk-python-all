#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderModifyRentInstallment import OrderModifyRentInstallment


class OrderModifyRentPlanInfo(object):

    def __init__(self):
        self._installments = None
        self._rent_end_time = None
        self._rent_start_time = None

    @property
    def installments(self):
        return self._installments

    @installments.setter
    def installments(self, value):
        if isinstance(value, list):
            self._installments = list()
            for i in value:
                if isinstance(i, OrderModifyRentInstallment):
                    self._installments.append(i)
                else:
                    self._installments.append(OrderModifyRentInstallment.from_alipay_dict(i))
    @property
    def rent_end_time(self):
        return self._rent_end_time

    @rent_end_time.setter
    def rent_end_time(self, value):
        self._rent_end_time = value
    @property
    def rent_start_time(self):
        return self._rent_start_time

    @rent_start_time.setter
    def rent_start_time(self, value):
        self._rent_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.installments:
            if isinstance(self.installments, list):
                for i in range(0, len(self.installments)):
                    element = self.installments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.installments[i] = element.to_alipay_dict()
            if hasattr(self.installments, 'to_alipay_dict'):
                params['installments'] = self.installments.to_alipay_dict()
            else:
                params['installments'] = self.installments
        if self.rent_end_time:
            if hasattr(self.rent_end_time, 'to_alipay_dict'):
                params['rent_end_time'] = self.rent_end_time.to_alipay_dict()
            else:
                params['rent_end_time'] = self.rent_end_time
        if self.rent_start_time:
            if hasattr(self.rent_start_time, 'to_alipay_dict'):
                params['rent_start_time'] = self.rent_start_time.to_alipay_dict()
            else:
                params['rent_start_time'] = self.rent_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderModifyRentPlanInfo()
        if 'installments' in d:
            o.installments = d['installments']
        if 'rent_end_time' in d:
            o.rent_end_time = d['rent_end_time']
        if 'rent_start_time' in d:
            o.rent_start_time = d['rent_start_time']
        return o


