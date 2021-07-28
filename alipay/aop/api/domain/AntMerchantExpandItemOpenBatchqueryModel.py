#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandItemOpenBatchqueryModel(object):

    def __init__(self):
        self._item_id_list = None

    @property
    def item_id_list(self):
        return self._item_id_list

    @item_id_list.setter
    def item_id_list(self, value):
        if isinstance(value, list):
            self._item_id_list = list()
            for i in value:
                self._item_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.item_id_list:
            if isinstance(self.item_id_list, list):
                for i in range(0, len(self.item_id_list)):
                    element = self.item_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_id_list[i] = element.to_alipay_dict()
            if hasattr(self.item_id_list, 'to_alipay_dict'):
                params['item_id_list'] = self.item_id_list.to_alipay_dict()
            else:
                params['item_id_list'] = self.item_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandItemOpenBatchqueryModel()
        if 'item_id_list' in d:
            o.item_id_list = d['item_id_list']
        return o


