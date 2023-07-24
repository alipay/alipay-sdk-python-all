#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MallItemDtos import MallItemDtos


class MallMergeCartRequestDto(object):

    def __init__(self):
        self._app_code = None
        self._fix_user_id = None
        self._items = None
        self._order_id = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def fix_user_id(self):
        return self._fix_user_id

    @fix_user_id.setter
    def fix_user_id(self, value):
        self._fix_user_id = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, MallItemDtos):
                    self._items.append(i)
                else:
                    self._items.append(MallItemDtos.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.fix_user_id:
            if hasattr(self.fix_user_id, 'to_alipay_dict'):
                params['fix_user_id'] = self.fix_user_id.to_alipay_dict()
            else:
                params['fix_user_id'] = self.fix_user_id
        if self.items:
            if isinstance(self.items, list):
                for i in range(0, len(self.items)):
                    element = self.items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.items[i] = element.to_alipay_dict()
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MallMergeCartRequestDto()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'fix_user_id' in d:
            o.fix_user_id = d['fix_user_id']
        if 'items' in d:
            o.items = d['items']
        if 'order_id' in d:
            o.order_id = d['order_id']
        return o


