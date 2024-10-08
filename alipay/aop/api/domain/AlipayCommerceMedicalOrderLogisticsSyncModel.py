#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalOrderLogisticsSyncModel(object):

    def __init__(self):
        self._carrier_order_no = None
        self._courier_name = None
        self._courier_phone = None
        self._logistics_status = None
        self._order_no = None
        self._provider_code = None
        self._provider_phone = None

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
    def logistics_status(self):
        return self._logistics_status

    @logistics_status.setter
    def logistics_status(self, value):
        self._logistics_status = value
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
        if self.logistics_status:
            if hasattr(self.logistics_status, 'to_alipay_dict'):
                params['logistics_status'] = self.logistics_status.to_alipay_dict()
            else:
                params['logistics_status'] = self.logistics_status
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
        if 'logistics_status' in d:
            o.logistics_status = d['logistics_status']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'provider_code' in d:
            o.provider_code = d['provider_code']
        if 'provider_phone' in d:
            o.provider_phone = d['provider_phone']
        return o


