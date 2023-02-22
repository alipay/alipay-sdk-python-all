#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LmModifySkuList import LmModifySkuList


class LmModifyItemList(object):

    def __init__(self):
        self._can_sell = None
        self._ext_json = None
        self._gmt_modified = None
        self._item_id = None
        self._lm_item_id = None
        self._sku_list = None

    @property
    def can_sell(self):
        return self._can_sell

    @can_sell.setter
    def can_sell(self, value):
        self._can_sell = value
    @property
    def ext_json(self):
        return self._ext_json

    @ext_json.setter
    def ext_json(self, value):
        self._ext_json = value
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
    def sku_list(self):
        return self._sku_list

    @sku_list.setter
    def sku_list(self, value):
        if isinstance(value, list):
            self._sku_list = list()
            for i in value:
                if isinstance(i, LmModifySkuList):
                    self._sku_list.append(i)
                else:
                    self._sku_list.append(LmModifySkuList.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.can_sell:
            if hasattr(self.can_sell, 'to_alipay_dict'):
                params['can_sell'] = self.can_sell.to_alipay_dict()
            else:
                params['can_sell'] = self.can_sell
        if self.ext_json:
            if hasattr(self.ext_json, 'to_alipay_dict'):
                params['ext_json'] = self.ext_json.to_alipay_dict()
            else:
                params['ext_json'] = self.ext_json
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
        if self.sku_list:
            if isinstance(self.sku_list, list):
                for i in range(0, len(self.sku_list)):
                    element = self.sku_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_list, 'to_alipay_dict'):
                params['sku_list'] = self.sku_list.to_alipay_dict()
            else:
                params['sku_list'] = self.sku_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LmModifyItemList()
        if 'can_sell' in d:
            o.can_sell = d['can_sell']
        if 'ext_json' in d:
            o.ext_json = d['ext_json']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'lm_item_id' in d:
            o.lm_item_id = d['lm_item_id']
        if 'sku_list' in d:
            o.sku_list = d['sku_list']
        return o


