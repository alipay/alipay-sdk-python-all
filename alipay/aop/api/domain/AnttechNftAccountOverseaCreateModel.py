#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftAccountOverseaCreateModel(object):

    def __init__(self):
        self._blockchain_address = None

    @property
    def blockchain_address(self):
        return self._blockchain_address

    @blockchain_address.setter
    def blockchain_address(self, value):
        self._blockchain_address = value


    def to_alipay_dict(self):
        params = dict()
        if self.blockchain_address:
            if hasattr(self.blockchain_address, 'to_alipay_dict'):
                params['blockchain_address'] = self.blockchain_address.to_alipay_dict()
            else:
                params['blockchain_address'] = self.blockchain_address
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftAccountOverseaCreateModel()
        if 'blockchain_address' in d:
            o.blockchain_address = d['blockchain_address']
        return o


