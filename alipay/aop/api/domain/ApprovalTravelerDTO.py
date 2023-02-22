#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApprovalTravelerDTO(object):

    def __init__(self):
        self._employee_id = None
        self._external_user_mobile = None
        self._external_user_name = None

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def external_user_mobile(self):
        return self._external_user_mobile

    @external_user_mobile.setter
    def external_user_mobile(self, value):
        self._external_user_mobile = value
    @property
    def external_user_name(self):
        return self._external_user_name

    @external_user_name.setter
    def external_user_name(self, value):
        self._external_user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.external_user_mobile:
            if hasattr(self.external_user_mobile, 'to_alipay_dict'):
                params['external_user_mobile'] = self.external_user_mobile.to_alipay_dict()
            else:
                params['external_user_mobile'] = self.external_user_mobile
        if self.external_user_name:
            if hasattr(self.external_user_name, 'to_alipay_dict'):
                params['external_user_name'] = self.external_user_name.to_alipay_dict()
            else:
                params['external_user_name'] = self.external_user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApprovalTravelerDTO()
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'external_user_mobile' in d:
            o.external_user_mobile = d['external_user_mobile']
        if 'external_user_name' in d:
            o.external_user_name = d['external_user_name']
        return o


