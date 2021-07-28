#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizfmcgGoods import BizfmcgGoods


class AlipayCommerceGoodsVoucherBatchqueryModel(object):

    def __init__(self):
        self._goods_list = None
        self._isv_pid = None
        self._merchant_pid = None

    @property
    def goods_list(self):
        return self._goods_list

    @goods_list.setter
    def goods_list(self, value):
        if isinstance(value, BizfmcgGoods):
            self._goods_list = value
        else:
            self._goods_list = BizfmcgGoods.from_alipay_dict(value)
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_list:
            if hasattr(self.goods_list, 'to_alipay_dict'):
                params['goods_list'] = self.goods_list.to_alipay_dict()
            else:
                params['goods_list'] = self.goods_list
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceGoodsVoucherBatchqueryModel()
        if 'goods_list' in d:
            o.goods_list = d['goods_list']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        return o


