#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppItemVoucherUseGuideInfo import AppItemVoucherUseGuideInfo


class AppItemVoucherCustomerGuideInfo(object):

    def __init__(self):
        self._app_item_voucher_use_guide_info = None

    @property
    def app_item_voucher_use_guide_info(self):
        return self._app_item_voucher_use_guide_info

    @app_item_voucher_use_guide_info.setter
    def app_item_voucher_use_guide_info(self, value):
        if isinstance(value, AppItemVoucherUseGuideInfo):
            self._app_item_voucher_use_guide_info = value
        else:
            self._app_item_voucher_use_guide_info = AppItemVoucherUseGuideInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.app_item_voucher_use_guide_info:
            if hasattr(self.app_item_voucher_use_guide_info, 'to_alipay_dict'):
                params['app_item_voucher_use_guide_info'] = self.app_item_voucher_use_guide_info.to_alipay_dict()
            else:
                params['app_item_voucher_use_guide_info'] = self.app_item_voucher_use_guide_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemVoucherCustomerGuideInfo()
        if 'app_item_voucher_use_guide_info' in d:
            o.app_item_voucher_use_guide_info = d['app_item_voucher_use_guide_info']
        return o


