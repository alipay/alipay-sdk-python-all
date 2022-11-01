#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduPlanInstanceInfo(object):

    def __init__(self):
        self._plan_instance_no = None
        self._plan_status = None
        self._serial = None

    @property
    def plan_instance_no(self):
        return self._plan_instance_no

    @plan_instance_no.setter
    def plan_instance_no(self, value):
        self._plan_instance_no = value
    @property
    def plan_status(self):
        return self._plan_status

    @plan_status.setter
    def plan_status(self, value):
        self._plan_status = value
    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, value):
        self._serial = value


    def to_alipay_dict(self):
        params = dict()
        if self.plan_instance_no:
            if hasattr(self.plan_instance_no, 'to_alipay_dict'):
                params['plan_instance_no'] = self.plan_instance_no.to_alipay_dict()
            else:
                params['plan_instance_no'] = self.plan_instance_no
        if self.plan_status:
            if hasattr(self.plan_status, 'to_alipay_dict'):
                params['plan_status'] = self.plan_status.to_alipay_dict()
            else:
                params['plan_status'] = self.plan_status
        if self.serial:
            if hasattr(self.serial, 'to_alipay_dict'):
                params['serial'] = self.serial.to_alipay_dict()
            else:
                params['serial'] = self.serial
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduPlanInstanceInfo()
        if 'plan_instance_no' in d:
            o.plan_instance_no = d['plan_instance_no']
        if 'plan_status' in d:
            o.plan_status = d['plan_status']
        if 'serial' in d:
            o.serial = d['serial']
        return o


