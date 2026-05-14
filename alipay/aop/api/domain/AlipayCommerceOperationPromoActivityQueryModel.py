#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NfcDeviceInfo import NfcDeviceInfo


class AlipayCommerceOperationPromoActivityQueryModel(object):

    def __init__(self):
        self._device_list = None
        self._out_merchant_no = None

    @property
    def device_list(self):
        return self._device_list

    @device_list.setter
    def device_list(self, value):
        if isinstance(value, list):
            self._device_list = list()
            for i in value:
                if isinstance(i, NfcDeviceInfo):
                    self._device_list.append(i)
                else:
                    self._device_list.append(NfcDeviceInfo.from_alipay_dict(i))
    @property
    def out_merchant_no(self):
        return self._out_merchant_no

    @out_merchant_no.setter
    def out_merchant_no(self, value):
        self._out_merchant_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_list:
            if isinstance(self.device_list, list):
                for i in range(0, len(self.device_list)):
                    element = self.device_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_list[i] = element.to_alipay_dict()
            if hasattr(self.device_list, 'to_alipay_dict'):
                params['device_list'] = self.device_list.to_alipay_dict()
            else:
                params['device_list'] = self.device_list
        if self.out_merchant_no:
            if hasattr(self.out_merchant_no, 'to_alipay_dict'):
                params['out_merchant_no'] = self.out_merchant_no.to_alipay_dict()
            else:
                params['out_merchant_no'] = self.out_merchant_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationPromoActivityQueryModel()
        if 'device_list' in d:
            o.device_list = d['device_list']
        if 'out_merchant_no' in d:
            o.out_merchant_no = d['out_merchant_no']
        return o


