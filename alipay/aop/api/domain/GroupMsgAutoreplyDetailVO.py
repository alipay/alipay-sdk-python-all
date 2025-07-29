#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupMsgAutoreplyRuleVO import GroupMsgAutoreplyRuleVO


class GroupMsgAutoreplyDetailVO(object):

    def __init__(self):
        self._autoreply_id = None
        self._global_valid = None
        self._gmt_create = None
        self._gmt_modified = None
        self._group_id_list = None
        self._name = None
        self._rule_config_list = None
        self._status = None

    @property
    def autoreply_id(self):
        return self._autoreply_id

    @autoreply_id.setter
    def autoreply_id(self, value):
        self._autoreply_id = value
    @property
    def global_valid(self):
        return self._global_valid

    @global_valid.setter
    def global_valid(self, value):
        self._global_valid = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def group_id_list(self):
        return self._group_id_list

    @group_id_list.setter
    def group_id_list(self, value):
        if isinstance(value, list):
            self._group_id_list = list()
            for i in value:
                self._group_id_list.append(i)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def rule_config_list(self):
        return self._rule_config_list

    @rule_config_list.setter
    def rule_config_list(self, value):
        if isinstance(value, list):
            self._rule_config_list = list()
            for i in value:
                if isinstance(i, GroupMsgAutoreplyRuleVO):
                    self._rule_config_list.append(i)
                else:
                    self._rule_config_list.append(GroupMsgAutoreplyRuleVO.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.autoreply_id:
            if hasattr(self.autoreply_id, 'to_alipay_dict'):
                params['autoreply_id'] = self.autoreply_id.to_alipay_dict()
            else:
                params['autoreply_id'] = self.autoreply_id
        if self.global_valid:
            if hasattr(self.global_valid, 'to_alipay_dict'):
                params['global_valid'] = self.global_valid.to_alipay_dict()
            else:
                params['global_valid'] = self.global_valid
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.group_id_list:
            if isinstance(self.group_id_list, list):
                for i in range(0, len(self.group_id_list)):
                    element = self.group_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_id_list[i] = element.to_alipay_dict()
            if hasattr(self.group_id_list, 'to_alipay_dict'):
                params['group_id_list'] = self.group_id_list.to_alipay_dict()
            else:
                params['group_id_list'] = self.group_id_list
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.rule_config_list:
            if isinstance(self.rule_config_list, list):
                for i in range(0, len(self.rule_config_list)):
                    element = self.rule_config_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rule_config_list[i] = element.to_alipay_dict()
            if hasattr(self.rule_config_list, 'to_alipay_dict'):
                params['rule_config_list'] = self.rule_config_list.to_alipay_dict()
            else:
                params['rule_config_list'] = self.rule_config_list
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupMsgAutoreplyDetailVO()
        if 'autoreply_id' in d:
            o.autoreply_id = d['autoreply_id']
        if 'global_valid' in d:
            o.global_valid = d['global_valid']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'group_id_list' in d:
            o.group_id_list = d['group_id_list']
        if 'name' in d:
            o.name = d['name']
        if 'rule_config_list' in d:
            o.rule_config_list = d['rule_config_list']
        if 'status' in d:
            o.status = d['status']
        return o


