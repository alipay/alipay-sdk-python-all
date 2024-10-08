#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupBaseInfoVO(object):

    def __init__(self):
        self._forbid_send_msg = None
        self._group_admin_open_id_list = None
        self._group_admin_user_id_list = None
        self._group_count = None
        self._group_id = None
        self._group_member_count = None
        self._group_name = None
        self._modify_history_group = None
        self._related_app_id = None
        self._related_app_logo = None

    @property
    def forbid_send_msg(self):
        return self._forbid_send_msg

    @forbid_send_msg.setter
    def forbid_send_msg(self, value):
        self._forbid_send_msg = value
    @property
    def group_admin_open_id_list(self):
        return self._group_admin_open_id_list

    @group_admin_open_id_list.setter
    def group_admin_open_id_list(self, value):
        if isinstance(value, list):
            self._group_admin_open_id_list = list()
            for i in value:
                self._group_admin_open_id_list.append(i)
    @property
    def group_admin_user_id_list(self):
        return self._group_admin_user_id_list

    @group_admin_user_id_list.setter
    def group_admin_user_id_list(self, value):
        if isinstance(value, list):
            self._group_admin_user_id_list = list()
            for i in value:
                self._group_admin_user_id_list.append(i)
    @property
    def group_count(self):
        return self._group_count

    @group_count.setter
    def group_count(self, value):
        self._group_count = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_member_count(self):
        return self._group_member_count

    @group_member_count.setter
    def group_member_count(self, value):
        self._group_member_count = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def modify_history_group(self):
        return self._modify_history_group

    @modify_history_group.setter
    def modify_history_group(self, value):
        self._modify_history_group = value
    @property
    def related_app_id(self):
        return self._related_app_id

    @related_app_id.setter
    def related_app_id(self, value):
        self._related_app_id = value
    @property
    def related_app_logo(self):
        return self._related_app_logo

    @related_app_logo.setter
    def related_app_logo(self, value):
        self._related_app_logo = value


    def to_alipay_dict(self):
        params = dict()
        if self.forbid_send_msg:
            if hasattr(self.forbid_send_msg, 'to_alipay_dict'):
                params['forbid_send_msg'] = self.forbid_send_msg.to_alipay_dict()
            else:
                params['forbid_send_msg'] = self.forbid_send_msg
        if self.group_admin_open_id_list:
            if isinstance(self.group_admin_open_id_list, list):
                for i in range(0, len(self.group_admin_open_id_list)):
                    element = self.group_admin_open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_admin_open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.group_admin_open_id_list, 'to_alipay_dict'):
                params['group_admin_open_id_list'] = self.group_admin_open_id_list.to_alipay_dict()
            else:
                params['group_admin_open_id_list'] = self.group_admin_open_id_list
        if self.group_admin_user_id_list:
            if isinstance(self.group_admin_user_id_list, list):
                for i in range(0, len(self.group_admin_user_id_list)):
                    element = self.group_admin_user_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_admin_user_id_list[i] = element.to_alipay_dict()
            if hasattr(self.group_admin_user_id_list, 'to_alipay_dict'):
                params['group_admin_user_id_list'] = self.group_admin_user_id_list.to_alipay_dict()
            else:
                params['group_admin_user_id_list'] = self.group_admin_user_id_list
        if self.group_count:
            if hasattr(self.group_count, 'to_alipay_dict'):
                params['group_count'] = self.group_count.to_alipay_dict()
            else:
                params['group_count'] = self.group_count
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_member_count:
            if hasattr(self.group_member_count, 'to_alipay_dict'):
                params['group_member_count'] = self.group_member_count.to_alipay_dict()
            else:
                params['group_member_count'] = self.group_member_count
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.modify_history_group:
            if hasattr(self.modify_history_group, 'to_alipay_dict'):
                params['modify_history_group'] = self.modify_history_group.to_alipay_dict()
            else:
                params['modify_history_group'] = self.modify_history_group
        if self.related_app_id:
            if hasattr(self.related_app_id, 'to_alipay_dict'):
                params['related_app_id'] = self.related_app_id.to_alipay_dict()
            else:
                params['related_app_id'] = self.related_app_id
        if self.related_app_logo:
            if hasattr(self.related_app_logo, 'to_alipay_dict'):
                params['related_app_logo'] = self.related_app_logo.to_alipay_dict()
            else:
                params['related_app_logo'] = self.related_app_logo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupBaseInfoVO()
        if 'forbid_send_msg' in d:
            o.forbid_send_msg = d['forbid_send_msg']
        if 'group_admin_open_id_list' in d:
            o.group_admin_open_id_list = d['group_admin_open_id_list']
        if 'group_admin_user_id_list' in d:
            o.group_admin_user_id_list = d['group_admin_user_id_list']
        if 'group_count' in d:
            o.group_count = d['group_count']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_member_count' in d:
            o.group_member_count = d['group_member_count']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'modify_history_group' in d:
            o.modify_history_group = d['modify_history_group']
        if 'related_app_id' in d:
            o.related_app_id = d['related_app_id']
        if 'related_app_logo' in d:
            o.related_app_logo = d['related_app_logo']
        return o


