#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentEcSignContractVO import RentEcSignContractVO


class RentEcSignApplyInfoVO(object):

    def __init__(self):
        self._biz_no = None
        self._contracts = None
        self._status = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def contracts(self):
        return self._contracts

    @contracts.setter
    def contracts(self, value):
        if isinstance(value, list):
            self._contracts = list()
            for i in value:
                if isinstance(i, RentEcSignContractVO):
                    self._contracts.append(i)
                else:
                    self._contracts.append(RentEcSignContractVO.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.contracts:
            if isinstance(self.contracts, list):
                for i in range(0, len(self.contracts)):
                    element = self.contracts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contracts[i] = element.to_alipay_dict()
            if hasattr(self.contracts, 'to_alipay_dict'):
                params['contracts'] = self.contracts.to_alipay_dict()
            else:
                params['contracts'] = self.contracts
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentEcSignApplyInfoVO()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'contracts' in d:
            o.contracts = d['contracts']
        if 'status' in d:
            o.status = d['status']
        return o


