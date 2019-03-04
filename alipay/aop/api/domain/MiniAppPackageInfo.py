#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppPackageInfo(object):

    def __init__(self):
        self._package_qr_code_url = None
        self._package_size = None
        self._package_status = None

    @property
    def package_qr_code_url(self):
        return self._package_qr_code_url

    @package_qr_code_url.setter
    def package_qr_code_url(self, value):
        self._package_qr_code_url = value
    @property
    def package_size(self):
        return self._package_size

    @package_size.setter
    def package_size(self, value):
        self._package_size = value
    @property
    def package_status(self):
        return self._package_status

    @package_status.setter
    def package_status(self, value):
        self._package_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.package_qr_code_url:
            if hasattr(self.package_qr_code_url, 'to_alipay_dict'):
                params['package_qr_code_url'] = self.package_qr_code_url.to_alipay_dict()
            else:
                params['package_qr_code_url'] = self.package_qr_code_url
        if self.package_size:
            if hasattr(self.package_size, 'to_alipay_dict'):
                params['package_size'] = self.package_size.to_alipay_dict()
            else:
                params['package_size'] = self.package_size
        if self.package_status:
            if hasattr(self.package_status, 'to_alipay_dict'):
                params['package_status'] = self.package_status.to_alipay_dict()
            else:
                params['package_status'] = self.package_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppPackageInfo()
        if 'package_qr_code_url' in d:
            o.package_qr_code_url = d['package_qr_code_url']
        if 'package_size' in d:
            o.package_size = d['package_size']
        if 'package_status' in d:
            o.package_status = d['package_status']
        return o


