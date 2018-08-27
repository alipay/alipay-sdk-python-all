#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailWmsProducerBatchqueryModel(object):

    def __init__(self):
        self._producer_ids = None

    @property
    def producer_ids(self):
        return self._producer_ids

    @producer_ids.setter
    def producer_ids(self, value):
        if isinstance(value, list):
            self._producer_ids = list()
            for i in value:
                self._producer_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.producer_ids:
            if isinstance(self.producer_ids, list):
                for i in range(0, len(self.producer_ids)):
                    element = self.producer_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.producer_ids[i] = element.to_alipay_dict()
            if hasattr(self.producer_ids, 'to_alipay_dict'):
                params['producer_ids'] = self.producer_ids.to_alipay_dict()
            else:
                params['producer_ids'] = self.producer_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsProducerBatchqueryModel()
        if 'producer_ids' in d:
            o.producer_ids = d['producer_ids']
        return o


