#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DepartmentJobCreateVO import DepartmentJobCreateVO


class StaffInfoVO(object):

    def __init__(self):
        self._alipay_account = None
        self._community_ids = None
        self._department_jobs = None
        self._name = None
        self._open_id = None
        self._open_saas = None
        self._phone = None
        self._request_id = None
        self._staff_id = None
        self._staff_no = None
        self._user_id = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def community_ids(self):
        return self._community_ids

    @community_ids.setter
    def community_ids(self, value):
        if isinstance(value, list):
            self._community_ids = list()
            for i in value:
                self._community_ids.append(i)
    @property
    def department_jobs(self):
        return self._department_jobs

    @department_jobs.setter
    def department_jobs(self, value):
        if isinstance(value, list):
            self._department_jobs = list()
            for i in value:
                if isinstance(i, DepartmentJobCreateVO):
                    self._department_jobs.append(i)
                else:
                    self._department_jobs.append(DepartmentJobCreateVO.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def open_saas(self):
        return self._open_saas

    @open_saas.setter
    def open_saas(self, value):
        self._open_saas = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def staff_id(self):
        return self._staff_id

    @staff_id.setter
    def staff_id(self, value):
        self._staff_id = value
    @property
    def staff_no(self):
        return self._staff_no

    @staff_no.setter
    def staff_no(self, value):
        self._staff_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.community_ids:
            if isinstance(self.community_ids, list):
                for i in range(0, len(self.community_ids)):
                    element = self.community_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.community_ids[i] = element.to_alipay_dict()
            if hasattr(self.community_ids, 'to_alipay_dict'):
                params['community_ids'] = self.community_ids.to_alipay_dict()
            else:
                params['community_ids'] = self.community_ids
        if self.department_jobs:
            if isinstance(self.department_jobs, list):
                for i in range(0, len(self.department_jobs)):
                    element = self.department_jobs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.department_jobs[i] = element.to_alipay_dict()
            if hasattr(self.department_jobs, 'to_alipay_dict'):
                params['department_jobs'] = self.department_jobs.to_alipay_dict()
            else:
                params['department_jobs'] = self.department_jobs
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.open_saas:
            if hasattr(self.open_saas, 'to_alipay_dict'):
                params['open_saas'] = self.open_saas.to_alipay_dict()
            else:
                params['open_saas'] = self.open_saas
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.staff_id:
            if hasattr(self.staff_id, 'to_alipay_dict'):
                params['staff_id'] = self.staff_id.to_alipay_dict()
            else:
                params['staff_id'] = self.staff_id
        if self.staff_no:
            if hasattr(self.staff_no, 'to_alipay_dict'):
                params['staff_no'] = self.staff_no.to_alipay_dict()
            else:
                params['staff_no'] = self.staff_no
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
        o = StaffInfoVO()
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'community_ids' in d:
            o.community_ids = d['community_ids']
        if 'department_jobs' in d:
            o.department_jobs = d['department_jobs']
        if 'name' in d:
            o.name = d['name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'open_saas' in d:
            o.open_saas = d['open_saas']
        if 'phone' in d:
            o.phone = d['phone']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'staff_id' in d:
            o.staff_id = d['staff_id']
        if 'staff_no' in d:
            o.staff_no = d['staff_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


