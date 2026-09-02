#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHomedoctorDoctorBindModel(object):

    def __init__(self):
        self._agent_id = None
        self._aq_open_id = None
        self._doctor_id = None
        self._group_notice = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def aq_open_id(self):
        return self._aq_open_id

    @aq_open_id.setter
    def aq_open_id(self, value):
        self._aq_open_id = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def group_notice(self):
        return self._group_notice

    @group_notice.setter
    def group_notice(self, value):
        self._group_notice = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.aq_open_id:
            if hasattr(self.aq_open_id, 'to_alipay_dict'):
                params['aq_open_id'] = self.aq_open_id.to_alipay_dict()
            else:
                params['aq_open_id'] = self.aq_open_id
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.group_notice:
            if hasattr(self.group_notice, 'to_alipay_dict'):
                params['group_notice'] = self.group_notice.to_alipay_dict()
            else:
                params['group_notice'] = self.group_notice
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHomedoctorDoctorBindModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'aq_open_id' in d:
            o.aq_open_id = d['aq_open_id']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'group_notice' in d:
            o.group_notice = d['group_notice']
        return o


