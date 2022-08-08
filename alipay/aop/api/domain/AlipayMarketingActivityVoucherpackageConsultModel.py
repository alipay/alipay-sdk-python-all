#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingActivityVoucherpackageConsultModel(object):

    def __init__(self):
        self._voucher_package_id_list = None

    @property
    def voucher_package_id_list(self):
        return self._voucher_package_id_list

    @voucher_package_id_list.setter
    def voucher_package_id_list(self, value):
        if isinstance(value, list):
            self._voucher_package_id_list = list()
            for i in value:
                self._voucher_package_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.voucher_package_id_list:
            if isinstance(self.voucher_package_id_list, list):
                for i in range(0, len(self.voucher_package_id_list)):
                    element = self.voucher_package_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.voucher_package_id_list[i] = element.to_alipay_dict()
            if hasattr(self.voucher_package_id_list, 'to_alipay_dict'):
                params['voucher_package_id_list'] = self.voucher_package_id_list.to_alipay_dict()
            else:
                params['voucher_package_id_list'] = self.voucher_package_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityVoucherpackageConsultModel()
        if 'voucher_package_id_list' in d:
            o.voucher_package_id_list = d['voucher_package_id_list']
        return o


