#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcenterpriseVehicleQueryModel(object):

    def __init__(self):
        self._corp_id = None
        self._corp_vehicle_id = None
        self._plate_color = None
        self._plate_no = None
        self._waybill_no = None

    @property
    def corp_id(self):
        return self._corp_id

    @corp_id.setter
    def corp_id(self, value):
        self._corp_id = value
    @property
    def corp_vehicle_id(self):
        return self._corp_vehicle_id

    @corp_vehicle_id.setter
    def corp_vehicle_id(self, value):
        self._corp_vehicle_id = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.corp_id:
            if hasattr(self.corp_id, 'to_alipay_dict'):
                params['corp_id'] = self.corp_id.to_alipay_dict()
            else:
                params['corp_id'] = self.corp_id
        if self.corp_vehicle_id:
            if hasattr(self.corp_vehicle_id, 'to_alipay_dict'):
                params['corp_vehicle_id'] = self.corp_vehicle_id.to_alipay_dict()
            else:
                params['corp_vehicle_id'] = self.corp_vehicle_id
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.waybill_no:
            if hasattr(self.waybill_no, 'to_alipay_dict'):
                params['waybill_no'] = self.waybill_no.to_alipay_dict()
            else:
                params['waybill_no'] = self.waybill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcenterpriseVehicleQueryModel()
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'corp_vehicle_id' in d:
            o.corp_vehicle_id = d['corp_vehicle_id']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o


