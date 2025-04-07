#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentAddress import RentAddress


class SellerSyncRentDeliveryExtInfo(object):

    def __init__(self):
        self._delivery_no = None
        self._receive_address = None

    @property
    def delivery_no(self):
        return self._delivery_no

    @delivery_no.setter
    def delivery_no(self, value):
        self._delivery_no = value
    @property
    def receive_address(self):
        return self._receive_address

    @receive_address.setter
    def receive_address(self, value):
        if isinstance(value, RentAddress):
            self._receive_address = value
        else:
            self._receive_address = RentAddress.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_no:
            if hasattr(self.delivery_no, 'to_alipay_dict'):
                params['delivery_no'] = self.delivery_no.to_alipay_dict()
            else:
                params['delivery_no'] = self.delivery_no
        if self.receive_address:
            if hasattr(self.receive_address, 'to_alipay_dict'):
                params['receive_address'] = self.receive_address.to_alipay_dict()
            else:
                params['receive_address'] = self.receive_address
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SellerSyncRentDeliveryExtInfo()
        if 'delivery_no' in d:
            o.delivery_no = d['delivery_no']
        if 'receive_address' in d:
            o.receive_address = d['receive_address']
        return o


