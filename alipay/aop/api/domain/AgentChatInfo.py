#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgentChatInfo(object):

    def __init__(self):
        self._ccs_instance_id = None
        self._extended_group_ids = None
        self._group_id = None
        self._level_id = None

    @property
    def ccs_instance_id(self):
        return self._ccs_instance_id

    @ccs_instance_id.setter
    def ccs_instance_id(self, value):
        self._ccs_instance_id = value
    @property
    def extended_group_ids(self):
        return self._extended_group_ids

    @extended_group_ids.setter
    def extended_group_ids(self, value):
        if isinstance(value, list):
            self._extended_group_ids = list()
            for i in value:
                self._extended_group_ids.append(i)
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def level_id(self):
        return self._level_id

    @level_id.setter
    def level_id(self, value):
        self._level_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ccs_instance_id:
            if hasattr(self.ccs_instance_id, 'to_alipay_dict'):
                params['ccs_instance_id'] = self.ccs_instance_id.to_alipay_dict()
            else:
                params['ccs_instance_id'] = self.ccs_instance_id
        if self.extended_group_ids:
            if isinstance(self.extended_group_ids, list):
                for i in range(0, len(self.extended_group_ids)):
                    element = self.extended_group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extended_group_ids[i] = element.to_alipay_dict()
            if hasattr(self.extended_group_ids, 'to_alipay_dict'):
                params['extended_group_ids'] = self.extended_group_ids.to_alipay_dict()
            else:
                params['extended_group_ids'] = self.extended_group_ids
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.level_id:
            if hasattr(self.level_id, 'to_alipay_dict'):
                params['level_id'] = self.level_id.to_alipay_dict()
            else:
                params['level_id'] = self.level_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgentChatInfo()
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'extended_group_ids' in d:
            o.extended_group_ids = d['extended_group_ids']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'level_id' in d:
            o.level_id = d['level_id']
        return o


