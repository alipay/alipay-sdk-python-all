#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreateMaterialsInfo(object):

    def __init__(self):
        self._desk_no = None
        self._num = None
        self._production_ext_info = None
        self._qr_code_url = None

    @property
    def desk_no(self):
        return self._desk_no

    @desk_no.setter
    def desk_no(self, value):
        self._desk_no = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def production_ext_info(self):
        return self._production_ext_info

    @production_ext_info.setter
    def production_ext_info(self, value):
        self._production_ext_info = value
    @property
    def qr_code_url(self):
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, value):
        self._qr_code_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.desk_no:
            if hasattr(self.desk_no, 'to_alipay_dict'):
                params['desk_no'] = self.desk_no.to_alipay_dict()
            else:
                params['desk_no'] = self.desk_no
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.production_ext_info:
            if hasattr(self.production_ext_info, 'to_alipay_dict'):
                params['production_ext_info'] = self.production_ext_info.to_alipay_dict()
            else:
                params['production_ext_info'] = self.production_ext_info
        if self.qr_code_url:
            if hasattr(self.qr_code_url, 'to_alipay_dict'):
                params['qr_code_url'] = self.qr_code_url.to_alipay_dict()
            else:
                params['qr_code_url'] = self.qr_code_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreateMaterialsInfo()
        if 'desk_no' in d:
            o.desk_no = d['desk_no']
        if 'num' in d:
            o.num = d['num']
        if 'production_ext_info' in d:
            o.production_ext_info = d['production_ext_info']
        if 'qr_code_url' in d:
            o.qr_code_url = d['qr_code_url']
        return o


