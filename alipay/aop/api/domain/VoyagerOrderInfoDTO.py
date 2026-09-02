#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StandardGoodsInfo import StandardGoodsInfo
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO
from alipay.aop.api.domain.SettlementStrategyDTO import SettlementStrategyDTO


class VoyagerOrderInfoDTO(object):

    def __init__(self):
        self._goods_list = None
        self._merchant_mcc = None
        self._order_amount = None
        self._order_description = None
        self._order_id = None
        self._reference_merchant_id = None
        self._settlement_strategy = None

    @property
    def goods_list(self):
        return self._goods_list

    @goods_list.setter
    def goods_list(self, value):
        if isinstance(value, list):
            self._goods_list = list()
            for i in value:
                if isinstance(i, StandardGoodsInfo):
                    self._goods_list.append(i)
                else:
                    self._goods_list.append(StandardGoodsInfo.from_alipay_dict(i))
    @property
    def merchant_mcc(self):
        return self._merchant_mcc

    @merchant_mcc.setter
    def merchant_mcc(self, value):
        self._merchant_mcc = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._order_amount = value
        else:
            self._order_amount = MultiCurrencyMoneyDTO.from_alipay_dict(value)
    @property
    def order_description(self):
        return self._order_description

    @order_description.setter
    def order_description(self, value):
        self._order_description = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def reference_merchant_id(self):
        return self._reference_merchant_id

    @reference_merchant_id.setter
    def reference_merchant_id(self, value):
        self._reference_merchant_id = value
    @property
    def settlement_strategy(self):
        return self._settlement_strategy

    @settlement_strategy.setter
    def settlement_strategy(self, value):
        if isinstance(value, SettlementStrategyDTO):
            self._settlement_strategy = value
        else:
            self._settlement_strategy = SettlementStrategyDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.goods_list:
            if isinstance(self.goods_list, list):
                for i in range(0, len(self.goods_list)):
                    element = self.goods_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_list, 'to_alipay_dict'):
                params['goods_list'] = self.goods_list.to_alipay_dict()
            else:
                params['goods_list'] = self.goods_list
        if self.merchant_mcc:
            if hasattr(self.merchant_mcc, 'to_alipay_dict'):
                params['merchant_mcc'] = self.merchant_mcc.to_alipay_dict()
            else:
                params['merchant_mcc'] = self.merchant_mcc
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_description:
            if hasattr(self.order_description, 'to_alipay_dict'):
                params['order_description'] = self.order_description.to_alipay_dict()
            else:
                params['order_description'] = self.order_description
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.reference_merchant_id:
            if hasattr(self.reference_merchant_id, 'to_alipay_dict'):
                params['reference_merchant_id'] = self.reference_merchant_id.to_alipay_dict()
            else:
                params['reference_merchant_id'] = self.reference_merchant_id
        if self.settlement_strategy:
            if hasattr(self.settlement_strategy, 'to_alipay_dict'):
                params['settlement_strategy'] = self.settlement_strategy.to_alipay_dict()
            else:
                params['settlement_strategy'] = self.settlement_strategy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoyagerOrderInfoDTO()
        if 'goods_list' in d:
            o.goods_list = d['goods_list']
        if 'merchant_mcc' in d:
            o.merchant_mcc = d['merchant_mcc']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_description' in d:
            o.order_description = d['order_description']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'reference_merchant_id' in d:
            o.reference_merchant_id = d['reference_merchant_id']
        if 'settlement_strategy' in d:
            o.settlement_strategy = d['settlement_strategy']
        return o


