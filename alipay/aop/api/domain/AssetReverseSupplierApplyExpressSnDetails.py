#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetReverseItemDetail import AssetReverseItemDetail
from alipay.aop.api.domain.LogisticsInfo import LogisticsInfo


class AssetReverseSupplierApplyExpressSnDetails(object):

    def __init__(self):
        self._apply_count = None
        self._asset_reverse_item_details = None
        self._logistics_infos = None
        self._sn_records = None

    @property
    def apply_count(self):
        return self._apply_count

    @apply_count.setter
    def apply_count(self, value):
        self._apply_count = value
    @property
    def asset_reverse_item_details(self):
        return self._asset_reverse_item_details

    @asset_reverse_item_details.setter
    def asset_reverse_item_details(self, value):
        if isinstance(value, list):
            self._asset_reverse_item_details = list()
            for i in value:
                if isinstance(i, AssetReverseItemDetail):
                    self._asset_reverse_item_details.append(i)
                else:
                    self._asset_reverse_item_details.append(AssetReverseItemDetail.from_alipay_dict(i))
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
        if self.apply_count:
            if hasattr(self.apply_count, 'to_alipay_dict'):
                params['apply_count'] = self.apply_count.to_alipay_dict()
            else:
                params['apply_count'] = self.apply_count
        if self.asset_reverse_item_details:
            if isinstance(self.asset_reverse_item_details, list):
                for i in range(0, len(self.asset_reverse_item_details)):
                    element = self.asset_reverse_item_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asset_reverse_item_details[i] = element.to_alipay_dict()
            if hasattr(self.asset_reverse_item_details, 'to_alipay_dict'):
                params['asset_reverse_item_details'] = self.asset_reverse_item_details.to_alipay_dict()
            else:
                params['asset_reverse_item_details'] = self.asset_reverse_item_details
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
        if 'apply_count' in d:
            o.apply_count = d['apply_count']
        if 'asset_reverse_item_details' in d:
            o.asset_reverse_item_details = d['asset_reverse_item_details']
        if 'logistics_infos' in d:
            o.logistics_infos = d['logistics_infos']
        if 'sn_records' in d:
            o.sn_records = d['sn_records']
        return o


