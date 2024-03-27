#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ImageDirectoryVO(object):

    def __init__(self):
        self._create_time = None
        self._image_directory_id = None
        self._image_directory_name = None
        self._modify_time = None
        self._parent_directory_id = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def image_directory_id(self):
        return self._image_directory_id

    @image_directory_id.setter
    def image_directory_id(self, value):
        self._image_directory_id = value
    @property
    def image_directory_name(self):
        return self._image_directory_name

    @image_directory_name.setter
    def image_directory_name(self, value):
        self._image_directory_name = value
    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value
    @property
    def parent_directory_id(self):
        return self._parent_directory_id

    @parent_directory_id.setter
    def parent_directory_id(self, value):
        self._parent_directory_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.image_directory_id:
            if hasattr(self.image_directory_id, 'to_alipay_dict'):
                params['image_directory_id'] = self.image_directory_id.to_alipay_dict()
            else:
                params['image_directory_id'] = self.image_directory_id
        if self.image_directory_name:
            if hasattr(self.image_directory_name, 'to_alipay_dict'):
                params['image_directory_name'] = self.image_directory_name.to_alipay_dict()
            else:
                params['image_directory_name'] = self.image_directory_name
        if self.modify_time:
            if hasattr(self.modify_time, 'to_alipay_dict'):
                params['modify_time'] = self.modify_time.to_alipay_dict()
            else:
                params['modify_time'] = self.modify_time
        if self.parent_directory_id:
            if hasattr(self.parent_directory_id, 'to_alipay_dict'):
                params['parent_directory_id'] = self.parent_directory_id.to_alipay_dict()
            else:
                params['parent_directory_id'] = self.parent_directory_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ImageDirectoryVO()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'image_directory_id' in d:
            o.image_directory_id = d['image_directory_id']
        if 'image_directory_name' in d:
            o.image_directory_name = d['image_directory_name']
        if 'modify_time' in d:
            o.modify_time = d['modify_time']
        if 'parent_directory_id' in d:
            o.parent_directory_id = d['parent_directory_id']
        return o


