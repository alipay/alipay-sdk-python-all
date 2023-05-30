#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetStandard(object):

    def __init__(self):
        self._pm_std = None

    @property
    def pm_std(self):
        return self._pm_std

    @pm_std.setter
    def pm_std(self, value):
        self._pm_std = value


    def to_alipay_dict(self):
        params = dict()
        if self.pm_std:
            if hasattr(self.pm_std, 'to_alipay_dict'):
                params['pm_std'] = self.pm_std.to_alipay_dict()
            else:
                params['pm_std'] = self.pm_std
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetStandard()
        if 'pm_std' in d:
            o.pm_std = d['pm_std']
        return o


