#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemFixQueryVoucherInfo import AppItemFixQueryVoucherInfo


class AppItemVoucherQueryDeductInfo(object):

    def __init__(self):
        self._app_item_fix_voucher_info = None
        self._promo_type = None

    @property
    def app_item_fix_voucher_info(self):
        return self._app_item_fix_voucher_info

    @app_item_fix_voucher_info.setter
    def app_item_fix_voucher_info(self, value):
        if isinstance(value, AppItemFixQueryVoucherInfo):
            self._app_item_fix_voucher_info = value
        else:
            self._app_item_fix_voucher_info = AppItemFixQueryVoucherInfo.from_alipay_dict(value)
    @property
    def promo_type(self):
        return self._promo_type

    @promo_type.setter
    def promo_type(self, value):
        self._promo_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_item_fix_voucher_info:
            if hasattr(self.app_item_fix_voucher_info, 'to_alipay_dict'):
                params['app_item_fix_voucher_info'] = self.app_item_fix_voucher_info.to_alipay_dict()
            else:
                params['app_item_fix_voucher_info'] = self.app_item_fix_voucher_info
        if self.promo_type:
            if hasattr(self.promo_type, 'to_alipay_dict'):
                params['promo_type'] = self.promo_type.to_alipay_dict()
            else:
                params['promo_type'] = self.promo_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemVoucherQueryDeductInfo()
        if 'app_item_fix_voucher_info' in d:
            o.app_item_fix_voucher_info = d['app_item_fix_voucher_info']
        if 'promo_type' in d:
            o.promo_type = d['promo_type']
        return o


