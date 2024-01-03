#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemAttrVO import AppItemAttrVO


class AlipayOpenAppLocalitemSpuSaveModel(object):

    def __init__(self):
        self._attrs = None
        self._category_id = None
        self._item_type = None
        self._out_spu_id = None
        self._spu_id = None
        self._spu_name = None
        self._spu_status = None

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        if isinstance(value, list):
            self._attrs = list()
            for i in value:
                if isinstance(i, AppItemAttrVO):
                    self._attrs.append(i)
                else:
                    self._attrs.append(AppItemAttrVO.from_alipay_dict(i))
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def out_spu_id(self):
        return self._out_spu_id

    @out_spu_id.setter
    def out_spu_id(self, value):
        self._out_spu_id = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value
    @property
    def spu_name(self):
        return self._spu_name

    @spu_name.setter
    def spu_name(self, value):
        self._spu_name = value
    @property
    def spu_status(self):
        return self._spu_status

    @spu_status.setter
    def spu_status(self, value):
        self._spu_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.attrs:
            if isinstance(self.attrs, list):
                for i in range(0, len(self.attrs)):
                    element = self.attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attrs[i] = element.to_alipay_dict()
            if hasattr(self.attrs, 'to_alipay_dict'):
                params['attrs'] = self.attrs.to_alipay_dict()
            else:
                params['attrs'] = self.attrs
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.out_spu_id:
            if hasattr(self.out_spu_id, 'to_alipay_dict'):
                params['out_spu_id'] = self.out_spu_id.to_alipay_dict()
            else:
                params['out_spu_id'] = self.out_spu_id
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        if self.spu_name:
            if hasattr(self.spu_name, 'to_alipay_dict'):
                params['spu_name'] = self.spu_name.to_alipay_dict()
            else:
                params['spu_name'] = self.spu_name
        if self.spu_status:
            if hasattr(self.spu_status, 'to_alipay_dict'):
                params['spu_status'] = self.spu_status.to_alipay_dict()
            else:
                params['spu_status'] = self.spu_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppLocalitemSpuSaveModel()
        if 'attrs' in d:
            o.attrs = d['attrs']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'out_spu_id' in d:
            o.out_spu_id = d['out_spu_id']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'spu_name' in d:
            o.spu_name = d['spu_name']
        if 'spu_status' in d:
            o.spu_status = d['spu_status']
        return o


