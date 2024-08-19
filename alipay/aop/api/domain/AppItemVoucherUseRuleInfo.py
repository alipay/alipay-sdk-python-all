#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemVoucherUseTimeInfo import AppItemVoucherUseTimeInfo


class AppItemVoucherUseRuleInfo(object):

    def __init__(self):
        self._app_item_voucher_use_time_info = None

    @property
    def app_item_voucher_use_time_info(self):
        return self._app_item_voucher_use_time_info

    @app_item_voucher_use_time_info.setter
    def app_item_voucher_use_time_info(self, value):
        if isinstance(value, AppItemVoucherUseTimeInfo):
            self._app_item_voucher_use_time_info = value
        else:
            self._app_item_voucher_use_time_info = AppItemVoucherUseTimeInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.app_item_voucher_use_time_info:
            if hasattr(self.app_item_voucher_use_time_info, 'to_alipay_dict'):
                params['app_item_voucher_use_time_info'] = self.app_item_voucher_use_time_info.to_alipay_dict()
            else:
                params['app_item_voucher_use_time_info'] = self.app_item_voucher_use_time_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemVoucherUseRuleInfo()
        if 'app_item_voucher_use_time_info' in d:
            o.app_item_voucher_use_time_info = d['app_item_voucher_use_time_info']
        return o


