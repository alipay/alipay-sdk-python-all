#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationMallhomeMallorderTransferModel(object):

    def __init__(self):
        self._device_id = None
        self._device_type = None
        self._digital_poi_id = None
        self._ext_info = None
        self._merchant_pid = None
        self._merchant_smid = None
        self._order_no = None
        self._order_price = None
        self._software_version_no = None
        self._store_address = None
        self._store_id = None
        self._store_name = None
        self._trade_no = None
        self._trade_price = None
        self._trade_time = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def digital_poi_id(self):
        return self._digital_poi_id

    @digital_poi_id.setter
    def digital_poi_id(self, value):
        self._digital_poi_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def merchant_smid(self):
        return self._merchant_smid

    @merchant_smid.setter
    def merchant_smid(self, value):
        self._merchant_smid = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_price(self):
        return self._order_price

    @order_price.setter
    def order_price(self, value):
        self._order_price = value
    @property
    def software_version_no(self):
        return self._software_version_no

    @software_version_no.setter
    def software_version_no(self, value):
        self._software_version_no = value
    @property
    def store_address(self):
        return self._store_address

    @store_address.setter
    def store_address(self, value):
        self._store_address = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_price(self):
        return self._trade_price

    @trade_price.setter
    def trade_price(self, value):
        self._trade_price = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.digital_poi_id:
            if hasattr(self.digital_poi_id, 'to_alipay_dict'):
                params['digital_poi_id'] = self.digital_poi_id.to_alipay_dict()
            else:
                params['digital_poi_id'] = self.digital_poi_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.merchant_smid:
            if hasattr(self.merchant_smid, 'to_alipay_dict'):
                params['merchant_smid'] = self.merchant_smid.to_alipay_dict()
            else:
                params['merchant_smid'] = self.merchant_smid
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_price:
            if hasattr(self.order_price, 'to_alipay_dict'):
                params['order_price'] = self.order_price.to_alipay_dict()
            else:
                params['order_price'] = self.order_price
        if self.software_version_no:
            if hasattr(self.software_version_no, 'to_alipay_dict'):
                params['software_version_no'] = self.software_version_no.to_alipay_dict()
            else:
                params['software_version_no'] = self.software_version_no
        if self.store_address:
            if hasattr(self.store_address, 'to_alipay_dict'):
                params['store_address'] = self.store_address.to_alipay_dict()
            else:
                params['store_address'] = self.store_address
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_price:
            if hasattr(self.trade_price, 'to_alipay_dict'):
                params['trade_price'] = self.trade_price.to_alipay_dict()
            else:
                params['trade_price'] = self.trade_price
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationMallhomeMallorderTransferModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'digital_poi_id' in d:
            o.digital_poi_id = d['digital_poi_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'merchant_smid' in d:
            o.merchant_smid = d['merchant_smid']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_price' in d:
            o.order_price = d['order_price']
        if 'software_version_no' in d:
            o.software_version_no = d['software_version_no']
        if 'store_address' in d:
            o.store_address = d['store_address']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_price' in d:
            o.trade_price = d['trade_price']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        return o


