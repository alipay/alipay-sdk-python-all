#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenInstantdeliveryAccountCreateModel(object):

    def __init__(self):
        self._logistics_codes = None
        self._out_biz_no = None

    @property
    def logistics_codes(self):
        return self._logistics_codes

    @logistics_codes.setter
    def logistics_codes(self, value):
        if isinstance(value, list):
            self._logistics_codes = list()
            for i in value:
                self._logistics_codes.append(i)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_codes:
            if isinstance(self.logistics_codes, list):
                for i in range(0, len(self.logistics_codes)):
                    element = self.logistics_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logistics_codes[i] = element.to_alipay_dict()
            if hasattr(self.logistics_codes, 'to_alipay_dict'):
                params['logistics_codes'] = self.logistics_codes.to_alipay_dict()
            else:
                params['logistics_codes'] = self.logistics_codes
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenInstantdeliveryAccountCreateModel()
        if 'logistics_codes' in d:
            o.logistics_codes = d['logistics_codes']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


