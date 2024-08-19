#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemVoucherQuerySendRuleInfo import AppItemVoucherQuerySendRuleInfo


class AppItemVoucherQuerySendModeInfo(object):

    def __init__(self):
        self._app_item_voucher_send_mode_info = None
        self._voucher_send_mode = None

    @property
    def app_item_voucher_send_mode_info(self):
        return self._app_item_voucher_send_mode_info

    @app_item_voucher_send_mode_info.setter
    def app_item_voucher_send_mode_info(self, value):
        if isinstance(value, AppItemVoucherQuerySendRuleInfo):
            self._app_item_voucher_send_mode_info = value
        else:
            self._app_item_voucher_send_mode_info = AppItemVoucherQuerySendRuleInfo.from_alipay_dict(value)
    @property
    def voucher_send_mode(self):
        return self._voucher_send_mode

    @voucher_send_mode.setter
    def voucher_send_mode(self, value):
        self._voucher_send_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_item_voucher_send_mode_info:
            if hasattr(self.app_item_voucher_send_mode_info, 'to_alipay_dict'):
                params['app_item_voucher_send_mode_info'] = self.app_item_voucher_send_mode_info.to_alipay_dict()
            else:
                params['app_item_voucher_send_mode_info'] = self.app_item_voucher_send_mode_info
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
        o = AppItemVoucherQuerySendModeInfo()
        if 'app_item_voucher_send_mode_info' in d:
            o.app_item_voucher_send_mode_info = d['app_item_voucher_send_mode_info']
        if 'voucher_send_mode' in d:
            o.voucher_send_mode = d['voucher_send_mode']
        return o


