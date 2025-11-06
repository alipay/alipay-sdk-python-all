#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserOrgEntityInfoDTO(object):

    def __init__(self):
        self._company_flag = None
        self._entity_name = None
        self._exit_org_flag = None
        self._exit_org_time = None
        self._join_org_time = None
        self._org_id = None
        self._org_name = None
        self._passport_id = None
        self._role = None
        self._root_id = None

    @property
    def company_flag(self):
        return self._company_flag

    @company_flag.setter
    def company_flag(self, value):
        self._company_flag = value
    @property
    def entity_name(self):
        return self._entity_name

    @entity_name.setter
    def entity_name(self, value):
        self._entity_name = value
    @property
    def exit_org_flag(self):
        return self._exit_org_flag

    @exit_org_flag.setter
    def exit_org_flag(self, value):
        self._exit_org_flag = value
    @property
    def exit_org_time(self):
        return self._exit_org_time

    @exit_org_time.setter
    def exit_org_time(self, value):
        self._exit_org_time = value
    @property
    def join_org_time(self):
        return self._join_org_time

    @join_org_time.setter
    def join_org_time(self, value):
        self._join_org_time = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def root_id(self):
        return self._root_id

    @root_id.setter
    def root_id(self, value):
        self._root_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_flag:
            if hasattr(self.company_flag, 'to_alipay_dict'):
                params['company_flag'] = self.company_flag.to_alipay_dict()
            else:
                params['company_flag'] = self.company_flag
        if self.entity_name:
            if hasattr(self.entity_name, 'to_alipay_dict'):
                params['entity_name'] = self.entity_name.to_alipay_dict()
            else:
                params['entity_name'] = self.entity_name
        if self.exit_org_flag:
            if hasattr(self.exit_org_flag, 'to_alipay_dict'):
                params['exit_org_flag'] = self.exit_org_flag.to_alipay_dict()
            else:
                params['exit_org_flag'] = self.exit_org_flag
        if self.exit_org_time:
            if hasattr(self.exit_org_time, 'to_alipay_dict'):
                params['exit_org_time'] = self.exit_org_time.to_alipay_dict()
            else:
                params['exit_org_time'] = self.exit_org_time
        if self.join_org_time:
            if hasattr(self.join_org_time, 'to_alipay_dict'):
                params['join_org_time'] = self.join_org_time.to_alipay_dict()
            else:
                params['join_org_time'] = self.join_org_time
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.root_id:
            if hasattr(self.root_id, 'to_alipay_dict'):
                params['root_id'] = self.root_id.to_alipay_dict()
            else:
                params['root_id'] = self.root_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserOrgEntityInfoDTO()
        if 'company_flag' in d:
            o.company_flag = d['company_flag']
        if 'entity_name' in d:
            o.entity_name = d['entity_name']
        if 'exit_org_flag' in d:
            o.exit_org_flag = d['exit_org_flag']
        if 'exit_org_time' in d:
            o.exit_org_time = d['exit_org_time']
        if 'join_org_time' in d:
            o.join_org_time = d['join_org_time']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'role' in d:
            o.role = d['role']
        if 'root_id' in d:
            o.root_id = d['root_id']
        return o


