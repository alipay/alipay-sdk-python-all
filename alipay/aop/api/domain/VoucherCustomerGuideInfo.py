#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherSendGuideInfo import VoucherSendGuideInfo
from alipay.aop.api.domain.VoucherUseGuideInfo import VoucherUseGuideInfo


class VoucherCustomerGuideInfo(object):

    def __init__(self):
        self._voucher_send_guide_info = None
        self._voucher_use_guide_info = None

    @property
    def voucher_send_guide_info(self):
        return self._voucher_send_guide_info

    @voucher_send_guide_info.setter
    def voucher_send_guide_info(self, value):
        if isinstance(value, VoucherSendGuideInfo):
            self._voucher_send_guide_info = value
        else:
            self._voucher_send_guide_info = VoucherSendGuideInfo.from_alipay_dict(value)
    @property
    def voucher_use_guide_info(self):
        return self._voucher_use_guide_info

    @voucher_use_guide_info.setter
    def voucher_use_guide_info(self, value):
        if isinstance(value, VoucherUseGuideInfo):
            self._voucher_use_guide_info = value
        else:
            self._voucher_use_guide_info = VoucherUseGuideInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.voucher_send_guide_info:
            if hasattr(self.voucher_send_guide_info, 'to_alipay_dict'):
                params['voucher_send_guide_info'] = self.voucher_send_guide_info.to_alipay_dict()
            else:
                params['voucher_send_guide_info'] = self.voucher_send_guide_info
        if self.voucher_use_guide_info:
            if hasattr(self.voucher_use_guide_info, 'to_alipay_dict'):
                params['voucher_use_guide_info'] = self.voucher_use_guide_info.to_alipay_dict()
            else:
                params['voucher_use_guide_info'] = self.voucher_use_guide_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherCustomerGuideInfo()
        if 'voucher_send_guide_info' in d:
            o.voucher_send_guide_info = d['voucher_send_guide_info']
        if 'voucher_use_guide_info' in d:
            o.voucher_use_guide_info = d['voucher_use_guide_info']
        return o


