#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntbookcontentVolumeSyncModel(object):

    def __init__(self):
        self._book_id = None
        self._create_time = None
        self._name = None
        self._operate_type = None
        self._sort_no = None
        self._update_time = None
        self._volume_id = None

    @property
    def book_id(self):
        return self._book_id

    @book_id.setter
    def book_id(self, value):
        self._book_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def sort_no(self):
        return self._sort_no

    @sort_no.setter
    def sort_no(self, value):
        self._sort_no = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def volume_id(self):
        return self._volume_id

    @volume_id.setter
    def volume_id(self, value):
        self._volume_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.book_id:
            if hasattr(self.book_id, 'to_alipay_dict'):
                params['book_id'] = self.book_id.to_alipay_dict()
            else:
                params['book_id'] = self.book_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.sort_no:
            if hasattr(self.sort_no, 'to_alipay_dict'):
                params['sort_no'] = self.sort_no.to_alipay_dict()
            else:
                params['sort_no'] = self.sort_no
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        if self.volume_id:
            if hasattr(self.volume_id, 'to_alipay_dict'):
                params['volume_id'] = self.volume_id.to_alipay_dict()
            else:
                params['volume_id'] = self.volume_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntbookcontentVolumeSyncModel()
        if 'book_id' in d:
            o.book_id = d['book_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'name' in d:
            o.name = d['name']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'sort_no' in d:
            o.sort_no = d['sort_no']
        if 'update_time' in d:
            o.update_time = d['update_time']
        if 'volume_id' in d:
            o.volume_id = d['volume_id']
        return o


