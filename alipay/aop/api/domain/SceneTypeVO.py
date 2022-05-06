#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneTypeVO(object):

    def __init__(self):
        self._creator = None
        self._creator_name = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._last_moder = None
        self._modifier = None
        self._modifier_name = None
        self._scene_type_code = None
        self._scene_type_name = None
        self._state = None
        self._tnt_inst_id = None

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def creator_name(self):
        return self._creator_name

    @creator_name.setter
    def creator_name(self, value):
        self._creator_name = value
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
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def last_moder(self):
        return self._last_moder

    @last_moder.setter
    def last_moder(self, value):
        self._last_moder = value
    @property
    def modifier(self):
        return self._modifier

    @modifier.setter
    def modifier(self, value):
        self._modifier = value
    @property
    def modifier_name(self):
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, value):
        self._modifier_name = value
    @property
    def scene_type_code(self):
        return self._scene_type_code

    @scene_type_code.setter
    def scene_type_code(self, value):
        self._scene_type_code = value
    @property
    def scene_type_name(self):
        return self._scene_type_name

    @scene_type_name.setter
    def scene_type_name(self, value):
        self._scene_type_name = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.creator_name:
            if hasattr(self.creator_name, 'to_alipay_dict'):
                params['creator_name'] = self.creator_name.to_alipay_dict()
            else:
                params['creator_name'] = self.creator_name
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
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.last_moder:
            if hasattr(self.last_moder, 'to_alipay_dict'):
                params['last_moder'] = self.last_moder.to_alipay_dict()
            else:
                params['last_moder'] = self.last_moder
        if self.modifier:
            if hasattr(self.modifier, 'to_alipay_dict'):
                params['modifier'] = self.modifier.to_alipay_dict()
            else:
                params['modifier'] = self.modifier
        if self.modifier_name:
            if hasattr(self.modifier_name, 'to_alipay_dict'):
                params['modifier_name'] = self.modifier_name.to_alipay_dict()
            else:
                params['modifier_name'] = self.modifier_name
        if self.scene_type_code:
            if hasattr(self.scene_type_code, 'to_alipay_dict'):
                params['scene_type_code'] = self.scene_type_code.to_alipay_dict()
            else:
                params['scene_type_code'] = self.scene_type_code
        if self.scene_type_name:
            if hasattr(self.scene_type_name, 'to_alipay_dict'):
                params['scene_type_name'] = self.scene_type_name.to_alipay_dict()
            else:
                params['scene_type_name'] = self.scene_type_name
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
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
        o = SceneTypeVO()
        if 'creator' in d:
            o.creator = d['creator']
        if 'creator_name' in d:
            o.creator_name = d['creator_name']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'last_moder' in d:
            o.last_moder = d['last_moder']
        if 'modifier' in d:
            o.modifier = d['modifier']
        if 'modifier_name' in d:
            o.modifier_name = d['modifier_name']
        if 'scene_type_code' in d:
            o.scene_type_code = d['scene_type_code']
        if 'scene_type_name' in d:
            o.scene_type_name = d['scene_type_name']
        if 'state' in d:
            o.state = d['state']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


