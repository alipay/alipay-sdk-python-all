#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandIotdeviceOnlinedataUploadModel(object):

    def __init__(self):
        self._device_online_time = None
        self._device_sn = None
        self._policy_type = None
        self._settled_alipay_id = None
        self._shop_name = None
        self._signed_alipay_id = None
        self._supplier_sn = None
        self._upload_date = None

    @property
    def device_online_time(self):
        return self._device_online_time

    @device_online_time.setter
    def device_online_time(self, value):
        self._device_online_time = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def policy_type(self):
        return self._policy_type

    @policy_type.setter
    def policy_type(self, value):
        self._policy_type = value
    @property
    def settled_alipay_id(self):
        return self._settled_alipay_id

    @settled_alipay_id.setter
    def settled_alipay_id(self, value):
        self._settled_alipay_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def signed_alipay_id(self):
        return self._signed_alipay_id

    @signed_alipay_id.setter
    def signed_alipay_id(self, value):
        self._signed_alipay_id = value
    @property
    def supplier_sn(self):
        return self._supplier_sn

    @supplier_sn.setter
    def supplier_sn(self, value):
        self._supplier_sn = value
    @property
    def upload_date(self):
        return self._upload_date

    @upload_date.setter
    def upload_date(self, value):
        self._upload_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_online_time:
            if hasattr(self.device_online_time, 'to_alipay_dict'):
                params['device_online_time'] = self.device_online_time.to_alipay_dict()
            else:
                params['device_online_time'] = self.device_online_time
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.policy_type:
            if hasattr(self.policy_type, 'to_alipay_dict'):
                params['policy_type'] = self.policy_type.to_alipay_dict()
            else:
                params['policy_type'] = self.policy_type
        if self.settled_alipay_id:
            if hasattr(self.settled_alipay_id, 'to_alipay_dict'):
                params['settled_alipay_id'] = self.settled_alipay_id.to_alipay_dict()
            else:
                params['settled_alipay_id'] = self.settled_alipay_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.signed_alipay_id:
            if hasattr(self.signed_alipay_id, 'to_alipay_dict'):
                params['signed_alipay_id'] = self.signed_alipay_id.to_alipay_dict()
            else:
                params['signed_alipay_id'] = self.signed_alipay_id
        if self.supplier_sn:
            if hasattr(self.supplier_sn, 'to_alipay_dict'):
                params['supplier_sn'] = self.supplier_sn.to_alipay_dict()
            else:
                params['supplier_sn'] = self.supplier_sn
        if self.upload_date:
            if hasattr(self.upload_date, 'to_alipay_dict'):
                params['upload_date'] = self.upload_date.to_alipay_dict()
            else:
                params['upload_date'] = self.upload_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIotdeviceOnlinedataUploadModel()
        if 'device_online_time' in d:
            o.device_online_time = d['device_online_time']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'policy_type' in d:
            o.policy_type = d['policy_type']
        if 'settled_alipay_id' in d:
            o.settled_alipay_id = d['settled_alipay_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'signed_alipay_id' in d:
            o.signed_alipay_id = d['signed_alipay_id']
        if 'supplier_sn' in d:
            o.supplier_sn = d['supplier_sn']
        if 'upload_date' in d:
            o.upload_date = d['upload_date']
        return o


