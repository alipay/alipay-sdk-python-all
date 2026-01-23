#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PBCScanParam import PBCScanParam


class AlipaySecurityRiskSanctionWatchlistCheckModel(object):

    def __init__(self):
        self._pbc_scan_params = None

    @property
    def pbc_scan_params(self):
        return self._pbc_scan_params

    @pbc_scan_params.setter
    def pbc_scan_params(self, value):
        if isinstance(value, list):
            self._pbc_scan_params = list()
            for i in value:
                if isinstance(i, PBCScanParam):
                    self._pbc_scan_params.append(i)
                else:
                    self._pbc_scan_params.append(PBCScanParam.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.pbc_scan_params:
            if isinstance(self.pbc_scan_params, list):
                for i in range(0, len(self.pbc_scan_params)):
                    element = self.pbc_scan_params[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pbc_scan_params[i] = element.to_alipay_dict()
            if hasattr(self.pbc_scan_params, 'to_alipay_dict'):
                params['pbc_scan_params'] = self.pbc_scan_params.to_alipay_dict()
            else:
                params['pbc_scan_params'] = self.pbc_scan_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskSanctionWatchlistCheckModel()
        if 'pbc_scan_params' in d:
            o.pbc_scan_params = d['pbc_scan_params']
        return o


