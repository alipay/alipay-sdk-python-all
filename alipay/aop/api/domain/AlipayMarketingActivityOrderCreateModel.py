#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SaleActivityInfo import SaleActivityInfo


class AlipayMarketingActivityOrderCreateModel(object):

    def __init__(self):
        self._buyer_id = None
        self._ch_info = None
        self._out_order_no = None
        self._promo_trace_info = None
        self._sale_activity_info_list = None
        self._total_amount = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def ch_info(self):
        return self._ch_info

    @ch_info.setter
    def ch_info(self, value):
        self._ch_info = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def promo_trace_info(self):
        return self._promo_trace_info

    @promo_trace_info.setter
    def promo_trace_info(self, value):
        self._promo_trace_info = value
    @property
    def sale_activity_info_list(self):
        return self._sale_activity_info_list

    @sale_activity_info_list.setter
    def sale_activity_info_list(self, value):
        if isinstance(value, list):
            self._sale_activity_info_list = list()
            for i in value:
                if isinstance(i, SaleActivityInfo):
                    self._sale_activity_info_list.append(i)
                else:
                    self._sale_activity_info_list.append(SaleActivityInfo.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.ch_info:
            if hasattr(self.ch_info, 'to_alipay_dict'):
                params['ch_info'] = self.ch_info.to_alipay_dict()
            else:
                params['ch_info'] = self.ch_info
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.promo_trace_info:
            if hasattr(self.promo_trace_info, 'to_alipay_dict'):
                params['promo_trace_info'] = self.promo_trace_info.to_alipay_dict()
            else:
                params['promo_trace_info'] = self.promo_trace_info
        if self.sale_activity_info_list:
            if isinstance(self.sale_activity_info_list, list):
                for i in range(0, len(self.sale_activity_info_list)):
                    element = self.sale_activity_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sale_activity_info_list[i] = element.to_alipay_dict()
            if hasattr(self.sale_activity_info_list, 'to_alipay_dict'):
                params['sale_activity_info_list'] = self.sale_activity_info_list.to_alipay_dict()
            else:
                params['sale_activity_info_list'] = self.sale_activity_info_list
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityOrderCreateModel()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'ch_info' in d:
            o.ch_info = d['ch_info']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'promo_trace_info' in d:
            o.promo_trace_info = d['promo_trace_info']
        if 'sale_activity_info_list' in d:
            o.sale_activity_info_list = d['sale_activity_info_list']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


