#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LinkTypeResult(object):

    def __init__(self):
        self._level = None
        self._link_type_code = None
        self._link_type_name = None
        self._parent_code = None
        self._state = None
        self._tnt_inst_id = None

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def link_type_code(self):
        return self._link_type_code

    @link_type_code.setter
    def link_type_code(self, value):
        self._link_type_code = value
    @property
    def link_type_name(self):
        return self._link_type_name

    @link_type_name.setter
    def link_type_name(self, value):
        self._link_type_name = value
    @property
    def parent_code(self):
        return self._parent_code

    @parent_code.setter
    def parent_code(self, value):
        self._parent_code = value
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
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.link_type_code:
            if hasattr(self.link_type_code, 'to_alipay_dict'):
                params['link_type_code'] = self.link_type_code.to_alipay_dict()
            else:
                params['link_type_code'] = self.link_type_code
        if self.link_type_name:
            if hasattr(self.link_type_name, 'to_alipay_dict'):
                params['link_type_name'] = self.link_type_name.to_alipay_dict()
            else:
                params['link_type_name'] = self.link_type_name
        if self.parent_code:
            if hasattr(self.parent_code, 'to_alipay_dict'):
                params['parent_code'] = self.parent_code.to_alipay_dict()
            else:
                params['parent_code'] = self.parent_code
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
        o = LinkTypeResult()
        if 'level' in d:
            o.level = d['level']
        if 'link_type_code' in d:
            o.link_type_code = d['link_type_code']
        if 'link_type_name' in d:
            o.link_type_name = d['link_type_name']
        if 'parent_code' in d:
            o.parent_code = d['parent_code']
        if 'state' in d:
            o.state = d['state']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


