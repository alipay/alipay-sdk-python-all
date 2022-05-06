#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupMemberDetail import GroupMemberDetail


class GroupDetail(object):

    def __init__(self):
        self._admin_user_ids = None
        self._create_time = None
        self._group_id = None
        self._group_img = None
        self._group_name = None
        self._master_user_id = None
        self._member_count = None
        self._members = None
        self._notice = None

    @property
    def admin_user_ids(self):
        return self._admin_user_ids

    @admin_user_ids.setter
    def admin_user_ids(self, value):
        if isinstance(value, list):
            self._admin_user_ids = list()
            for i in value:
                self._admin_user_ids.append(i)
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
    def group_img(self):
        return self._group_img

    @group_img.setter
    def group_img(self, value):
        self._group_img = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def master_user_id(self):
        return self._master_user_id

    @master_user_id.setter
    def master_user_id(self, value):
        self._master_user_id = value
    @property
    def member_count(self):
        return self._member_count

    @member_count.setter
    def member_count(self, value):
        self._member_count = value
    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, value):
        if isinstance(value, list):
            self._members = list()
            for i in value:
                if isinstance(i, GroupMemberDetail):
                    self._members.append(i)
                else:
                    self._members.append(GroupMemberDetail.from_alipay_dict(i))
    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value


    def to_alipay_dict(self):
        params = dict()
        if self.admin_user_ids:
            if isinstance(self.admin_user_ids, list):
                for i in range(0, len(self.admin_user_ids)):
                    element = self.admin_user_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.admin_user_ids[i] = element.to_alipay_dict()
            if hasattr(self.admin_user_ids, 'to_alipay_dict'):
                params['admin_user_ids'] = self.admin_user_ids.to_alipay_dict()
            else:
                params['admin_user_ids'] = self.admin_user_ids
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
        if self.group_img:
            if hasattr(self.group_img, 'to_alipay_dict'):
                params['group_img'] = self.group_img.to_alipay_dict()
            else:
                params['group_img'] = self.group_img
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.master_user_id:
            if hasattr(self.master_user_id, 'to_alipay_dict'):
                params['master_user_id'] = self.master_user_id.to_alipay_dict()
            else:
                params['master_user_id'] = self.master_user_id
        if self.member_count:
            if hasattr(self.member_count, 'to_alipay_dict'):
                params['member_count'] = self.member_count.to_alipay_dict()
            else:
                params['member_count'] = self.member_count
        if self.members:
            if isinstance(self.members, list):
                for i in range(0, len(self.members)):
                    element = self.members[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.members[i] = element.to_alipay_dict()
            if hasattr(self.members, 'to_alipay_dict'):
                params['members'] = self.members.to_alipay_dict()
            else:
                params['members'] = self.members
        if self.notice:
            if hasattr(self.notice, 'to_alipay_dict'):
                params['notice'] = self.notice.to_alipay_dict()
            else:
                params['notice'] = self.notice
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupDetail()
        if 'admin_user_ids' in d:
            o.admin_user_ids = d['admin_user_ids']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_img' in d:
            o.group_img = d['group_img']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'master_user_id' in d:
            o.master_user_id = d['master_user_id']
        if 'member_count' in d:
            o.member_count = d['member_count']
        if 'members' in d:
            o.members = d['members']
        if 'notice' in d:
            o.notice = d['notice']
        return o


