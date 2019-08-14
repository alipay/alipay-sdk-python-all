#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAccountAliyunUnbindModel(object):

    def __init__(self):
        self._bind_id = None
        self._havana_bind_station = None
        self._pk = None

    @property
    def bind_id(self):
        return self._bind_id

    @bind_id.setter
    def bind_id(self, value):
        self._bind_id = value
    @property
    def havana_bind_station(self):
        return self._havana_bind_station

    @havana_bind_station.setter
    def havana_bind_station(self, value):
        self._havana_bind_station = value
    @property
    def pk(self):
        return self._pk

    @pk.setter
    def pk(self, value):
        self._pk = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_id:
            if hasattr(self.bind_id, 'to_alipay_dict'):
                params['bind_id'] = self.bind_id.to_alipay_dict()
            else:
                params['bind_id'] = self.bind_id
        if self.havana_bind_station:
            if hasattr(self.havana_bind_station, 'to_alipay_dict'):
                params['havana_bind_station'] = self.havana_bind_station.to_alipay_dict()
            else:
                params['havana_bind_station'] = self.havana_bind_station
        if self.pk:
            if hasattr(self.pk, 'to_alipay_dict'):
                params['pk'] = self.pk.to_alipay_dict()
            else:
                params['pk'] = self.pk
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAccountAliyunUnbindModel()
        if 'bind_id' in d:
            o.bind_id = d['bind_id']
        if 'havana_bind_station' in d:
            o.havana_bind_station = d['havana_bind_station']
        if 'pk' in d:
            o.pk = d['pk']
        return o


