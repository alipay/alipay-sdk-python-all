#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliverySubOrderVO(object):

    def __init__(self):
        self._delivery_date = None
        self._period = None
        self._status = None

    @property
    def delivery_date(self):
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, value):
        self._delivery_date = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_date:
            if hasattr(self.delivery_date, 'to_alipay_dict'):
                params['delivery_date'] = self.delivery_date.to_alipay_dict()
            else:
                params['delivery_date'] = self.delivery_date
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliverySubOrderVO()
        if 'delivery_date' in d:
            o.delivery_date = d['delivery_date']
        if 'period' in d:
            o.period = d['period']
        if 'status' in d:
            o.status = d['status']
        return o


