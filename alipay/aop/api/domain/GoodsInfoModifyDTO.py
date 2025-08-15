#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AttrExtInfoDTO import AttrExtInfoDTO
from alipay.aop.api.domain.RentInfoDTO import RentInfoDTO


class GoodsInfoModifyDTO(object):

    def __init__(self):
        self._attr_ext_info_list = None
        self._inspect_price = None
        self._out_item_id = None
        self._out_sku_id = None
        self._recycle_status = None
        self._rent_info = None

    @property
    def attr_ext_info_list(self):
        return self._attr_ext_info_list

    @attr_ext_info_list.setter
    def attr_ext_info_list(self, value):
        if isinstance(value, list):
            self._attr_ext_info_list = list()
            for i in value:
                if isinstance(i, AttrExtInfoDTO):
                    self._attr_ext_info_list.append(i)
                else:
                    self._attr_ext_info_list.append(AttrExtInfoDTO.from_alipay_dict(i))
    @property
    def inspect_price(self):
        return self._inspect_price

    @inspect_price.setter
    def inspect_price(self, value):
        self._inspect_price = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def recycle_status(self):
        return self._recycle_status

    @recycle_status.setter
    def recycle_status(self, value):
        self._recycle_status = value
    @property
    def rent_info(self):
        return self._rent_info

    @rent_info.setter
    def rent_info(self, value):
        if isinstance(value, RentInfoDTO):
            self._rent_info = value
        else:
            self._rent_info = RentInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.attr_ext_info_list:
            if isinstance(self.attr_ext_info_list, list):
                for i in range(0, len(self.attr_ext_info_list)):
                    element = self.attr_ext_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attr_ext_info_list[i] = element.to_alipay_dict()
            if hasattr(self.attr_ext_info_list, 'to_alipay_dict'):
                params['attr_ext_info_list'] = self.attr_ext_info_list.to_alipay_dict()
            else:
                params['attr_ext_info_list'] = self.attr_ext_info_list
        if self.inspect_price:
            if hasattr(self.inspect_price, 'to_alipay_dict'):
                params['inspect_price'] = self.inspect_price.to_alipay_dict()
            else:
                params['inspect_price'] = self.inspect_price
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.recycle_status:
            if hasattr(self.recycle_status, 'to_alipay_dict'):
                params['recycle_status'] = self.recycle_status.to_alipay_dict()
            else:
                params['recycle_status'] = self.recycle_status
        if self.rent_info:
            if hasattr(self.rent_info, 'to_alipay_dict'):
                params['rent_info'] = self.rent_info.to_alipay_dict()
            else:
                params['rent_info'] = self.rent_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsInfoModifyDTO()
        if 'attr_ext_info_list' in d:
            o.attr_ext_info_list = d['attr_ext_info_list']
        if 'inspect_price' in d:
            o.inspect_price = d['inspect_price']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'recycle_status' in d:
            o.recycle_status = d['recycle_status']
        if 'rent_info' in d:
            o.rent_info = d['rent_info']
        return o


