#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnswerModel(object):

    def __init__(self):
        self._extra = None
        self._item_id = None
        self._option_id = None

    @property
    def extra(self):
        return self._extra

    @extra.setter
    def extra(self, value):
        self._extra = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def option_id(self):
        return self._option_id

    @option_id.setter
    def option_id(self, value):
        self._option_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.extra:
            if hasattr(self.extra, 'to_alipay_dict'):
                params['extra'] = self.extra.to_alipay_dict()
            else:
                params['extra'] = self.extra
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.option_id:
            if hasattr(self.option_id, 'to_alipay_dict'):
                params['option_id'] = self.option_id.to_alipay_dict()
            else:
                params['option_id'] = self.option_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnswerModel()
        if 'extra' in d:
            o.extra = d['extra']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'option_id' in d:
            o.option_id = d['option_id']
        return o


