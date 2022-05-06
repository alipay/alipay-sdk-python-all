#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShellCompanyGsChangeDetail(object):

    def __init__(self):
        self._after_content = None
        self._before_content = None
        self._change_type = None
        self._description = None
        self._title = None
        self._update_time = None

    @property
    def after_content(self):
        return self._after_content

    @after_content.setter
    def after_content(self, value):
        self._after_content = value
    @property
    def before_content(self):
        return self._before_content

    @before_content.setter
    def before_content(self, value):
        self._before_content = value
    @property
    def change_type(self):
        return self._change_type

    @change_type.setter
    def change_type(self, value):
        self._change_type = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.after_content:
            if hasattr(self.after_content, 'to_alipay_dict'):
                params['after_content'] = self.after_content.to_alipay_dict()
            else:
                params['after_content'] = self.after_content
        if self.before_content:
            if hasattr(self.before_content, 'to_alipay_dict'):
                params['before_content'] = self.before_content.to_alipay_dict()
            else:
                params['before_content'] = self.before_content
        if self.change_type:
            if hasattr(self.change_type, 'to_alipay_dict'):
                params['change_type'] = self.change_type.to_alipay_dict()
            else:
                params['change_type'] = self.change_type
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShellCompanyGsChangeDetail()
        if 'after_content' in d:
            o.after_content = d['after_content']
        if 'before_content' in d:
            o.before_content = d['before_content']
        if 'change_type' in d:
            o.change_type = d['change_type']
        if 'description' in d:
            o.description = d['description']
        if 'title' in d:
            o.title = d['title']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


