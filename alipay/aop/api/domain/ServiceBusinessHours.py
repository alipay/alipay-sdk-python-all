#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessTime import BusinessTime


class ServiceBusinessHours(object):

    def __init__(self):
        self._business_date = None
        self._business_time = None

    @property
    def business_date(self):
        return self._business_date

    @business_date.setter
    def business_date(self, value):
        if isinstance(value, list):
            self._business_date = list()
            for i in value:
                self._business_date.append(i)
    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        if isinstance(value, list):
            self._business_time = list()
            for i in value:
                if isinstance(i, BusinessTime):
                    self._business_time.append(i)
                else:
                    self._business_time.append(BusinessTime.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.business_date:
            if isinstance(self.business_date, list):
                for i in range(0, len(self.business_date)):
                    element = self.business_date[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_date[i] = element.to_alipay_dict()
            if hasattr(self.business_date, 'to_alipay_dict'):
                params['business_date'] = self.business_date.to_alipay_dict()
            else:
                params['business_date'] = self.business_date
        if self.business_time:
            if isinstance(self.business_time, list):
                for i in range(0, len(self.business_time)):
                    element = self.business_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_time[i] = element.to_alipay_dict()
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceBusinessHours()
        if 'business_date' in d:
            o.business_date = d['business_date']
        if 'business_time' in d:
            o.business_time = d['business_time']
        return o


