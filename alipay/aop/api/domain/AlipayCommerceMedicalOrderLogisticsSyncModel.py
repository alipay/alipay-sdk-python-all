#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalOrderLogisticsSyncModel(object):

    def __init__(self):
        self._carrier_order_no = None
        self._courier_name = None
        self._courier_phone = None
        self._latitude = None
        self._logistics_status = None
        self._longitude = None
        self._order_no = None
        self._provider_code = None
        self._provider_phone = None
        self._reason = None
        self._reason_code = None
        self._utc = None

    @property
    def carrier_order_no(self):
        return self._carrier_order_no

    @carrier_order_no.setter
    def carrier_order_no(self, value):
        self._carrier_order_no = value
    @property
    def courier_name(self):
        return self._courier_name

    @courier_name.setter
    def courier_name(self, value):
        self._courier_name = value
    @property
    def courier_phone(self):
        return self._courier_phone

    @courier_phone.setter
    def courier_phone(self, value):
        self._courier_phone = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def logistics_status(self):
        return self._logistics_status

    @logistics_status.setter
    def logistics_status(self, value):
        self._logistics_status = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def provider_code(self):
        return self._provider_code

    @provider_code.setter
    def provider_code(self, value):
        self._provider_code = value
    @property
    def provider_phone(self):
        return self._provider_phone

    @provider_phone.setter
    def provider_phone(self, value):
        self._provider_phone = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def utc(self):
        return self._utc

    @utc.setter
    def utc(self, value):
        self._utc = value


    def to_alipay_dict(self):
        params = dict()
        if self.carrier_order_no:
            if hasattr(self.carrier_order_no, 'to_alipay_dict'):
                params['carrier_order_no'] = self.carrier_order_no.to_alipay_dict()
            else:
                params['carrier_order_no'] = self.carrier_order_no
        if self.courier_name:
            if hasattr(self.courier_name, 'to_alipay_dict'):
                params['courier_name'] = self.courier_name.to_alipay_dict()
            else:
                params['courier_name'] = self.courier_name
        if self.courier_phone:
            if hasattr(self.courier_phone, 'to_alipay_dict'):
                params['courier_phone'] = self.courier_phone.to_alipay_dict()
            else:
                params['courier_phone'] = self.courier_phone
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.logistics_status:
            if hasattr(self.logistics_status, 'to_alipay_dict'):
                params['logistics_status'] = self.logistics_status.to_alipay_dict()
            else:
                params['logistics_status'] = self.logistics_status
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.provider_code:
            if hasattr(self.provider_code, 'to_alipay_dict'):
                params['provider_code'] = self.provider_code.to_alipay_dict()
            else:
                params['provider_code'] = self.provider_code
        if self.provider_phone:
            if hasattr(self.provider_phone, 'to_alipay_dict'):
                params['provider_phone'] = self.provider_phone.to_alipay_dict()
            else:
                params['provider_phone'] = self.provider_phone
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.reason_code:
            if hasattr(self.reason_code, 'to_alipay_dict'):
                params['reason_code'] = self.reason_code.to_alipay_dict()
            else:
                params['reason_code'] = self.reason_code
        if self.utc:
            if hasattr(self.utc, 'to_alipay_dict'):
                params['utc'] = self.utc.to_alipay_dict()
            else:
                params['utc'] = self.utc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalOrderLogisticsSyncModel()
        if 'carrier_order_no' in d:
            o.carrier_order_no = d['carrier_order_no']
        if 'courier_name' in d:
            o.courier_name = d['courier_name']
        if 'courier_phone' in d:
            o.courier_phone = d['courier_phone']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'logistics_status' in d:
            o.logistics_status = d['logistics_status']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'provider_code' in d:
            o.provider_code = d['provider_code']
        if 'provider_phone' in d:
            o.provider_phone = d['provider_phone']
        if 'reason' in d:
            o.reason = d['reason']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        if 'utc' in d:
            o.utc = d['utc']
        return o


