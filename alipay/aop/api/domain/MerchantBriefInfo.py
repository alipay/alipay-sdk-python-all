#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayMerchantInfo import AlipayMerchantInfo
from alipay.aop.api.domain.DeviceRelationPair import DeviceRelationPair


class MerchantBriefInfo(object):

    def __init__(self):
        self._merchant_list = None
        self._out_merchant_no = None
        self._sn_bind_pair_list = None

    @property
    def merchant_list(self):
        return self._merchant_list

    @merchant_list.setter
    def merchant_list(self, value):
        if isinstance(value, list):
            self._merchant_list = list()
            for i in value:
                if isinstance(i, AlipayMerchantInfo):
                    self._merchant_list.append(i)
                else:
                    self._merchant_list.append(AlipayMerchantInfo.from_alipay_dict(i))
    @property
    def out_merchant_no(self):
        return self._out_merchant_no

    @out_merchant_no.setter
    def out_merchant_no(self, value):
        self._out_merchant_no = value
    @property
    def sn_bind_pair_list(self):
        return self._sn_bind_pair_list

    @sn_bind_pair_list.setter
    def sn_bind_pair_list(self, value):
        if isinstance(value, list):
            self._sn_bind_pair_list = list()
            for i in value:
                if isinstance(i, DeviceRelationPair):
                    self._sn_bind_pair_list.append(i)
                else:
                    self._sn_bind_pair_list.append(DeviceRelationPair.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_list:
            if isinstance(self.merchant_list, list):
                for i in range(0, len(self.merchant_list)):
                    element = self.merchant_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_list[i] = element.to_alipay_dict()
            if hasattr(self.merchant_list, 'to_alipay_dict'):
                params['merchant_list'] = self.merchant_list.to_alipay_dict()
            else:
                params['merchant_list'] = self.merchant_list
        if self.out_merchant_no:
            if hasattr(self.out_merchant_no, 'to_alipay_dict'):
                params['out_merchant_no'] = self.out_merchant_no.to_alipay_dict()
            else:
                params['out_merchant_no'] = self.out_merchant_no
        if self.sn_bind_pair_list:
            if isinstance(self.sn_bind_pair_list, list):
                for i in range(0, len(self.sn_bind_pair_list)):
                    element = self.sn_bind_pair_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sn_bind_pair_list[i] = element.to_alipay_dict()
            if hasattr(self.sn_bind_pair_list, 'to_alipay_dict'):
                params['sn_bind_pair_list'] = self.sn_bind_pair_list.to_alipay_dict()
            else:
                params['sn_bind_pair_list'] = self.sn_bind_pair_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantBriefInfo()
        if 'merchant_list' in d:
            o.merchant_list = d['merchant_list']
        if 'out_merchant_no' in d:
            o.out_merchant_no = d['out_merchant_no']
        if 'sn_bind_pair_list' in d:
            o.sn_bind_pair_list = d['sn_bind_pair_list']
        return o


