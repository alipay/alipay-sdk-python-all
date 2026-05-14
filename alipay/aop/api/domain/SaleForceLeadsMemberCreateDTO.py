#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaleForceLeadsMemberCreateDTO(object):

    def __init__(self):
        self._leads_id = None
        self._leads_member_id = None
        self._member_role = None
        self._member_work_no = None
        self._work_no_create = None

    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def leads_member_id(self):
        return self._leads_member_id

    @leads_member_id.setter
    def leads_member_id(self, value):
        self._leads_member_id = value
    @property
    def member_role(self):
        return self._member_role

    @member_role.setter
    def member_role(self, value):
        self._member_role = value
    @property
    def member_work_no(self):
        return self._member_work_no

    @member_work_no.setter
    def member_work_no(self, value):
        self._member_work_no = value
    @property
    def work_no_create(self):
        return self._work_no_create

    @work_no_create.setter
    def work_no_create(self, value):
        self._work_no_create = value


    def to_alipay_dict(self):
        params = dict()
        if self.leads_id:
            if hasattr(self.leads_id, 'to_alipay_dict'):
                params['leads_id'] = self.leads_id.to_alipay_dict()
            else:
                params['leads_id'] = self.leads_id
        if self.leads_member_id:
            if hasattr(self.leads_member_id, 'to_alipay_dict'):
                params['leads_member_id'] = self.leads_member_id.to_alipay_dict()
            else:
                params['leads_member_id'] = self.leads_member_id
        if self.member_role:
            if hasattr(self.member_role, 'to_alipay_dict'):
                params['member_role'] = self.member_role.to_alipay_dict()
            else:
                params['member_role'] = self.member_role
        if self.member_work_no:
            if hasattr(self.member_work_no, 'to_alipay_dict'):
                params['member_work_no'] = self.member_work_no.to_alipay_dict()
            else:
                params['member_work_no'] = self.member_work_no
        if self.work_no_create:
            if hasattr(self.work_no_create, 'to_alipay_dict'):
                params['work_no_create'] = self.work_no_create.to_alipay_dict()
            else:
                params['work_no_create'] = self.work_no_create
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaleForceLeadsMemberCreateDTO()
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        if 'leads_member_id' in d:
            o.leads_member_id = d['leads_member_id']
        if 'member_role' in d:
            o.member_role = d['member_role']
        if 'member_work_no' in d:
            o.member_work_no = d['member_work_no']
        if 'work_no_create' in d:
            o.work_no_create = d['work_no_create']
        return o


