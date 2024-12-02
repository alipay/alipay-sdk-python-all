#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupMemberDetail import GroupMemberDetail


class GroupChangedNotice(object):

    def __init__(self):
        self._create_time = None
        self._group_id = None
        self._group_instance_id = None
        self._group_name = None
        self._group_oid = None
        self._mem_change_cnt = None
        self._mem_change_list = None
        self._pid = None
        self._update_info = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_instance_id(self):
        return self._group_instance_id

    @group_instance_id.setter
    def group_instance_id(self, value):
        self._group_instance_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def group_oid(self):
        return self._group_oid

    @group_oid.setter
    def group_oid(self, value):
        self._group_oid = value
    @property
    def mem_change_cnt(self):
        return self._mem_change_cnt

    @mem_change_cnt.setter
    def mem_change_cnt(self, value):
        self._mem_change_cnt = value
    @property
    def mem_change_list(self):
        return self._mem_change_list

    @mem_change_list.setter
    def mem_change_list(self, value):
        if isinstance(value, list):
            self._mem_change_list = list()
            for i in value:
                if isinstance(i, GroupMemberDetail):
                    self._mem_change_list.append(i)
                else:
                    self._mem_change_list.append(GroupMemberDetail.from_alipay_dict(i))
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def update_info(self):
        return self._update_info

    @update_info.setter
    def update_info(self, value):
        self._update_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_instance_id:
            if hasattr(self.group_instance_id, 'to_alipay_dict'):
                params['group_instance_id'] = self.group_instance_id.to_alipay_dict()
            else:
                params['group_instance_id'] = self.group_instance_id
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.group_oid:
            if hasattr(self.group_oid, 'to_alipay_dict'):
                params['group_oid'] = self.group_oid.to_alipay_dict()
            else:
                params['group_oid'] = self.group_oid
        if self.mem_change_cnt:
            if hasattr(self.mem_change_cnt, 'to_alipay_dict'):
                params['mem_change_cnt'] = self.mem_change_cnt.to_alipay_dict()
            else:
                params['mem_change_cnt'] = self.mem_change_cnt
        if self.mem_change_list:
            if isinstance(self.mem_change_list, list):
                for i in range(0, len(self.mem_change_list)):
                    element = self.mem_change_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mem_change_list[i] = element.to_alipay_dict()
            if hasattr(self.mem_change_list, 'to_alipay_dict'):
                params['mem_change_list'] = self.mem_change_list.to_alipay_dict()
            else:
                params['mem_change_list'] = self.mem_change_list
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.update_info:
            if hasattr(self.update_info, 'to_alipay_dict'):
                params['update_info'] = self.update_info.to_alipay_dict()
            else:
                params['update_info'] = self.update_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupChangedNotice()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_instance_id' in d:
            o.group_instance_id = d['group_instance_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'group_oid' in d:
            o.group_oid = d['group_oid']
        if 'mem_change_cnt' in d:
            o.mem_change_cnt = d['mem_change_cnt']
        if 'mem_change_list' in d:
            o.mem_change_list = d['mem_change_list']
        if 'pid' in d:
            o.pid = d['pid']
        if 'update_info' in d:
            o.update_info = d['update_info']
        return o


