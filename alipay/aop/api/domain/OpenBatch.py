#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenBatch(object):

    def __init__(self):
        self._batch_id = None
        self._batch_status = None
        self._item_num = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def batch_status(self):
        return self._batch_status

    @batch_status.setter
    def batch_status(self, value):
        self._batch_status = value
    @property
    def item_num(self):
        return self._item_num

    @item_num.setter
    def item_num(self, value):
        self._item_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.batch_status:
            if hasattr(self.batch_status, 'to_alipay_dict'):
                params['batch_status'] = self.batch_status.to_alipay_dict()
            else:
                params['batch_status'] = self.batch_status
        if self.item_num:
            if hasattr(self.item_num, 'to_alipay_dict'):
                params['item_num'] = self.item_num.to_alipay_dict()
            else:
                params['item_num'] = self.item_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenBatch()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'batch_status' in d:
            o.batch_status = d['batch_status']
        if 'item_num' in d:
            o.item_num = d['item_num']
        return o


