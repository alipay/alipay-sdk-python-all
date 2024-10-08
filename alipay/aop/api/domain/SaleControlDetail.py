#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaleControlDetail(object):

    def __init__(self):
        self._crowd_type = None
        self._lower_limit = None
        self._passenger_type = None
        self._up_limit = None

    @property
    def crowd_type(self):
        return self._crowd_type

    @crowd_type.setter
    def crowd_type(self, value):
        self._crowd_type = value
    @property
    def lower_limit(self):
        return self._lower_limit

    @lower_limit.setter
    def lower_limit(self, value):
        self._lower_limit = value
    @property
    def passenger_type(self):
        return self._passenger_type

    @passenger_type.setter
    def passenger_type(self, value):
        self._passenger_type = value
    @property
    def up_limit(self):
        return self._up_limit

    @up_limit.setter
    def up_limit(self, value):
        self._up_limit = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_type:
            if hasattr(self.crowd_type, 'to_alipay_dict'):
                params['crowd_type'] = self.crowd_type.to_alipay_dict()
            else:
                params['crowd_type'] = self.crowd_type
        if self.lower_limit:
            if hasattr(self.lower_limit, 'to_alipay_dict'):
                params['lower_limit'] = self.lower_limit.to_alipay_dict()
            else:
                params['lower_limit'] = self.lower_limit
        if self.passenger_type:
            if hasattr(self.passenger_type, 'to_alipay_dict'):
                params['passenger_type'] = self.passenger_type.to_alipay_dict()
            else:
                params['passenger_type'] = self.passenger_type
        if self.up_limit:
            if hasattr(self.up_limit, 'to_alipay_dict'):
                params['up_limit'] = self.up_limit.to_alipay_dict()
            else:
                params['up_limit'] = self.up_limit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaleControlDetail()
        if 'crowd_type' in d:
            o.crowd_type = d['crowd_type']
        if 'lower_limit' in d:
            o.lower_limit = d['lower_limit']
        if 'passenger_type' in d:
            o.passenger_type = d['passenger_type']
        if 'up_limit' in d:
            o.up_limit = d['up_limit']
        return o


