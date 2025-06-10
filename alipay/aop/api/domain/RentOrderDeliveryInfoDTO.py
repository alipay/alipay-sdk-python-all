#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentPickupShopInfoDTO import RentPickupShopInfoDTO


class RentOrderDeliveryInfoDTO(object):

    def __init__(self):
        self._delivery_end_time = None
        self._delivery_start_time = None
        self._delivery_type = None
        self._shop_info = None

    @property
    def delivery_end_time(self):
        return self._delivery_end_time

    @delivery_end_time.setter
    def delivery_end_time(self, value):
        self._delivery_end_time = value
    @property
    def delivery_start_time(self):
        return self._delivery_start_time

    @delivery_start_time.setter
    def delivery_start_time(self, value):
        self._delivery_start_time = value
    @property
    def delivery_type(self):
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, value):
        self._delivery_type = value
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, RentPickupShopInfoDTO):
            self._shop_info = value
        else:
            self._shop_info = RentPickupShopInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_end_time:
            if hasattr(self.delivery_end_time, 'to_alipay_dict'):
                params['delivery_end_time'] = self.delivery_end_time.to_alipay_dict()
            else:
                params['delivery_end_time'] = self.delivery_end_time
        if self.delivery_start_time:
            if hasattr(self.delivery_start_time, 'to_alipay_dict'):
                params['delivery_start_time'] = self.delivery_start_time.to_alipay_dict()
            else:
                params['delivery_start_time'] = self.delivery_start_time
        if self.delivery_type:
            if hasattr(self.delivery_type, 'to_alipay_dict'):
                params['delivery_type'] = self.delivery_type.to_alipay_dict()
            else:
                params['delivery_type'] = self.delivery_type
        if self.shop_info:
            if hasattr(self.shop_info, 'to_alipay_dict'):
                params['shop_info'] = self.shop_info.to_alipay_dict()
            else:
                params['shop_info'] = self.shop_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentOrderDeliveryInfoDTO()
        if 'delivery_end_time' in d:
            o.delivery_end_time = d['delivery_end_time']
        if 'delivery_start_time' in d:
            o.delivery_start_time = d['delivery_start_time']
        if 'delivery_type' in d:
            o.delivery_type = d['delivery_type']
        if 'shop_info' in d:
            o.shop_info = d['shop_info']
        return o


