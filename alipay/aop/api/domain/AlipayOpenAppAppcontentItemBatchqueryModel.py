#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppAppcontentItemBatchqueryModel(object):

    def __init__(self):
        self._item_ids = None

    @property
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, value):
        if isinstance(value, list):
            self._item_ids = list()
            for i in value:
                self._item_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.item_ids:
            if isinstance(self.item_ids, list):
                for i in range(0, len(self.item_ids)):
                    element = self.item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_ids[i] = element.to_alipay_dict()
            if hasattr(self.item_ids, 'to_alipay_dict'):
                params['item_ids'] = self.item_ids.to_alipay_dict()
            else:
                params['item_ids'] = self.item_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppAppcontentItemBatchqueryModel()
        if 'item_ids' in d:
            o.item_ids = d['item_ids']
        return o


