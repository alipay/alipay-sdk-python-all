#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceDtevalIdentitycheckQueryModel(object):

    def __init__(self):
        self._biz_no = None
        self._col_cert_no = None
        self._col_mobile = None
        self._col_user_name = None
        self._ext_map = None
        self._real_cert_no = None
        self._real_mobile = None
        self._real_user_name = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def col_cert_no(self):
        return self._col_cert_no

    @col_cert_no.setter
    def col_cert_no(self, value):
        self._col_cert_no = value
    @property
    def col_mobile(self):
        return self._col_mobile

    @col_mobile.setter
    def col_mobile(self, value):
        self._col_mobile = value
    @property
    def col_user_name(self):
        return self._col_user_name

    @col_user_name.setter
    def col_user_name(self, value):
        self._col_user_name = value
    @property
    def ext_map(self):
        return self._ext_map

    @ext_map.setter
    def ext_map(self, value):
        self._ext_map = value
    @property
    def real_cert_no(self):
        return self._real_cert_no

    @real_cert_no.setter
    def real_cert_no(self, value):
        self._real_cert_no = value
    @property
    def real_mobile(self):
        return self._real_mobile

    @real_mobile.setter
    def real_mobile(self, value):
        self._real_mobile = value
    @property
    def real_user_name(self):
        return self._real_user_name

    @real_user_name.setter
    def real_user_name(self, value):
        self._real_user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.col_cert_no:
            if hasattr(self.col_cert_no, 'to_alipay_dict'):
                params['col_cert_no'] = self.col_cert_no.to_alipay_dict()
            else:
                params['col_cert_no'] = self.col_cert_no
        if self.col_mobile:
            if hasattr(self.col_mobile, 'to_alipay_dict'):
                params['col_mobile'] = self.col_mobile.to_alipay_dict()
            else:
                params['col_mobile'] = self.col_mobile
        if self.col_user_name:
            if hasattr(self.col_user_name, 'to_alipay_dict'):
                params['col_user_name'] = self.col_user_name.to_alipay_dict()
            else:
                params['col_user_name'] = self.col_user_name
        if self.ext_map:
            if hasattr(self.ext_map, 'to_alipay_dict'):
                params['ext_map'] = self.ext_map.to_alipay_dict()
            else:
                params['ext_map'] = self.ext_map
        if self.real_cert_no:
            if hasattr(self.real_cert_no, 'to_alipay_dict'):
                params['real_cert_no'] = self.real_cert_no.to_alipay_dict()
            else:
                params['real_cert_no'] = self.real_cert_no
        if self.real_mobile:
            if hasattr(self.real_mobile, 'to_alipay_dict'):
                params['real_mobile'] = self.real_mobile.to_alipay_dict()
            else:
                params['real_mobile'] = self.real_mobile
        if self.real_user_name:
            if hasattr(self.real_user_name, 'to_alipay_dict'):
                params['real_user_name'] = self.real_user_name.to_alipay_dict()
            else:
                params['real_user_name'] = self.real_user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceDtevalIdentitycheckQueryModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'col_cert_no' in d:
            o.col_cert_no = d['col_cert_no']
        if 'col_mobile' in d:
            o.col_mobile = d['col_mobile']
        if 'col_user_name' in d:
            o.col_user_name = d['col_user_name']
        if 'ext_map' in d:
            o.ext_map = d['ext_map']
        if 'real_cert_no' in d:
            o.real_cert_no = d['real_cert_no']
        if 'real_mobile' in d:
            o.real_mobile = d['real_mobile']
        if 'real_user_name' in d:
            o.real_user_name = d['real_user_name']
        return o


