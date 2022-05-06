#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GoodsInfoDTO import GoodsInfoDTO


class UserTradeInfoDTO(object):

    def __init__(self):
        self._goods_info_list = None
        self._partner_id = None
        self._risk_level = None
        self._trade_amount = None
        self._trade_no = None
        self._trade_time = None
        self._unfiltered_total_goods_count = None
        self._user_id = None

    @property
    def goods_info_list(self):
        return self._goods_info_list

    @goods_info_list.setter
    def goods_info_list(self, value):
        if isinstance(value, list):
            self._goods_info_list = list()
            for i in value:
                if isinstance(i, GoodsInfoDTO):
                    self._goods_info_list.append(i)
                else:
                    self._goods_info_list.append(GoodsInfoDTO.from_alipay_dict(i))
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value
    @property
    def unfiltered_total_goods_count(self):
        return self._unfiltered_total_goods_count

    @unfiltered_total_goods_count.setter
    def unfiltered_total_goods_count(self, value):
        self._unfiltered_total_goods_count = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_info_list:
            if isinstance(self.goods_info_list, list):
                for i in range(0, len(self.goods_info_list)):
                    element = self.goods_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_info_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_info_list, 'to_alipay_dict'):
                params['goods_info_list'] = self.goods_info_list.to_alipay_dict()
            else:
                params['goods_info_list'] = self.goods_info_list
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
        if self.unfiltered_total_goods_count:
            if hasattr(self.unfiltered_total_goods_count, 'to_alipay_dict'):
                params['unfiltered_total_goods_count'] = self.unfiltered_total_goods_count.to_alipay_dict()
            else:
                params['unfiltered_total_goods_count'] = self.unfiltered_total_goods_count
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserTradeInfoDTO()
        if 'goods_info_list' in d:
            o.goods_info_list = d['goods_info_list']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        if 'unfiltered_total_goods_count' in d:
            o.unfiltered_total_goods_count = d['unfiltered_total_goods_count']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


