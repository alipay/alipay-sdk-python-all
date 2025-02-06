#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeductionDataSyncRequest import DeductionDataSyncRequest


class AlipayCommerceMerchantcardDeductionSyncModel(object):

    def __init__(self):
        self._batch_id = None
        self._deduction_data_list = None
        self._sync_type = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def deduction_data_list(self):
        return self._deduction_data_list

    @deduction_data_list.setter
    def deduction_data_list(self, value):
        if isinstance(value, list):
            self._deduction_data_list = list()
            for i in value:
                if isinstance(i, DeductionDataSyncRequest):
                    self._deduction_data_list.append(i)
                else:
                    self._deduction_data_list.append(DeductionDataSyncRequest.from_alipay_dict(i))
    @property
    def sync_type(self):
        return self._sync_type

    @sync_type.setter
    def sync_type(self, value):
        self._sync_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.deduction_data_list:
            if isinstance(self.deduction_data_list, list):
                for i in range(0, len(self.deduction_data_list)):
                    element = self.deduction_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.deduction_data_list[i] = element.to_alipay_dict()
            if hasattr(self.deduction_data_list, 'to_alipay_dict'):
                params['deduction_data_list'] = self.deduction_data_list.to_alipay_dict()
            else:
                params['deduction_data_list'] = self.deduction_data_list
        if self.sync_type:
            if hasattr(self.sync_type, 'to_alipay_dict'):
                params['sync_type'] = self.sync_type.to_alipay_dict()
            else:
                params['sync_type'] = self.sync_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardDeductionSyncModel()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'deduction_data_list' in d:
            o.deduction_data_list = d['deduction_data_list']
        if 'sync_type' in d:
            o.sync_type = d['sync_type']
        return o


