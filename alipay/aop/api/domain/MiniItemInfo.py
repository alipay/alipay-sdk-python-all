#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniItemInfo(object):

    def __init__(self):
        self._head_img_url = None
        self._item_id = None
        self._item_name = None
        self._item_type = None
        self._item_type_desc = None
        self._out_item_id = None

    @property
    def head_img_url(self):
        return self._head_img_url

    @head_img_url.setter
    def head_img_url(self, value):
        self._head_img_url = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def item_type_desc(self):
        return self._item_type_desc

    @item_type_desc.setter
    def item_type_desc(self, value):
        self._item_type_desc = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.head_img_url:
            if hasattr(self.head_img_url, 'to_alipay_dict'):
                params['head_img_url'] = self.head_img_url.to_alipay_dict()
            else:
                params['head_img_url'] = self.head_img_url
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.item_type_desc:
            if hasattr(self.item_type_desc, 'to_alipay_dict'):
                params['item_type_desc'] = self.item_type_desc.to_alipay_dict()
            else:
                params['item_type_desc'] = self.item_type_desc
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
        o = MiniItemInfo()
        if 'head_img_url' in d:
            o.head_img_url = d['head_img_url']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'item_type_desc' in d:
            o.item_type_desc = d['item_type_desc']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        return o


