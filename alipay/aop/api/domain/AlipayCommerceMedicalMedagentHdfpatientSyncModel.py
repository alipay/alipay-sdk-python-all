#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMedagentHdfpatientSyncModel(object):

    def __init__(self):
        self._aq_u_id = None
        self._birth_day = None
        self._name = None
        self._patient_id = None
        self._relation = None
        self._sex = None

    @property
    def aq_u_id(self):
        return self._aq_u_id

    @aq_u_id.setter
    def aq_u_id(self, value):
        self._aq_u_id = value
    @property
    def birth_day(self):
        return self._birth_day

    @birth_day.setter
    def birth_day(self, value):
        self._birth_day = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value
    @property
    def relation(self):
        return self._relation

    @relation.setter
    def relation(self, value):
        self._relation = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value


    def to_alipay_dict(self):
        params = dict()
        if self.aq_u_id:
            if hasattr(self.aq_u_id, 'to_alipay_dict'):
                params['aq_u_id'] = self.aq_u_id.to_alipay_dict()
            else:
                params['aq_u_id'] = self.aq_u_id
        if self.birth_day:
            if hasattr(self.birth_day, 'to_alipay_dict'):
                params['birth_day'] = self.birth_day.to_alipay_dict()
            else:
                params['birth_day'] = self.birth_day
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.patient_id:
            if hasattr(self.patient_id, 'to_alipay_dict'):
                params['patient_id'] = self.patient_id.to_alipay_dict()
            else:
                params['patient_id'] = self.patient_id
        if self.relation:
            if hasattr(self.relation, 'to_alipay_dict'):
                params['relation'] = self.relation.to_alipay_dict()
            else:
                params['relation'] = self.relation
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedagentHdfpatientSyncModel()
        if 'aq_u_id' in d:
            o.aq_u_id = d['aq_u_id']
        if 'birth_day' in d:
            o.birth_day = d['birth_day']
        if 'name' in d:
            o.name = d['name']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'relation' in d:
            o.relation = d['relation']
        if 'sex' in d:
            o.sex = d['sex']
        return o


