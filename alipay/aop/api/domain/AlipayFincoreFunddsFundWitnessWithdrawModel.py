#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TradeDetailInfoDTO import TradeDetailInfoDTO
from alipay.aop.api.domain.WithdrawClauseDetailDTO import WithdrawClauseDetailDTO


class AlipayFincoreFunddsFundWitnessWithdrawModel(object):

    def __init__(self):
        self._out_request_no = None
        self._product_code = None
        self._sharding_id = None
        self._trade_detail_info_list = None
        self._withdraw_clause_detail = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def sharding_id(self):
        return self._sharding_id

    @sharding_id.setter
    def sharding_id(self, value):
        self._sharding_id = value
    @property
    def trade_detail_info_list(self):
        return self._trade_detail_info_list

    @trade_detail_info_list.setter
    def trade_detail_info_list(self, value):
        if isinstance(value, list):
            self._trade_detail_info_list = list()
            for i in value:
                if isinstance(i, TradeDetailInfoDTO):
                    self._trade_detail_info_list.append(i)
                else:
                    self._trade_detail_info_list.append(TradeDetailInfoDTO.from_alipay_dict(i))
    @property
    def withdraw_clause_detail(self):
        return self._withdraw_clause_detail

    @withdraw_clause_detail.setter
    def withdraw_clause_detail(self, value):
        if isinstance(value, WithdrawClauseDetailDTO):
            self._withdraw_clause_detail = value
        else:
            self._withdraw_clause_detail = WithdrawClauseDetailDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.sharding_id:
            if hasattr(self.sharding_id, 'to_alipay_dict'):
                params['sharding_id'] = self.sharding_id.to_alipay_dict()
            else:
                params['sharding_id'] = self.sharding_id
        if self.trade_detail_info_list:
            if isinstance(self.trade_detail_info_list, list):
                for i in range(0, len(self.trade_detail_info_list)):
                    element = self.trade_detail_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_detail_info_list[i] = element.to_alipay_dict()
            if hasattr(self.trade_detail_info_list, 'to_alipay_dict'):
                params['trade_detail_info_list'] = self.trade_detail_info_list.to_alipay_dict()
            else:
                params['trade_detail_info_list'] = self.trade_detail_info_list
        if self.withdraw_clause_detail:
            if hasattr(self.withdraw_clause_detail, 'to_alipay_dict'):
                params['withdraw_clause_detail'] = self.withdraw_clause_detail.to_alipay_dict()
            else:
                params['withdraw_clause_detail'] = self.withdraw_clause_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreFunddsFundWitnessWithdrawModel()
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'sharding_id' in d:
            o.sharding_id = d['sharding_id']
        if 'trade_detail_info_list' in d:
            o.trade_detail_info_list = d['trade_detail_info_list']
        if 'withdraw_clause_detail' in d:
            o.withdraw_clause_detail = d['withdraw_clause_detail']
        return o


