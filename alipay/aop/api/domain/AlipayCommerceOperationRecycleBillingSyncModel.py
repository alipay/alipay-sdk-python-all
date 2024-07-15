#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleFundsInfo import RecycleFundsInfo


class AlipayCommerceOperationRecycleBillingSyncModel(object):

    def __init__(self):
        self._funds_details = None
        self._order_source = None
        self._out_biz_recycle_id = None

    @property
    def funds_details(self):
        return self._funds_details

    @funds_details.setter
    def funds_details(self, value):
        if isinstance(value, list):
            self._funds_details = list()
            for i in value:
                if isinstance(i, RecycleFundsInfo):
                    self._funds_details.append(i)
                else:
                    self._funds_details.append(RecycleFundsInfo.from_alipay_dict(i))
    @property
    def order_source(self):
        return self._order_source

    @order_source.setter
    def order_source(self, value):
        self._order_source = value
    @property
    def out_biz_recycle_id(self):
        return self._out_biz_recycle_id

    @out_biz_recycle_id.setter
    def out_biz_recycle_id(self, value):
        self._out_biz_recycle_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.funds_details:
            if isinstance(self.funds_details, list):
                for i in range(0, len(self.funds_details)):
                    element = self.funds_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.funds_details[i] = element.to_alipay_dict()
            if hasattr(self.funds_details, 'to_alipay_dict'):
                params['funds_details'] = self.funds_details.to_alipay_dict()
            else:
                params['funds_details'] = self.funds_details
        if self.order_source:
            if hasattr(self.order_source, 'to_alipay_dict'):
                params['order_source'] = self.order_source.to_alipay_dict()
            else:
                params['order_source'] = self.order_source
        if self.out_biz_recycle_id:
            if hasattr(self.out_biz_recycle_id, 'to_alipay_dict'):
                params['out_biz_recycle_id'] = self.out_biz_recycle_id.to_alipay_dict()
            else:
                params['out_biz_recycle_id'] = self.out_biz_recycle_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationRecycleBillingSyncModel()
        if 'funds_details' in d:
            o.funds_details = d['funds_details']
        if 'order_source' in d:
            o.order_source = d['order_source']
        if 'out_biz_recycle_id' in d:
            o.out_biz_recycle_id = d['out_biz_recycle_id']
        return o


