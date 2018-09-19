#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.OpenApiRoyaltyDetailInfoPojo import OpenApiRoyaltyDetailInfoPojo


class AlipayTradeRefundModel(object):

    def __init__(self):
        self._goods_detail = None
        self._operator_id = None
        self._org_pid = None
        self._out_request_no = None
        self._out_trade_no = None
        self._refund_amount = None
        self._refund_currency = None
        self._refund_reason = None
        self._refund_royalty_parameters = None
        self._store_id = None
        self._terminal_id = None
        self._trade_no = None

    @property
    def goods_detail(self):
        return self._goods_detail

    @goods_detail.setter
    def goods_detail(self, value):
        if isinstance(value, list):
            self._goods_detail = list()
            for i in value:
                if isinstance(i, GoodsDetail):
                    self._goods_detail.append(i)
                else:
                    self._goods_detail.append(GoodsDetail.from_alipay_dict(i))
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def org_pid(self):
        return self._org_pid

    @org_pid.setter
    def org_pid(self, value):
        self._org_pid = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_currency(self):
        return self._refund_currency

    @refund_currency.setter
    def refund_currency(self, value):
        self._refund_currency = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def refund_royalty_parameters(self):
        return self._refund_royalty_parameters

    @refund_royalty_parameters.setter
    def refund_royalty_parameters(self, value):
        if isinstance(value, list):
            self._refund_royalty_parameters = list()
            for i in value:
                if isinstance(i, OpenApiRoyaltyDetailInfoPojo):
                    self._refund_royalty_parameters.append(i)
                else:
                    self._refund_royalty_parameters.append(OpenApiRoyaltyDetailInfoPojo.from_alipay_dict(i))
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def terminal_id(self):
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_detail:
            if isinstance(self.goods_detail, list):
                for i in range(0, len(self.goods_detail)):
                    element = self.goods_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_detail[i] = element.to_alipay_dict()
            if hasattr(self.goods_detail, 'to_alipay_dict'):
                params['goods_detail'] = self.goods_detail.to_alipay_dict()
            else:
                params['goods_detail'] = self.goods_detail
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.org_pid:
            if hasattr(self.org_pid, 'to_alipay_dict'):
                params['org_pid'] = self.org_pid.to_alipay_dict()
            else:
                params['org_pid'] = self.org_pid
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_currency:
            if hasattr(self.refund_currency, 'to_alipay_dict'):
                params['refund_currency'] = self.refund_currency.to_alipay_dict()
            else:
                params['refund_currency'] = self.refund_currency
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.refund_royalty_parameters:
            if isinstance(self.refund_royalty_parameters, list):
                for i in range(0, len(self.refund_royalty_parameters)):
                    element = self.refund_royalty_parameters[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_royalty_parameters[i] = element.to_alipay_dict()
            if hasattr(self.refund_royalty_parameters, 'to_alipay_dict'):
                params['refund_royalty_parameters'] = self.refund_royalty_parameters.to_alipay_dict()
            else:
                params['refund_royalty_parameters'] = self.refund_royalty_parameters
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.terminal_id:
            if hasattr(self.terminal_id, 'to_alipay_dict'):
                params['terminal_id'] = self.terminal_id.to_alipay_dict()
            else:
                params['terminal_id'] = self.terminal_id
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
        o = AlipayTradeRefundModel()
        if 'goods_detail' in d:
            o.goods_detail = d['goods_detail']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'org_pid' in d:
            o.org_pid = d['org_pid']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_currency' in d:
            o.refund_currency = d['refund_currency']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'refund_royalty_parameters' in d:
            o.refund_royalty_parameters = d['refund_royalty_parameters']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'terminal_id' in d:
            o.terminal_id = d['terminal_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


