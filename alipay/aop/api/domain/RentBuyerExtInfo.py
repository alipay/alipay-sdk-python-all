#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentAddress import RentAddress
from alipay.aop.api.domain.RentFile import RentFile
from alipay.aop.api.domain.RentFile import RentFile
from alipay.aop.api.domain.RentFile import RentFile


class RentBuyerExtInfo(object):

    def __init__(self):
        self._cert_address = None
        self._cert_back_pic = None
        self._cert_font_pic = None
        self._cert_no = None
        self._live_pic = None
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
    def cert_back_pic(self):
        return self._cert_back_pic

    @cert_back_pic.setter
    def cert_back_pic(self, value):
        if isinstance(value, RentFile):
            self._cert_back_pic = value
        else:
            self._cert_back_pic = RentFile.from_alipay_dict(value)
    @property
    def cert_font_pic(self):
        return self._cert_font_pic

    @cert_font_pic.setter
    def cert_font_pic(self, value):
        if isinstance(value, RentFile):
            self._cert_font_pic = value
        else:
            self._cert_font_pic = RentFile.from_alipay_dict(value)
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def live_pic(self):
        return self._live_pic

    @live_pic.setter
    def live_pic(self, value):
        if isinstance(value, RentFile):
            self._live_pic = value
        else:
            self._live_pic = RentFile.from_alipay_dict(value)
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
        if self.cert_back_pic:
            if hasattr(self.cert_back_pic, 'to_alipay_dict'):
                params['cert_back_pic'] = self.cert_back_pic.to_alipay_dict()
            else:
                params['cert_back_pic'] = self.cert_back_pic
        if self.cert_font_pic:
            if hasattr(self.cert_font_pic, 'to_alipay_dict'):
                params['cert_font_pic'] = self.cert_font_pic.to_alipay_dict()
            else:
                params['cert_font_pic'] = self.cert_font_pic
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.live_pic:
            if hasattr(self.live_pic, 'to_alipay_dict'):
                params['live_pic'] = self.live_pic.to_alipay_dict()
            else:
                params['live_pic'] = self.live_pic
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
        o = RentBuyerExtInfo()
        if 'cert_address' in d:
            o.cert_address = d['cert_address']
        if 'cert_back_pic' in d:
            o.cert_back_pic = d['cert_back_pic']
        if 'cert_font_pic' in d:
            o.cert_font_pic = d['cert_font_pic']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'live_pic' in d:
            o.live_pic = d['live_pic']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        return o


