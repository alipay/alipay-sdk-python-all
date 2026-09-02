#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtccardBindConsultModel(object):

    def __init__(self):
        self._isv_id = None
        self._mobile_no = None
        self._plate_no = None

    @property
    def isv_id(self):
        return self._isv_id

    @isv_id.setter
    def isv_id(self, value):
        self._isv_id = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_id:
            if hasattr(self.isv_id, 'to_alipay_dict'):
                params['isv_id'] = self.isv_id.to_alipay_dict()
            else:
                params['isv_id'] = self.isv_id
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtccardBindConsultModel()
        if 'isv_id' in d:
            o.isv_id = d['isv_id']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        return o


