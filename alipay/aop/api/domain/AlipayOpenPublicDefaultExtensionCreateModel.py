#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtensionArea import ExtensionArea


class AlipayOpenPublicDefaultExtensionCreateModel(object):

    def __init__(self):
        self._areas = None

    @property
    def areas(self):
        return self._areas

    @areas.setter
    def areas(self, value):
        if isinstance(value, list):
            self._areas = list()
            for i in value:
                if isinstance(i, ExtensionArea):
                    self._areas.append(i)
                else:
                    self._areas.append(ExtensionArea.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.areas:
            if isinstance(self.areas, list):
                for i in range(0, len(self.areas)):
                    element = self.areas[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.areas[i] = element.to_alipay_dict()
            if hasattr(self.areas, 'to_alipay_dict'):
                params['areas'] = self.areas.to_alipay_dict()
            else:
                params['areas'] = self.areas
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicDefaultExtensionCreateModel()
        if 'areas' in d:
            o.areas = d['areas']
        return o


