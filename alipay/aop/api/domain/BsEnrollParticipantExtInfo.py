#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BsEnrollParticipantAddress import BsEnrollParticipantAddress


class BsEnrollParticipantExtInfo(object):

    def __init__(self):
        self._out_store_address = None
        self._out_store_name = None

    @property
    def out_store_address(self):
        return self._out_store_address

    @out_store_address.setter
    def out_store_address(self, value):
        if isinstance(value, BsEnrollParticipantAddress):
            self._out_store_address = value
        else:
            self._out_store_address = BsEnrollParticipantAddress.from_alipay_dict(value)
    @property
    def out_store_name(self):
        return self._out_store_name

    @out_store_name.setter
    def out_store_name(self, value):
        self._out_store_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_store_address:
            if hasattr(self.out_store_address, 'to_alipay_dict'):
                params['out_store_address'] = self.out_store_address.to_alipay_dict()
            else:
                params['out_store_address'] = self.out_store_address
        if self.out_store_name:
            if hasattr(self.out_store_name, 'to_alipay_dict'):
                params['out_store_name'] = self.out_store_name.to_alipay_dict()
            else:
                params['out_store_name'] = self.out_store_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BsEnrollParticipantExtInfo()
        if 'out_store_address' in d:
            o.out_store_address = d['out_store_address']
        if 'out_store_name' in d:
            o.out_store_name = d['out_store_name']
        return o


