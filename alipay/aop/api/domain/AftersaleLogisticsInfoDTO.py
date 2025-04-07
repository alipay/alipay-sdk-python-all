#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SendOrderContactInfoDTO import SendOrderContactInfoDTO
from alipay.aop.api.domain.ShopInfoDTO import ShopInfoDTO


class AftersaleLogisticsInfoDTO(object):

    def __init__(self):
        self._delivery_id = None
        self._pick_up_code = None
        self._send_order_contact_info = None
        self._shop_info = None
        self._waybill_id = None

    @property
    def delivery_id(self):
        return self._delivery_id

    @delivery_id.setter
    def delivery_id(self, value):
        self._delivery_id = value
    @property
    def pick_up_code(self):
        return self._pick_up_code

    @pick_up_code.setter
    def pick_up_code(self, value):
        self._pick_up_code = value
    @property
    def send_order_contact_info(self):
        return self._send_order_contact_info

    @send_order_contact_info.setter
    def send_order_contact_info(self, value):
        if isinstance(value, SendOrderContactInfoDTO):
            self._send_order_contact_info = value
        else:
            self._send_order_contact_info = SendOrderContactInfoDTO.from_alipay_dict(value)
    @property
    def shop_info(self):
        return self._shop_info

    @shop_info.setter
    def shop_info(self, value):
        if isinstance(value, ShopInfoDTO):
            self._shop_info = value
        else:
            self._shop_info = ShopInfoDTO.from_alipay_dict(value)
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
        if self.pick_up_code:
            if hasattr(self.pick_up_code, 'to_alipay_dict'):
                params['pick_up_code'] = self.pick_up_code.to_alipay_dict()
            else:
                params['pick_up_code'] = self.pick_up_code
        if self.send_order_contact_info:
            if hasattr(self.send_order_contact_info, 'to_alipay_dict'):
                params['send_order_contact_info'] = self.send_order_contact_info.to_alipay_dict()
            else:
                params['send_order_contact_info'] = self.send_order_contact_info
        if self.shop_info:
            if hasattr(self.shop_info, 'to_alipay_dict'):
                params['shop_info'] = self.shop_info.to_alipay_dict()
            else:
                params['shop_info'] = self.shop_info
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
        o = AftersaleLogisticsInfoDTO()
        if 'delivery_id' in d:
            o.delivery_id = d['delivery_id']
        if 'pick_up_code' in d:
            o.pick_up_code = d['pick_up_code']
        if 'send_order_contact_info' in d:
            o.send_order_contact_info = d['send_order_contact_info']
        if 'shop_info' in d:
            o.shop_info = d['shop_info']
        if 'waybill_id' in d:
            o.waybill_id = d['waybill_id']
        return o


