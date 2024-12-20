#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalMedregisterSourcesQueryModel(object):

    def __init__(self):
        self._am_pm = None
        self._hospital_id = None
        self._open_id = None
        self._org_id = None
        self._out_user_id = None
        self._out_user_type = None
        self._schedule_id = None
        self._session_id = None
        self._treat_date = None

    @property
    def am_pm(self):
        return self._am_pm

    @am_pm.setter
    def am_pm(self, value):
        self._am_pm = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def out_user_type(self):
        return self._out_user_type

    @out_user_type.setter
    def out_user_type(self, value):
        self._out_user_type = value
    @property
    def schedule_id(self):
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, value):
        self._schedule_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def treat_date(self):
        return self._treat_date

    @treat_date.setter
    def treat_date(self, value):
        self._treat_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.am_pm:
            if hasattr(self.am_pm, 'to_alipay_dict'):
                params['am_pm'] = self.am_pm.to_alipay_dict()
            else:
                params['am_pm'] = self.am_pm
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.out_user_type:
            if hasattr(self.out_user_type, 'to_alipay_dict'):
                params['out_user_type'] = self.out_user_type.to_alipay_dict()
            else:
                params['out_user_type'] = self.out_user_type
        if self.schedule_id:
            if hasattr(self.schedule_id, 'to_alipay_dict'):
                params['schedule_id'] = self.schedule_id.to_alipay_dict()
            else:
                params['schedule_id'] = self.schedule_id
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.treat_date:
            if hasattr(self.treat_date, 'to_alipay_dict'):
                params['treat_date'] = self.treat_date.to_alipay_dict()
            else:
                params['treat_date'] = self.treat_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedregisterSourcesQueryModel()
        if 'am_pm' in d:
            o.am_pm = d['am_pm']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'out_user_type' in d:
            o.out_user_type = d['out_user_type']
        if 'schedule_id' in d:
            o.schedule_id = d['schedule_id']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'treat_date' in d:
            o.treat_date = d['treat_date']
        return o


