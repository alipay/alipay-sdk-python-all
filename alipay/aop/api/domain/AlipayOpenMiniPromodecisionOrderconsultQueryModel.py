#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderDetailInfo import OrderDetailInfo
from alipay.aop.api.domain.OutPromoInfo import OutPromoInfo


class AlipayOpenMiniPromodecisionOrderconsultQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._order_detail_info = None
        self._out_promo_info = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_detail_info(self):
        return self._order_detail_info

    @order_detail_info.setter
    def order_detail_info(self, value):
        if isinstance(value, OrderDetailInfo):
            self._order_detail_info = value
        else:
            self._order_detail_info = OrderDetailInfo.from_alipay_dict(value)
    @property
    def out_promo_info(self):
        return self._out_promo_info

    @out_promo_info.setter
    def out_promo_info(self, value):
        if isinstance(value, OutPromoInfo):
            self._out_promo_info = value
        else:
            self._out_promo_info = OutPromoInfo.from_alipay_dict(value)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_detail_info:
            if hasattr(self.order_detail_info, 'to_alipay_dict'):
                params['order_detail_info'] = self.order_detail_info.to_alipay_dict()
            else:
                params['order_detail_info'] = self.order_detail_info
        if self.out_promo_info:
            if hasattr(self.out_promo_info, 'to_alipay_dict'):
                params['out_promo_info'] = self.out_promo_info.to_alipay_dict()
            else:
                params['out_promo_info'] = self.out_promo_info
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
        o = AlipayOpenMiniPromodecisionOrderconsultQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_detail_info' in d:
            o.order_detail_info = d['order_detail_info']
        if 'out_promo_info' in d:
            o.out_promo_info = d['out_promo_info']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


