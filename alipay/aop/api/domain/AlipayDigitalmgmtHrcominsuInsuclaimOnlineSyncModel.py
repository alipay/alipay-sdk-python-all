#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsuClaimRecordVo import InsuClaimRecordVo


class AlipayDigitalmgmtHrcominsuInsuclaimOnlineSyncModel(object):

    def __init__(self):
        self._data_key = None
        self._insu_claim_vos = None

    @property
    def data_key(self):
        return self._data_key

    @data_key.setter
    def data_key(self, value):
        self._data_key = value
    @property
    def insu_claim_vos(self):
        return self._insu_claim_vos

    @insu_claim_vos.setter
    def insu_claim_vos(self, value):
        if isinstance(value, list):
            self._insu_claim_vos = list()
            for i in value:
                if isinstance(i, InsuClaimRecordVo):
                    self._insu_claim_vos.append(i)
                else:
                    self._insu_claim_vos.append(InsuClaimRecordVo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.data_key:
            if hasattr(self.data_key, 'to_alipay_dict'):
                params['data_key'] = self.data_key.to_alipay_dict()
            else:
                params['data_key'] = self.data_key
        if self.insu_claim_vos:
            if isinstance(self.insu_claim_vos, list):
                for i in range(0, len(self.insu_claim_vos)):
                    element = self.insu_claim_vos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.insu_claim_vos[i] = element.to_alipay_dict()
            if hasattr(self.insu_claim_vos, 'to_alipay_dict'):
                params['insu_claim_vos'] = self.insu_claim_vos.to_alipay_dict()
            else:
                params['insu_claim_vos'] = self.insu_claim_vos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtHrcominsuInsuclaimOnlineSyncModel()
        if 'data_key' in d:
            o.data_key = d['data_key']
        if 'insu_claim_vos' in d:
            o.insu_claim_vos = d['insu_claim_vos']
        return o


