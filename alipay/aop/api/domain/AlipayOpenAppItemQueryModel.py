#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppItemQueryModel(object):

    def __init__(self):
        self._item_id = None
        self._need_edit_spu = None
        self._out_item_id = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def need_edit_spu(self):
        return self._need_edit_spu

    @need_edit_spu.setter
    def need_edit_spu(self, value):
        self._need_edit_spu = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.need_edit_spu:
            if hasattr(self.need_edit_spu, 'to_alipay_dict'):
                params['need_edit_spu'] = self.need_edit_spu.to_alipay_dict()
            else:
                params['need_edit_spu'] = self.need_edit_spu
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
        o = AlipayOpenAppItemQueryModel()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'need_edit_spu' in d:
            o.need_edit_spu = d['need_edit_spu']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        return o


