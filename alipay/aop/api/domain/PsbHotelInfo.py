#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PsbHotelInfo(object):

    def __init__(self):
        self._license_key = None
        self._psb_code = None
        self._psb_hotel_id = None

    @property
    def license_key(self):
        return self._license_key

    @license_key.setter
    def license_key(self, value):
        self._license_key = value
    @property
    def psb_code(self):
        return self._psb_code

    @psb_code.setter
    def psb_code(self, value):
        self._psb_code = value
    @property
    def psb_hotel_id(self):
        return self._psb_hotel_id

    @psb_hotel_id.setter
    def psb_hotel_id(self, value):
        self._psb_hotel_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.license_key:
            if hasattr(self.license_key, 'to_alipay_dict'):
                params['license_key'] = self.license_key.to_alipay_dict()
            else:
                params['license_key'] = self.license_key
        if self.psb_code:
            if hasattr(self.psb_code, 'to_alipay_dict'):
                params['psb_code'] = self.psb_code.to_alipay_dict()
            else:
                params['psb_code'] = self.psb_code
        if self.psb_hotel_id:
            if hasattr(self.psb_hotel_id, 'to_alipay_dict'):
                params['psb_hotel_id'] = self.psb_hotel_id.to_alipay_dict()
            else:
                params['psb_hotel_id'] = self.psb_hotel_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PsbHotelInfo()
        if 'license_key' in d:
            o.license_key = d['license_key']
        if 'psb_code' in d:
            o.psb_code = d['psb_code']
        if 'psb_hotel_id' in d:
            o.psb_hotel_id = d['psb_hotel_id']
        return o


