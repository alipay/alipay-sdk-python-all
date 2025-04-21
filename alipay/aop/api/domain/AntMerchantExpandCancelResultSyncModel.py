#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandCancelResultSyncModel(object):

    def __init__(self):
        self._batch_no = None
        self._order_id = None
        self._status = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        if isinstance(value, list):
            self._order_id = list()
            for i in value:
                self._order_id.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.order_id:
            if isinstance(self.order_id, list):
                for i in range(0, len(self.order_id)):
                    element = self.order_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_id[i] = element.to_alipay_dict()
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
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
        o = AntMerchantExpandCancelResultSyncModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'status' in d:
            o.status = d['status']
        return o


