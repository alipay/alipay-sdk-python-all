#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO


class VoyagerPriceInfoDTO(object):

    def __init__(self):
        self._discount_percentage = None
        self._original_price = None
        self._original_sale_price = None
        self._promo_discount_price = None
        self._sale_price = None
        self._supplier_discount_price = None
        self._total_discount_price = None

    @property
    def discount_percentage(self):
        return self._discount_percentage

    @discount_percentage.setter
    def discount_percentage(self, value):
        self._discount_percentage = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._original_price = value
        else:
            self._original_price = MultiCurrencyMoneyDTO.from_alipay_dict(value)
    @property
    def original_sale_price(self):
        return self._original_sale_price

    @original_sale_price.setter
    def original_sale_price(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._original_sale_price = value
        else:
            self._original_sale_price = MultiCurrencyMoneyDTO.from_alipay_dict(value)
    @property
    def promo_discount_price(self):
        return self._promo_discount_price

    @promo_discount_price.setter
    def promo_discount_price(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._promo_discount_price = value
        else:
            self._promo_discount_price = MultiCurrencyMoneyDTO.from_alipay_dict(value)
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._sale_price = value
        else:
            self._sale_price = MultiCurrencyMoneyDTO.from_alipay_dict(value)
    @property
    def supplier_discount_price(self):
        return self._supplier_discount_price

    @supplier_discount_price.setter
    def supplier_discount_price(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._supplier_discount_price = value
        else:
            self._supplier_discount_price = MultiCurrencyMoneyDTO.from_alipay_dict(value)
    @property
    def total_discount_price(self):
        return self._total_discount_price

    @total_discount_price.setter
    def total_discount_price(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._total_discount_price = value
        else:
            self._total_discount_price = MultiCurrencyMoneyDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.discount_percentage:
            if hasattr(self.discount_percentage, 'to_alipay_dict'):
                params['discount_percentage'] = self.discount_percentage.to_alipay_dict()
            else:
                params['discount_percentage'] = self.discount_percentage
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.original_sale_price:
            if hasattr(self.original_sale_price, 'to_alipay_dict'):
                params['original_sale_price'] = self.original_sale_price.to_alipay_dict()
            else:
                params['original_sale_price'] = self.original_sale_price
        if self.promo_discount_price:
            if hasattr(self.promo_discount_price, 'to_alipay_dict'):
                params['promo_discount_price'] = self.promo_discount_price.to_alipay_dict()
            else:
                params['promo_discount_price'] = self.promo_discount_price
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.supplier_discount_price:
            if hasattr(self.supplier_discount_price, 'to_alipay_dict'):
                params['supplier_discount_price'] = self.supplier_discount_price.to_alipay_dict()
            else:
                params['supplier_discount_price'] = self.supplier_discount_price
        if self.total_discount_price:
            if hasattr(self.total_discount_price, 'to_alipay_dict'):
                params['total_discount_price'] = self.total_discount_price.to_alipay_dict()
            else:
                params['total_discount_price'] = self.total_discount_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoyagerPriceInfoDTO()
        if 'discount_percentage' in d:
            o.discount_percentage = d['discount_percentage']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'original_sale_price' in d:
            o.original_sale_price = d['original_sale_price']
        if 'promo_discount_price' in d:
            o.promo_discount_price = d['promo_discount_price']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'supplier_discount_price' in d:
            o.supplier_discount_price = d['supplier_discount_price']
        if 'total_discount_price' in d:
            o.total_discount_price = d['total_discount_price']
        return o


