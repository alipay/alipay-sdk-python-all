#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNordermaterialsDeliveryUploadModel(object):

    def __init__(self):
        self._delivery_address = None
        self._logistics_code = None
        self._materials_count = None
        self._production_order_no = None
        self._receiver_name = None
        self._receiver_phone = None
        self._shop_order_no = None
        self._tracking_number = None

    @property
    def delivery_address(self):
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, value):
        self._delivery_address = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def materials_count(self):
        return self._materials_count

    @materials_count.setter
    def materials_count(self, value):
        self._materials_count = value
    @property
    def production_order_no(self):
        return self._production_order_no

    @production_order_no.setter
    def production_order_no(self, value):
        self._production_order_no = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value
    @property
    def receiver_phone(self):
        return self._receiver_phone

    @receiver_phone.setter
    def receiver_phone(self, value):
        self._receiver_phone = value
    @property
    def shop_order_no(self):
        return self._shop_order_no

    @shop_order_no.setter
    def shop_order_no(self, value):
        self._shop_order_no = value
    @property
    def tracking_number(self):
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, value):
        self._tracking_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_address:
            if hasattr(self.delivery_address, 'to_alipay_dict'):
                params['delivery_address'] = self.delivery_address.to_alipay_dict()
            else:
                params['delivery_address'] = self.delivery_address
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.materials_count:
            if hasattr(self.materials_count, 'to_alipay_dict'):
                params['materials_count'] = self.materials_count.to_alipay_dict()
            else:
                params['materials_count'] = self.materials_count
        if self.production_order_no:
            if hasattr(self.production_order_no, 'to_alipay_dict'):
                params['production_order_no'] = self.production_order_no.to_alipay_dict()
            else:
                params['production_order_no'] = self.production_order_no
        if self.receiver_name:
            if hasattr(self.receiver_name, 'to_alipay_dict'):
                params['receiver_name'] = self.receiver_name.to_alipay_dict()
            else:
                params['receiver_name'] = self.receiver_name
        if self.receiver_phone:
            if hasattr(self.receiver_phone, 'to_alipay_dict'):
                params['receiver_phone'] = self.receiver_phone.to_alipay_dict()
            else:
                params['receiver_phone'] = self.receiver_phone
        if self.shop_order_no:
            if hasattr(self.shop_order_no, 'to_alipay_dict'):
                params['shop_order_no'] = self.shop_order_no.to_alipay_dict()
            else:
                params['shop_order_no'] = self.shop_order_no
        if self.tracking_number:
            if hasattr(self.tracking_number, 'to_alipay_dict'):
                params['tracking_number'] = self.tracking_number.to_alipay_dict()
            else:
                params['tracking_number'] = self.tracking_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNordermaterialsDeliveryUploadModel()
        if 'delivery_address' in d:
            o.delivery_address = d['delivery_address']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'materials_count' in d:
            o.materials_count = d['materials_count']
        if 'production_order_no' in d:
            o.production_order_no = d['production_order_no']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'receiver_phone' in d:
            o.receiver_phone = d['receiver_phone']
        if 'shop_order_no' in d:
            o.shop_order_no = d['shop_order_no']
        if 'tracking_number' in d:
            o.tracking_number = d['tracking_number']
        return o


