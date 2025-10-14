#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IsvItemIdItemPriceFailDTO(object):

    def __init__(self):
        self._desc = None
        self._isv_item_id = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def isv_item_id(self):
        return self._isv_item_id

    @isv_item_id.setter
    def isv_item_id(self, value):
        self._isv_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.isv_item_id:
            if hasattr(self.isv_item_id, 'to_alipay_dict'):
                params['isv_item_id'] = self.isv_item_id.to_alipay_dict()
            else:
                params['isv_item_id'] = self.isv_item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IsvItemIdItemPriceFailDTO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'isv_item_id' in d:
            o.isv_item_id = d['isv_item_id']
        return o


