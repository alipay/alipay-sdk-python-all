#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetReverseItemDetail(object):

    def __init__(self):
        self._count = None
        self._item_id = None
        self._sn_records = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def sn_records(self):
        return self._sn_records

    @sn_records.setter
    def sn_records(self, value):
        if isinstance(value, list):
            self._sn_records = list()
            for i in value:
                self._sn_records.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.sn_records:
            if isinstance(self.sn_records, list):
                for i in range(0, len(self.sn_records)):
                    element = self.sn_records[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sn_records[i] = element.to_alipay_dict()
            if hasattr(self.sn_records, 'to_alipay_dict'):
                params['sn_records'] = self.sn_records.to_alipay_dict()
            else:
                params['sn_records'] = self.sn_records
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetReverseItemDetail()
        if 'count' in d:
            o.count = d['count']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'sn_records' in d:
            o.sn_records = d['sn_records']
        return o


