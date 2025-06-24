#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceCompanyQueryModel(object):

    def __init__(self):
        self._tax_no = None
        self._update_check_info = None

    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def update_check_info(self):
        return self._update_check_info

    @update_check_info.setter
    def update_check_info(self, value):
        self._update_check_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        if self.update_check_info:
            if hasattr(self.update_check_info, 'to_alipay_dict'):
                params['update_check_info'] = self.update_check_info.to_alipay_dict()
            else:
                params['update_check_info'] = self.update_check_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceCompanyQueryModel()
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        if 'update_check_info' in d:
            o.update_check_info = d['update_check_info']
        return o


