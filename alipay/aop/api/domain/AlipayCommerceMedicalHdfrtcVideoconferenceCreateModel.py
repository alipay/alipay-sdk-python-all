#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfrtcVideoconferenceCreateModel(object):

    def __init__(self):
        self._patient_id = None
        self._scheduled_end_time = None
        self._scheduled_start_time = None
        self._source_id = None
        self._source_type = None
        self._space_id = None
        self._user_id = None

    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value
    @property
    def scheduled_end_time(self):
        return self._scheduled_end_time

    @scheduled_end_time.setter
    def scheduled_end_time(self, value):
        self._scheduled_end_time = value
    @property
    def scheduled_start_time(self):
        return self._scheduled_start_time

    @scheduled_start_time.setter
    def scheduled_start_time(self, value):
        self._scheduled_start_time = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
    @property
    def space_id(self):
        return self._space_id

    @space_id.setter
    def space_id(self, value):
        self._space_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.patient_id:
            if hasattr(self.patient_id, 'to_alipay_dict'):
                params['patient_id'] = self.patient_id.to_alipay_dict()
            else:
                params['patient_id'] = self.patient_id
        if self.scheduled_end_time:
            if hasattr(self.scheduled_end_time, 'to_alipay_dict'):
                params['scheduled_end_time'] = self.scheduled_end_time.to_alipay_dict()
            else:
                params['scheduled_end_time'] = self.scheduled_end_time
        if self.scheduled_start_time:
            if hasattr(self.scheduled_start_time, 'to_alipay_dict'):
                params['scheduled_start_time'] = self.scheduled_start_time.to_alipay_dict()
            else:
                params['scheduled_start_time'] = self.scheduled_start_time
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        if self.space_id:
            if hasattr(self.space_id, 'to_alipay_dict'):
                params['space_id'] = self.space_id.to_alipay_dict()
            else:
                params['space_id'] = self.space_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfrtcVideoconferenceCreateModel()
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'scheduled_end_time' in d:
            o.scheduled_end_time = d['scheduled_end_time']
        if 'scheduled_start_time' in d:
            o.scheduled_start_time = d['scheduled_start_time']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'space_id' in d:
            o.space_id = d['space_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


