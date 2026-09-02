#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalHmActivityRecord(object):

    def __init__(self):
        self._activity_end_date = None
        self._activity_id = None
        self._activity_start_date = None
        self._activity_sub_title = None
        self._activity_title = None
        self._registration_date = None

    @property
    def activity_end_date(self):
        return self._activity_end_date

    @activity_end_date.setter
    def activity_end_date(self, value):
        self._activity_end_date = value
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_start_date(self):
        return self._activity_start_date

    @activity_start_date.setter
    def activity_start_date(self, value):
        self._activity_start_date = value
    @property
    def activity_sub_title(self):
        return self._activity_sub_title

    @activity_sub_title.setter
    def activity_sub_title(self, value):
        self._activity_sub_title = value
    @property
    def activity_title(self):
        return self._activity_title

    @activity_title.setter
    def activity_title(self, value):
        self._activity_title = value
    @property
    def registration_date(self):
        return self._registration_date

    @registration_date.setter
    def registration_date(self, value):
        self._registration_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_end_date:
            if hasattr(self.activity_end_date, 'to_alipay_dict'):
                params['activity_end_date'] = self.activity_end_date.to_alipay_dict()
            else:
                params['activity_end_date'] = self.activity_end_date
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_start_date:
            if hasattr(self.activity_start_date, 'to_alipay_dict'):
                params['activity_start_date'] = self.activity_start_date.to_alipay_dict()
            else:
                params['activity_start_date'] = self.activity_start_date
        if self.activity_sub_title:
            if hasattr(self.activity_sub_title, 'to_alipay_dict'):
                params['activity_sub_title'] = self.activity_sub_title.to_alipay_dict()
            else:
                params['activity_sub_title'] = self.activity_sub_title
        if self.activity_title:
            if hasattr(self.activity_title, 'to_alipay_dict'):
                params['activity_title'] = self.activity_title.to_alipay_dict()
            else:
                params['activity_title'] = self.activity_title
        if self.registration_date:
            if hasattr(self.registration_date, 'to_alipay_dict'):
                params['registration_date'] = self.registration_date.to_alipay_dict()
            else:
                params['registration_date'] = self.registration_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalHmActivityRecord()
        if 'activity_end_date' in d:
            o.activity_end_date = d['activity_end_date']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_start_date' in d:
            o.activity_start_date = d['activity_start_date']
        if 'activity_sub_title' in d:
            o.activity_sub_title = d['activity_sub_title']
        if 'activity_title' in d:
            o.activity_title = d['activity_title']
        if 'registration_date' in d:
            o.registration_date = d['registration_date']
        return o


