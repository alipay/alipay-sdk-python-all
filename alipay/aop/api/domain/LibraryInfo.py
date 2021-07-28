#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LibraryInfo(object):

    def __init__(self):
        self._id = None
        self._name = None
        self._tree_id = None
        self._update_time = None

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
    def tree_id(self):
        return self._tree_id

    @tree_id.setter
    def tree_id(self, value):
        self._tree_id = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.tree_id:
            if hasattr(self.tree_id, 'to_alipay_dict'):
                params['tree_id'] = self.tree_id.to_alipay_dict()
            else:
                params['tree_id'] = self.tree_id
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
        o = LibraryInfo()
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'tree_id' in d:
            o.tree_id = d['tree_id']
        if 'update_time' in d:
            o.update_time = d['update_time']
        return o


