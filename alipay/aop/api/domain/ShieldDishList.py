#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShieldDishList(object):

    def __init__(self):
        self._dish_id = None
        self._ext_infos = None
        self._num = None
        self._sku_id = None

    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShieldDishList()
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'num' in d:
            o.num = d['num']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


