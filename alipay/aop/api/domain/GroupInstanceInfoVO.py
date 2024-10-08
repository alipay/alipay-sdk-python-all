#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupUserVO import GroupUserVO
from alipay.aop.api.domain.GroupUserVO import GroupUserVO
from alipay.aop.api.domain.GroupUserVO import GroupUserVO


class GroupInstanceInfoVO(object):

    def __init__(self):
        self._auto_create_group_instance = None
        self._forbid_admin_chat = None
        self._forbid_member_chat = None
        self._gmt_create = None
        self._group_id = None
        self._group_instance_admin_user_list = None
        self._group_instance_desc = None
        self._group_instance_id = None
        self._group_instance_master = None
        self._group_instance_member_count = None
        self._group_instance_name = None
        self._head_img = None
        self._member_list = None
        self._notice = None
        self._open_invite = None

    @property
    def auto_create_group_instance(self):
        return self._auto_create_group_instance

    @auto_create_group_instance.setter
    def auto_create_group_instance(self, value):
        self._auto_create_group_instance = value
    @property
    def forbid_admin_chat(self):
        return self._forbid_admin_chat

    @forbid_admin_chat.setter
    def forbid_admin_chat(self, value):
        self._forbid_admin_chat = value
    @property
    def forbid_member_chat(self):
        return self._forbid_member_chat

    @forbid_member_chat.setter
    def forbid_member_chat(self, value):
        self._forbid_member_chat = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_instance_admin_user_list(self):
        return self._group_instance_admin_user_list

    @group_instance_admin_user_list.setter
    def group_instance_admin_user_list(self, value):
        if isinstance(value, list):
            self._group_instance_admin_user_list = list()
            for i in value:
                if isinstance(i, GroupUserVO):
                    self._group_instance_admin_user_list.append(i)
                else:
                    self._group_instance_admin_user_list.append(GroupUserVO.from_alipay_dict(i))
    @property
    def group_instance_desc(self):
        return self._group_instance_desc

    @group_instance_desc.setter
    def group_instance_desc(self, value):
        self._group_instance_desc = value
    @property
    def group_instance_id(self):
        return self._group_instance_id

    @group_instance_id.setter
    def group_instance_id(self, value):
        self._group_instance_id = value
    @property
    def group_instance_master(self):
        return self._group_instance_master

    @group_instance_master.setter
    def group_instance_master(self, value):
        if isinstance(value, GroupUserVO):
            self._group_instance_master = value
        else:
            self._group_instance_master = GroupUserVO.from_alipay_dict(value)
    @property
    def group_instance_member_count(self):
        return self._group_instance_member_count

    @group_instance_member_count.setter
    def group_instance_member_count(self, value):
        self._group_instance_member_count = value
    @property
    def group_instance_name(self):
        return self._group_instance_name

    @group_instance_name.setter
    def group_instance_name(self, value):
        self._group_instance_name = value
    @property
    def head_img(self):
        return self._head_img

    @head_img.setter
    def head_img(self, value):
        self._head_img = value
    @property
    def member_list(self):
        return self._member_list

    @member_list.setter
    def member_list(self, value):
        if isinstance(value, list):
            self._member_list = list()
            for i in value:
                if isinstance(i, GroupUserVO):
                    self._member_list.append(i)
                else:
                    self._member_list.append(GroupUserVO.from_alipay_dict(i))
    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value
    @property
    def open_invite(self):
        return self._open_invite

    @open_invite.setter
    def open_invite(self, value):
        self._open_invite = value


    def to_alipay_dict(self):
        params = dict()
        if self.auto_create_group_instance:
            if hasattr(self.auto_create_group_instance, 'to_alipay_dict'):
                params['auto_create_group_instance'] = self.auto_create_group_instance.to_alipay_dict()
            else:
                params['auto_create_group_instance'] = self.auto_create_group_instance
        if self.forbid_admin_chat:
            if hasattr(self.forbid_admin_chat, 'to_alipay_dict'):
                params['forbid_admin_chat'] = self.forbid_admin_chat.to_alipay_dict()
            else:
                params['forbid_admin_chat'] = self.forbid_admin_chat
        if self.forbid_member_chat:
            if hasattr(self.forbid_member_chat, 'to_alipay_dict'):
                params['forbid_member_chat'] = self.forbid_member_chat.to_alipay_dict()
            else:
                params['forbid_member_chat'] = self.forbid_member_chat
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_instance_admin_user_list:
            if isinstance(self.group_instance_admin_user_list, list):
                for i in range(0, len(self.group_instance_admin_user_list)):
                    element = self.group_instance_admin_user_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_instance_admin_user_list[i] = element.to_alipay_dict()
            if hasattr(self.group_instance_admin_user_list, 'to_alipay_dict'):
                params['group_instance_admin_user_list'] = self.group_instance_admin_user_list.to_alipay_dict()
            else:
                params['group_instance_admin_user_list'] = self.group_instance_admin_user_list
        if self.group_instance_desc:
            if hasattr(self.group_instance_desc, 'to_alipay_dict'):
                params['group_instance_desc'] = self.group_instance_desc.to_alipay_dict()
            else:
                params['group_instance_desc'] = self.group_instance_desc
        if self.group_instance_id:
            if hasattr(self.group_instance_id, 'to_alipay_dict'):
                params['group_instance_id'] = self.group_instance_id.to_alipay_dict()
            else:
                params['group_instance_id'] = self.group_instance_id
        if self.group_instance_master:
            if hasattr(self.group_instance_master, 'to_alipay_dict'):
                params['group_instance_master'] = self.group_instance_master.to_alipay_dict()
            else:
                params['group_instance_master'] = self.group_instance_master
        if self.group_instance_member_count:
            if hasattr(self.group_instance_member_count, 'to_alipay_dict'):
                params['group_instance_member_count'] = self.group_instance_member_count.to_alipay_dict()
            else:
                params['group_instance_member_count'] = self.group_instance_member_count
        if self.group_instance_name:
            if hasattr(self.group_instance_name, 'to_alipay_dict'):
                params['group_instance_name'] = self.group_instance_name.to_alipay_dict()
            else:
                params['group_instance_name'] = self.group_instance_name
        if self.head_img:
            if hasattr(self.head_img, 'to_alipay_dict'):
                params['head_img'] = self.head_img.to_alipay_dict()
            else:
                params['head_img'] = self.head_img
        if self.member_list:
            if isinstance(self.member_list, list):
                for i in range(0, len(self.member_list)):
                    element = self.member_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.member_list[i] = element.to_alipay_dict()
            if hasattr(self.member_list, 'to_alipay_dict'):
                params['member_list'] = self.member_list.to_alipay_dict()
            else:
                params['member_list'] = self.member_list
        if self.notice:
            if hasattr(self.notice, 'to_alipay_dict'):
                params['notice'] = self.notice.to_alipay_dict()
            else:
                params['notice'] = self.notice
        if self.open_invite:
            if hasattr(self.open_invite, 'to_alipay_dict'):
                params['open_invite'] = self.open_invite.to_alipay_dict()
            else:
                params['open_invite'] = self.open_invite
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupInstanceInfoVO()
        if 'auto_create_group_instance' in d:
            o.auto_create_group_instance = d['auto_create_group_instance']
        if 'forbid_admin_chat' in d:
            o.forbid_admin_chat = d['forbid_admin_chat']
        if 'forbid_member_chat' in d:
            o.forbid_member_chat = d['forbid_member_chat']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_instance_admin_user_list' in d:
            o.group_instance_admin_user_list = d['group_instance_admin_user_list']
        if 'group_instance_desc' in d:
            o.group_instance_desc = d['group_instance_desc']
        if 'group_instance_id' in d:
            o.group_instance_id = d['group_instance_id']
        if 'group_instance_master' in d:
            o.group_instance_master = d['group_instance_master']
        if 'group_instance_member_count' in d:
            o.group_instance_member_count = d['group_instance_member_count']
        if 'group_instance_name' in d:
            o.group_instance_name = d['group_instance_name']
        if 'head_img' in d:
            o.head_img = d['head_img']
        if 'member_list' in d:
            o.member_list = d['member_list']
        if 'notice' in d:
            o.notice = d['notice']
        if 'open_invite' in d:
            o.open_invite = d['open_invite']
        return o


