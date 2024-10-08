#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GroupBuyInfo import GroupBuyInfo
from alipay.aop.api.domain.OrderItemInfoVO import OrderItemInfoVO
from alipay.aop.api.domain.OrderTagInfo import OrderTagInfo
from alipay.aop.api.domain.PayInfoVO import PayInfoVO
from alipay.aop.api.domain.PriceInfoVO import PriceInfoVO
from alipay.aop.api.domain.PromoApplyInfoVO import PromoApplyInfoVO
from alipay.aop.api.domain.PromoInfoVO import PromoInfoVO


class OrderDetailInfoVO(object):

    def __init__(self):
        self._group_buy_info = None
        self._item_infos = None
        self._order_tag_info = None
        self._pay_info = None
        self._price_info = None
        self._promo_apply_info = None
        self._promo_info = None

    @property
    def group_buy_info(self):
        return self._group_buy_info

    @group_buy_info.setter
    def group_buy_info(self, value):
        if isinstance(value, GroupBuyInfo):
            self._group_buy_info = value
        else:
            self._group_buy_info = GroupBuyInfo.from_alipay_dict(value)
    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, OrderItemInfoVO):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(OrderItemInfoVO.from_alipay_dict(i))
    @property
    def order_tag_info(self):
        return self._order_tag_info

    @order_tag_info.setter
    def order_tag_info(self, value):
        if isinstance(value, OrderTagInfo):
            self._order_tag_info = value
        else:
            self._order_tag_info = OrderTagInfo.from_alipay_dict(value)
    @property
    def pay_info(self):
        return self._pay_info

    @pay_info.setter
    def pay_info(self, value):
        if isinstance(value, PayInfoVO):
            self._pay_info = value
        else:
            self._pay_info = PayInfoVO.from_alipay_dict(value)
    @property
    def price_info(self):
        return self._price_info

    @price_info.setter
    def price_info(self, value):
        if isinstance(value, PriceInfoVO):
            self._price_info = value
        else:
            self._price_info = PriceInfoVO.from_alipay_dict(value)
    @property
    def promo_apply_info(self):
        return self._promo_apply_info

    @promo_apply_info.setter
    def promo_apply_info(self, value):
        if isinstance(value, PromoApplyInfoVO):
            self._promo_apply_info = value
        else:
            self._promo_apply_info = PromoApplyInfoVO.from_alipay_dict(value)
    @property
    def promo_info(self):
        return self._promo_info

    @promo_info.setter
    def promo_info(self, value):
        if isinstance(value, PromoInfoVO):
            self._promo_info = value
        else:
            self._promo_info = PromoInfoVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.group_buy_info:
            if hasattr(self.group_buy_info, 'to_alipay_dict'):
                params['group_buy_info'] = self.group_buy_info.to_alipay_dict()
            else:
                params['group_buy_info'] = self.group_buy_info
        if self.item_infos:
            if isinstance(self.item_infos, list):
                for i in range(0, len(self.item_infos)):
                    element = self.item_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_infos[i] = element.to_alipay_dict()
            if hasattr(self.item_infos, 'to_alipay_dict'):
                params['item_infos'] = self.item_infos.to_alipay_dict()
            else:
                params['item_infos'] = self.item_infos
        if self.order_tag_info:
            if hasattr(self.order_tag_info, 'to_alipay_dict'):
                params['order_tag_info'] = self.order_tag_info.to_alipay_dict()
            else:
                params['order_tag_info'] = self.order_tag_info
        if self.pay_info:
            if hasattr(self.pay_info, 'to_alipay_dict'):
                params['pay_info'] = self.pay_info.to_alipay_dict()
            else:
                params['pay_info'] = self.pay_info
        if self.price_info:
            if hasattr(self.price_info, 'to_alipay_dict'):
                params['price_info'] = self.price_info.to_alipay_dict()
            else:
                params['price_info'] = self.price_info
        if self.promo_apply_info:
            if hasattr(self.promo_apply_info, 'to_alipay_dict'):
                params['promo_apply_info'] = self.promo_apply_info.to_alipay_dict()
            else:
                params['promo_apply_info'] = self.promo_apply_info
        if self.promo_info:
            if hasattr(self.promo_info, 'to_alipay_dict'):
                params['promo_info'] = self.promo_info.to_alipay_dict()
            else:
                params['promo_info'] = self.promo_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderDetailInfoVO()
        if 'group_buy_info' in d:
            o.group_buy_info = d['group_buy_info']
        if 'item_infos' in d:
            o.item_infos = d['item_infos']
        if 'order_tag_info' in d:
            o.order_tag_info = d['order_tag_info']
        if 'pay_info' in d:
            o.pay_info = d['pay_info']
        if 'price_info' in d:
            o.price_info = d['price_info']
        if 'promo_apply_info' in d:
            o.promo_apply_info = d['promo_apply_info']
        if 'promo_info' in d:
            o.promo_info = d['promo_info']
        return o


