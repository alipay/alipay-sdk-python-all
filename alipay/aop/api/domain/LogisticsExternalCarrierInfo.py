#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LogisticsExternalCarrierInfo(object):

    def __init__(self):
        self._carrier_no = None
        self._carrier_status = None
        self._carrier_sub_id = None
        self._carrier_sub_no = None

    @property
    def carrier_no(self):
        return self._carrier_no

    @carrier_no.setter
    def carrier_no(self, value):
        self._carrier_no = value
    @property
    def carrier_status(self):
        return self._carrier_status

    @carrier_status.setter
    def carrier_status(self, value):
        self._carrier_status = value
    @property
    def carrier_sub_id(self):
        return self._carrier_sub_id

    @carrier_sub_id.setter
    def carrier_sub_id(self, value):
        self._carrier_sub_id = value
    @property
    def carrier_sub_no(self):
        return self._carrier_sub_no

    @carrier_sub_no.setter
    def carrier_sub_no(self, value):
        self._carrier_sub_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.carrier_no:
            if hasattr(self.carrier_no, 'to_alipay_dict'):
                params['carrier_no'] = self.carrier_no.to_alipay_dict()
            else:
                params['carrier_no'] = self.carrier_no
        if self.carrier_status:
            if hasattr(self.carrier_status, 'to_alipay_dict'):
                params['carrier_status'] = self.carrier_status.to_alipay_dict()
            else:
                params['carrier_status'] = self.carrier_status
        if self.carrier_sub_id:
            if hasattr(self.carrier_sub_id, 'to_alipay_dict'):
                params['carrier_sub_id'] = self.carrier_sub_id.to_alipay_dict()
            else:
                params['carrier_sub_id'] = self.carrier_sub_id
        if self.carrier_sub_no:
            if hasattr(self.carrier_sub_no, 'to_alipay_dict'):
                params['carrier_sub_no'] = self.carrier_sub_no.to_alipay_dict()
            else:
                params['carrier_sub_no'] = self.carrier_sub_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsExternalCarrierInfo()
        if 'carrier_no' in d:
            o.carrier_no = d['carrier_no']
        if 'carrier_status' in d:
            o.carrier_status = d['carrier_status']
        if 'carrier_sub_id' in d:
            o.carrier_sub_id = d['carrier_sub_id']
        if 'carrier_sub_no' in d:
            o.carrier_sub_no = d['carrier_sub_no']
        return o


