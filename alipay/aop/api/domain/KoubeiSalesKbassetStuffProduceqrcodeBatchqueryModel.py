#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiSalesKbassetStuffProduceqrcodeBatchqueryModel(object):

    def __init__(self):
        self._batch_id = None
        self._page_size = None
        self._produce_order_id = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def produce_order_id(self):
        return self._produce_order_id

    @produce_order_id.setter
    def produce_order_id(self, value):
        self._produce_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.produce_order_id:
            if hasattr(self.produce_order_id, 'to_alipay_dict'):
                params['produce_order_id'] = self.produce_order_id.to_alipay_dict()
            else:
                params['produce_order_id'] = self.produce_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiSalesKbassetStuffProduceqrcodeBatchqueryModel()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'produce_order_id' in d:
            o.produce_order_id = d['produce_order_id']
        return o


