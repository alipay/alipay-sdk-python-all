#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingActivityOrdervoucherCodedepositModel(object):

    def __init__(self):
        self._activity_id = None
        self._out_biz_no = None
        self._voucher_codes = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def voucher_codes(self):
        return self._voucher_codes

    @voucher_codes.setter
    def voucher_codes(self, value):
        if isinstance(value, list):
            self._voucher_codes = list()
            for i in value:
                self._voucher_codes.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.voucher_codes:
            if isinstance(self.voucher_codes, list):
                for i in range(0, len(self.voucher_codes)):
                    element = self.voucher_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_codes[i] = element.to_alipay_dict()
            if hasattr(self.voucher_codes, 'to_alipay_dict'):
                params['voucher_codes'] = self.voucher_codes.to_alipay_dict()
            else:
                params['voucher_codes'] = self.voucher_codes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityOrdervoucherCodedepositModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'voucher_codes' in d:
            o.voucher_codes = d['voucher_codes']
        return o


