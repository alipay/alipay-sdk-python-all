#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MaterialResultInfo(object):

    def __init__(self):
        self._item_id = None
        self._result_img = None
        self._status = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def result_img(self):
        return self._result_img

    @result_img.setter
    def result_img(self, value):
        self._result_img = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.result_img:
            if hasattr(self.result_img, 'to_alipay_dict'):
                params['result_img'] = self.result_img.to_alipay_dict()
            else:
                params['result_img'] = self.result_img
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MaterialResultInfo()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'result_img' in d:
            o.result_img = d['result_img']
        if 'status' in d:
            o.status = d['status']
        return o


