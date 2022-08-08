#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherPackageModeInfo import VoucherPackageModeInfo
from alipay.aop.api.domain.VoucherSaleModeInfo import VoucherSaleModeInfo
from alipay.aop.api.domain.VoucherSendRuleInfo import VoucherSendRuleInfo


class VoucherSendModeInfo(object):

    def __init__(self):
        self._voucher_package_mode_info = None
        self._voucher_sale_mode_info = None
        self._voucher_send_mode = None
        self._voucher_send_rule_info = None

    @property
    def voucher_package_mode_info(self):
        return self._voucher_package_mode_info

    @voucher_package_mode_info.setter
    def voucher_package_mode_info(self, value):
        if isinstance(value, VoucherPackageModeInfo):
            self._voucher_package_mode_info = value
        else:
            self._voucher_package_mode_info = VoucherPackageModeInfo.from_alipay_dict(value)
    @property
    def voucher_sale_mode_info(self):
        return self._voucher_sale_mode_info

    @voucher_sale_mode_info.setter
    def voucher_sale_mode_info(self, value):
        if isinstance(value, VoucherSaleModeInfo):
            self._voucher_sale_mode_info = value
        else:
            self._voucher_sale_mode_info = VoucherSaleModeInfo.from_alipay_dict(value)
    @property
    def voucher_send_mode(self):
        return self._voucher_send_mode

    @voucher_send_mode.setter
    def voucher_send_mode(self, value):
        self._voucher_send_mode = value
    @property
    def voucher_send_rule_info(self):
        return self._voucher_send_rule_info

    @voucher_send_rule_info.setter
    def voucher_send_rule_info(self, value):
        if isinstance(value, VoucherSendRuleInfo):
            self._voucher_send_rule_info = value
        else:
            self._voucher_send_rule_info = VoucherSendRuleInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.voucher_package_mode_info:
            if hasattr(self.voucher_package_mode_info, 'to_alipay_dict'):
                params['voucher_package_mode_info'] = self.voucher_package_mode_info.to_alipay_dict()
            else:
                params['voucher_package_mode_info'] = self.voucher_package_mode_info
        if self.voucher_sale_mode_info:
            if hasattr(self.voucher_sale_mode_info, 'to_alipay_dict'):
                params['voucher_sale_mode_info'] = self.voucher_sale_mode_info.to_alipay_dict()
            else:
                params['voucher_sale_mode_info'] = self.voucher_sale_mode_info
        if self.voucher_send_mode:
            if hasattr(self.voucher_send_mode, 'to_alipay_dict'):
                params['voucher_send_mode'] = self.voucher_send_mode.to_alipay_dict()
            else:
                params['voucher_send_mode'] = self.voucher_send_mode
        if self.voucher_send_rule_info:
            if hasattr(self.voucher_send_rule_info, 'to_alipay_dict'):
                params['voucher_send_rule_info'] = self.voucher_send_rule_info.to_alipay_dict()
            else:
                params['voucher_send_rule_info'] = self.voucher_send_rule_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherSendModeInfo()
        if 'voucher_package_mode_info' in d:
            o.voucher_package_mode_info = d['voucher_package_mode_info']
        if 'voucher_sale_mode_info' in d:
            o.voucher_sale_mode_info = d['voucher_sale_mode_info']
        if 'voucher_send_mode' in d:
            o.voucher_send_mode = d['voucher_send_mode']
        if 'voucher_send_rule_info' in d:
            o.voucher_send_rule_info = d['voucher_send_rule_info']
        return o


