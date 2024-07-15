#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemAttrVO import AppItemAttrVO


class AlipayOpenAppRoomrentModifyModel(object):

    def __init__(self):
        self._attrs = None
        self._category_id = None
        self._head_img = None
        self._out_item_id = None

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
    def head_img(self):
        return self._head_img

    @head_img.setter
    def head_img(self, value):
        self._head_img = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value


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
        if self.head_img:
            if hasattr(self.head_img, 'to_alipay_dict'):
                params['head_img'] = self.head_img.to_alipay_dict()
            else:
                params['head_img'] = self.head_img
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppRoomrentModifyModel()
        if 'attrs' in d:
            o.attrs = d['attrs']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'head_img' in d:
            o.head_img = d['head_img']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        return o


