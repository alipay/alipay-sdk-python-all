#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PharmacistVO(object):

    def __init__(self):
        self._app_store_code = None
        self._channel = None
        self._pharmacist_code = None
        self._pharmacist_name = None
        self._pharmacist_status = None
        self._seller_id = None

    @property
    def app_store_code(self):
        return self._app_store_code

    @app_store_code.setter
    def app_store_code(self, value):
        self._app_store_code = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def pharmacist_code(self):
        return self._pharmacist_code

    @pharmacist_code.setter
    def pharmacist_code(self, value):
        self._pharmacist_code = value
    @property
    def pharmacist_name(self):
        return self._pharmacist_name

    @pharmacist_name.setter
    def pharmacist_name(self, value):
        self._pharmacist_name = value
    @property
    def pharmacist_status(self):
        return self._pharmacist_status

    @pharmacist_status.setter
    def pharmacist_status(self, value):
        self._pharmacist_status = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_store_code:
            if hasattr(self.app_store_code, 'to_alipay_dict'):
                params['app_store_code'] = self.app_store_code.to_alipay_dict()
            else:
                params['app_store_code'] = self.app_store_code
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.pharmacist_code:
            if hasattr(self.pharmacist_code, 'to_alipay_dict'):
                params['pharmacist_code'] = self.pharmacist_code.to_alipay_dict()
            else:
                params['pharmacist_code'] = self.pharmacist_code
        if self.pharmacist_name:
            if hasattr(self.pharmacist_name, 'to_alipay_dict'):
                params['pharmacist_name'] = self.pharmacist_name.to_alipay_dict()
            else:
                params['pharmacist_name'] = self.pharmacist_name
        if self.pharmacist_status:
            if hasattr(self.pharmacist_status, 'to_alipay_dict'):
                params['pharmacist_status'] = self.pharmacist_status.to_alipay_dict()
            else:
                params['pharmacist_status'] = self.pharmacist_status
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PharmacistVO()
        if 'app_store_code' in d:
            o.app_store_code = d['app_store_code']
        if 'channel' in d:
            o.channel = d['channel']
        if 'pharmacist_code' in d:
            o.pharmacist_code = d['pharmacist_code']
        if 'pharmacist_name' in d:
            o.pharmacist_name = d['pharmacist_name']
        if 'pharmacist_status' in d:
            o.pharmacist_status = d['pharmacist_status']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        return o


