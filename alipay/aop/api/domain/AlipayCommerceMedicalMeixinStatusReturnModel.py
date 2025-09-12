#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicineInfo import MedicineInfo


class AlipayCommerceMedicalMeixinStatusReturnModel(object):

    def __init__(self):
        self._case_no = None
        self._company_type = None
        self._event_type = None
        self._medicine_list = None
        self._open_id = None
        self._policy_no = None
        self._status = None
        self._user_id = None

    @property
    def case_no(self):
        return self._case_no

    @case_no.setter
    def case_no(self, value):
        self._case_no = value
    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def medicine_list(self):
        return self._medicine_list

    @medicine_list.setter
    def medicine_list(self, value):
        if isinstance(value, list):
            self._medicine_list = list()
            for i in value:
                if isinstance(i, MedicineInfo):
                    self._medicine_list.append(i)
                else:
                    self._medicine_list.append(MedicineInfo.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.case_no:
            if hasattr(self.case_no, 'to_alipay_dict'):
                params['case_no'] = self.case_no.to_alipay_dict()
            else:
                params['case_no'] = self.case_no
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.medicine_list:
            if isinstance(self.medicine_list, list):
                for i in range(0, len(self.medicine_list)):
                    element = self.medicine_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.medicine_list[i] = element.to_alipay_dict()
            if hasattr(self.medicine_list, 'to_alipay_dict'):
                params['medicine_list'] = self.medicine_list.to_alipay_dict()
            else:
                params['medicine_list'] = self.medicine_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AlipayCommerceMedicalMeixinStatusReturnModel()
        if 'case_no' in d:
            o.case_no = d['case_no']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'medicine_list' in d:
            o.medicine_list = d['medicine_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


