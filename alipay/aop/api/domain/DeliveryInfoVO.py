#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryItemInfoVO import DeliveryItemInfoVO


class DeliveryInfoVO(object):

    def __init__(self):
        self._delivery_id = None
        self._item_info_list = None
        self._waybill_id = None

    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
    @property
    def item_info_list(self):
        return self._item_info_list

    @item_info_list.setter
    def item_info_list(self, value):
        if isinstance(value, list):
            self._item_info_list = list()
            for i in value:
                if isinstance(i, DeliveryItemInfoVO):
                    self._item_info_list.append(i)
                else:
                    self._item_info_list.append(DeliveryItemInfoVO.from_alipay_dict(i))
    @property
    def waybill_id(self):
        return self._waybill_id

    @waybill_id.setter
    def waybill_id(self, value):
        self._waybill_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_id:
            if hasattr(self.delivery_id, 'to_alipay_dict'):
                params['delivery_id'] = self.delivery_id.to_alipay_dict()
            else:
                params['delivery_id'] = self.delivery_id
        if self.item_info_list:
            if isinstance(self.item_info_list, list):
                for i in range(0, len(self.item_info_list)):
                    element = self.item_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_info_list[i] = element.to_alipay_dict()
            if hasattr(self.item_info_list, 'to_alipay_dict'):
                params['item_info_list'] = self.item_info_list.to_alipay_dict()
            else:
                params['item_info_list'] = self.item_info_list
        if self.waybill_id:
            if hasattr(self.waybill_id, 'to_alipay_dict'):
                params['waybill_id'] = self.waybill_id.to_alipay_dict()
            else:
                params['waybill_id'] = self.waybill_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryInfoVO()
        if 'delivery_id' in d:
            o.delivery_id = d['delivery_id']
        if 'item_info_list' in d:
            o.item_info_list = d['item_info_list']
        if 'waybill_id' in d:
            o.waybill_id = d['waybill_id']
        return o


