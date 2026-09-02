#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarfinLendApplyStatusNotifyOther(object):

    def __init__(self):
        self._needs_gps_installation = None

    @property
    def needs_gps_installation(self):
        return self._needs_gps_installation

    @needs_gps_installation.setter
    def needs_gps_installation(self, value):
        self._needs_gps_installation = value


    def to_alipay_dict(self):
        params = dict()
        if self.needs_gps_installation:
            if hasattr(self.needs_gps_installation, 'to_alipay_dict'):
                params['needs_gps_installation'] = self.needs_gps_installation.to_alipay_dict()
            else:
                params['needs_gps_installation'] = self.needs_gps_installation
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinLendApplyStatusNotifyOther()
        if 'needs_gps_installation' in d:
            o.needs_gps_installation = d['needs_gps_installation']
        return o


