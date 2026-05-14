#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SaleForceLeadsMemberDeleteDTO(object):

    def __init__(self):
        self._leads_id = None
        self._leads_member_id = None
        self._work_no_delete = None

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
    def work_no_delete(self):
        return self._work_no_delete

    @work_no_delete.setter
    def work_no_delete(self, value):
        self._work_no_delete = value


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
        if self.work_no_delete:
            if hasattr(self.work_no_delete, 'to_alipay_dict'):
                params['work_no_delete'] = self.work_no_delete.to_alipay_dict()
            else:
                params['work_no_delete'] = self.work_no_delete
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SaleForceLeadsMemberDeleteDTO()
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        if 'leads_member_id' in d:
            o.leads_member_id = d['leads_member_id']
        if 'work_no_delete' in d:
            o.work_no_delete = d['work_no_delete']
        return o


