#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DistributionMerchantAddressDTO import DistributionMerchantAddressDTO
from alipay.aop.api.domain.DistributionMerchantAddressDTO import DistributionMerchantAddressDTO


class DistributionBuyerAddressModifyApplyInfoDTO(object):

    def __init__(self):
        self._address = None
        self._source_address = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, DistributionMerchantAddressDTO):
            self._address = value
        else:
            self._address = DistributionMerchantAddressDTO.from_alipay_dict(value)
    @property
    def source_address(self):
        return self._source_address

    @source_address.setter
    def source_address(self, value):
        if isinstance(value, DistributionMerchantAddressDTO):
            self._source_address = value
        else:
            self._source_address = DistributionMerchantAddressDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.source_address:
            if hasattr(self.source_address, 'to_alipay_dict'):
                params['source_address'] = self.source_address.to_alipay_dict()
            else:
                params['source_address'] = self.source_address
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DistributionBuyerAddressModifyApplyInfoDTO()
        if 'address' in d:
            o.address = d['address']
        if 'source_address' in d:
            o.source_address = d['source_address']
        return o


