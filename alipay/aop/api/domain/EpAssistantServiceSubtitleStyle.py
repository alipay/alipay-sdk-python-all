#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpAssistantServiceSubtitleStyle(object):

    def __init__(self):
        self._color = None
        self._font_weight = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
    @property
    def font_weight(self):
        return self._font_weight

    @font_weight.setter
    def font_weight(self, value):
        self._font_weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.color:
            if hasattr(self.color, 'to_alipay_dict'):
                params['color'] = self.color.to_alipay_dict()
            else:
                params['color'] = self.color
        if self.font_weight:
            if hasattr(self.font_weight, 'to_alipay_dict'):
                params['font_weight'] = self.font_weight.to_alipay_dict()
            else:
                params['font_weight'] = self.font_weight
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpAssistantServiceSubtitleStyle()
        if 'color' in d:
            o.color = d['color']
        if 'font_weight' in d:
            o.font_weight = d['font_weight']
        return o


