#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentRoyalty(object):

    def __init__(self):
        self._period = None
        self._royalty_after_price = None
        self._royalty_price = None
        self._royalty_status = None
        self._royalty_time = None
        self._stage = None
        self._type = None

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def royalty_after_price(self):
        return self._royalty_after_price

    @royalty_after_price.setter
    def royalty_after_price(self, value):
        self._royalty_after_price = value
    @property
    def royalty_price(self):
        return self._royalty_price

    @royalty_price.setter
    def royalty_price(self, value):
        self._royalty_price = value
    @property
    def royalty_status(self):
        return self._royalty_status

    @royalty_status.setter
    def royalty_status(self, value):
        self._royalty_status = value
    @property
    def royalty_time(self):
        return self._royalty_time

    @royalty_time.setter
    def royalty_time(self, value):
        self._royalty_time = value
    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        self._stage = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.royalty_after_price:
            if hasattr(self.royalty_after_price, 'to_alipay_dict'):
                params['royalty_after_price'] = self.royalty_after_price.to_alipay_dict()
            else:
                params['royalty_after_price'] = self.royalty_after_price
        if self.royalty_price:
            if hasattr(self.royalty_price, 'to_alipay_dict'):
                params['royalty_price'] = self.royalty_price.to_alipay_dict()
            else:
                params['royalty_price'] = self.royalty_price
        if self.royalty_status:
            if hasattr(self.royalty_status, 'to_alipay_dict'):
                params['royalty_status'] = self.royalty_status.to_alipay_dict()
            else:
                params['royalty_status'] = self.royalty_status
        if self.royalty_time:
            if hasattr(self.royalty_time, 'to_alipay_dict'):
                params['royalty_time'] = self.royalty_time.to_alipay_dict()
            else:
                params['royalty_time'] = self.royalty_time
        if self.stage:
            if hasattr(self.stage, 'to_alipay_dict'):
                params['stage'] = self.stage.to_alipay_dict()
            else:
                params['stage'] = self.stage
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentRoyalty()
        if 'period' in d:
            o.period = d['period']
        if 'royalty_after_price' in d:
            o.royalty_after_price = d['royalty_after_price']
        if 'royalty_price' in d:
            o.royalty_price = d['royalty_price']
        if 'royalty_status' in d:
            o.royalty_status = d['royalty_status']
        if 'royalty_time' in d:
            o.royalty_time = d['royalty_time']
        if 'stage' in d:
            o.stage = d['stage']
        if 'type' in d:
            o.type = d['type']
        return o


