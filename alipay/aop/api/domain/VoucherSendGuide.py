#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherSendGuide(object):

    def __init__(self):
        self._voucher_detail_url = None

    @property
    def voucher_detail_url(self):
        return self._voucher_detail_url

    @voucher_detail_url.setter
    def voucher_detail_url(self, value):
        self._voucher_detail_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.voucher_detail_url:
            if hasattr(self.voucher_detail_url, 'to_alipay_dict'):
                params['voucher_detail_url'] = self.voucher_detail_url.to_alipay_dict()
            else:
                params['voucher_detail_url'] = self.voucher_detail_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherSendGuide()
        if 'voucher_detail_url' in d:
            o.voucher_detail_url = d['voucher_detail_url']
        return o


