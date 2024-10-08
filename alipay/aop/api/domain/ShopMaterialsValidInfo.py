#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopMaterialsValidInfo(object):

    def __init__(self):
        self._chip_id = None
        self._desk_no = None
        self._materials_instance_id = None
        self._nfc_url = None
        self._production_ext_info = None
        self._qr_code_url = None
        self._shop_order_no = None

    @property
    def chip_id(self):
        return self._chip_id

    @chip_id.setter
    def chip_id(self, value):
        self._chip_id = value
    @property
    def desk_no(self):
        return self._desk_no

    @desk_no.setter
    def desk_no(self, value):
        self._desk_no = value
    @property
    def materials_instance_id(self):
        return self._materials_instance_id

    @materials_instance_id.setter
    def materials_instance_id(self, value):
        self._materials_instance_id = value
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
    def shop_order_no(self):
        return self._shop_order_no

    @shop_order_no.setter
    def shop_order_no(self, value):
        self._shop_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.chip_id:
            if hasattr(self.chip_id, 'to_alipay_dict'):
                params['chip_id'] = self.chip_id.to_alipay_dict()
            else:
                params['chip_id'] = self.chip_id
        if self.desk_no:
            if hasattr(self.desk_no, 'to_alipay_dict'):
                params['desk_no'] = self.desk_no.to_alipay_dict()
            else:
                params['desk_no'] = self.desk_no
        if self.materials_instance_id:
            if hasattr(self.materials_instance_id, 'to_alipay_dict'):
                params['materials_instance_id'] = self.materials_instance_id.to_alipay_dict()
            else:
                params['materials_instance_id'] = self.materials_instance_id
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
        if self.shop_order_no:
            if hasattr(self.shop_order_no, 'to_alipay_dict'):
                params['shop_order_no'] = self.shop_order_no.to_alipay_dict()
            else:
                params['shop_order_no'] = self.shop_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopMaterialsValidInfo()
        if 'chip_id' in d:
            o.chip_id = d['chip_id']
        if 'desk_no' in d:
            o.desk_no = d['desk_no']
        if 'materials_instance_id' in d:
            o.materials_instance_id = d['materials_instance_id']
        if 'nfc_url' in d:
            o.nfc_url = d['nfc_url']
        if 'production_ext_info' in d:
            o.production_ext_info = d['production_ext_info']
        if 'qr_code_url' in d:
            o.qr_code_url = d['qr_code_url']
        if 'shop_order_no' in d:
            o.shop_order_no = d['shop_order_no']
        return o


