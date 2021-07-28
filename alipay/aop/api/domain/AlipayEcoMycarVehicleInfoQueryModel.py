#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarVehicleInfoQueryModel(object):

    def __init__(self):
        self._plate_no = None
        self._vi_id = None

    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def vi_id(self):
        return self._vi_id

    @vi_id.setter
    def vi_id(self, value):
        self._vi_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.vi_id:
            if hasattr(self.vi_id, 'to_alipay_dict'):
                params['vi_id'] = self.vi_id.to_alipay_dict()
            else:
                params['vi_id'] = self.vi_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarVehicleInfoQueryModel()
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'vi_id' in d:
            o.vi_id = d['vi_id']
        return o


