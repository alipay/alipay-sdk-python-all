#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TransportTrip import TransportTrip


class WorkSchedulePlan(object):

    def __init__(self):
        self._ext_param = None
        self._line_key = None
        self._trip_chain = None
        self._vehicle_id = None

    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def line_key(self):
        return self._line_key

    @line_key.setter
    def line_key(self, value):
        self._line_key = value
    @property
    def trip_chain(self):
        return self._trip_chain

    @trip_chain.setter
    def trip_chain(self, value):
        if isinstance(value, list):
            self._trip_chain = list()
            for i in value:
                if isinstance(i, TransportTrip):
                    self._trip_chain.append(i)
                else:
                    self._trip_chain.append(TransportTrip.from_alipay_dict(i))
    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, value):
        self._vehicle_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.line_key:
            if hasattr(self.line_key, 'to_alipay_dict'):
                params['line_key'] = self.line_key.to_alipay_dict()
            else:
                params['line_key'] = self.line_key
        if self.trip_chain:
            if isinstance(self.trip_chain, list):
                for i in range(0, len(self.trip_chain)):
                    element = self.trip_chain[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trip_chain[i] = element.to_alipay_dict()
            if hasattr(self.trip_chain, 'to_alipay_dict'):
                params['trip_chain'] = self.trip_chain.to_alipay_dict()
            else:
                params['trip_chain'] = self.trip_chain
        if self.vehicle_id:
            if hasattr(self.vehicle_id, 'to_alipay_dict'):
                params['vehicle_id'] = self.vehicle_id.to_alipay_dict()
            else:
                params['vehicle_id'] = self.vehicle_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WorkSchedulePlan()
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'line_key' in d:
            o.line_key = d['line_key']
        if 'trip_chain' in d:
            o.trip_chain = d['trip_chain']
        if 'vehicle_id' in d:
            o.vehicle_id = d['vehicle_id']
        return o


