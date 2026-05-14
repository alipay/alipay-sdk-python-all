#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaleForceLeadsMemberModifyDTO(object):

    def __init__(self):
        self._leads_id = None
        self._leads_member_id = None
        self._new_member_role = None
        self._new_member_work_no = None
        self._work_no_update = None

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
    def new_member_role(self):
        return self._new_member_role

    @new_member_role.setter
    def new_member_role(self, value):
        self._new_member_role = value
    @property
    def new_member_work_no(self):
        return self._new_member_work_no

    @new_member_work_no.setter
    def new_member_work_no(self, value):
        self._new_member_work_no = value
    @property
    def work_no_update(self):
        return self._work_no_update

    @work_no_update.setter
    def work_no_update(self, value):
        self._work_no_update = value


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
        if self.new_member_role:
            if hasattr(self.new_member_role, 'to_alipay_dict'):
                params['new_member_role'] = self.new_member_role.to_alipay_dict()
            else:
                params['new_member_role'] = self.new_member_role
        if self.new_member_work_no:
            if hasattr(self.new_member_work_no, 'to_alipay_dict'):
                params['new_member_work_no'] = self.new_member_work_no.to_alipay_dict()
            else:
                params['new_member_work_no'] = self.new_member_work_no
        if self.work_no_update:
            if hasattr(self.work_no_update, 'to_alipay_dict'):
                params['work_no_update'] = self.work_no_update.to_alipay_dict()
            else:
                params['work_no_update'] = self.work_no_update
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaleForceLeadsMemberModifyDTO()
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        if 'leads_member_id' in d:
            o.leads_member_id = d['leads_member_id']
        if 'new_member_role' in d:
            o.new_member_role = d['new_member_role']
        if 'new_member_work_no' in d:
            o.new_member_work_no = d['new_member_work_no']
        if 'work_no_update' in d:
            o.work_no_update = d['work_no_update']
        return o


