#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BoxDetail(object):

    def __init__(self):
        self._biz_id = None
        self._block_type = None
        self._box_version = None
        self._desc = None
        self._img = None
        self._index = None
        self._material_id = None
        self._name = None
        self._service_code = None
        self._sub_service_code = None
        self._url = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def block_type(self):
        return self._block_type

    @block_type.setter
    def block_type(self, value):
        self._block_type = value
    @property
    def box_version(self):
        return self._box_version

    @box_version.setter
    def box_version(self, value):
        self._box_version = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        self._img = value
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value
    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def sub_service_code(self):
        return self._sub_service_code

    @sub_service_code.setter
    def sub_service_code(self, value):
        self._sub_service_code = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.block_type:
            if hasattr(self.block_type, 'to_alipay_dict'):
                params['block_type'] = self.block_type.to_alipay_dict()
            else:
                params['block_type'] = self.block_type
        if self.box_version:
            if hasattr(self.box_version, 'to_alipay_dict'):
                params['box_version'] = self.box_version.to_alipay_dict()
            else:
                params['box_version'] = self.box_version
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.img:
            if hasattr(self.img, 'to_alipay_dict'):
                params['img'] = self.img.to_alipay_dict()
            else:
                params['img'] = self.img
        if self.index:
            if hasattr(self.index, 'to_alipay_dict'):
                params['index'] = self.index.to_alipay_dict()
            else:
                params['index'] = self.index
        if self.material_id:
            if hasattr(self.material_id, 'to_alipay_dict'):
                params['material_id'] = self.material_id.to_alipay_dict()
            else:
                params['material_id'] = self.material_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.sub_service_code:
            if hasattr(self.sub_service_code, 'to_alipay_dict'):
                params['sub_service_code'] = self.sub_service_code.to_alipay_dict()
            else:
                params['sub_service_code'] = self.sub_service_code
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BoxDetail()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'block_type' in d:
            o.block_type = d['block_type']
        if 'box_version' in d:
            o.box_version = d['box_version']
        if 'desc' in d:
            o.desc = d['desc']
        if 'img' in d:
            o.img = d['img']
        if 'index' in d:
            o.index = d['index']
        if 'material_id' in d:
            o.material_id = d['material_id']
        if 'name' in d:
            o.name = d['name']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'sub_service_code' in d:
            o.sub_service_code = d['sub_service_code']
        if 'url' in d:
            o.url = d['url']
        return o


