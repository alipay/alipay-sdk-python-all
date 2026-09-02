#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DistributionMerchantAddressDTO import DistributionMerchantAddressDTO


class AlipayCommerceRentDistmerchantAddressCreateModel(object):

    def __init__(self):
        self._address = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, DistributionMerchantAddressDTO):
            self._address = value
        else:
            self._address = DistributionMerchantAddressDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentDistmerchantAddressCreateModel()
        if 'address' in d:
            o.address = d['address']
        return o


