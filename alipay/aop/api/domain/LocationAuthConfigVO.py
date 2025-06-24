#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LocationAuthConfigVO(object):

    def __init__(self):
        self._lbs_switch = None

    @property
    def lbs_switch(self):
        return self._lbs_switch

    @lbs_switch.setter
    def lbs_switch(self, value):
        self._lbs_switch = value


    def to_alipay_dict(self):
        params = dict()
        if self.lbs_switch:
            if hasattr(self.lbs_switch, 'to_alipay_dict'):
                params['lbs_switch'] = self.lbs_switch.to_alipay_dict()
            else:
                params['lbs_switch'] = self.lbs_switch
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LocationAuthConfigVO()
        if 'lbs_switch' in d:
            o.lbs_switch = d['lbs_switch']
        return o


