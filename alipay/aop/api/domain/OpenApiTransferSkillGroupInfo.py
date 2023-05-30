#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiSceneInstanceInfo import OpenApiSceneInstanceInfo
from alipay.aop.api.domain.OpenApiSkillGroupChannelInfo import OpenApiSkillGroupChannelInfo


class OpenApiTransferSkillGroupInfo(object):

    def __init__(self):
        self._clv_meta_organization_id = None
        self._clv_skill_group_id = None
        self._clv_skill_group_type = None
        self._scene_instance_info = None
        self._skill_group_channel = None
        self._skill_group_id = None
        self._skill_group_name = None
        self._tnt_inst_id = None

    @property
    def clv_meta_organization_id(self):
        return self._clv_meta_organization_id

    @clv_meta_organization_id.setter
    def clv_meta_organization_id(self, value):
        self._clv_meta_organization_id = value
    @property
    def clv_skill_group_id(self):
        return self._clv_skill_group_id

    @clv_skill_group_id.setter
    def clv_skill_group_id(self, value):
        self._clv_skill_group_id = value
    @property
    def clv_skill_group_type(self):
        return self._clv_skill_group_type

    @clv_skill_group_type.setter
    def clv_skill_group_type(self, value):
        self._clv_skill_group_type = value
    @property
    def scene_instance_info(self):
        return self._scene_instance_info

    @scene_instance_info.setter
    def scene_instance_info(self, value):
        if isinstance(value, OpenApiSceneInstanceInfo):
            self._scene_instance_info = value
        else:
            self._scene_instance_info = OpenApiSceneInstanceInfo.from_alipay_dict(value)
    @property
    def skill_group_channel(self):
        return self._skill_group_channel

    @skill_group_channel.setter
    def skill_group_channel(self, value):
        if isinstance(value, OpenApiSkillGroupChannelInfo):
            self._skill_group_channel = value
        else:
            self._skill_group_channel = OpenApiSkillGroupChannelInfo.from_alipay_dict(value)
    @property
    def skill_group_id(self):
        return self._skill_group_id

    @skill_group_id.setter
    def skill_group_id(self, value):
        self._skill_group_id = value
    @property
    def skill_group_name(self):
        return self._skill_group_name

    @skill_group_name.setter
    def skill_group_name(self, value):
        self._skill_group_name = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.clv_meta_organization_id:
            if hasattr(self.clv_meta_organization_id, 'to_alipay_dict'):
                params['clv_meta_organization_id'] = self.clv_meta_organization_id.to_alipay_dict()
            else:
                params['clv_meta_organization_id'] = self.clv_meta_organization_id
        if self.clv_skill_group_id:
            if hasattr(self.clv_skill_group_id, 'to_alipay_dict'):
                params['clv_skill_group_id'] = self.clv_skill_group_id.to_alipay_dict()
            else:
                params['clv_skill_group_id'] = self.clv_skill_group_id
        if self.clv_skill_group_type:
            if hasattr(self.clv_skill_group_type, 'to_alipay_dict'):
                params['clv_skill_group_type'] = self.clv_skill_group_type.to_alipay_dict()
            else:
                params['clv_skill_group_type'] = self.clv_skill_group_type
        if self.scene_instance_info:
            if hasattr(self.scene_instance_info, 'to_alipay_dict'):
                params['scene_instance_info'] = self.scene_instance_info.to_alipay_dict()
            else:
                params['scene_instance_info'] = self.scene_instance_info
        if self.skill_group_channel:
            if hasattr(self.skill_group_channel, 'to_alipay_dict'):
                params['skill_group_channel'] = self.skill_group_channel.to_alipay_dict()
            else:
                params['skill_group_channel'] = self.skill_group_channel
        if self.skill_group_id:
            if hasattr(self.skill_group_id, 'to_alipay_dict'):
                params['skill_group_id'] = self.skill_group_id.to_alipay_dict()
            else:
                params['skill_group_id'] = self.skill_group_id
        if self.skill_group_name:
            if hasattr(self.skill_group_name, 'to_alipay_dict'):
                params['skill_group_name'] = self.skill_group_name.to_alipay_dict()
            else:
                params['skill_group_name'] = self.skill_group_name
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiTransferSkillGroupInfo()
        if 'clv_meta_organization_id' in d:
            o.clv_meta_organization_id = d['clv_meta_organization_id']
        if 'clv_skill_group_id' in d:
            o.clv_skill_group_id = d['clv_skill_group_id']
        if 'clv_skill_group_type' in d:
            o.clv_skill_group_type = d['clv_skill_group_type']
        if 'scene_instance_info' in d:
            o.scene_instance_info = d['scene_instance_info']
        if 'skill_group_channel' in d:
            o.skill_group_channel = d['skill_group_channel']
        if 'skill_group_id' in d:
            o.skill_group_id = d['skill_group_id']
        if 'skill_group_name' in d:
            o.skill_group_name = d['skill_group_name']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


