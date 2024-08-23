#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TransferCarUpdateData(object):

    def __init__(self):
        self._isv_update_date = None
        self._out_id = None
        self._price = None
        self._status = None

    @property
    def isv_update_date(self):
        return self._isv_update_date

    @isv_update_date.setter
    def isv_update_date(self, value):
        self._isv_update_date = value
    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_update_date:
            if hasattr(self.isv_update_date, 'to_alipay_dict'):
                params['isv_update_date'] = self.isv_update_date.to_alipay_dict()
            else:
                params['isv_update_date'] = self.isv_update_date
        if self.out_id:
            if hasattr(self.out_id, 'to_alipay_dict'):
                params['out_id'] = self.out_id.to_alipay_dict()
            else:
                params['out_id'] = self.out_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
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
        o = TransferCarUpdateData()
        if 'isv_update_date' in d:
            o.isv_update_date = d['isv_update_date']
        if 'out_id' in d:
            o.out_id = d['out_id']
        if 'price' in d:
            o.price = d['price']
        if 'status' in d:
            o.status = d['status']
        return o


