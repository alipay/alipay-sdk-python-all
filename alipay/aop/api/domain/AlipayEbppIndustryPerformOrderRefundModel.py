#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProfitSharing import ProfitSharing


class AlipayEbppIndustryPerformOrderRefundModel(object):

    def __init__(self):
        self._bill_no = None
        self._is_sub_merchant = None
        self._out_no = None
        self._profit_sharing_list = None
        self._reason = None
        self._refund_money = None
        self._refund_scene = None
        self._request_id = None
        self._trade_no = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def is_sub_merchant(self):
        return self._is_sub_merchant

    @is_sub_merchant.setter
    def is_sub_merchant(self, value):
        self._is_sub_merchant = value
    @property
    def out_no(self):
        return self._out_no

    @out_no.setter
    def out_no(self, value):
        self._out_no = value
    @property
    def profit_sharing_list(self):
        return self._profit_sharing_list

    @profit_sharing_list.setter
    def profit_sharing_list(self, value):
        if isinstance(value, list):
            self._profit_sharing_list = list()
            for i in value:
                if isinstance(i, ProfitSharing):
                    self._profit_sharing_list.append(i)
                else:
                    self._profit_sharing_list.append(ProfitSharing.from_alipay_dict(i))
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def refund_money(self):
        return self._refund_money

    @refund_money.setter
    def refund_money(self, value):
        self._refund_money = value
    @property
    def refund_scene(self):
        return self._refund_scene

    @refund_scene.setter
    def refund_scene(self, value):
        self._refund_scene = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.is_sub_merchant:
            if hasattr(self.is_sub_merchant, 'to_alipay_dict'):
                params['is_sub_merchant'] = self.is_sub_merchant.to_alipay_dict()
            else:
                params['is_sub_merchant'] = self.is_sub_merchant
        if self.out_no:
            if hasattr(self.out_no, 'to_alipay_dict'):
                params['out_no'] = self.out_no.to_alipay_dict()
            else:
                params['out_no'] = self.out_no
        if self.profit_sharing_list:
            if isinstance(self.profit_sharing_list, list):
                for i in range(0, len(self.profit_sharing_list)):
                    element = self.profit_sharing_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.profit_sharing_list[i] = element.to_alipay_dict()
            if hasattr(self.profit_sharing_list, 'to_alipay_dict'):
                params['profit_sharing_list'] = self.profit_sharing_list.to_alipay_dict()
            else:
                params['profit_sharing_list'] = self.profit_sharing_list
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.refund_money:
            if hasattr(self.refund_money, 'to_alipay_dict'):
                params['refund_money'] = self.refund_money.to_alipay_dict()
            else:
                params['refund_money'] = self.refund_money
        if self.refund_scene:
            if hasattr(self.refund_scene, 'to_alipay_dict'):
                params['refund_scene'] = self.refund_scene.to_alipay_dict()
            else:
                params['refund_scene'] = self.refund_scene
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryPerformOrderRefundModel()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'is_sub_merchant' in d:
            o.is_sub_merchant = d['is_sub_merchant']
        if 'out_no' in d:
            o.out_no = d['out_no']
        if 'profit_sharing_list' in d:
            o.profit_sharing_list = d['profit_sharing_list']
        if 'reason' in d:
            o.reason = d['reason']
        if 'refund_money' in d:
            o.refund_money = d['refund_money']
        if 'refund_scene' in d:
            o.refund_scene = d['refund_scene']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


