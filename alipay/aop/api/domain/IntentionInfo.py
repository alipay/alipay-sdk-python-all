#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IntentionAreaInfo import IntentionAreaInfo
from alipay.aop.api.domain.IntentionBaseInfo import IntentionBaseInfo


class IntentionInfo(object):

    def __init__(self):
        self._area_info = None
        self._base_info = None

    @property
    def area_info(self):
        return self._area_info

    @area_info.setter
    def area_info(self, value):
        if isinstance(value, IntentionAreaInfo):
            self._area_info = value
        else:
            self._area_info = IntentionAreaInfo.from_alipay_dict(value)
    @property
    def base_info(self):
        return self._base_info

    @base_info.setter
    def base_info(self, value):
        if isinstance(value, IntentionBaseInfo):
            self._base_info = value
        else:
            self._base_info = IntentionBaseInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.area_info:
            if hasattr(self.area_info, 'to_alipay_dict'):
                params['area_info'] = self.area_info.to_alipay_dict()
            else:
                params['area_info'] = self.area_info
        if self.base_info:
            if hasattr(self.base_info, 'to_alipay_dict'):
                params['base_info'] = self.base_info.to_alipay_dict()
            else:
                params['base_info'] = self.base_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IntentionInfo()
        if 'area_info' in d:
            o.area_info = d['area_info']
        if 'base_info' in d:
            o.base_info = d['base_info']
        return o


