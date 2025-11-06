#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecommendDoctorScmDetail(object):

    def __init__(self):
        self._biz_scm = None
        self._doctor_id = None
        self._doctor_inner_id = None
        self._med_ora_scm = None

    @property
    def biz_scm(self):
        return self._biz_scm

    @biz_scm.setter
    def biz_scm(self, value):
        self._biz_scm = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_inner_id(self):
        return self._doctor_inner_id

    @doctor_inner_id.setter
    def doctor_inner_id(self, value):
        self._doctor_inner_id = value
    @property
    def med_ora_scm(self):
        return self._med_ora_scm

    @med_ora_scm.setter
    def med_ora_scm(self, value):
        self._med_ora_scm = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scm:
            if hasattr(self.biz_scm, 'to_alipay_dict'):
                params['biz_scm'] = self.biz_scm.to_alipay_dict()
            else:
                params['biz_scm'] = self.biz_scm
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_inner_id:
            if hasattr(self.doctor_inner_id, 'to_alipay_dict'):
                params['doctor_inner_id'] = self.doctor_inner_id.to_alipay_dict()
            else:
                params['doctor_inner_id'] = self.doctor_inner_id
        if self.med_ora_scm:
            if hasattr(self.med_ora_scm, 'to_alipay_dict'):
                params['med_ora_scm'] = self.med_ora_scm.to_alipay_dict()
            else:
                params['med_ora_scm'] = self.med_ora_scm
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecommendDoctorScmDetail()
        if 'biz_scm' in d:
            o.biz_scm = d['biz_scm']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_inner_id' in d:
            o.doctor_inner_id = d['doctor_inner_id']
        if 'med_ora_scm' in d:
            o.med_ora_scm = d['med_ora_scm']
        return o


