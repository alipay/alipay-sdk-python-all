#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtInfoPair import ExtInfoPair
from alipay.aop.api.domain.ItemPromoInfoSyncRequest import ItemPromoInfoSyncRequest
from alipay.aop.api.domain.ExtInfoPair import ExtInfoPair


class IndustryItemSkuSyncRequest(object):

    def __init__(self):
        self._ext_info = None
        self._origin_price = None
        self._price = None
        self._price_unit = None
        self._promo_infos = None
        self._sell_status = None
        self._sku_attrs = None
        self._sku_id = None
        self._sku_image = None
        self._sku_name = None
        self._stock_num = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ExtInfoPair):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ExtInfoPair.from_alipay_dict(i))
    @property
    def origin_price(self):
        return self._origin_price

    @origin_price.setter
    def origin_price(self, value):
        self._origin_price = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def price_unit(self):
        return self._price_unit

    @price_unit.setter
    def price_unit(self, value):
        self._price_unit = value
    @property
    def promo_infos(self):
        return self._promo_infos

    @promo_infos.setter
    def promo_infos(self, value):
        if isinstance(value, list):
            self._promo_infos = list()
            for i in value:
                if isinstance(i, ItemPromoInfoSyncRequest):
                    self._promo_infos.append(i)
                else:
                    self._promo_infos.append(ItemPromoInfoSyncRequest.from_alipay_dict(i))
    @property
    def sell_status(self):
        return self._sell_status

    @sell_status.setter
    def sell_status(self, value):
        self._sell_status = value
    @property
    def sku_attrs(self):
        return self._sku_attrs

    @sku_attrs.setter
    def sku_attrs(self, value):
        if isinstance(value, list):
            self._sku_attrs = list()
            for i in value:
                if isinstance(i, ExtInfoPair):
                    self._sku_attrs.append(i)
                else:
                    self._sku_attrs.append(ExtInfoPair.from_alipay_dict(i))
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_image(self):
        return self._sku_image

    @sku_image.setter
    def sku_image(self, value):
        self._sku_image = value
    @property
    def sku_name(self):
        return self._sku_name

    @sku_name.setter
    def sku_name(self, value):
        self._sku_name = value
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.origin_price:
            if hasattr(self.origin_price, 'to_alipay_dict'):
                params['origin_price'] = self.origin_price.to_alipay_dict()
            else:
                params['origin_price'] = self.origin_price
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.price_unit:
            if hasattr(self.price_unit, 'to_alipay_dict'):
                params['price_unit'] = self.price_unit.to_alipay_dict()
            else:
                params['price_unit'] = self.price_unit
        if self.promo_infos:
            if isinstance(self.promo_infos, list):
                for i in range(0, len(self.promo_infos)):
                    element = self.promo_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_infos[i] = element.to_alipay_dict()
            if hasattr(self.promo_infos, 'to_alipay_dict'):
                params['promo_infos'] = self.promo_infos.to_alipay_dict()
            else:
                params['promo_infos'] = self.promo_infos
        if self.sell_status:
            if hasattr(self.sell_status, 'to_alipay_dict'):
                params['sell_status'] = self.sell_status.to_alipay_dict()
            else:
                params['sell_status'] = self.sell_status
        if self.sku_attrs:
            if isinstance(self.sku_attrs, list):
                for i in range(0, len(self.sku_attrs)):
                    element = self.sku_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_attrs[i] = element.to_alipay_dict()
            if hasattr(self.sku_attrs, 'to_alipay_dict'):
                params['sku_attrs'] = self.sku_attrs.to_alipay_dict()
            else:
                params['sku_attrs'] = self.sku_attrs
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_image:
            if hasattr(self.sku_image, 'to_alipay_dict'):
                params['sku_image'] = self.sku_image.to_alipay_dict()
            else:
                params['sku_image'] = self.sku_image
        if self.sku_name:
            if hasattr(self.sku_name, 'to_alipay_dict'):
                params['sku_name'] = self.sku_name.to_alipay_dict()
            else:
                params['sku_name'] = self.sku_name
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryItemSkuSyncRequest()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'origin_price' in d:
            o.origin_price = d['origin_price']
        if 'price' in d:
            o.price = d['price']
        if 'price_unit' in d:
            o.price_unit = d['price_unit']
        if 'promo_infos' in d:
            o.promo_infos = d['promo_infos']
        if 'sell_status' in d:
            o.sell_status = d['sell_status']
        if 'sku_attrs' in d:
            o.sku_attrs = d['sku_attrs']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_image' in d:
            o.sku_image = d['sku_image']
        if 'sku_name' in d:
            o.sku_name = d['sku_name']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        return o


