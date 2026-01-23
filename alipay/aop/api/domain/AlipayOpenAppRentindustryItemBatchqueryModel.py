#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppRentindustryItemBatchqueryModel(object):

    def __init__(self):
        self._out_item_ids = None

    @property
    def out_item_ids(self):
        return self._out_item_ids

    @out_item_ids.setter
    def out_item_ids(self, value):
        if isinstance(value, list):
            self._out_item_ids = list()
            for i in value:
                self._out_item_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.out_item_ids:
            if isinstance(self.out_item_ids, list):
                for i in range(0, len(self.out_item_ids)):
                    element = self.out_item_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_item_ids[i] = element.to_alipay_dict()
            if hasattr(self.out_item_ids, 'to_alipay_dict'):
                params['out_item_ids'] = self.out_item_ids.to_alipay_dict()
            else:
                params['out_item_ids'] = self.out_item_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppRentindustryItemBatchqueryModel()
        if 'out_item_ids' in d:
            o.out_item_ids = d['out_item_ids']
        return o


