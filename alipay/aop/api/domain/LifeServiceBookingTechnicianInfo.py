#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LifeServiceBookingTechnicianInfo(object):

    def __init__(self):
        self._technician_name = None

    @property
    def technician_name(self):
        return self._technician_name

    @technician_name.setter
    def technician_name(self, value):
        self._technician_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.technician_name:
            if hasattr(self.technician_name, 'to_alipay_dict'):
                params['technician_name'] = self.technician_name.to_alipay_dict()
            else:
                params['technician_name'] = self.technician_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LifeServiceBookingTechnicianInfo()
        if 'technician_name' in d:
            o.technician_name = d['technician_name']
        return o


