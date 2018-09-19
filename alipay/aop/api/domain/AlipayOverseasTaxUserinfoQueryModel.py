#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTaxUserinfoQueryModel(object):

    def __init__(self):
        self._identify_account_no = None
        self._identify_account_type = None

    @property
    def identify_account_no(self):
        return self._identify_account_no

    @identify_account_no.setter
    def identify_account_no(self, value):
        self._identify_account_no = value
    @property
    def identify_account_type(self):
        return self._identify_account_type

    @identify_account_type.setter
    def identify_account_type(self, value):
        self._identify_account_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.identify_account_no:
            if hasattr(self.identify_account_no, 'to_alipay_dict'):
                params['identify_account_no'] = self.identify_account_no.to_alipay_dict()
            else:
                params['identify_account_no'] = self.identify_account_no
        if self.identify_account_type:
            if hasattr(self.identify_account_type, 'to_alipay_dict'):
                params['identify_account_type'] = self.identify_account_type.to_alipay_dict()
            else:
                params['identify_account_type'] = self.identify_account_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTaxUserinfoQueryModel()
        if 'identify_account_no' in d:
            o.identify_account_no = d['identify_account_no']
        if 'identify_account_type' in d:
            o.identify_account_type = d['identify_account_type']
        return o


