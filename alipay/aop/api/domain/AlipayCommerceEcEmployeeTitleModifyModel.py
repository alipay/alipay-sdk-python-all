#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcEmployeeTitleModifyModel(object):

    def __init__(self):
        self._account_id = None
        self._create_by = None
        self._employee_id = None
        self._enterprise_id = None
        self._modify_by = None
        self._new_title_id = None
        self._old_title_id = None
        self._open_id = None
        self._title_tag = None
        self._user_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def create_by(self):
        return self._create_by

    @create_by.setter
    def create_by(self, value):
        self._create_by = value
    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def modify_by(self):
        return self._modify_by

    @modify_by.setter
    def modify_by(self, value):
        self._modify_by = value
    @property
    def new_title_id(self):
        return self._new_title_id

    @new_title_id.setter
    def new_title_id(self, value):
        self._new_title_id = value
    @property
    def old_title_id(self):
        return self._old_title_id

    @old_title_id.setter
    def old_title_id(self, value):
        self._old_title_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def title_tag(self):
        return self._title_tag

    @title_tag.setter
    def title_tag(self, value):
        self._title_tag = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.create_by:
            if hasattr(self.create_by, 'to_alipay_dict'):
                params['create_by'] = self.create_by.to_alipay_dict()
            else:
                params['create_by'] = self.create_by
        if self.employee_id:
            if hasattr(self.employee_id, 'to_alipay_dict'):
                params['employee_id'] = self.employee_id.to_alipay_dict()
            else:
                params['employee_id'] = self.employee_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.modify_by:
            if hasattr(self.modify_by, 'to_alipay_dict'):
                params['modify_by'] = self.modify_by.to_alipay_dict()
            else:
                params['modify_by'] = self.modify_by
        if self.new_title_id:
            if hasattr(self.new_title_id, 'to_alipay_dict'):
                params['new_title_id'] = self.new_title_id.to_alipay_dict()
            else:
                params['new_title_id'] = self.new_title_id
        if self.old_title_id:
            if hasattr(self.old_title_id, 'to_alipay_dict'):
                params['old_title_id'] = self.old_title_id.to_alipay_dict()
            else:
                params['old_title_id'] = self.old_title_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.title_tag:
            if hasattr(self.title_tag, 'to_alipay_dict'):
                params['title_tag'] = self.title_tag.to_alipay_dict()
            else:
                params['title_tag'] = self.title_tag
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
        o = AlipayCommerceEcEmployeeTitleModifyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'create_by' in d:
            o.create_by = d['create_by']
        if 'employee_id' in d:
            o.employee_id = d['employee_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'modify_by' in d:
            o.modify_by = d['modify_by']
        if 'new_title_id' in d:
            o.new_title_id = d['new_title_id']
        if 'old_title_id' in d:
            o.old_title_id = d['old_title_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'title_tag' in d:
            o.title_tag = d['title_tag']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


