#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalServicepackageGrantbyphoneCreateModel(object):

    def __init__(self):
        self._effect_days = None
        self._phone_no = None
        self._project_id = None

    @property
    def effect_days(self):
        return self._effect_days

    @effect_days.setter
    def effect_days(self, value):
        self._effect_days = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.effect_days:
            if hasattr(self.effect_days, 'to_alipay_dict'):
                params['effect_days'] = self.effect_days.to_alipay_dict()
            else:
                params['effect_days'] = self.effect_days
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalServicepackageGrantbyphoneCreateModel()
        if 'effect_days' in d:
            o.effect_days = d['effect_days']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'project_id' in d:
            o.project_id = d['project_id']
        return o


