#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderDataSyncRequest import OrderDataSyncRequest


class AlipayCommerceMerchantcardOrderSyncModel(object):

    def __init__(self):
        self._batch_id = None
        self._order_data_list = None
        self._sync_type = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def order_data_list(self):
        return self._order_data_list

    @order_data_list.setter
    def order_data_list(self, value):
        if isinstance(value, list):
            self._order_data_list = list()
            for i in value:
                if isinstance(i, OrderDataSyncRequest):
                    self._order_data_list.append(i)
                else:
                    self._order_data_list.append(OrderDataSyncRequest.from_alipay_dict(i))
    @property
    def sync_type(self):
        return self._sync_type

    @sync_type.setter
    def sync_type(self, value):
        self._sync_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.order_data_list:
            if isinstance(self.order_data_list, list):
                for i in range(0, len(self.order_data_list)):
                    element = self.order_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_data_list[i] = element.to_alipay_dict()
            if hasattr(self.order_data_list, 'to_alipay_dict'):
                params['order_data_list'] = self.order_data_list.to_alipay_dict()
            else:
                params['order_data_list'] = self.order_data_list
        if self.sync_type:
            if hasattr(self.sync_type, 'to_alipay_dict'):
                params['sync_type'] = self.sync_type.to_alipay_dict()
            else:
                params['sync_type'] = self.sync_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardOrderSyncModel()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'order_data_list' in d:
            o.order_data_list = d['order_data_list']
        if 'sync_type' in d:
            o.sync_type = d['sync_type']
        return o


