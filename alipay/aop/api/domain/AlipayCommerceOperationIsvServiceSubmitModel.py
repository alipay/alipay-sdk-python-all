#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtraInfo import ExtraInfo
from alipay.aop.api.domain.CateringMerchantInfo import CateringMerchantInfo
from alipay.aop.api.domain.ServiceBusinessHours import ServiceBusinessHours
from alipay.aop.api.domain.CateringServiceScopeInfo import CateringServiceScopeInfo
from alipay.aop.api.domain.CateringStoreInfo import CateringStoreInfo


class AlipayCommerceOperationIsvServiceSubmitModel(object):

    def __init__(self):
        self._extra_info = None
        self._merchant_info = None
        self._service_business_hours = None
        self._service_description = None
        self._service_name = None
        self._service_scope_info = None
        self._service_status = None
        self._service_sub_type = None
        self._service_type = None
        self._service_url = None
        self._store_info = None

    @property
    def extra_info(self):
        return self._extra_info

    @extra_info.setter
    def extra_info(self, value):
        if isinstance(value, list):
            self._extra_info = list()
            for i in value:
                if isinstance(i, ExtraInfo):
                    self._extra_info.append(i)
                else:
                    self._extra_info.append(ExtraInfo.from_alipay_dict(i))
    @property
    def merchant_info(self):
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        if isinstance(value, CateringMerchantInfo):
            self._merchant_info = value
        else:
            self._merchant_info = CateringMerchantInfo.from_alipay_dict(value)
    @property
    def service_business_hours(self):
        return self._service_business_hours

    @service_business_hours.setter
    def service_business_hours(self, value):
        if isinstance(value, list):
            self._service_business_hours = list()
            for i in value:
                if isinstance(i, ServiceBusinessHours):
                    self._service_business_hours.append(i)
                else:
                    self._service_business_hours.append(ServiceBusinessHours.from_alipay_dict(i))
    @property
    def service_description(self):
        return self._service_description

    @service_description.setter
    def service_description(self, value):
        self._service_description = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_scope_info(self):
        return self._service_scope_info

    @service_scope_info.setter
    def service_scope_info(self, value):
        if isinstance(value, CateringServiceScopeInfo):
            self._service_scope_info = value
        else:
            self._service_scope_info = CateringServiceScopeInfo.from_alipay_dict(value)
    @property
    def service_status(self):
        return self._service_status

    @service_status.setter
    def service_status(self, value):
        self._service_status = value
    @property
    def service_sub_type(self):
        return self._service_sub_type

    @service_sub_type.setter
    def service_sub_type(self, value):
        self._service_sub_type = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value
    @property
    def store_info(self):
        return self._store_info

    @store_info.setter
    def store_info(self, value):
        if isinstance(value, CateringStoreInfo):
            self._store_info = value
        else:
            self._store_info = CateringStoreInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.extra_info:
            if isinstance(self.extra_info, list):
                for i in range(0, len(self.extra_info)):
                    element = self.extra_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extra_info[i] = element.to_alipay_dict()
            if hasattr(self.extra_info, 'to_alipay_dict'):
                params['extra_info'] = self.extra_info.to_alipay_dict()
            else:
                params['extra_info'] = self.extra_info
        if self.merchant_info:
            if hasattr(self.merchant_info, 'to_alipay_dict'):
                params['merchant_info'] = self.merchant_info.to_alipay_dict()
            else:
                params['merchant_info'] = self.merchant_info
        if self.service_business_hours:
            if isinstance(self.service_business_hours, list):
                for i in range(0, len(self.service_business_hours)):
                    element = self.service_business_hours[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_business_hours[i] = element.to_alipay_dict()
            if hasattr(self.service_business_hours, 'to_alipay_dict'):
                params['service_business_hours'] = self.service_business_hours.to_alipay_dict()
            else:
                params['service_business_hours'] = self.service_business_hours
        if self.service_description:
            if hasattr(self.service_description, 'to_alipay_dict'):
                params['service_description'] = self.service_description.to_alipay_dict()
            else:
                params['service_description'] = self.service_description
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_scope_info:
            if hasattr(self.service_scope_info, 'to_alipay_dict'):
                params['service_scope_info'] = self.service_scope_info.to_alipay_dict()
            else:
                params['service_scope_info'] = self.service_scope_info
        if self.service_status:
            if hasattr(self.service_status, 'to_alipay_dict'):
                params['service_status'] = self.service_status.to_alipay_dict()
            else:
                params['service_status'] = self.service_status
        if self.service_sub_type:
            if hasattr(self.service_sub_type, 'to_alipay_dict'):
                params['service_sub_type'] = self.service_sub_type.to_alipay_dict()
            else:
                params['service_sub_type'] = self.service_sub_type
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.service_url:
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
        if self.store_info:
            if hasattr(self.store_info, 'to_alipay_dict'):
                params['store_info'] = self.store_info.to_alipay_dict()
            else:
                params['store_info'] = self.store_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationIsvServiceSubmitModel()
        if 'extra_info' in d:
            o.extra_info = d['extra_info']
        if 'merchant_info' in d:
            o.merchant_info = d['merchant_info']
        if 'service_business_hours' in d:
            o.service_business_hours = d['service_business_hours']
        if 'service_description' in d:
            o.service_description = d['service_description']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_scope_info' in d:
            o.service_scope_info = d['service_scope_info']
        if 'service_status' in d:
            o.service_status = d['service_status']
        if 'service_sub_type' in d:
            o.service_sub_type = d['service_sub_type']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'service_url' in d:
            o.service_url = d['service_url']
        if 'store_info' in d:
            o.store_info = d['store_info']
        return o


