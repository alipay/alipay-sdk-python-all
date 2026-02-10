#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoboWelcomeLightInfo(object):

    def __init__(self):
        self._light_ability = None
        self._light_color = None

    @property
    def light_ability(self):
        return self._light_ability

    @light_ability.setter
    def light_ability(self, value):
        self._light_ability = value
    @property
    def light_color(self):
        return self._light_color

    @light_color.setter
    def light_color(self, value):
        self._light_color = value


    def to_alipay_dict(self):
        params = dict()
        if self.light_ability:
            if hasattr(self.light_ability, 'to_alipay_dict'):
                params['light_ability'] = self.light_ability.to_alipay_dict()
            else:
                params['light_ability'] = self.light_ability
        if self.light_color:
            if hasattr(self.light_color, 'to_alipay_dict'):
                params['light_color'] = self.light_color.to_alipay_dict()
            else:
                params['light_color'] = self.light_color
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoboWelcomeLightInfo()
        if 'light_ability' in d:
            o.light_ability = d['light_ability']
        if 'light_color' in d:
            o.light_color = d['light_color']
        return o


