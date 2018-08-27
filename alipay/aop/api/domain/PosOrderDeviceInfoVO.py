#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PosOrderDeviceInfoVO(object):

    def __init__(self):
        self._device_amt = None
        self._device_status = None
        self._device_type = None
        self._device_version = None
        self._implement_status = None
        self._service_status = None
        self._shop_id = None
        self._sn_no = None
        self._warehouse_id = None
        self._warehouse_type = None

    @property
    def device_amt(self):
        return self._device_amt

    @device_amt.setter
    def device_amt(self, value):
        self._device_amt = value
    @property
    def device_status(self):
        return self._device_status

    @device_status.setter
    def device_status(self, value):
        self._device_status = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def device_version(self):
        return self._device_version

    @device_version.setter
    def device_version(self, value):
        self._device_version = value
    @property
    def implement_status(self):
        return self._implement_status

    @implement_status.setter
    def implement_status(self, value):
        self._implement_status = value
    @property
    def service_status(self):
        return self._service_status

    @service_status.setter
    def service_status(self, value):
        self._service_status = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sn_no(self):
        return self._sn_no

    @sn_no.setter
    def sn_no(self, value):
        self._sn_no = value
    @property
    def warehouse_id(self):
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, value):
        self._warehouse_id = value
    @property
    def warehouse_type(self):
        return self._warehouse_type

    @warehouse_type.setter
    def warehouse_type(self, value):
        self._warehouse_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_amt:
            if hasattr(self.device_amt, 'to_alipay_dict'):
                params['device_amt'] = self.device_amt.to_alipay_dict()
            else:
                params['device_amt'] = self.device_amt
        if self.device_status:
            if hasattr(self.device_status, 'to_alipay_dict'):
                params['device_status'] = self.device_status.to_alipay_dict()
            else:
                params['device_status'] = self.device_status
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.device_version:
            if hasattr(self.device_version, 'to_alipay_dict'):
                params['device_version'] = self.device_version.to_alipay_dict()
            else:
                params['device_version'] = self.device_version
        if self.implement_status:
            if hasattr(self.implement_status, 'to_alipay_dict'):
                params['implement_status'] = self.implement_status.to_alipay_dict()
            else:
                params['implement_status'] = self.implement_status
        if self.service_status:
            if hasattr(self.service_status, 'to_alipay_dict'):
                params['service_status'] = self.service_status.to_alipay_dict()
            else:
                params['service_status'] = self.service_status
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sn_no:
            if hasattr(self.sn_no, 'to_alipay_dict'):
                params['sn_no'] = self.sn_no.to_alipay_dict()
            else:
                params['sn_no'] = self.sn_no
        if self.warehouse_id:
            if hasattr(self.warehouse_id, 'to_alipay_dict'):
                params['warehouse_id'] = self.warehouse_id.to_alipay_dict()
            else:
                params['warehouse_id'] = self.warehouse_id
        if self.warehouse_type:
            if hasattr(self.warehouse_type, 'to_alipay_dict'):
                params['warehouse_type'] = self.warehouse_type.to_alipay_dict()
            else:
                params['warehouse_type'] = self.warehouse_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PosOrderDeviceInfoVO()
        if 'device_amt' in d:
            o.device_amt = d['device_amt']
        if 'device_status' in d:
            o.device_status = d['device_status']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'device_version' in d:
            o.device_version = d['device_version']
        if 'implement_status' in d:
            o.implement_status = d['implement_status']
        if 'service_status' in d:
            o.service_status = d['service_status']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sn_no' in d:
            o.sn_no = d['sn_no']
        if 'warehouse_id' in d:
            o.warehouse_id = d['warehouse_id']
        if 'warehouse_type' in d:
            o.warehouse_type = d['warehouse_type']
        return o


