#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SimpleOpenApiPrivilegeDetail(object):

    def __init__(self):
        self._display_content = None
        self._privilege_alias_name = None
        self._privilege_id = None
        self._privilege_name = None

    @property
    def display_content(self):
        return self._display_content

    @display_content.setter
    def display_content(self, value):
        self._display_content = value
    @property
    def privilege_alias_name(self):
        return self._privilege_alias_name

    @privilege_alias_name.setter
    def privilege_alias_name(self, value):
        self._privilege_alias_name = value
    @property
    def privilege_id(self):
        return self._privilege_id

    @privilege_id.setter
    def privilege_id(self, value):
        self._privilege_id = value
    @property
    def privilege_name(self):
        return self._privilege_name

    @privilege_name.setter
    def privilege_name(self, value):
        self._privilege_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.display_content:
            if hasattr(self.display_content, 'to_alipay_dict'):
                params['display_content'] = self.display_content.to_alipay_dict()
            else:
                params['display_content'] = self.display_content
        if self.privilege_alias_name:
            if hasattr(self.privilege_alias_name, 'to_alipay_dict'):
                params['privilege_alias_name'] = self.privilege_alias_name.to_alipay_dict()
            else:
                params['privilege_alias_name'] = self.privilege_alias_name
        if self.privilege_id:
            if hasattr(self.privilege_id, 'to_alipay_dict'):
                params['privilege_id'] = self.privilege_id.to_alipay_dict()
            else:
                params['privilege_id'] = self.privilege_id
        if self.privilege_name:
            if hasattr(self.privilege_name, 'to_alipay_dict'):
                params['privilege_name'] = self.privilege_name.to_alipay_dict()
            else:
                params['privilege_name'] = self.privilege_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SimpleOpenApiPrivilegeDetail()
        if 'display_content' in d:
            o.display_content = d['display_content']
        if 'privilege_alias_name' in d:
            o.privilege_alias_name = d['privilege_alias_name']
        if 'privilege_id' in d:
            o.privilege_id = d['privilege_id']
        if 'privilege_name' in d:
            o.privilege_name = d['privilege_name']
        return o


