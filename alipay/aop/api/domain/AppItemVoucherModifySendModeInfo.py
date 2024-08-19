#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemVoucherModifySendRuleInfo import AppItemVoucherModifySendRuleInfo


class AppItemVoucherModifySendModeInfo(object):

    def __init__(self):
        self._app_item_voucher_send_rule_info = None

    @property
    def app_item_voucher_send_rule_info(self):
        return self._app_item_voucher_send_rule_info

    @app_item_voucher_send_rule_info.setter
    def app_item_voucher_send_rule_info(self, value):
        if isinstance(value, AppItemVoucherModifySendRuleInfo):
            self._app_item_voucher_send_rule_info = value
        else:
            self._app_item_voucher_send_rule_info = AppItemVoucherModifySendRuleInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.app_item_voucher_send_rule_info:
            if hasattr(self.app_item_voucher_send_rule_info, 'to_alipay_dict'):
                params['app_item_voucher_send_rule_info'] = self.app_item_voucher_send_rule_info.to_alipay_dict()
            else:
                params['app_item_voucher_send_rule_info'] = self.app_item_voucher_send_rule_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemVoucherModifySendModeInfo()
        if 'app_item_voucher_send_rule_info' in d:
            o.app_item_voucher_send_rule_info = d['app_item_voucher_send_rule_info']
        return o


