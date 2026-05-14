#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarfinVehicleVerificationInfo(object):

    def __init__(self):
        self._vehicle_self_flag = None

    @property
    def vehicle_self_flag(self):
        return self._vehicle_self_flag

    @vehicle_self_flag.setter
    def vehicle_self_flag(self, value):
        self._vehicle_self_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.vehicle_self_flag:
            if hasattr(self.vehicle_self_flag, 'to_alipay_dict'):
                params['vehicle_self_flag'] = self.vehicle_self_flag.to_alipay_dict()
            else:
                params['vehicle_self_flag'] = self.vehicle_self_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinVehicleVerificationInfo()
        if 'vehicle_self_flag' in d:
            o.vehicle_self_flag = d['vehicle_self_flag']
        return o


