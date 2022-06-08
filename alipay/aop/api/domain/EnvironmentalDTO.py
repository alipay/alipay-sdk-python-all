#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnvironmentalDTO(object):

    def __init__(self):
        self._energy_amount = None
        self._environmental = None
        self._failure_code = None
        self._failure_reason = None
        self._status = None

    @property
    def energy_amount(self):
        return self._energy_amount

    @energy_amount.setter
    def energy_amount(self, value):
        self._energy_amount = value
    @property
    def environmental(self):
        return self._environmental

    @environmental.setter
    def environmental(self, value):
        self._environmental = value
    @property
    def failure_code(self):
        return self._failure_code

    @failure_code.setter
    def failure_code(self, value):
        self._failure_code = value
    @property
    def failure_reason(self):
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, value):
        self._failure_reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.energy_amount:
            if hasattr(self.energy_amount, 'to_alipay_dict'):
                params['energy_amount'] = self.energy_amount.to_alipay_dict()
            else:
                params['energy_amount'] = self.energy_amount
        if self.environmental:
            if hasattr(self.environmental, 'to_alipay_dict'):
                params['environmental'] = self.environmental.to_alipay_dict()
            else:
                params['environmental'] = self.environmental
        if self.failure_code:
            if hasattr(self.failure_code, 'to_alipay_dict'):
                params['failure_code'] = self.failure_code.to_alipay_dict()
            else:
                params['failure_code'] = self.failure_code
        if self.failure_reason:
            if hasattr(self.failure_reason, 'to_alipay_dict'):
                params['failure_reason'] = self.failure_reason.to_alipay_dict()
            else:
                params['failure_reason'] = self.failure_reason
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnvironmentalDTO()
        if 'energy_amount' in d:
            o.energy_amount = d['energy_amount']
        if 'environmental' in d:
            o.environmental = d['environmental']
        if 'failure_code' in d:
            o.failure_code = d['failure_code']
        if 'failure_reason' in d:
            o.failure_reason = d['failure_reason']
        if 'status' in d:
            o.status = d['status']
        return o


