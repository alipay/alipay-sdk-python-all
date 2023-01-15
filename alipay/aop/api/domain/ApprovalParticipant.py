#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApprovalParticipant(object):

    def __init__(self):
        self._employee_id = None
        self._external_user = None
        self._mobile = None
        self._participant_name = None

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def external_user(self):
        return self._external_user

    @external_user.setter
    def external_user(self, value):
        self._external_user = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def participant_name(self):
        return self._participant_name

    @participant_name.setter
    def participant_name(self, value):
        self._participant_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.external_user:
            if hasattr(self.external_user, 'to_alipay_dict'):
                params['external_user'] = self.external_user.to_alipay_dict()
            else:
                params['external_user'] = self.external_user
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.participant_name:
            if hasattr(self.participant_name, 'to_alipay_dict'):
                params['participant_name'] = self.participant_name.to_alipay_dict()
            else:
                params['participant_name'] = self.participant_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApprovalParticipant()
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'external_user' in d:
            o.external_user = d['external_user']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'participant_name' in d:
            o.participant_name = d['participant_name']
        return o


