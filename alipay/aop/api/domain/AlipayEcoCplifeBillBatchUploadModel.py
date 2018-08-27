#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CPBillSet import CPBillSet


class AlipayEcoCplifeBillBatchUploadModel(object):

    def __init__(self):
        self._batch_id = None
        self._bill_set = None
        self._community_id = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def bill_set(self):
        return self._bill_set

    @bill_set.setter
    def bill_set(self, value):
        if isinstance(value, list):
            self._bill_set = list()
            for i in value:
                if isinstance(i, CPBillSet):
                    self._bill_set.append(i)
                else:
                    self._bill_set.append(CPBillSet.from_alipay_dict(i))
    @property
    def community_id(self):
        return self._community_id

    @community_id.setter
    def community_id(self, value):
        self._community_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.bill_set:
            if isinstance(self.bill_set, list):
                for i in range(0, len(self.bill_set)):
                    element = self.bill_set[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_set[i] = element.to_alipay_dict()
            if hasattr(self.bill_set, 'to_alipay_dict'):
                params['bill_set'] = self.bill_set.to_alipay_dict()
            else:
                params['bill_set'] = self.bill_set
        if self.community_id:
            if hasattr(self.community_id, 'to_alipay_dict'):
                params['community_id'] = self.community_id.to_alipay_dict()
            else:
                params['community_id'] = self.community_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCplifeBillBatchUploadModel()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'bill_set' in d:
            o.bill_set = d['bill_set']
        if 'community_id' in d:
            o.community_id = d['community_id']
        return o


