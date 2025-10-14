#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemStatusUpdateByIsvItemIdParam import ItemStatusUpdateByIsvItemIdParam


class AlipayCommerceMedicalItemstatusByisvitemidModifyModel(object):

    def __init__(self):
        self._isv_store_code = None
        self._item_status_list = None

    @property
    def isv_store_code(self):
        return self._isv_store_code

    @isv_store_code.setter
    def isv_store_code(self, value):
        self._isv_store_code = value
    @property
    def item_status_list(self):
        return self._item_status_list

    @item_status_list.setter
    def item_status_list(self, value):
        if isinstance(value, list):
            self._item_status_list = list()
            for i in value:
                if isinstance(i, ItemStatusUpdateByIsvItemIdParam):
                    self._item_status_list.append(i)
                else:
                    self._item_status_list.append(ItemStatusUpdateByIsvItemIdParam.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.isv_store_code:
            if hasattr(self.isv_store_code, 'to_alipay_dict'):
                params['isv_store_code'] = self.isv_store_code.to_alipay_dict()
            else:
                params['isv_store_code'] = self.isv_store_code
        if self.item_status_list:
            if isinstance(self.item_status_list, list):
                for i in range(0, len(self.item_status_list)):
                    element = self.item_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_status_list[i] = element.to_alipay_dict()
            if hasattr(self.item_status_list, 'to_alipay_dict'):
                params['item_status_list'] = self.item_status_list.to_alipay_dict()
            else:
                params['item_status_list'] = self.item_status_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalItemstatusByisvitemidModifyModel()
        if 'isv_store_code' in d:
            o.isv_store_code = d['isv_store_code']
        if 'item_status_list' in d:
            o.item_status_list = d['item_status_list']
        return o


