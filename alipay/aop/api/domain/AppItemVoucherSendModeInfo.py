#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemVoucherSendRuleInfo import AppItemVoucherSendRuleInfo


class AppItemVoucherSendModeInfo(object):

    def __init__(self):
        self._app_item_voucher_send_rule_info = None
        self._voucher_send_mode = None

    @property
    def app_item_voucher_send_rule_info(self):
        return self._app_item_voucher_send_rule_info

    @app_item_voucher_send_rule_info.setter
    def app_item_voucher_send_rule_info(self, value):
        if isinstance(value, AppItemVoucherSendRuleInfo):
            self._app_item_voucher_send_rule_info = value
        else:
            self._app_item_voucher_send_rule_info = AppItemVoucherSendRuleInfo.from_alipay_dict(value)
    @property
    def voucher_send_mode(self):
        return self._voucher_send_mode

    @voucher_send_mode.setter
    def voucher_send_mode(self, value):
        self._voucher_send_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_item_voucher_send_rule_info:
            if hasattr(self.app_item_voucher_send_rule_info, 'to_alipay_dict'):
                params['app_item_voucher_send_rule_info'] = self.app_item_voucher_send_rule_info.to_alipay_dict()
            else:
                params['app_item_voucher_send_rule_info'] = self.app_item_voucher_send_rule_info
        if self.voucher_send_mode:
            if hasattr(self.voucher_send_mode, 'to_alipay_dict'):
                params['voucher_send_mode'] = self.voucher_send_mode.to_alipay_dict()
            else:
                params['voucher_send_mode'] = self.voucher_send_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemVoucherSendModeInfo()
        if 'app_item_voucher_send_rule_info' in d:
            o.app_item_voucher_send_rule_info = d['app_item_voucher_send_rule_info']
        if 'voucher_send_mode' in d:
            o.voucher_send_mode = d['voucher_send_mode']
        return o


