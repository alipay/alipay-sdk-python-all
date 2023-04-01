#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniGoodsDetailInfoDTO import MiniGoodsDetailInfoDTO
from alipay.aop.api.domain.PayInfoDTO import PayInfoDTO
from alipay.aop.api.domain.PriceInfoDTO import PriceInfoDTO


class MiniOrderDetailDTO(object):

    def __init__(self):
        self._item_infos = None
        self._pay_info = None
        self._price_info = None

    @property
    def item_infos(self):
        return self._item_infos

    @item_infos.setter
    def item_infos(self, value):
        if isinstance(value, list):
            self._item_infos = list()
            for i in value:
                if isinstance(i, MiniGoodsDetailInfoDTO):
                    self._item_infos.append(i)
                else:
                    self._item_infos.append(MiniGoodsDetailInfoDTO.from_alipay_dict(i))
    @property
    def pay_info(self):
        return self._pay_info

    @pay_info.setter
    def pay_info(self, value):
        if isinstance(value, PayInfoDTO):
            self._pay_info = value
        else:
            self._pay_info = PayInfoDTO.from_alipay_dict(value)
    @property
    def price_info(self):
        return self._price_info

    @price_info.setter
    def price_info(self, value):
        if isinstance(value, PriceInfoDTO):
            self._price_info = value
        else:
            self._price_info = PriceInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniOrderDetailDTO()
        if 'item_infos' in d:
            o.item_infos = d['item_infos']
        if 'pay_info' in d:
            o.pay_info = d['pay_info']
        if 'price_info' in d:
            o.price_info = d['price_info']
        return o


