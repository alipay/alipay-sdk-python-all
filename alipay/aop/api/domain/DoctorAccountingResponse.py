#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DoctorAccountingResponse(object):

    def __init__(self):
        self._doctor_accounting_detail_no = None
        self._event_flow_no = None

    @property
    def doctor_accounting_detail_no(self):
        return self._doctor_accounting_detail_no

    @doctor_accounting_detail_no.setter
    def doctor_accounting_detail_no(self, value):
        self._doctor_accounting_detail_no = value
    @property
    def event_flow_no(self):
        return self._event_flow_no

    @event_flow_no.setter
    def event_flow_no(self, value):
        if isinstance(value, list):
            self._event_flow_no = list()
            for i in value:
                self._event_flow_no.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.doctor_accounting_detail_no:
            if hasattr(self.doctor_accounting_detail_no, 'to_alipay_dict'):
                params['doctor_accounting_detail_no'] = self.doctor_accounting_detail_no.to_alipay_dict()
            else:
                params['doctor_accounting_detail_no'] = self.doctor_accounting_detail_no
        if self.event_flow_no:
            if isinstance(self.event_flow_no, list):
                for i in range(0, len(self.event_flow_no)):
                    element = self.event_flow_no[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.event_flow_no[i] = element.to_alipay_dict()
            if hasattr(self.event_flow_no, 'to_alipay_dict'):
                params['event_flow_no'] = self.event_flow_no.to_alipay_dict()
            else:
                params['event_flow_no'] = self.event_flow_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DoctorAccountingResponse()
        if 'doctor_accounting_detail_no' in d:
            o.doctor_accounting_detail_no = d['doctor_accounting_detail_no']
        if 'event_flow_no' in d:
            o.event_flow_no = d['event_flow_no']
        return o


