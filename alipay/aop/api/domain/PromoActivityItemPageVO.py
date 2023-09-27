#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoActivityItemPageVO(object):

    def __init__(self):
        self._discount_id = None
        self._is_online = None
        self._item_id = None
        self._out_item_id = None
        self._title = None

    @property
    def discount_id(self):
        return self._discount_id

    @discount_id.setter
    def discount_id(self, value):
        self._discount_id = value
    @property
    def is_online(self):
        return self._is_online

    @is_online.setter
    def is_online(self, value):
        self._is_online = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_id:
            if hasattr(self.discount_id, 'to_alipay_dict'):
                params['discount_id'] = self.discount_id.to_alipay_dict()
            else:
                params['discount_id'] = self.discount_id
        if self.is_online:
            if hasattr(self.is_online, 'to_alipay_dict'):
                params['is_online'] = self.is_online.to_alipay_dict()
            else:
                params['is_online'] = self.is_online
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoActivityItemPageVO()
        if 'discount_id' in d:
            o.discount_id = d['discount_id']
        if 'is_online' in d:
            o.is_online = d['is_online']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'title' in d:
            o.title = d['title']
        return o


