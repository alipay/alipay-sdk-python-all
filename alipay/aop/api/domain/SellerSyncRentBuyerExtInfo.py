#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentAddress import RentAddress


class SellerSyncRentBuyerExtInfo(object):

    def __init__(self):
        self._cert_address = None
        self._cert_no = None
        self._mobile = None
        self._name = None

    @property
    def cert_address(self):
        return self._cert_address

    @cert_address.setter
    def cert_address(self, value):
        if isinstance(value, RentAddress):
            self._cert_address = value
        else:
            self._cert_address = RentAddress.from_alipay_dict(value)
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_address:
            if hasattr(self.cert_address, 'to_alipay_dict'):
                params['cert_address'] = self.cert_address.to_alipay_dict()
            else:
                params['cert_address'] = self.cert_address
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SellerSyncRentBuyerExtInfo()
        if 'cert_address' in d:
            o.cert_address = d['cert_address']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        return o


