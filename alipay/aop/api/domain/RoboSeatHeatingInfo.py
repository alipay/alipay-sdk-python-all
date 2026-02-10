#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RoboCurrentLevel import RoboCurrentLevel


class RoboSeatHeatingInfo(object):

    def __init__(self):
        self._current_level = None
        self._heating_ability = None

    @property
    def current_level(self):
        return self._current_level

    @current_level.setter
    def current_level(self, value):
        if isinstance(value, RoboCurrentLevel):
            self._current_level = value
        else:
            self._current_level = RoboCurrentLevel.from_alipay_dict(value)
    @property
    def heating_ability(self):
        return self._heating_ability

    @heating_ability.setter
    def heating_ability(self, value):
        self._heating_ability = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_level:
            if hasattr(self.current_level, 'to_alipay_dict'):
                params['current_level'] = self.current_level.to_alipay_dict()
            else:
                params['current_level'] = self.current_level
        if self.heating_ability:
            if hasattr(self.heating_ability, 'to_alipay_dict'):
                params['heating_ability'] = self.heating_ability.to_alipay_dict()
            else:
                params['heating_ability'] = self.heating_ability
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoboSeatHeatingInfo()
        if 'current_level' in d:
            o.current_level = d['current_level']
        if 'heating_ability' in d:
            o.heating_ability = d['heating_ability']
        return o


