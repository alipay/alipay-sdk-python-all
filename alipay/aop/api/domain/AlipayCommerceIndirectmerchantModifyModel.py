#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantSettleRelationProcessorRequest import MerchantSettleRelationProcessorRequest


class AlipayCommerceIndirectmerchantModifyModel(object):

    def __init__(self):
        self._industry_template_code = None
        self._logo_image_id = None
        self._logo_url = None
        self._merchant_app_id = None
        self._merchant_name = None
        self._merchant_pid = None
        self._merchant_settle_relation_list = None
        self._phone = None

    @property
    def industry_template_code(self):
        return self._industry_template_code

    @industry_template_code.setter
    def industry_template_code(self, value):
        self._industry_template_code = value
    @property
    def logo_image_id(self):
        return self._logo_image_id

    @logo_image_id.setter
    def logo_image_id(self, value):
        self._logo_image_id = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def merchant_app_id(self):
        return self._merchant_app_id

    @merchant_app_id.setter
    def merchant_app_id(self, value):
        self._merchant_app_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def merchant_settle_relation_list(self):
        return self._merchant_settle_relation_list

    @merchant_settle_relation_list.setter
    def merchant_settle_relation_list(self, value):
        if isinstance(value, list):
            self._merchant_settle_relation_list = list()
            for i in value:
                if isinstance(i, MerchantSettleRelationProcessorRequest):
                    self._merchant_settle_relation_list.append(i)
                else:
                    self._merchant_settle_relation_list.append(MerchantSettleRelationProcessorRequest.from_alipay_dict(i))
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.industry_template_code:
            if hasattr(self.industry_template_code, 'to_alipay_dict'):
                params['industry_template_code'] = self.industry_template_code.to_alipay_dict()
            else:
                params['industry_template_code'] = self.industry_template_code
        if self.logo_image_id:
            if hasattr(self.logo_image_id, 'to_alipay_dict'):
                params['logo_image_id'] = self.logo_image_id.to_alipay_dict()
            else:
                params['logo_image_id'] = self.logo_image_id
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.merchant_app_id:
            if hasattr(self.merchant_app_id, 'to_alipay_dict'):
                params['merchant_app_id'] = self.merchant_app_id.to_alipay_dict()
            else:
                params['merchant_app_id'] = self.merchant_app_id
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.merchant_settle_relation_list:
            if isinstance(self.merchant_settle_relation_list, list):
                for i in range(0, len(self.merchant_settle_relation_list)):
                    element = self.merchant_settle_relation_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_settle_relation_list[i] = element.to_alipay_dict()
            if hasattr(self.merchant_settle_relation_list, 'to_alipay_dict'):
                params['merchant_settle_relation_list'] = self.merchant_settle_relation_list.to_alipay_dict()
            else:
                params['merchant_settle_relation_list'] = self.merchant_settle_relation_list
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIndirectmerchantModifyModel()
        if 'industry_template_code' in d:
            o.industry_template_code = d['industry_template_code']
        if 'logo_image_id' in d:
            o.logo_image_id = d['logo_image_id']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'merchant_app_id' in d:
            o.merchant_app_id = d['merchant_app_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'merchant_settle_relation_list' in d:
            o.merchant_settle_relation_list = d['merchant_settle_relation_list']
        if 'phone' in d:
            o.phone = d['phone']
        return o


