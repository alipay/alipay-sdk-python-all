#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LogisticsInfo import LogisticsInfo


class AssetReverseSupplierApplyExpressSnDetails(object):

    def __init__(self):
        self._logistics_infos = None
        self._sn_records = None

    @property
    def logistics_infos(self):
        return self._logistics_infos

    @logistics_infos.setter
    def logistics_infos(self, value):
        if isinstance(value, LogisticsInfo):
            self._logistics_infos = value
        else:
            self._logistics_infos = LogisticsInfo.from_alipay_dict(value)
    @property
    def sn_records(self):
        return self._sn_records

    @sn_records.setter
    def sn_records(self, value):
        if isinstance(value, list):
            self._sn_records = list()
            for i in value:
                self._sn_records.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_infos:
            if hasattr(self.logistics_infos, 'to_alipay_dict'):
                params['logistics_infos'] = self.logistics_infos.to_alipay_dict()
            else:
                params['logistics_infos'] = self.logistics_infos
        if self.sn_records:
            if isinstance(self.sn_records, list):
                for i in range(0, len(self.sn_records)):
                    element = self.sn_records[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sn_records[i] = element.to_alipay_dict()
            if hasattr(self.sn_records, 'to_alipay_dict'):
                params['sn_records'] = self.sn_records.to_alipay_dict()
            else:
                params['sn_records'] = self.sn_records
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetReverseSupplierApplyExpressSnDetails()
        if 'logistics_infos' in d:
            o.logistics_infos = d['logistics_infos']
        if 'sn_records' in d:
            o.sn_records = d['sn_records']
        return o


