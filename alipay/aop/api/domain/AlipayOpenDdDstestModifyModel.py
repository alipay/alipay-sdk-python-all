#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenDdDstestModifyModel(object):

    def __init__(self):
        self._address = None
        self._address_open_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def address_open_id(self):
        return self._address_open_id

    @address_open_id.setter
    def address_open_id(self, value):
        self._address_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.address_open_id:
            if hasattr(self.address_open_id, 'to_alipay_dict'):
                params['address_open_id'] = self.address_open_id.to_alipay_dict()
            else:
                params['address_open_id'] = self.address_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenDdDstestModifyModel()
        if 'address' in d:
            o.address = d['address']
        if 'address_open_id' in d:
            o.address_open_id = d['address_open_id']
        return o


