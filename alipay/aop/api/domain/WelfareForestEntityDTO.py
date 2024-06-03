#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WelfareForestEntityDTO(object):

    def __init__(self):
        self._desc = None
        self._display_info = None
        self._icon = None
        self._id = None
        self._name = None
        self._solid_water_value = None
        self._status = None
        self._title = None
        self._tree_name = None
        self._type = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def display_info(self):
        return self._display_info

    @display_info.setter
    def display_info(self, value):
        self._display_info = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def solid_water_value(self):
        return self._solid_water_value

    @solid_water_value.setter
    def solid_water_value(self, value):
        self._solid_water_value = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def tree_name(self):
        return self._tree_name

    @tree_name.setter
    def tree_name(self, value):
        self._tree_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.display_info:
            if hasattr(self.display_info, 'to_alipay_dict'):
                params['display_info'] = self.display_info.to_alipay_dict()
            else:
                params['display_info'] = self.display_info
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.solid_water_value:
            if hasattr(self.solid_water_value, 'to_alipay_dict'):
                params['solid_water_value'] = self.solid_water_value.to_alipay_dict()
            else:
                params['solid_water_value'] = self.solid_water_value
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.tree_name:
            if hasattr(self.tree_name, 'to_alipay_dict'):
                params['tree_name'] = self.tree_name.to_alipay_dict()
            else:
                params['tree_name'] = self.tree_name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WelfareForestEntityDTO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'display_info' in d:
            o.display_info = d['display_info']
        if 'icon' in d:
            o.icon = d['icon']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'solid_water_value' in d:
            o.solid_water_value = d['solid_water_value']
        if 'status' in d:
            o.status = d['status']
        if 'title' in d:
            o.title = d['title']
        if 'tree_name' in d:
            o.tree_name = d['tree_name']
        if 'type' in d:
            o.type = d['type']
        return o


