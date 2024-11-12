#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupAccountVO import GroupAccountVO


class AlipayMerchantGroupDeliveryCreateModel(object):

    def __init__(self):
        self._bind_scene = None
        self._delivery_join_rule_id = None
        self._delivery_name = None
        self._end_time = None
        self._group_accounts = None
        self._group_id = None
        self._start_time = None

    @property
    def bind_scene(self):
        return self._bind_scene

    @bind_scene.setter
    def bind_scene(self, value):
        self._bind_scene = value
    @property
    def delivery_join_rule_id(self):
        return self._delivery_join_rule_id

    @delivery_join_rule_id.setter
    def delivery_join_rule_id(self, value):
        self._delivery_join_rule_id = value
    @property
    def delivery_name(self):
        return self._delivery_name

    @delivery_name.setter
    def delivery_name(self, value):
        self._delivery_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def group_accounts(self):
        return self._group_accounts

    @group_accounts.setter
    def group_accounts(self, value):
        if isinstance(value, list):
            self._group_accounts = list()
            for i in value:
                if isinstance(i, GroupAccountVO):
                    self._group_accounts.append(i)
                else:
                    self._group_accounts.append(GroupAccountVO.from_alipay_dict(i))
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_scene:
            if hasattr(self.bind_scene, 'to_alipay_dict'):
                params['bind_scene'] = self.bind_scene.to_alipay_dict()
            else:
                params['bind_scene'] = self.bind_scene
        if self.delivery_join_rule_id:
            if hasattr(self.delivery_join_rule_id, 'to_alipay_dict'):
                params['delivery_join_rule_id'] = self.delivery_join_rule_id.to_alipay_dict()
            else:
                params['delivery_join_rule_id'] = self.delivery_join_rule_id
        if self.delivery_name:
            if hasattr(self.delivery_name, 'to_alipay_dict'):
                params['delivery_name'] = self.delivery_name.to_alipay_dict()
            else:
                params['delivery_name'] = self.delivery_name
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.group_accounts:
            if isinstance(self.group_accounts, list):
                for i in range(0, len(self.group_accounts)):
                    element = self.group_accounts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_accounts[i] = element.to_alipay_dict()
            if hasattr(self.group_accounts, 'to_alipay_dict'):
                params['group_accounts'] = self.group_accounts.to_alipay_dict()
            else:
                params['group_accounts'] = self.group_accounts
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupDeliveryCreateModel()
        if 'bind_scene' in d:
            o.bind_scene = d['bind_scene']
        if 'delivery_join_rule_id' in d:
            o.delivery_join_rule_id = d['delivery_join_rule_id']
        if 'delivery_name' in d:
            o.delivery_name = d['delivery_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'group_accounts' in d:
            o.group_accounts = d['group_accounts']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


