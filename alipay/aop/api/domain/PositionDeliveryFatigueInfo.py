#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryFatigueInfo import DeliveryFatigueInfo


class PositionDeliveryFatigueInfo(object):

    def __init__(self):
        self._fatigue_model_info = None
        self._position_code = None

    @property
    def fatigue_model_info(self):
        return self._fatigue_model_info

    @fatigue_model_info.setter
    def fatigue_model_info(self, value):
        if isinstance(value, list):
            self._fatigue_model_info = list()
            for i in value:
                if isinstance(i, DeliveryFatigueInfo):
                    self._fatigue_model_info.append(i)
                else:
                    self._fatigue_model_info.append(DeliveryFatigueInfo.from_alipay_dict(i))
    @property
    def position_code(self):
        return self._position_code

    @position_code.setter
    def position_code(self, value):
        self._position_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.fatigue_model_info:
            if isinstance(self.fatigue_model_info, list):
                for i in range(0, len(self.fatigue_model_info)):
                    element = self.fatigue_model_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fatigue_model_info[i] = element.to_alipay_dict()
            if hasattr(self.fatigue_model_info, 'to_alipay_dict'):
                params['fatigue_model_info'] = self.fatigue_model_info.to_alipay_dict()
            else:
                params['fatigue_model_info'] = self.fatigue_model_info
        if self.position_code:
            if hasattr(self.position_code, 'to_alipay_dict'):
                params['position_code'] = self.position_code.to_alipay_dict()
            else:
                params['position_code'] = self.position_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PositionDeliveryFatigueInfo()
        if 'fatigue_model_info' in d:
            o.fatigue_model_info = d['fatigue_model_info']
        if 'position_code' in d:
            o.position_code = d['position_code']
        return o


