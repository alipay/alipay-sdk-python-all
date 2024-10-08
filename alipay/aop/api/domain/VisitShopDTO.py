#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VisitShopDTO(object):

    def __init__(self):
        self._address = None
        self._check_times = None
        self._finish = None
        self._name = None
        self._shop_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def check_times(self):
        return self._check_times

    @check_times.setter
    def check_times(self, value):
        self._check_times = value
    @property
    def finish(self):
        return self._finish

    @finish.setter
    def finish(self, value):
        self._finish = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.check_times:
            if hasattr(self.check_times, 'to_alipay_dict'):
                params['check_times'] = self.check_times.to_alipay_dict()
            else:
                params['check_times'] = self.check_times
        if self.finish:
            if hasattr(self.finish, 'to_alipay_dict'):
                params['finish'] = self.finish.to_alipay_dict()
            else:
                params['finish'] = self.finish
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VisitShopDTO()
        if 'address' in d:
            o.address = d['address']
        if 'check_times' in d:
            o.check_times = d['check_times']
        if 'finish' in d:
            o.finish = d['finish']
        if 'name' in d:
            o.name = d['name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


