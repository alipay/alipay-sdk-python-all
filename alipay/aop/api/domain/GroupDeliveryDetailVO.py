#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupAccountVO import GroupAccountVO


class GroupDeliveryDetailVO(object):

    def __init__(self):
        self._audit_status = None
        self._bind_scene = None
        self._delivery_id = None
        self._delivery_name = None
        self._end_time = None
        self._group_accounts = None
        self._group_id = None
        self._group_name = None
        self._start_time = None
        self._status = None

    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def bind_scene(self):
        return self._bind_scene

    @bind_scene.setter
    def bind_scene(self, value):
        self._bind_scene = value
    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
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
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.bind_scene:
            if hasattr(self.bind_scene, 'to_alipay_dict'):
                params['bind_scene'] = self.bind_scene.to_alipay_dict()
            else:
                params['bind_scene'] = self.bind_scene
        if self.delivery_id:
            if hasattr(self.delivery_id, 'to_alipay_dict'):
                params['delivery_id'] = self.delivery_id.to_alipay_dict()
            else:
                params['delivery_id'] = self.delivery_id
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
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        o = GroupDeliveryDetailVO()
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'bind_scene' in d:
            o.bind_scene = d['bind_scene']
        if 'delivery_id' in d:
            o.delivery_id = d['delivery_id']
        if 'delivery_name' in d:
            o.delivery_name = d['delivery_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'group_accounts' in d:
            o.group_accounts = d['group_accounts']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o


