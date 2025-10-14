#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemStatusUpdateByIsvItemIdParam(object):

    def __init__(self):
        self._isv_item_id = None
        self._status = None

    @property
    def isv_item_id(self):
        return self._isv_item_id

    @isv_item_id.setter
    def isv_item_id(self, value):
        self._isv_item_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_item_id:
            if hasattr(self.isv_item_id, 'to_alipay_dict'):
                params['isv_item_id'] = self.isv_item_id.to_alipay_dict()
            else:
                params['isv_item_id'] = self.isv_item_id
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
        o = ItemStatusUpdateByIsvItemIdParam()
        if 'isv_item_id' in d:
            o.isv_item_id = d['isv_item_id']
        if 'status' in d:
            o.status = d['status']
        return o


