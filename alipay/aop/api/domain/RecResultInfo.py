#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecItemInfo import RecItemInfo


class RecResultInfo(object):

    def __init__(self):
        self._code = None
        self._items = None
        self._msg = None
        self._position_id = None
        self._success = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, RecItemInfo):
                    self._items.append(i)
                else:
                    self._items.append(RecItemInfo.from_alipay_dict(i))
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def position_id(self):
        return self._position_id

    @position_id.setter
    def position_id(self, value):
        self._position_id = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
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
        if self.msg:
            if hasattr(self.msg, 'to_alipay_dict'):
                params['msg'] = self.msg.to_alipay_dict()
            else:
                params['msg'] = self.msg
        if self.position_id:
            if hasattr(self.position_id, 'to_alipay_dict'):
                params['position_id'] = self.position_id.to_alipay_dict()
            else:
                params['position_id'] = self.position_id
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecResultInfo()
        if 'code' in d:
            o.code = d['code']
        if 'items' in d:
            o.items = d['items']
        if 'msg' in d:
            o.msg = d['msg']
        if 'position_id' in d:
            o.position_id = d['position_id']
        if 'success' in d:
            o.success = d['success']
        return o


