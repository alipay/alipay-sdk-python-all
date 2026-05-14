#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PBCHitDetail(object):

    def __init__(self):
        self._match_param = None
        self._query_param = None
        self._record_aka = None
        self._record_birth = None
        self._record_gender = None
        self._record_id = None
        self._record_name = None
        self._record_nation = None
        self._record_type = None
        self._reference_id = None
        self._scan_event_id = None

    @property
    def match_param(self):
        return self._match_param

    @match_param.setter
    def match_param(self, value):
        self._match_param = value
    @property
    def query_param(self):
        return self._query_param

    @query_param.setter
    def query_param(self, value):
        self._query_param = value
    @property
    def record_aka(self):
        return self._record_aka

    @record_aka.setter
    def record_aka(self, value):
        self._record_aka = value
    @property
    def record_birth(self):
        return self._record_birth

    @record_birth.setter
    def record_birth(self, value):
        self._record_birth = value
    @property
    def record_gender(self):
        return self._record_gender

    @record_gender.setter
    def record_gender(self, value):
        self._record_gender = value
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def record_name(self):
        return self._record_name

    @record_name.setter
    def record_name(self, value):
        self._record_name = value
    @property
    def record_nation(self):
        return self._record_nation

    @record_nation.setter
    def record_nation(self, value):
        self._record_nation = value
    @property
    def record_type(self):
        return self._record_type

    @record_type.setter
    def record_type(self, value):
        self._record_type = value
    @property
    def reference_id(self):
        return self._reference_id

    @reference_id.setter
    def reference_id(self, value):
        self._reference_id = value
    @property
    def scan_event_id(self):
        return self._scan_event_id

    @scan_event_id.setter
    def scan_event_id(self, value):
        self._scan_event_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.match_param:
            if hasattr(self.match_param, 'to_alipay_dict'):
                params['match_param'] = self.match_param.to_alipay_dict()
            else:
                params['match_param'] = self.match_param
        if self.query_param:
            if hasattr(self.query_param, 'to_alipay_dict'):
                params['query_param'] = self.query_param.to_alipay_dict()
            else:
                params['query_param'] = self.query_param
        if self.record_aka:
            if hasattr(self.record_aka, 'to_alipay_dict'):
                params['record_aka'] = self.record_aka.to_alipay_dict()
            else:
                params['record_aka'] = self.record_aka
        if self.record_birth:
            if hasattr(self.record_birth, 'to_alipay_dict'):
                params['record_birth'] = self.record_birth.to_alipay_dict()
            else:
                params['record_birth'] = self.record_birth
        if self.record_gender:
            if hasattr(self.record_gender, 'to_alipay_dict'):
                params['record_gender'] = self.record_gender.to_alipay_dict()
            else:
                params['record_gender'] = self.record_gender
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.record_name:
            if hasattr(self.record_name, 'to_alipay_dict'):
                params['record_name'] = self.record_name.to_alipay_dict()
            else:
                params['record_name'] = self.record_name
        if self.record_nation:
            if hasattr(self.record_nation, 'to_alipay_dict'):
                params['record_nation'] = self.record_nation.to_alipay_dict()
            else:
                params['record_nation'] = self.record_nation
        if self.record_type:
            if hasattr(self.record_type, 'to_alipay_dict'):
                params['record_type'] = self.record_type.to_alipay_dict()
            else:
                params['record_type'] = self.record_type
        if self.reference_id:
            if hasattr(self.reference_id, 'to_alipay_dict'):
                params['reference_id'] = self.reference_id.to_alipay_dict()
            else:
                params['reference_id'] = self.reference_id
        if self.scan_event_id:
            if hasattr(self.scan_event_id, 'to_alipay_dict'):
                params['scan_event_id'] = self.scan_event_id.to_alipay_dict()
            else:
                params['scan_event_id'] = self.scan_event_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PBCHitDetail()
        if 'match_param' in d:
            o.match_param = d['match_param']
        if 'query_param' in d:
            o.query_param = d['query_param']
        if 'record_aka' in d:
            o.record_aka = d['record_aka']
        if 'record_birth' in d:
            o.record_birth = d['record_birth']
        if 'record_gender' in d:
            o.record_gender = d['record_gender']
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'record_name' in d:
            o.record_name = d['record_name']
        if 'record_nation' in d:
            o.record_nation = d['record_nation']
        if 'record_type' in d:
            o.record_type = d['record_type']
        if 'reference_id' in d:
            o.reference_id = d['reference_id']
        if 'scan_event_id' in d:
            o.scan_event_id = d['scan_event_id']
        return o


