#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WaybillStep import WaybillStep


class LogisticsWaybill(object):

    def __init__(self):
        self._logistics_code = None
        self._status = None
        self._steps = None
        self._waybill_no = None

    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, value):
        if isinstance(value, list):
            self._steps = list()
            for i in value:
                if isinstance(i, WaybillStep):
                    self._steps.append(i)
                else:
                    self._steps.append(WaybillStep.from_alipay_dict(i))
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.steps:
            if isinstance(self.steps, list):
                for i in range(0, len(self.steps)):
                    element = self.steps[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.steps[i] = element.to_alipay_dict()
            if hasattr(self.steps, 'to_alipay_dict'):
                params['steps'] = self.steps.to_alipay_dict()
            else:
                params['steps'] = self.steps
        if self.waybill_no:
            if hasattr(self.waybill_no, 'to_alipay_dict'):
                params['waybill_no'] = self.waybill_no.to_alipay_dict()
            else:
                params['waybill_no'] = self.waybill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsWaybill()
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'status' in d:
            o.status = d['status']
        if 'steps' in d:
            o.steps = d['steps']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o


