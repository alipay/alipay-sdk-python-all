#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceTpaeventSyncModel(object):

    def __init__(self):
        self._code_value = None
        self._event_action = None
        self._hospital_code = None
        self._hospital_name = None
        self._tpa_id = None
        self._visit_date = None

    @property
    def code_value(self):
        return self._code_value

    @code_value.setter
    def code_value(self, value):
        self._code_value = value
    @property
    def event_action(self):
        return self._event_action

    @event_action.setter
    def event_action(self, value):
        self._event_action = value
    @property
    def hospital_code(self):
        return self._hospital_code

    @hospital_code.setter
    def hospital_code(self, value):
        self._hospital_code = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def tpa_id(self):
        return self._tpa_id

    @tpa_id.setter
    def tpa_id(self, value):
        self._tpa_id = value
    @property
    def visit_date(self):
        return self._visit_date

    @visit_date.setter
    def visit_date(self, value):
        self._visit_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_value:
            if hasattr(self.code_value, 'to_alipay_dict'):
                params['code_value'] = self.code_value.to_alipay_dict()
            else:
                params['code_value'] = self.code_value
        if self.event_action:
            if hasattr(self.event_action, 'to_alipay_dict'):
                params['event_action'] = self.event_action.to_alipay_dict()
            else:
                params['event_action'] = self.event_action
        if self.hospital_code:
            if hasattr(self.hospital_code, 'to_alipay_dict'):
                params['hospital_code'] = self.hospital_code.to_alipay_dict()
            else:
                params['hospital_code'] = self.hospital_code
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.tpa_id:
            if hasattr(self.tpa_id, 'to_alipay_dict'):
                params['tpa_id'] = self.tpa_id.to_alipay_dict()
            else:
                params['tpa_id'] = self.tpa_id
        if self.visit_date:
            if hasattr(self.visit_date, 'to_alipay_dict'):
                params['visit_date'] = self.visit_date.to_alipay_dict()
            else:
                params['visit_date'] = self.visit_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceTpaeventSyncModel()
        if 'code_value' in d:
            o.code_value = d['code_value']
        if 'event_action' in d:
            o.event_action = d['event_action']
        if 'hospital_code' in d:
            o.hospital_code = d['hospital_code']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'tpa_id' in d:
            o.tpa_id = d['tpa_id']
        if 'visit_date' in d:
            o.visit_date = d['visit_date']
        return o


