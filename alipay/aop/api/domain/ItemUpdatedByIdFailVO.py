#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemUpdatedByIdFailVO(object):

    def __init__(self):
        self._desc = None
        self._source_item_id = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def source_item_id(self):
        return self._source_item_id

    @source_item_id.setter
    def source_item_id(self, value):
        self._source_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.source_item_id:
            if hasattr(self.source_item_id, 'to_alipay_dict'):
                params['source_item_id'] = self.source_item_id.to_alipay_dict()
            else:
                params['source_item_id'] = self.source_item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemUpdatedByIdFailVO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'source_item_id' in d:
            o.source_item_id = d['source_item_id']
        return o


