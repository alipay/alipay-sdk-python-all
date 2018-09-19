#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperatorChannelInfo(object):

    def __init__(self):
        self._item_code = None
        self._item_desc = None
        self._item_name = None
        self._item_status = None

    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def item_desc(self):
        return self._item_desc

    @item_desc.setter
    def item_desc(self, value):
        self._item_desc = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_status(self):
        return self._item_status

    @item_status.setter
    def item_status(self, value):
        self._item_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.item_desc:
            if hasattr(self.item_desc, 'to_alipay_dict'):
                params['item_desc'] = self.item_desc.to_alipay_dict()
            else:
                params['item_desc'] = self.item_desc
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_status:
            if hasattr(self.item_status, 'to_alipay_dict'):
                params['item_status'] = self.item_status.to_alipay_dict()
            else:
                params['item_status'] = self.item_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperatorChannelInfo()
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_desc' in d:
            o.item_desc = d['item_desc']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_status' in d:
            o.item_status = d['item_status']
        return o


