#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAddressQueryModel(object):

    def __init__(self):
        self._address_id = None

    @property
    def address_id(self):
        return self._address_id

    @address_id.setter
    def address_id(self, value):
        self._address_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_id:
            if hasattr(self.address_id, 'to_alipay_dict'):
                params['address_id'] = self.address_id.to_alipay_dict()
            else:
                params['address_id'] = self.address_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAddressQueryModel()
        if 'address_id' in d:
            o.address_id = d['address_id']
        return o


