#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfAttachBatchqueryModel(object):

    def __init__(self):
        self._attachment_id_list = None
        self._auth_params = None
        self._auth_way = None
        self._biz = None
        self._biz_type = None
        self._expire_time = None
        self._file_path = None
        self._height = None
        self._img_format = None
        self._owner_id = None
        self._patient_attachment_id_list = None
        self._pic_params = None
        self._size_type = None
        self._width = None

    @property
    def attachment_id_list(self):
        return self._attachment_id_list

    @attachment_id_list.setter
    def attachment_id_list(self, value):
        if isinstance(value, list):
            self._attachment_id_list = list()
            for i in value:
                self._attachment_id_list.append(i)
    @property
    def auth_params(self):
        return self._auth_params

    @auth_params.setter
    def auth_params(self, value):
        self._auth_params = value
    @property
    def auth_way(self):
        return self._auth_way

    @auth_way.setter
    def auth_way(self, value):
        self._auth_way = value
    @property
    def biz(self):
        return self._biz

    @biz.setter
    def biz(self, value):
        self._biz = value
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
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def patient_attachment_id_list(self):
        return self._patient_attachment_id_list

    @patient_attachment_id_list.setter
    def patient_attachment_id_list(self, value):
        if isinstance(value, list):
            self._patient_attachment_id_list = list()
            for i in value:
                self._patient_attachment_id_list.append(i)
    @property
    def pic_params(self):
        return self._pic_params

    @pic_params.setter
    def pic_params(self, value):
        self._pic_params = value
    @property
    def size_type(self):
        return self._size_type

    @size_type.setter
    def size_type(self, value):
        self._size_type = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_id_list:
            if isinstance(self.attachment_id_list, list):
                for i in range(0, len(self.attachment_id_list)):
                    element = self.attachment_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachment_id_list[i] = element.to_alipay_dict()
            if hasattr(self.attachment_id_list, 'to_alipay_dict'):
                params['attachment_id_list'] = self.attachment_id_list.to_alipay_dict()
            else:
                params['attachment_id_list'] = self.attachment_id_list
        if self.auth_params:
            if hasattr(self.auth_params, 'to_alipay_dict'):
                params['auth_params'] = self.auth_params.to_alipay_dict()
            else:
                params['auth_params'] = self.auth_params
        if self.auth_way:
            if hasattr(self.auth_way, 'to_alipay_dict'):
                params['auth_way'] = self.auth_way.to_alipay_dict()
            else:
                params['auth_way'] = self.auth_way
        if self.biz:
            if hasattr(self.biz, 'to_alipay_dict'):
                params['biz'] = self.biz.to_alipay_dict()
            else:
                params['biz'] = self.biz
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
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.patient_attachment_id_list:
            if isinstance(self.patient_attachment_id_list, list):
                for i in range(0, len(self.patient_attachment_id_list)):
                    element = self.patient_attachment_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.patient_attachment_id_list[i] = element.to_alipay_dict()
            if hasattr(self.patient_attachment_id_list, 'to_alipay_dict'):
                params['patient_attachment_id_list'] = self.patient_attachment_id_list.to_alipay_dict()
            else:
                params['patient_attachment_id_list'] = self.patient_attachment_id_list
        if self.pic_params:
            if hasattr(self.pic_params, 'to_alipay_dict'):
                params['pic_params'] = self.pic_params.to_alipay_dict()
            else:
                params['pic_params'] = self.pic_params
        if self.size_type:
            if hasattr(self.size_type, 'to_alipay_dict'):
                params['size_type'] = self.size_type.to_alipay_dict()
            else:
                params['size_type'] = self.size_type
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
        o = AlipayCommerceMedicalHdfAttachBatchqueryModel()
        if 'attachment_id_list' in d:
            o.attachment_id_list = d['attachment_id_list']
        if 'auth_params' in d:
            o.auth_params = d['auth_params']
        if 'auth_way' in d:
            o.auth_way = d['auth_way']
        if 'biz' in d:
            o.biz = d['biz']
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
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'patient_attachment_id_list' in d:
            o.patient_attachment_id_list = d['patient_attachment_id_list']
        if 'pic_params' in d:
            o.pic_params = d['pic_params']
        if 'size_type' in d:
            o.size_type = d['size_type']
        if 'width' in d:
            o.width = d['width']
        return o


