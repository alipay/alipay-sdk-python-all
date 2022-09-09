#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcomBuyerDTO import EcomBuyerDTO
from alipay.aop.api.domain.EcomItemDTO import EcomItemDTO
from alipay.aop.api.domain.EcomSellerDTO import EcomSellerDTO


class InsureAdmitDTO(object):

    def __init__(self):
        self._buyer = None
        self._echo_key = None
        self._item = None
        self._seller = None

    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, EcomBuyerDTO):
            self._buyer = value
        else:
            self._buyer = EcomBuyerDTO.from_alipay_dict(value)
    @property
    def echo_key(self):
        return self._echo_key

    @echo_key.setter
    def echo_key(self, value):
        self._echo_key = value
    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        if isinstance(value, EcomItemDTO):
            self._item = value
        else:
            self._item = EcomItemDTO.from_alipay_dict(value)
    @property
    def seller(self):
        return self._seller

    @seller.setter
    def seller(self, value):
        if isinstance(value, EcomSellerDTO):
            self._seller = value
        else:
            self._seller = EcomSellerDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.echo_key:
            if hasattr(self.echo_key, 'to_alipay_dict'):
                params['echo_key'] = self.echo_key.to_alipay_dict()
            else:
                params['echo_key'] = self.echo_key
        if self.item:
            if hasattr(self.item, 'to_alipay_dict'):
                params['item'] = self.item.to_alipay_dict()
            else:
                params['item'] = self.item
        if self.seller:
            if hasattr(self.seller, 'to_alipay_dict'):
                params['seller'] = self.seller.to_alipay_dict()
            else:
                params['seller'] = self.seller
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsureAdmitDTO()
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'echo_key' in d:
            o.echo_key = d['echo_key']
        if 'item' in d:
            o.item = d['item']
        if 'seller' in d:
            o.seller = d['seller']
        return o


