#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfAttachQueryModel(object):

    def __init__(self):
        self._attachment_id = None
        self._biz_type = None
        self._expire_time = None
        self._file_path = None
        self._height = None
        self._img_format = None
        self._width = None

    @property
    def attachment_id(self):
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, value):
        self._attachment_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def img_format(self):
        return self._img_format

    @img_format.setter
    def img_format(self, value):
        self._img_format = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_id:
            if hasattr(self.attachment_id, 'to_alipay_dict'):
                params['attachment_id'] = self.attachment_id.to_alipay_dict()
            else:
                params['attachment_id'] = self.attachment_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.file_path:
            if hasattr(self.file_path, 'to_alipay_dict'):
                params['file_path'] = self.file_path.to_alipay_dict()
            else:
                params['file_path'] = self.file_path
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.img_format:
            if hasattr(self.img_format, 'to_alipay_dict'):
                params['img_format'] = self.img_format.to_alipay_dict()
            else:
                params['img_format'] = self.img_format
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
        o = AlipayCommerceMedicalHdfAttachQueryModel()
        if 'attachment_id' in d:
            o.attachment_id = d['attachment_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'file_path' in d:
            o.file_path = d['file_path']
        if 'height' in d:
            o.height = d['height']
        if 'img_format' in d:
            o.img_format = d['img_format']
        if 'width' in d:
            o.width = d['width']
        return o


