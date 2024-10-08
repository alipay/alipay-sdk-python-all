#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopMaterialsInfo(object):

    def __init__(self):
        self._delivery_address = None
        self._desk_no = None
        self._materials_count = None
        self._materials_instance_id = None
        self._merchant_name = None
        self._nfc_url = None
        self._production_ext_info = None
        self._qr_code_url = None
        self._receiver_name = None
        self._receiver_phone = None
        self._shop_name = None
        self._shop_order_no = None
        self._shop_serial_number = None

    @property
    def delivery_address(self):
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, value):
        self._delivery_address = value
    @property
    def desk_no(self):
        return self._desk_no

    @desk_no.setter
    def desk_no(self, value):
        self._desk_no = value
    @property
    def materials_count(self):
        return self._materials_count

    @materials_count.setter
    def materials_count(self, value):
        self._materials_count = value
    @property
    def materials_instance_id(self):
        return self._materials_instance_id

    @materials_instance_id.setter
    def materials_instance_id(self, value):
        self._materials_instance_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def nfc_url(self):
        return self._nfc_url

    @nfc_url.setter
    def nfc_url(self, value):
        self._nfc_url = value
    @property
    def production_ext_info(self):
        return self._production_ext_info

    @production_ext_info.setter
    def production_ext_info(self, value):
        self._production_ext_info = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value
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
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_order_no(self):
        return self._shop_order_no

    @shop_order_no.setter
    def shop_order_no(self, value):
        self._shop_order_no = value
    @property
    def shop_serial_number(self):
        return self._shop_serial_number

    @shop_serial_number.setter
    def shop_serial_number(self, value):
        self._shop_serial_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_address:
            if hasattr(self.delivery_address, 'to_alipay_dict'):
                params['delivery_address'] = self.delivery_address.to_alipay_dict()
            else:
                params['delivery_address'] = self.delivery_address
        if self.desk_no:
            if hasattr(self.desk_no, 'to_alipay_dict'):
                params['desk_no'] = self.desk_no.to_alipay_dict()
            else:
                params['desk_no'] = self.desk_no
        if self.materials_count:
            if hasattr(self.materials_count, 'to_alipay_dict'):
                params['materials_count'] = self.materials_count.to_alipay_dict()
            else:
                params['materials_count'] = self.materials_count
        if self.materials_instance_id:
            if hasattr(self.materials_instance_id, 'to_alipay_dict'):
                params['materials_instance_id'] = self.materials_instance_id.to_alipay_dict()
            else:
                params['materials_instance_id'] = self.materials_instance_id
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.nfc_url:
            if hasattr(self.nfc_url, 'to_alipay_dict'):
                params['nfc_url'] = self.nfc_url.to_alipay_dict()
            else:
                params['nfc_url'] = self.nfc_url
        if self.production_ext_info:
            if hasattr(self.production_ext_info, 'to_alipay_dict'):
                params['production_ext_info'] = self.production_ext_info.to_alipay_dict()
            else:
                params['production_ext_info'] = self.production_ext_info
        if self.qr_code_url:
            if hasattr(self.qr_code_url, 'to_alipay_dict'):
                params['qr_code_url'] = self.qr_code_url.to_alipay_dict()
            else:
                params['qr_code_url'] = self.qr_code_url
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
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_order_no:
            if hasattr(self.shop_order_no, 'to_alipay_dict'):
                params['shop_order_no'] = self.shop_order_no.to_alipay_dict()
            else:
                params['shop_order_no'] = self.shop_order_no
        if self.shop_serial_number:
            if hasattr(self.shop_serial_number, 'to_alipay_dict'):
                params['shop_serial_number'] = self.shop_serial_number.to_alipay_dict()
            else:
                params['shop_serial_number'] = self.shop_serial_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopMaterialsInfo()
        if 'delivery_address' in d:
            o.delivery_address = d['delivery_address']
        if 'desk_no' in d:
            o.desk_no = d['desk_no']
        if 'materials_count' in d:
            o.materials_count = d['materials_count']
        if 'materials_instance_id' in d:
            o.materials_instance_id = d['materials_instance_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'nfc_url' in d:
            o.nfc_url = d['nfc_url']
        if 'production_ext_info' in d:
            o.production_ext_info = d['production_ext_info']
        if 'qr_code_url' in d:
            o.qr_code_url = d['qr_code_url']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'receiver_phone' in d:
            o.receiver_phone = d['receiver_phone']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_order_no' in d:
            o.shop_order_no = d['shop_order_no']
        if 'shop_serial_number' in d:
            o.shop_serial_number = d['shop_serial_number']
        return o


