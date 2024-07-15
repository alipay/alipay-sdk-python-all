#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalShopDeliveryInfo import MedicalShopDeliveryInfo


class AlipayCommerceMedicalMedicineShopdeliveryModifyModel(object):

    def __init__(self):
        self._delivery_info = None
        self._out_store_id = None
        self._shop_id = None

    @property
    def delivery_info(self):
        return self._delivery_info

    @delivery_info.setter
    def delivery_info(self, value):
        if isinstance(value, list):
            self._delivery_info = list()
            for i in value:
                if isinstance(i, MedicalShopDeliveryInfo):
                    self._delivery_info.append(i)
                else:
                    self._delivery_info.append(MedicalShopDeliveryInfo.from_alipay_dict(i))
    @property
    def out_store_id(self):
        return self._out_store_id

    @out_store_id.setter
    def out_store_id(self, value):
        self._out_store_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_info:
            if isinstance(self.delivery_info, list):
                for i in range(0, len(self.delivery_info)):
                    element = self.delivery_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_info[i] = element.to_alipay_dict()
            if hasattr(self.delivery_info, 'to_alipay_dict'):
                params['delivery_info'] = self.delivery_info.to_alipay_dict()
            else:
                params['delivery_info'] = self.delivery_info
        if self.out_store_id:
            if hasattr(self.out_store_id, 'to_alipay_dict'):
                params['out_store_id'] = self.out_store_id.to_alipay_dict()
            else:
                params['out_store_id'] = self.out_store_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedicineShopdeliveryModifyModel()
        if 'delivery_info' in d:
            o.delivery_info = d['delivery_info']
        if 'out_store_id' in d:
            o.out_store_id = d['out_store_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


