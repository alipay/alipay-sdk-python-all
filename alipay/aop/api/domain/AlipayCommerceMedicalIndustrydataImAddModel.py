#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceProvider import ServiceProvider


class AlipayCommerceMedicalIndustrydataImAddModel(object):

    def __init__(self):
        self._alipay_order_id = None
        self._merchant_user_id = None
        self._out_biz_no = None
        self._out_chat_id = None
        self._service_providers = None

    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_chat_id(self):
        return self._out_chat_id

    @out_chat_id.setter
    def out_chat_id(self, value):
        self._out_chat_id = value
    @property
    def service_providers(self):
        return self._service_providers

    @service_providers.setter
    def service_providers(self, value):
        if isinstance(value, list):
            self._service_providers = list()
            for i in value:
                if isinstance(i, ServiceProvider):
                    self._service_providers.append(i)
                else:
                    self._service_providers.append(ServiceProvider.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_id:
            if hasattr(self.alipay_order_id, 'to_alipay_dict'):
                params['alipay_order_id'] = self.alipay_order_id.to_alipay_dict()
            else:
                params['alipay_order_id'] = self.alipay_order_id
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_chat_id:
            if hasattr(self.out_chat_id, 'to_alipay_dict'):
                params['out_chat_id'] = self.out_chat_id.to_alipay_dict()
            else:
                params['out_chat_id'] = self.out_chat_id
        if self.service_providers:
            if isinstance(self.service_providers, list):
                for i in range(0, len(self.service_providers)):
                    element = self.service_providers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_providers[i] = element.to_alipay_dict()
            if hasattr(self.service_providers, 'to_alipay_dict'):
                params['service_providers'] = self.service_providers.to_alipay_dict()
            else:
                params['service_providers'] = self.service_providers
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataImAddModel()
        if 'alipay_order_id' in d:
            o.alipay_order_id = d['alipay_order_id']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_chat_id' in d:
            o.out_chat_id = d['out_chat_id']
        if 'service_providers' in d:
            o.service_providers = d['service_providers']
        return o


