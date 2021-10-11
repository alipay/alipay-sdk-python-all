#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentVoucherAvailableMerchantModify(object):

    def __init__(self):
        self._available_pids = None
        self._available_smids = None

    @property
    def available_pids(self):
        return self._available_pids

    @available_pids.setter
    def available_pids(self, value):
        if isinstance(value, list):
            self._available_pids = list()
            for i in value:
                self._available_pids.append(i)
    @property
    def available_smids(self):
        return self._available_smids

    @available_smids.setter
    def available_smids(self, value):
        if isinstance(value, list):
            self._available_smids = list()
            for i in value:
                self._available_smids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.available_pids:
            if isinstance(self.available_pids, list):
                for i in range(0, len(self.available_pids)):
                    element = self.available_pids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_pids[i] = element.to_alipay_dict()
            if hasattr(self.available_pids, 'to_alipay_dict'):
                params['available_pids'] = self.available_pids.to_alipay_dict()
            else:
                params['available_pids'] = self.available_pids
        if self.available_smids:
            if isinstance(self.available_smids, list):
                for i in range(0, len(self.available_smids)):
                    element = self.available_smids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_smids[i] = element.to_alipay_dict()
            if hasattr(self.available_smids, 'to_alipay_dict'):
                params['available_smids'] = self.available_smids.to_alipay_dict()
            else:
                params['available_smids'] = self.available_smids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentVoucherAvailableMerchantModify()
        if 'available_pids' in d:
            o.available_pids = d['available_pids']
        if 'available_smids' in d:
            o.available_smids = d['available_smids']
        return o


