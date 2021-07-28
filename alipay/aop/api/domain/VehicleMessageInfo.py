#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VehicleConditionInfo import VehicleConditionInfo
from alipay.aop.api.domain.VehicleModuleInfo import VehicleModuleInfo


class VehicleMessageInfo(object):

    def __init__(self):
        self._vehicle_cond_infos = None
        self._vehicle_module_infos = None

    @property
    def vehicle_cond_infos(self):
        return self._vehicle_cond_infos

    @vehicle_cond_infos.setter
    def vehicle_cond_infos(self, value):
        if isinstance(value, list):
            self._vehicle_cond_infos = list()
            for i in value:
                if isinstance(i, VehicleConditionInfo):
                    self._vehicle_cond_infos.append(i)
                else:
                    self._vehicle_cond_infos.append(VehicleConditionInfo.from_alipay_dict(i))
    @property
    def vehicle_module_infos(self):
        return self._vehicle_module_infos

    @vehicle_module_infos.setter
    def vehicle_module_infos(self, value):
        if isinstance(value, list):
            self._vehicle_module_infos = list()
            for i in value:
                if isinstance(i, VehicleModuleInfo):
                    self._vehicle_module_infos.append(i)
                else:
                    self._vehicle_module_infos.append(VehicleModuleInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.vehicle_cond_infos:
            if isinstance(self.vehicle_cond_infos, list):
                for i in range(0, len(self.vehicle_cond_infos)):
                    element = self.vehicle_cond_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.vehicle_cond_infos[i] = element.to_alipay_dict()
            if hasattr(self.vehicle_cond_infos, 'to_alipay_dict'):
                params['vehicle_cond_infos'] = self.vehicle_cond_infos.to_alipay_dict()
            else:
                params['vehicle_cond_infos'] = self.vehicle_cond_infos
        if self.vehicle_module_infos:
            if isinstance(self.vehicle_module_infos, list):
                for i in range(0, len(self.vehicle_module_infos)):
                    element = self.vehicle_module_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.vehicle_module_infos[i] = element.to_alipay_dict()
            if hasattr(self.vehicle_module_infos, 'to_alipay_dict'):
                params['vehicle_module_infos'] = self.vehicle_module_infos.to_alipay_dict()
            else:
                params['vehicle_module_infos'] = self.vehicle_module_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehicleMessageInfo()
        if 'vehicle_cond_infos' in d:
            o.vehicle_cond_infos = d['vehicle_cond_infos']
        if 'vehicle_module_infos' in d:
            o.vehicle_module_infos = d['vehicle_module_infos']
        return o


