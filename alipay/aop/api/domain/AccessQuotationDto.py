#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccessLadderPriceDto import AccessLadderPriceDto
from alipay.aop.api.domain.AccessSkuAttrValueDto import AccessSkuAttrValueDto


class AccessQuotationDto(object):

    def __init__(self):
        self._currency_code = None
        self._effective_date = None
        self._expire_date = None
        self._ladder_price = None
        self._ladder_price_list = None
        self._origin_unit_price = None
        self._sku_attr_value_list = None
        self._source_sku_id = None
        self._unit_price = None

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
    def ladder_price(self):
        return self._ladder_price

    @ladder_price.setter
    def ladder_price(self, value):
        self._ladder_price = value
    @property
    def ladder_price_list(self):
        return self._ladder_price_list

    @ladder_price_list.setter
    def ladder_price_list(self, value):
        if isinstance(value, list):
            self._ladder_price_list = list()
            for i in value:
                if isinstance(i, AccessLadderPriceDto):
                    self._ladder_price_list.append(i)
                else:
                    self._ladder_price_list.append(AccessLadderPriceDto.from_alipay_dict(i))
    @property
    def origin_unit_price(self):
        return self._origin_unit_price

    @origin_unit_price.setter
    def origin_unit_price(self, value):
        self._origin_unit_price = value
    @property
    def sku_attr_value_list(self):
        return self._sku_attr_value_list

    @sku_attr_value_list.setter
    def sku_attr_value_list(self, value):
        if isinstance(value, list):
            self._sku_attr_value_list = list()
            for i in value:
                if isinstance(i, AccessSkuAttrValueDto):
                    self._sku_attr_value_list.append(i)
                else:
                    self._sku_attr_value_list.append(AccessSkuAttrValueDto.from_alipay_dict(i))
    @property
    def source_sku_id(self):
        return self._source_sku_id

    @source_sku_id.setter
    def source_sku_id(self, value):
        self._source_sku_id = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.ladder_price:
            if hasattr(self.ladder_price, 'to_alipay_dict'):
                params['ladder_price'] = self.ladder_price.to_alipay_dict()
            else:
                params['ladder_price'] = self.ladder_price
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
        if self.origin_unit_price:
            if hasattr(self.origin_unit_price, 'to_alipay_dict'):
                params['origin_unit_price'] = self.origin_unit_price.to_alipay_dict()
            else:
                params['origin_unit_price'] = self.origin_unit_price
        if self.sku_attr_value_list:
            if isinstance(self.sku_attr_value_list, list):
                for i in range(0, len(self.sku_attr_value_list)):
                    element = self.sku_attr_value_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_attr_value_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_attr_value_list, 'to_alipay_dict'):
                params['sku_attr_value_list'] = self.sku_attr_value_list.to_alipay_dict()
            else:
                params['sku_attr_value_list'] = self.sku_attr_value_list
        if self.source_sku_id:
            if hasattr(self.source_sku_id, 'to_alipay_dict'):
                params['source_sku_id'] = self.source_sku_id.to_alipay_dict()
            else:
                params['source_sku_id'] = self.source_sku_id
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
        o = AccessQuotationDto()
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        if 'effective_date' in d:
            o.effective_date = d['effective_date']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'ladder_price' in d:
            o.ladder_price = d['ladder_price']
        if 'ladder_price_list' in d:
            o.ladder_price_list = d['ladder_price_list']
        if 'origin_unit_price' in d:
            o.origin_unit_price = d['origin_unit_price']
        if 'sku_attr_value_list' in d:
            o.sku_attr_value_list = d['sku_attr_value_list']
        if 'source_sku_id' in d:
            o.source_sku_id = d['source_sku_id']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


