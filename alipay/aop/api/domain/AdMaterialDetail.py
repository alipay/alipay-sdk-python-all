#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdMaterialDetail(object):

    def __init__(self):
        self._duration = None
        self._height = None
        self._material_type = None
        self._material_value = None
        self._size = None
        self._source = None
        self._status = None
        self._upload_time = None
        self._user_material_lib_id = None
        self._width = None

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value
    @property
    def material_value(self):
        return self._material_value

    @material_value.setter
    def material_value(self, value):
        self._material_value = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def upload_time(self):
        return self._upload_time

    @upload_time.setter
    def upload_time(self, value):
        self._upload_time = value
    @property
    def user_material_lib_id(self):
        return self._user_material_lib_id

    @user_material_lib_id.setter
    def user_material_lib_id(self, value):
        self._user_material_lib_id = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.duration:
            if hasattr(self.duration, 'to_alipay_dict'):
                params['duration'] = self.duration.to_alipay_dict()
            else:
                params['duration'] = self.duration
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.material_type:
            if hasattr(self.material_type, 'to_alipay_dict'):
                params['material_type'] = self.material_type.to_alipay_dict()
            else:
                params['material_type'] = self.material_type
        if self.material_value:
            if hasattr(self.material_value, 'to_alipay_dict'):
                params['material_value'] = self.material_value.to_alipay_dict()
            else:
                params['material_value'] = self.material_value
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.upload_time:
            if hasattr(self.upload_time, 'to_alipay_dict'):
                params['upload_time'] = self.upload_time.to_alipay_dict()
            else:
                params['upload_time'] = self.upload_time
        if self.user_material_lib_id:
            if hasattr(self.user_material_lib_id, 'to_alipay_dict'):
                params['user_material_lib_id'] = self.user_material_lib_id.to_alipay_dict()
            else:
                params['user_material_lib_id'] = self.user_material_lib_id
        if self.width:
            if hasattr(self.width, 'to_alipay_dict'):
                params['width'] = self.width.to_alipay_dict()
            else:
                params['width'] = self.width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdMaterialDetail()
        if 'duration' in d:
            o.duration = d['duration']
        if 'height' in d:
            o.height = d['height']
        if 'material_type' in d:
            o.material_type = d['material_type']
        if 'material_value' in d:
            o.material_value = d['material_value']
        if 'size' in d:
            o.size = d['size']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        if 'upload_time' in d:
            o.upload_time = d['upload_time']
        if 'user_material_lib_id' in d:
            o.user_material_lib_id = d['user_material_lib_id']
        if 'width' in d:
            o.width = d['width']
        return o


