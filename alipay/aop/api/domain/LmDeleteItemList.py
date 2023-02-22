#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LmDeleteItemList(object):

    def __init__(self):
        self._gmt_modified = None
        self._item_id = None
        self._lm_item_id = None
        self._sku_id_list = None

    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def lm_item_id(self):
        return self._lm_item_id

    @lm_item_id.setter
    def lm_item_id(self, value):
        self._lm_item_id = value
    @property
    def sku_id_list(self):
        return self._sku_id_list

    @sku_id_list.setter
    def sku_id_list(self, value):
        if isinstance(value, list):
            self._sku_id_list = list()
            for i in value:
                self._sku_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.lm_item_id:
            if hasattr(self.lm_item_id, 'to_alipay_dict'):
                params['lm_item_id'] = self.lm_item_id.to_alipay_dict()
            else:
                params['lm_item_id'] = self.lm_item_id
        if self.sku_id_list:
            if isinstance(self.sku_id_list, list):
                for i in range(0, len(self.sku_id_list)):
                    element = self.sku_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_id_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_id_list, 'to_alipay_dict'):
                params['sku_id_list'] = self.sku_id_list.to_alipay_dict()
            else:
                params['sku_id_list'] = self.sku_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LmDeleteItemList()
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'lm_item_id' in d:
            o.lm_item_id = d['lm_item_id']
        if 'sku_id_list' in d:
            o.sku_id_list = d['sku_id_list']
        return o


