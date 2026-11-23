#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAipayNowpayProductBatchqueryModel(object):

    def __init__(self):
        self._external_owner_id = None
        self._out_product_ids = None

    @property
    def external_owner_id(self):
        return self._external_owner_id

    @external_owner_id.setter
    def external_owner_id(self, value):
        self._external_owner_id = value
    @property
    def out_product_ids(self):
        return self._out_product_ids

    @out_product_ids.setter
    def out_product_ids(self, value):
        if isinstance(value, list):
            self._out_product_ids = list()
            for i in value:
                self._out_product_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.external_owner_id:
            if hasattr(self.external_owner_id, 'to_alipay_dict'):
                params['external_owner_id'] = self.external_owner_id.to_alipay_dict()
            else:
                params['external_owner_id'] = self.external_owner_id
        if self.out_product_ids:
            if isinstance(self.out_product_ids, list):
                for i in range(0, len(self.out_product_ids)):
                    element = self.out_product_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_product_ids[i] = element.to_alipay_dict()
            if hasattr(self.out_product_ids, 'to_alipay_dict'):
                params['out_product_ids'] = self.out_product_ids.to_alipay_dict()
            else:
                params['out_product_ids'] = self.out_product_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAipayNowpayProductBatchqueryModel()
        if 'external_owner_id' in d:
            o.external_owner_id = d['external_owner_id']
        if 'out_product_ids' in d:
            o.out_product_ids = d['out_product_ids']
        return o


