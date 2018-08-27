#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomsDeclareBuyerInfo(object):

    def __init__(self):
        self._buyer_cert_no = None
        self._buyer_name = None

    @property
    def buyer_cert_no(self):
        return self._buyer_cert_no

    @buyer_cert_no.setter
    def buyer_cert_no(self, value):
        self._buyer_cert_no = value
    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, value):
        self._buyer_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_cert_no:
            if hasattr(self.buyer_cert_no, 'to_alipay_dict'):
                params['buyer_cert_no'] = self.buyer_cert_no.to_alipay_dict()
            else:
                params['buyer_cert_no'] = self.buyer_cert_no
        if self.buyer_name:
            if hasattr(self.buyer_name, 'to_alipay_dict'):
                params['buyer_name'] = self.buyer_name.to_alipay_dict()
            else:
                params['buyer_name'] = self.buyer_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomsDeclareBuyerInfo()
        if 'buyer_cert_no' in d:
            o.buyer_cert_no = d['buyer_cert_no']
        if 'buyer_name' in d:
            o.buyer_name = d['buyer_name']
        return o


