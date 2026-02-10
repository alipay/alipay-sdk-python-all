#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoboWhistleInfo(object):

    def __init__(self):
        self._whistle_ability = None

    @property
    def whistle_ability(self):
        return self._whistle_ability

    @whistle_ability.setter
    def whistle_ability(self, value):
        self._whistle_ability = value


    def to_alipay_dict(self):
        params = dict()
        if self.whistle_ability:
            if hasattr(self.whistle_ability, 'to_alipay_dict'):
                params['whistle_ability'] = self.whistle_ability.to_alipay_dict()
            else:
                params['whistle_ability'] = self.whistle_ability
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoboWhistleInfo()
        if 'whistle_ability' in d:
            o.whistle_ability = d['whistle_ability']
        return o


