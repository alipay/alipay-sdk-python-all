#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrganizationContractDTO(object):

    def __init__(self):
        self._contract_id = None
        self._contract_no = None
        self._contract_title = None
        self._effective_time = None
        self._id = None
        self._ma_end_time = None
        self._ma_start_time = None
        self._org_id = None

    @property
    def contract_id(self):
        return self._contract_id

    @contract_id.setter
    def contract_id(self, value):
        self._contract_id = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def contract_title(self):
        return self._contract_title

    @contract_title.setter
    def contract_title(self, value):
        self._contract_title = value
    @property
    def effective_time(self):
        return self._effective_time

    @effective_time.setter
    def effective_time(self, value):
        self._effective_time = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def ma_end_time(self):
        return self._ma_end_time

    @ma_end_time.setter
    def ma_end_time(self, value):
        self._ma_end_time = value
    @property
    def ma_start_time(self):
        return self._ma_start_time

    @ma_start_time.setter
    def ma_start_time(self, value):
        self._ma_start_time = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_id:
            if hasattr(self.contract_id, 'to_alipay_dict'):
                params['contract_id'] = self.contract_id.to_alipay_dict()
            else:
                params['contract_id'] = self.contract_id
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.contract_title:
            if hasattr(self.contract_title, 'to_alipay_dict'):
                params['contract_title'] = self.contract_title.to_alipay_dict()
            else:
                params['contract_title'] = self.contract_title
        if self.effective_time:
            if hasattr(self.effective_time, 'to_alipay_dict'):
                params['effective_time'] = self.effective_time.to_alipay_dict()
            else:
                params['effective_time'] = self.effective_time
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.ma_end_time:
            if hasattr(self.ma_end_time, 'to_alipay_dict'):
                params['ma_end_time'] = self.ma_end_time.to_alipay_dict()
            else:
                params['ma_end_time'] = self.ma_end_time
        if self.ma_start_time:
            if hasattr(self.ma_start_time, 'to_alipay_dict'):
                params['ma_start_time'] = self.ma_start_time.to_alipay_dict()
            else:
                params['ma_start_time'] = self.ma_start_time
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrganizationContractDTO()
        if 'contract_id' in d:
            o.contract_id = d['contract_id']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'contract_title' in d:
            o.contract_title = d['contract_title']
        if 'effective_time' in d:
            o.effective_time = d['effective_time']
        if 'id' in d:
            o.id = d['id']
        if 'ma_end_time' in d:
            o.ma_end_time = d['ma_end_time']
        if 'ma_start_time' in d:
            o.ma_start_time = d['ma_start_time']
        if 'org_id' in d:
            o.org_id = d['org_id']
        return o


