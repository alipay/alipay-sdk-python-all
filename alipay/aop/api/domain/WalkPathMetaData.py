#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WalkPathMetaData(object):

    def __init__(self):
        self._group_id = None
        self._path_id = None
        self._path_length = None
        self._path_step_count = None
        self._str_path_length = None
        self._title = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def path_id(self):
        return self._path_id

    @path_id.setter
    def path_id(self, value):
        self._path_id = value
    @property
    def path_length(self):
        return self._path_length

    @path_length.setter
    def path_length(self, value):
        self._path_length = value
    @property
    def path_step_count(self):
        return self._path_step_count

    @path_step_count.setter
    def path_step_count(self, value):
        self._path_step_count = value
    @property
    def str_path_length(self):
        return self._str_path_length

    @str_path_length.setter
    def str_path_length(self, value):
        self._str_path_length = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.path_id:
            if hasattr(self.path_id, 'to_alipay_dict'):
                params['path_id'] = self.path_id.to_alipay_dict()
            else:
                params['path_id'] = self.path_id
        if self.path_length:
            if hasattr(self.path_length, 'to_alipay_dict'):
                params['path_length'] = self.path_length.to_alipay_dict()
            else:
                params['path_length'] = self.path_length
        if self.path_step_count:
            if hasattr(self.path_step_count, 'to_alipay_dict'):
                params['path_step_count'] = self.path_step_count.to_alipay_dict()
            else:
                params['path_step_count'] = self.path_step_count
        if self.str_path_length:
            if hasattr(self.str_path_length, 'to_alipay_dict'):
                params['str_path_length'] = self.str_path_length.to_alipay_dict()
            else:
                params['str_path_length'] = self.str_path_length
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WalkPathMetaData()
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'path_id' in d:
            o.path_id = d['path_id']
        if 'path_length' in d:
            o.path_length = d['path_length']
        if 'path_step_count' in d:
            o.path_step_count = d['path_step_count']
        if 'str_path_length' in d:
            o.str_path_length = d['str_path_length']
        if 'title' in d:
            o.title = d['title']
        return o


