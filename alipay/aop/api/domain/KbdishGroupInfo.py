#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishGroupDetailInfo import KbdishGroupDetailInfo


class KbdishGroupInfo(object):

    def __init__(self):
        self._create_user = None
        self._detail_list = None
        self._group_id = None
        self._group_name = None
        self._group_rule = None
        self._group_version = None
        self._merchant_id = None
        self._min_count_limit = None
        self._status = None
        self._unit_count_limit = None
        self._update_user = None

    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def detail_list(self):
        return self._detail_list

    @detail_list.setter
    def detail_list(self, value):
        if isinstance(value, list):
            self._detail_list = list()
            for i in value:
                if isinstance(i, KbdishGroupDetailInfo):
                    self._detail_list.append(i)
                else:
                    self._detail_list.append(KbdishGroupDetailInfo.from_alipay_dict(i))
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def group_rule(self):
        return self._group_rule

    @group_rule.setter
    def group_rule(self, value):
        self._group_rule = value
    @property
    def group_version(self):
        return self._group_version

    @group_version.setter
    def group_version(self, value):
        self._group_version = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def min_count_limit(self):
        return self._min_count_limit

    @min_count_limit.setter
    def min_count_limit(self, value):
        self._min_count_limit = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def unit_count_limit(self):
        return self._unit_count_limit

    @unit_count_limit.setter
    def unit_count_limit(self, value):
        self._unit_count_limit = value
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.detail_list:
            if isinstance(self.detail_list, list):
                for i in range(0, len(self.detail_list)):
                    element = self.detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detail_list[i] = element.to_alipay_dict()
            if hasattr(self.detail_list, 'to_alipay_dict'):
                params['detail_list'] = self.detail_list.to_alipay_dict()
            else:
                params['detail_list'] = self.detail_list
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.group_rule:
            if hasattr(self.group_rule, 'to_alipay_dict'):
                params['group_rule'] = self.group_rule.to_alipay_dict()
            else:
                params['group_rule'] = self.group_rule
        if self.group_version:
            if hasattr(self.group_version, 'to_alipay_dict'):
                params['group_version'] = self.group_version.to_alipay_dict()
            else:
                params['group_version'] = self.group_version
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.min_count_limit:
            if hasattr(self.min_count_limit, 'to_alipay_dict'):
                params['min_count_limit'] = self.min_count_limit.to_alipay_dict()
            else:
                params['min_count_limit'] = self.min_count_limit
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.unit_count_limit:
            if hasattr(self.unit_count_limit, 'to_alipay_dict'):
                params['unit_count_limit'] = self.unit_count_limit.to_alipay_dict()
            else:
                params['unit_count_limit'] = self.unit_count_limit
        if self.update_user:
            if hasattr(self.update_user, 'to_alipay_dict'):
                params['update_user'] = self.update_user.to_alipay_dict()
            else:
                params['update_user'] = self.update_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishGroupInfo()
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'detail_list' in d:
            o.detail_list = d['detail_list']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'group_rule' in d:
            o.group_rule = d['group_rule']
        if 'group_version' in d:
            o.group_version = d['group_version']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'min_count_limit' in d:
            o.min_count_limit = d['min_count_limit']
        if 'status' in d:
            o.status = d['status']
        if 'unit_count_limit' in d:
            o.unit_count_limit = d['unit_count_limit']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o


