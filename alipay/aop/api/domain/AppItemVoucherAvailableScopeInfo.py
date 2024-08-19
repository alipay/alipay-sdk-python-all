#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherAvailableAppItemInfo import VoucherAvailableAppItemInfo


class AppItemVoucherAvailableScopeInfo(object):

    def __init__(self):
        self._app_item_voucher_available_info_list = None

    @property
    def app_item_voucher_available_info_list(self):
        return self._app_item_voucher_available_info_list

    @app_item_voucher_available_info_list.setter
    def app_item_voucher_available_info_list(self, value):
        if isinstance(value, list):
            self._app_item_voucher_available_info_list = list()
            for i in value:
                if isinstance(i, VoucherAvailableAppItemInfo):
                    self._app_item_voucher_available_info_list.append(i)
                else:
                    self._app_item_voucher_available_info_list.append(VoucherAvailableAppItemInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.app_item_voucher_available_info_list:
            if isinstance(self.app_item_voucher_available_info_list, list):
                for i in range(0, len(self.app_item_voucher_available_info_list)):
                    element = self.app_item_voucher_available_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_item_voucher_available_info_list[i] = element.to_alipay_dict()
            if hasattr(self.app_item_voucher_available_info_list, 'to_alipay_dict'):
                params['app_item_voucher_available_info_list'] = self.app_item_voucher_available_info_list.to_alipay_dict()
            else:
                params['app_item_voucher_available_info_list'] = self.app_item_voucher_available_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemVoucherAvailableScopeInfo()
        if 'app_item_voucher_available_info_list' in d:
            o.app_item_voucher_available_info_list = d['app_item_voucher_available_info_list']
        return o


