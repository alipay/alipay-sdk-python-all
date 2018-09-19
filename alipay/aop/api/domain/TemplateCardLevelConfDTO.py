#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateCardLevelConfDTO(object):

    def __init__(self):
        self._level = None
        self._level_desc = None
        self._level_icon = None
        self._level_show_name = None

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def level_desc(self):
        return self._level_desc

    @level_desc.setter
    def level_desc(self, value):
        self._level_desc = value
    @property
    def level_icon(self):
        return self._level_icon

    @level_icon.setter
    def level_icon(self, value):
        self._level_icon = value
    @property
    def level_show_name(self):
        return self._level_show_name

    @level_show_name.setter
    def level_show_name(self, value):
        self._level_show_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.level_desc:
            if hasattr(self.level_desc, 'to_alipay_dict'):
                params['level_desc'] = self.level_desc.to_alipay_dict()
            else:
                params['level_desc'] = self.level_desc
        if self.level_icon:
            if hasattr(self.level_icon, 'to_alipay_dict'):
                params['level_icon'] = self.level_icon.to_alipay_dict()
            else:
                params['level_icon'] = self.level_icon
        if self.level_show_name:
            if hasattr(self.level_show_name, 'to_alipay_dict'):
                params['level_show_name'] = self.level_show_name.to_alipay_dict()
            else:
                params['level_show_name'] = self.level_show_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateCardLevelConfDTO()
        if 'level' in d:
            o.level = d['level']
        if 'level_desc' in d:
            o.level_desc = d['level_desc']
        if 'level_icon' in d:
            o.level_icon = d['level_icon']
        if 'level_show_name' in d:
            o.level_show_name = d['level_show_name']
        return o


