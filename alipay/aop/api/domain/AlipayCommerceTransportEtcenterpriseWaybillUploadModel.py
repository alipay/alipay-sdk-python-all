#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcenterpriseWaybillUploadModel(object):

    def __init__(self):
        self._corp_id = None
        self._corp_vehicle_id = None
        self._highway_fee = None
        self._plate_color = None
        self._plate_no = None
        self._waybill_end_address = None
        self._waybill_end_time = None
        self._waybill_fee = None
        self._waybill_no = None
        self._waybill_start_address = None
        self._waybill_start_time = None
        self._waybill_status = None

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
    def highway_fee(self):
        return self._highway_fee

    @highway_fee.setter
    def highway_fee(self, value):
        self._highway_fee = value
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
    def waybill_end_address(self):
        return self._waybill_end_address

    @waybill_end_address.setter
    def waybill_end_address(self, value):
        self._waybill_end_address = value
    @property
    def waybill_end_time(self):
        return self._waybill_end_time

    @waybill_end_time.setter
    def waybill_end_time(self, value):
        self._waybill_end_time = value
    @property
    def waybill_fee(self):
        return self._waybill_fee

    @waybill_fee.setter
    def waybill_fee(self, value):
        self._waybill_fee = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value
    @property
    def waybill_start_address(self):
        return self._waybill_start_address

    @waybill_start_address.setter
    def waybill_start_address(self, value):
        self._waybill_start_address = value
    @property
    def waybill_start_time(self):
        return self._waybill_start_time

    @waybill_start_time.setter
    def waybill_start_time(self, value):
        self._waybill_start_time = value
    @property
    def waybill_status(self):
        return self._waybill_status

    @waybill_status.setter
    def waybill_status(self, value):
        self._waybill_status = value


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
        if self.highway_fee:
            if hasattr(self.highway_fee, 'to_alipay_dict'):
                params['highway_fee'] = self.highway_fee.to_alipay_dict()
            else:
                params['highway_fee'] = self.highway_fee
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
        if self.waybill_end_address:
            if hasattr(self.waybill_end_address, 'to_alipay_dict'):
                params['waybill_end_address'] = self.waybill_end_address.to_alipay_dict()
            else:
                params['waybill_end_address'] = self.waybill_end_address
        if self.waybill_end_time:
            if hasattr(self.waybill_end_time, 'to_alipay_dict'):
                params['waybill_end_time'] = self.waybill_end_time.to_alipay_dict()
            else:
                params['waybill_end_time'] = self.waybill_end_time
        if self.waybill_fee:
            if hasattr(self.waybill_fee, 'to_alipay_dict'):
                params['waybill_fee'] = self.waybill_fee.to_alipay_dict()
            else:
                params['waybill_fee'] = self.waybill_fee
        if self.waybill_no:
            if hasattr(self.waybill_no, 'to_alipay_dict'):
                params['waybill_no'] = self.waybill_no.to_alipay_dict()
            else:
                params['waybill_no'] = self.waybill_no
        if self.waybill_start_address:
            if hasattr(self.waybill_start_address, 'to_alipay_dict'):
                params['waybill_start_address'] = self.waybill_start_address.to_alipay_dict()
            else:
                params['waybill_start_address'] = self.waybill_start_address
        if self.waybill_start_time:
            if hasattr(self.waybill_start_time, 'to_alipay_dict'):
                params['waybill_start_time'] = self.waybill_start_time.to_alipay_dict()
            else:
                params['waybill_start_time'] = self.waybill_start_time
        if self.waybill_status:
            if hasattr(self.waybill_status, 'to_alipay_dict'):
                params['waybill_status'] = self.waybill_status.to_alipay_dict()
            else:
                params['waybill_status'] = self.waybill_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcenterpriseWaybillUploadModel()
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'corp_vehicle_id' in d:
            o.corp_vehicle_id = d['corp_vehicle_id']
        if 'highway_fee' in d:
            o.highway_fee = d['highway_fee']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'waybill_end_address' in d:
            o.waybill_end_address = d['waybill_end_address']
        if 'waybill_end_time' in d:
            o.waybill_end_time = d['waybill_end_time']
        if 'waybill_fee' in d:
            o.waybill_fee = d['waybill_fee']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        if 'waybill_start_address' in d:
            o.waybill_start_address = d['waybill_start_address']
        if 'waybill_start_time' in d:
            o.waybill_start_time = d['waybill_start_time']
        if 'waybill_status' in d:
            o.waybill_status = d['waybill_status']
        return o


