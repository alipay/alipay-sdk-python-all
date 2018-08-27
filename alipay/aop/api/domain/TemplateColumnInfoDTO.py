#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MoreInfoDTO import MoreInfoDTO


class TemplateColumnInfoDTO(object):

    def __init__(self):
        self._code = None
        self._group_title = None
        self._icon_id = None
        self._more_info = None
        self._operate_type = None
        self._tag = None
        self._title = None
        self._value = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def group_title(self):
        return self._group_title

    @group_title.setter
    def group_title(self, value):
        self._group_title = value
    @property
    def icon_id(self):
        return self._icon_id

    @icon_id.setter
    def icon_id(self, value):
        self._icon_id = value
    @property
    def more_info(self):
        return self._more_info

    @more_info.setter
    def more_info(self, value):
        if isinstance(value, MoreInfoDTO):
            self._more_info = value
        else:
            self._more_info = MoreInfoDTO.from_alipay_dict(value)
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.group_title:
            if hasattr(self.group_title, 'to_alipay_dict'):
                params['group_title'] = self.group_title.to_alipay_dict()
            else:
                params['group_title'] = self.group_title
        if self.icon_id:
            if hasattr(self.icon_id, 'to_alipay_dict'):
                params['icon_id'] = self.icon_id.to_alipay_dict()
            else:
                params['icon_id'] = self.icon_id
        if self.more_info:
            if hasattr(self.more_info, 'to_alipay_dict'):
                params['more_info'] = self.more_info.to_alipay_dict()
            else:
                params['more_info'] = self.more_info
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateColumnInfoDTO()
        if 'code' in d:
            o.code = d['code']
        if 'group_title' in d:
            o.group_title = d['group_title']
        if 'icon_id' in d:
            o.icon_id = d['icon_id']
        if 'more_info' in d:
            o.more_info = d['more_info']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'tag' in d:
            o.tag = d['tag']
        if 'title' in d:
            o.title = d['title']
        if 'value' in d:
            o.value = d['value']
        return o


