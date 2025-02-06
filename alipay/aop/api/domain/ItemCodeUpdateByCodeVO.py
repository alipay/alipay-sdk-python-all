#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemCodeUpdateByCodeVO(object):

    def __init__(self):
        self._source_item_code = None
        self._target_item_code = None

    @property
    def source_item_code(self):
        return self._source_item_code

    @source_item_code.setter
    def source_item_code(self, value):
        self._source_item_code = value
    @property
    def target_item_code(self):
        return self._target_item_code

    @target_item_code.setter
    def target_item_code(self, value):
        self._target_item_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.source_item_code:
            if hasattr(self.source_item_code, 'to_alipay_dict'):
                params['source_item_code'] = self.source_item_code.to_alipay_dict()
            else:
                params['source_item_code'] = self.source_item_code
        if self.target_item_code:
            if hasattr(self.target_item_code, 'to_alipay_dict'):
                params['target_item_code'] = self.target_item_code.to_alipay_dict()
            else:
                params['target_item_code'] = self.target_item_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemCodeUpdateByCodeVO()
        if 'source_item_code' in d:
            o.source_item_code = d['source_item_code']
        if 'target_item_code' in d:
            o.target_item_code = d['target_item_code']
        return o


