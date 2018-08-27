#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InterfaceInfoList import InterfaceInfoList


class AlipayEcoMycarParkingConfigSetModel(object):

    def __init__(self):
        self._account_no = None
        self._interface_info_list = None
        self._merchant_logo = None
        self._merchant_name = None
        self._merchant_service_phone = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def interface_info_list(self):
        return self._interface_info_list

    @interface_info_list.setter
    def interface_info_list(self, value):
        if isinstance(value, list):
            self._interface_info_list = list()
            for i in value:
                if isinstance(i, InterfaceInfoList):
                    self._interface_info_list.append(i)
                else:
                    self._interface_info_list.append(InterfaceInfoList.from_alipay_dict(i))
    @property
    def merchant_logo(self):
        return self._merchant_logo

    @merchant_logo.setter
    def merchant_logo(self, value):
        self._merchant_logo = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_service_phone(self):
        return self._merchant_service_phone

    @merchant_service_phone.setter
    def merchant_service_phone(self, value):
        self._merchant_service_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.interface_info_list:
            if isinstance(self.interface_info_list, list):
                for i in range(0, len(self.interface_info_list)):
                    element = self.interface_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.interface_info_list[i] = element.to_alipay_dict()
            if hasattr(self.interface_info_list, 'to_alipay_dict'):
                params['interface_info_list'] = self.interface_info_list.to_alipay_dict()
            else:
                params['interface_info_list'] = self.interface_info_list
        if self.merchant_logo:
            if hasattr(self.merchant_logo, 'to_alipay_dict'):
                params['merchant_logo'] = self.merchant_logo.to_alipay_dict()
            else:
                params['merchant_logo'] = self.merchant_logo
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_service_phone:
            if hasattr(self.merchant_service_phone, 'to_alipay_dict'):
                params['merchant_service_phone'] = self.merchant_service_phone.to_alipay_dict()
            else:
                params['merchant_service_phone'] = self.merchant_service_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarParkingConfigSetModel()
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'interface_info_list' in d:
            o.interface_info_list = d['interface_info_list']
        if 'merchant_logo' in d:
            o.merchant_logo = d['merchant_logo']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_service_phone' in d:
            o.merchant_service_phone = d['merchant_service_phone']
        return o


