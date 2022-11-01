#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAnttechQqqCccQueryModel(object):

    def __init__(self):
        self._babab = None
        self._er_1_openid = None
        self._pppp = None
        self._province_code = None
        self._re = None

    @property
    def babab(self):
        return self._babab

    @babab.setter
    def babab(self, value):
        self._babab = value
    @property
    def er_1_openid(self):
        return self._er_1_openid

    @er_1_openid.setter
    def er_1_openid(self, value):
        self._er_1_openid = value
    @property
    def pppp(self):
        return self._pppp

    @pppp.setter
    def pppp(self, value):
        self._pppp = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def re(self):
        return self._re

    @re.setter
    def re(self, value):
        self._re = value


    def to_alipay_dict(self):
        params = dict()
        if self.babab:
            if hasattr(self.babab, 'to_alipay_dict'):
                params['babab'] = self.babab.to_alipay_dict()
            else:
                params['babab'] = self.babab
        if self.er_1_openid:
            if hasattr(self.er_1_openid, 'to_alipay_dict'):
                params['er_1_openid'] = self.er_1_openid.to_alipay_dict()
            else:
                params['er_1_openid'] = self.er_1_openid
        if self.pppp:
            if hasattr(self.pppp, 'to_alipay_dict'):
                params['pppp'] = self.pppp.to_alipay_dict()
            else:
                params['pppp'] = self.pppp
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.re:
            if hasattr(self.re, 'to_alipay_dict'):
                params['re'] = self.re.to_alipay_dict()
            else:
                params['re'] = self.re
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAnttechQqqCccQueryModel()
        if 'babab' in d:
            o.babab = d['babab']
        if 'er_1_openid' in d:
            o.er_1_openid = d['er_1_openid']
        if 'pppp' in d:
            o.pppp = d['pppp']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 're' in d:
            o.re = d['re']
        return o


