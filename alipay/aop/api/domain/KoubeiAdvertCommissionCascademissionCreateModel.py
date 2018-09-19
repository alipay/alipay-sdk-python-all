#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CascadeMissionConfModel import CascadeMissionConfModel


class KoubeiAdvertCommissionCascademissionCreateModel(object):

    def __init__(self):
        self._cascade_mission_conf = None
        self._identify = None
        self._identify_type = None
        self._name = None

    @property
    def cascade_mission_conf(self):
        return self._cascade_mission_conf

    @cascade_mission_conf.setter
    def cascade_mission_conf(self, value):
        if isinstance(value, list):
            self._cascade_mission_conf = list()
            for i in value:
                if isinstance(i, CascadeMissionConfModel):
                    self._cascade_mission_conf.append(i)
                else:
                    self._cascade_mission_conf.append(CascadeMissionConfModel.from_alipay_dict(i))
    @property
    def identify(self):
        return self._identify

    @identify.setter
    def identify(self, value):
        self._identify = value
    @property
    def identify_type(self):
        return self._identify_type

    @identify_type.setter
    def identify_type(self, value):
        self._identify_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cascade_mission_conf:
            if isinstance(self.cascade_mission_conf, list):
                for i in range(0, len(self.cascade_mission_conf)):
                    element = self.cascade_mission_conf[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cascade_mission_conf[i] = element.to_alipay_dict()
            if hasattr(self.cascade_mission_conf, 'to_alipay_dict'):
                params['cascade_mission_conf'] = self.cascade_mission_conf.to_alipay_dict()
            else:
                params['cascade_mission_conf'] = self.cascade_mission_conf
        if self.identify:
            if hasattr(self.identify, 'to_alipay_dict'):
                params['identify'] = self.identify.to_alipay_dict()
            else:
                params['identify'] = self.identify
        if self.identify_type:
            if hasattr(self.identify_type, 'to_alipay_dict'):
                params['identify_type'] = self.identify_type.to_alipay_dict()
            else:
                params['identify_type'] = self.identify_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiAdvertCommissionCascademissionCreateModel()
        if 'cascade_mission_conf' in d:
            o.cascade_mission_conf = d['cascade_mission_conf']
        if 'identify' in d:
            o.identify = d['identify']
        if 'identify_type' in d:
            o.identify_type = d['identify_type']
        if 'name' in d:
            o.name = d['name']
        return o


