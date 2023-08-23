#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FenceDto import FenceDto


class Area(object):

    def __init__(self):
        self._fences = None

    @property
    def fences(self):
        return self._fences

    @fences.setter
    def fences(self, value):
        if isinstance(value, list):
            self._fences = list()
            for i in value:
                if isinstance(i, FenceDto):
                    self._fences.append(i)
                else:
                    self._fences.append(FenceDto.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.fences:
            if isinstance(self.fences, list):
                for i in range(0, len(self.fences)):
                    element = self.fences[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fences[i] = element.to_alipay_dict()
            if hasattr(self.fences, 'to_alipay_dict'):
                params['fences'] = self.fences.to_alipay_dict()
            else:
                params['fences'] = self.fences
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Area()
        if 'fences' in d:
            o.fences = d['fences']
        return o


