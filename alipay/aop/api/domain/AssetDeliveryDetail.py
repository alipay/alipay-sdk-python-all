#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LogisticsInfo import LogisticsInfo


class AssetDeliveryDetail(object):

    def __init__(self):
        self._amount = None
        self._assign_item_id = None
        self._batch_no = None
        self._ext_info = None
        self._logistics_infos = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def logistics_infos(self):
        return self._logistics_infos

    @logistics_infos.setter
    def logistics_infos(self, value):
        if isinstance(value, list):
            self._logistics_infos = list()
            for i in value:
                if isinstance(i, LogisticsInfo):
                    self._logistics_infos.append(i)
                else:
                    self._logistics_infos.append(LogisticsInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.assign_item_id:
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.logistics_infos:
            if isinstance(self.logistics_infos, list):
                for i in range(0, len(self.logistics_infos)):
                    element = self.logistics_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logistics_infos[i] = element.to_alipay_dict()
            if hasattr(self.logistics_infos, 'to_alipay_dict'):
                params['logistics_infos'] = self.logistics_infos.to_alipay_dict()
            else:
                params['logistics_infos'] = self.logistics_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetDeliveryDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'logistics_infos' in d:
            o.logistics_infos = d['logistics_infos']
        return o


