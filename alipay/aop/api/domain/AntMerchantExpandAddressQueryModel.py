#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandAddressQueryModel(object):

    def __init__(self):
        self._address_ids = None

    @property
    def address_ids(self):
        return self._address_ids

    @address_ids.setter
    def address_ids(self, value):
        if isinstance(value, list):
            self._address_ids = list()
            for i in value:
                self._address_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.address_ids:
            if isinstance(self.address_ids, list):
                for i in range(0, len(self.address_ids)):
                    element = self.address_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.address_ids[i] = element.to_alipay_dict()
            if hasattr(self.address_ids, 'to_alipay_dict'):
                params['address_ids'] = self.address_ids.to_alipay_dict()
            else:
                params['address_ids'] = self.address_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAddressQueryModel()
        if 'address_ids' in d:
            o.address_ids = d['address_ids']
        return o


