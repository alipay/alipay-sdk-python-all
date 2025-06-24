#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderUserinfoExpoCreateModel(object):

    def __init__(self):
        self._company_name = None
        self._meeting_role = None
        self._phone = None
        self._remark = None
        self._time_uuid = None

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def meeting_role(self):
        return self._meeting_role

    @meeting_role.setter
    def meeting_role(self, value):
        self._meeting_role = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def time_uuid(self):
        return self._time_uuid

    @time_uuid.setter
    def time_uuid(self, value):
        self._time_uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.meeting_role:
            if hasattr(self.meeting_role, 'to_alipay_dict'):
                params['meeting_role'] = self.meeting_role.to_alipay_dict()
            else:
                params['meeting_role'] = self.meeting_role
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.time_uuid:
            if hasattr(self.time_uuid, 'to_alipay_dict'):
                params['time_uuid'] = self.time_uuid.to_alipay_dict()
            else:
                params['time_uuid'] = self.time_uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderUserinfoExpoCreateModel()
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'meeting_role' in d:
            o.meeting_role = d['meeting_role']
        if 'phone' in d:
            o.phone = d['phone']
        if 'remark' in d:
            o.remark = d['remark']
        if 'time_uuid' in d:
            o.time_uuid = d['time_uuid']
        return o


