#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantSettleRelationProcessorResponse import MerchantSettleRelationProcessorResponse


class IndirectMerchantProcessorResponse(object):

    def __init__(self):
        self._audit_status = None
        self._business_status = None
        self._industry_template_code = None
        self._industry_template_name = None
        self._login_id = None
        self._logo_url = None
        self._merchant_app_id = None
        self._merchant_name = None
        self._merchant_pid = None
        self._merchant_settle_relation_list = None
        self._operator = None
        self._phone = None
        self._smid = None
        self._zm_service_id = None

    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def business_status(self):
        return self._business_status

    @business_status.setter
    def business_status(self, value):
        self._business_status = value
    @property
    def industry_template_code(self):
        return self._industry_template_code

    @industry_template_code.setter
    def industry_template_code(self, value):
        self._industry_template_code = value
    @property
    def industry_template_name(self):
        return self._industry_template_name

    @industry_template_name.setter
    def industry_template_name(self, value):
        self._industry_template_name = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
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
                if isinstance(i, MerchantSettleRelationProcessorResponse):
                    self._merchant_settle_relation_list.append(i)
                else:
                    self._merchant_settle_relation_list.append(MerchantSettleRelationProcessorResponse.from_alipay_dict(i))
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def zm_service_id(self):
        return self._zm_service_id

    @zm_service_id.setter
    def zm_service_id(self, value):
        self._zm_service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.business_status:
            if hasattr(self.business_status, 'to_alipay_dict'):
                params['business_status'] = self.business_status.to_alipay_dict()
            else:
                params['business_status'] = self.business_status
        if self.industry_template_code:
            if hasattr(self.industry_template_code, 'to_alipay_dict'):
                params['industry_template_code'] = self.industry_template_code.to_alipay_dict()
            else:
                params['industry_template_code'] = self.industry_template_code
        if self.industry_template_name:
            if hasattr(self.industry_template_name, 'to_alipay_dict'):
                params['industry_template_name'] = self.industry_template_name.to_alipay_dict()
            else:
                params['industry_template_name'] = self.industry_template_name
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
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
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.zm_service_id:
            if hasattr(self.zm_service_id, 'to_alipay_dict'):
                params['zm_service_id'] = self.zm_service_id.to_alipay_dict()
            else:
                params['zm_service_id'] = self.zm_service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndirectMerchantProcessorResponse()
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'business_status' in d:
            o.business_status = d['business_status']
        if 'industry_template_code' in d:
            o.industry_template_code = d['industry_template_code']
        if 'industry_template_name' in d:
            o.industry_template_name = d['industry_template_name']
        if 'login_id' in d:
            o.login_id = d['login_id']
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
        if 'operator' in d:
            o.operator = d['operator']
        if 'phone' in d:
            o.phone = d['phone']
        if 'smid' in d:
            o.smid = d['smid']
        if 'zm_service_id' in d:
            o.zm_service_id = d['zm_service_id']
        return o


