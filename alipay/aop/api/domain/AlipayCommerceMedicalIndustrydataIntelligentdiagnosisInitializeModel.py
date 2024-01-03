#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalIndustrydataIntelligentdiagnosisInitializeModel(object):

    def __init__(self):
        self._age = None
        self._gender = None
        self._open_id = None
        self._outer_user_no = None
        self._outer_user_type = None
        self._refresh = None
        self._source_type = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def outer_user_no(self):
        return self._outer_user_no

    @outer_user_no.setter
    def outer_user_no(self, value):
        self._outer_user_no = value
    @property
    def outer_user_type(self):
        return self._outer_user_type

    @outer_user_type.setter
    def outer_user_type(self, value):
        self._outer_user_type = value
    @property
    def refresh(self):
        return self._refresh

    @refresh.setter
    def refresh(self, value):
        self._refresh = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.outer_user_no:
            if hasattr(self.outer_user_no, 'to_alipay_dict'):
                params['outer_user_no'] = self.outer_user_no.to_alipay_dict()
            else:
                params['outer_user_no'] = self.outer_user_no
        if self.outer_user_type:
            if hasattr(self.outer_user_type, 'to_alipay_dict'):
                params['outer_user_type'] = self.outer_user_type.to_alipay_dict()
            else:
                params['outer_user_type'] = self.outer_user_type
        if self.refresh:
            if hasattr(self.refresh, 'to_alipay_dict'):
                params['refresh'] = self.refresh.to_alipay_dict()
            else:
                params['refresh'] = self.refresh
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataIntelligentdiagnosisInitializeModel()
        if 'age' in d:
            o.age = d['age']
        if 'gender' in d:
            o.gender = d['gender']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'outer_user_no' in d:
            o.outer_user_no = d['outer_user_no']
        if 'outer_user_type' in d:
            o.outer_user_type = d['outer_user_type']
        if 'refresh' in d:
            o.refresh = d['refresh']
        if 'source_type' in d:
            o.source_type = d['source_type']
        return o


