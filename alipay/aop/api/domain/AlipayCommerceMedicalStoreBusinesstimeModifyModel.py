#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessDateDTO import BusinessDateDTO


class AlipayCommerceMedicalStoreBusinesstimeModifyModel(object):

    def __init__(self):
        self._business_dates = None
        self._store_code = None

    @property
    def business_dates(self):
        return self._business_dates

    @business_dates.setter
    def business_dates(self, value):
        if isinstance(value, list):
            self._business_dates = list()
            for i in value:
                if isinstance(i, BusinessDateDTO):
                    self._business_dates.append(i)
                else:
                    self._business_dates.append(BusinessDateDTO.from_alipay_dict(i))
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_dates:
            if isinstance(self.business_dates, list):
                for i in range(0, len(self.business_dates)):
                    element = self.business_dates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_dates[i] = element.to_alipay_dict()
            if hasattr(self.business_dates, 'to_alipay_dict'):
                params['business_dates'] = self.business_dates.to_alipay_dict()
            else:
                params['business_dates'] = self.business_dates
        if self.store_code:
            if hasattr(self.store_code, 'to_alipay_dict'):
                params['store_code'] = self.store_code.to_alipay_dict()
            else:
                params['store_code'] = self.store_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalStoreBusinesstimeModifyModel()
        if 'business_dates' in d:
            o.business_dates = d['business_dates']
        if 'store_code' in d:
            o.store_code = d['store_code']
        return o


