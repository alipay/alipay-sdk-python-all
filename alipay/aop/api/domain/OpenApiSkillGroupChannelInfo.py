#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiSkillGroupChannelInfo(object):

    def __init__(self):
        self._admin_id = None
        self._channel_account_ref_organization = None
        self._channel_account_role = None
        self._channel_scene_id = None
        self._channel_scene_name = None
        self._channel_skill_group_id = None
        self._channel_skill_group_name = None
        self._sub_channel = None
        self._sub_channel_name = None

    @property
    def admin_id(self):
        return self._admin_id

    @admin_id.setter
    def admin_id(self, value):
        self._admin_id = value
    @property
    def channel_account_ref_organization(self):
        return self._channel_account_ref_organization

    @channel_account_ref_organization.setter
    def channel_account_ref_organization(self, value):
        self._channel_account_ref_organization = value
    @property
    def channel_account_role(self):
        return self._channel_account_role

    @channel_account_role.setter
    def channel_account_role(self, value):
        self._channel_account_role = value
    @property
    def channel_scene_id(self):
        return self._channel_scene_id

    @channel_scene_id.setter
    def channel_scene_id(self, value):
        self._channel_scene_id = value
    @property
    def channel_scene_name(self):
        return self._channel_scene_name

    @channel_scene_name.setter
    def channel_scene_name(self, value):
        self._channel_scene_name = value
    @property
    def channel_skill_group_id(self):
        return self._channel_skill_group_id

    @channel_skill_group_id.setter
    def channel_skill_group_id(self, value):
        self._channel_skill_group_id = value
    @property
    def channel_skill_group_name(self):
        return self._channel_skill_group_name

    @channel_skill_group_name.setter
    def channel_skill_group_name(self, value):
        self._channel_skill_group_name = value
    @property
    def sub_channel(self):
        return self._sub_channel

    @sub_channel.setter
    def sub_channel(self, value):
        self._sub_channel = value
    @property
    def sub_channel_name(self):
        return self._sub_channel_name

    @sub_channel_name.setter
    def sub_channel_name(self, value):
        self._sub_channel_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.admin_id:
            if hasattr(self.admin_id, 'to_alipay_dict'):
                params['admin_id'] = self.admin_id.to_alipay_dict()
            else:
                params['admin_id'] = self.admin_id
        if self.channel_account_ref_organization:
            if hasattr(self.channel_account_ref_organization, 'to_alipay_dict'):
                params['channel_account_ref_organization'] = self.channel_account_ref_organization.to_alipay_dict()
            else:
                params['channel_account_ref_organization'] = self.channel_account_ref_organization
        if self.channel_account_role:
            if hasattr(self.channel_account_role, 'to_alipay_dict'):
                params['channel_account_role'] = self.channel_account_role.to_alipay_dict()
            else:
                params['channel_account_role'] = self.channel_account_role
        if self.channel_scene_id:
            if hasattr(self.channel_scene_id, 'to_alipay_dict'):
                params['channel_scene_id'] = self.channel_scene_id.to_alipay_dict()
            else:
                params['channel_scene_id'] = self.channel_scene_id
        if self.channel_scene_name:
            if hasattr(self.channel_scene_name, 'to_alipay_dict'):
                params['channel_scene_name'] = self.channel_scene_name.to_alipay_dict()
            else:
                params['channel_scene_name'] = self.channel_scene_name
        if self.channel_skill_group_id:
            if hasattr(self.channel_skill_group_id, 'to_alipay_dict'):
                params['channel_skill_group_id'] = self.channel_skill_group_id.to_alipay_dict()
            else:
                params['channel_skill_group_id'] = self.channel_skill_group_id
        if self.channel_skill_group_name:
            if hasattr(self.channel_skill_group_name, 'to_alipay_dict'):
                params['channel_skill_group_name'] = self.channel_skill_group_name.to_alipay_dict()
            else:
                params['channel_skill_group_name'] = self.channel_skill_group_name
        if self.sub_channel:
            if hasattr(self.sub_channel, 'to_alipay_dict'):
                params['sub_channel'] = self.sub_channel.to_alipay_dict()
            else:
                params['sub_channel'] = self.sub_channel
        if self.sub_channel_name:
            if hasattr(self.sub_channel_name, 'to_alipay_dict'):
                params['sub_channel_name'] = self.sub_channel_name.to_alipay_dict()
            else:
                params['sub_channel_name'] = self.sub_channel_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiSkillGroupChannelInfo()
        if 'admin_id' in d:
            o.admin_id = d['admin_id']
        if 'channel_account_ref_organization' in d:
            o.channel_account_ref_organization = d['channel_account_ref_organization']
        if 'channel_account_role' in d:
            o.channel_account_role = d['channel_account_role']
        if 'channel_scene_id' in d:
            o.channel_scene_id = d['channel_scene_id']
        if 'channel_scene_name' in d:
            o.channel_scene_name = d['channel_scene_name']
        if 'channel_skill_group_id' in d:
            o.channel_skill_group_id = d['channel_skill_group_id']
        if 'channel_skill_group_name' in d:
            o.channel_skill_group_name = d['channel_skill_group_name']
        if 'sub_channel' in d:
            o.sub_channel = d['sub_channel']
        if 'sub_channel_name' in d:
            o.sub_channel_name = d['sub_channel_name']
        return o


