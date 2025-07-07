#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MallSkuAttrValue import MallSkuAttrValue
from alipay.aop.api.domain.MallLadderPriceDTO import MallLadderPriceDTO


class MallGoodsPrice(object):

    def __init__(self):
        self._attr_value_list = None
        self._contract_code = None
        self._currency_code = None
        self._effective_date = None
        self._expire_date = None
        self._goods_id = None
        self._goods_quotation_id = None
        self._is_ladder_price = None
        self._ladder_price_list = None
        self._product_name = None
        self._sku_id = None
        self._supplier_code = None
        self._supplier_id = None
        self._tax_rate = None
        self._unit_price = None

    @property
    def attr_value_list(self):
        return self._attr_value_list

    @attr_value_list.setter
    def attr_value_list(self, value):
        if isinstance(value, list):
            self._attr_value_list = list()
            for i in value:
                if isinstance(i, MallSkuAttrValue):
                    self._attr_value_list.append(i)
                else:
                    self._attr_value_list.append(MallSkuAttrValue.from_alipay_dict(i))
    @property
    def contract_code(self):
        return self._contract_code

    @contract_code.setter
    def contract_code(self, value):
        self._contract_code = value
    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value
    @property
    def effective_date(self):
        return self._effective_date

    @effective_date.setter
    def effective_date(self, value):
        self._effective_date = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_quotation_id(self):
        return self._goods_quotation_id

    @goods_quotation_id.setter
    def goods_quotation_id(self, value):
        self._goods_quotation_id = value
    @property
    def is_ladder_price(self):
        return self._is_ladder_price

    @is_ladder_price.setter
    def is_ladder_price(self, value):
        self._is_ladder_price = value
    @property
    def ladder_price_list(self):
        return self._ladder_price_list

    @ladder_price_list.setter
    def ladder_price_list(self, value):
        if isinstance(value, list):
            self._ladder_price_list = list()
            for i in value:
                if isinstance(i, MallLadderPriceDTO):
                    self._ladder_price_list.append(i)
                else:
                    self._ladder_price_list.append(MallLadderPriceDTO.from_alipay_dict(i))
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def supplier_code(self):
        return self._supplier_code

    @supplier_code.setter
    def supplier_code(self, value):
        self._supplier_code = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.attr_value_list:
            if isinstance(self.attr_value_list, list):
                for i in range(0, len(self.attr_value_list)):
                    element = self.attr_value_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attr_value_list[i] = element.to_alipay_dict()
            if hasattr(self.attr_value_list, 'to_alipay_dict'):
                params['attr_value_list'] = self.attr_value_list.to_alipay_dict()
            else:
                params['attr_value_list'] = self.attr_value_list
        if self.contract_code:
            if hasattr(self.contract_code, 'to_alipay_dict'):
                params['contract_code'] = self.contract_code.to_alipay_dict()
            else:
                params['contract_code'] = self.contract_code
        if self.currency_code:
            if hasattr(self.currency_code, 'to_alipay_dict'):
                params['currency_code'] = self.currency_code.to_alipay_dict()
            else:
                params['currency_code'] = self.currency_code
        if self.effective_date:
            if hasattr(self.effective_date, 'to_alipay_dict'):
                params['effective_date'] = self.effective_date.to_alipay_dict()
            else:
                params['effective_date'] = self.effective_date
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_quotation_id:
            if hasattr(self.goods_quotation_id, 'to_alipay_dict'):
                params['goods_quotation_id'] = self.goods_quotation_id.to_alipay_dict()
            else:
                params['goods_quotation_id'] = self.goods_quotation_id
        if self.is_ladder_price:
            if hasattr(self.is_ladder_price, 'to_alipay_dict'):
                params['is_ladder_price'] = self.is_ladder_price.to_alipay_dict()
            else:
                params['is_ladder_price'] = self.is_ladder_price
        if self.ladder_price_list:
            if isinstance(self.ladder_price_list, list):
                for i in range(0, len(self.ladder_price_list)):
                    element = self.ladder_price_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ladder_price_list[i] = element.to_alipay_dict()
            if hasattr(self.ladder_price_list, 'to_alipay_dict'):
                params['ladder_price_list'] = self.ladder_price_list.to_alipay_dict()
            else:
                params['ladder_price_list'] = self.ladder_price_list
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.supplier_code:
            if hasattr(self.supplier_code, 'to_alipay_dict'):
                params['supplier_code'] = self.supplier_code.to_alipay_dict()
            else:
                params['supplier_code'] = self.supplier_code
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MallGoodsPrice()
        if 'attr_value_list' in d:
            o.attr_value_list = d['attr_value_list']
        if 'contract_code' in d:
            o.contract_code = d['contract_code']
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        if 'effective_date' in d:
            o.effective_date = d['effective_date']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_quotation_id' in d:
            o.goods_quotation_id = d['goods_quotation_id']
        if 'is_ladder_price' in d:
            o.is_ladder_price = d['is_ladder_price']
        if 'ladder_price_list' in d:
            o.ladder_price_list = d['ladder_price_list']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'supplier_code' in d:
            o.supplier_code = d['supplier_code']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


