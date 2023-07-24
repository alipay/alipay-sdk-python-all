#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LeasePlanOfferDTO(object):

    def __init__(self):
        self._lessor_path = None
        self._lessor_pid = None
        self._offer_time = None
        self._price = None
        self._sku_id = None
        self._status = None

    @property
    def lessor_path(self):
        return self._lessor_path

    @lessor_path.setter
    def lessor_path(self, value):
        self._lessor_path = value
    @property
    def lessor_pid(self):
        return self._lessor_pid

    @lessor_pid.setter
    def lessor_pid(self, value):
        self._lessor_pid = value
    @property
    def offer_time(self):
        return self._offer_time

    @offer_time.setter
    def offer_time(self, value):
        self._offer_time = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.lessor_path:
            if hasattr(self.lessor_path, 'to_alipay_dict'):
                params['lessor_path'] = self.lessor_path.to_alipay_dict()
            else:
                params['lessor_path'] = self.lessor_path
        if self.lessor_pid:
            if hasattr(self.lessor_pid, 'to_alipay_dict'):
                params['lessor_pid'] = self.lessor_pid.to_alipay_dict()
            else:
                params['lessor_pid'] = self.lessor_pid
        if self.offer_time:
            if hasattr(self.offer_time, 'to_alipay_dict'):
                params['offer_time'] = self.offer_time.to_alipay_dict()
            else:
                params['offer_time'] = self.offer_time
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
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
        o = LeasePlanOfferDTO()
        if 'lessor_path' in d:
            o.lessor_path = d['lessor_path']
        if 'lessor_pid' in d:
            o.lessor_pid = d['lessor_pid']
        if 'offer_time' in d:
            o.offer_time = d['offer_time']
        if 'price' in d:
            o.price = d['price']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'status' in d:
            o.status = d['status']
        return o


