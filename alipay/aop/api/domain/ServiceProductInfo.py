#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceProductPreviewInfo import ServiceProductPreviewInfo
from alipay.aop.api.domain.ServiceProductAbilityInfo import ServiceProductAbilityInfo


class ServiceProductInfo(object):

    def __init__(self):
        self._service_desc = None
        self._service_expense_sub_type = None
        self._service_expense_sub_type_name = None
        self._service_id = None
        self._service_name = None
        self._service_order_model = None
        self._service_point = None
        self._service_preview_urls = None
        self._service_product_ability_info = None
        self._service_publish_id = None
        self._service_publish_name = None
        self._service_publish_type = None
        self._service_sign_type = None
        self._service_status = None
        self._service_type = None

    @property
    def service_desc(self):
        return self._service_desc

    @service_desc.setter
    def service_desc(self, value):
        self._service_desc = value
    @property
    def service_expense_sub_type(self):
        return self._service_expense_sub_type

    @service_expense_sub_type.setter
    def service_expense_sub_type(self, value):
        self._service_expense_sub_type = value
    @property
    def service_expense_sub_type_name(self):
        return self._service_expense_sub_type_name

    @service_expense_sub_type_name.setter
    def service_expense_sub_type_name(self, value):
        self._service_expense_sub_type_name = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_order_model(self):
        return self._service_order_model

    @service_order_model.setter
    def service_order_model(self, value):
        self._service_order_model = value
    @property
    def service_point(self):
        return self._service_point

    @service_point.setter
    def service_point(self, value):
        self._service_point = value
    @property
    def service_preview_urls(self):
        return self._service_preview_urls

    @service_preview_urls.setter
    def service_preview_urls(self, value):
        if isinstance(value, list):
            self._service_preview_urls = list()
            for i in value:
                if isinstance(i, ServiceProductPreviewInfo):
                    self._service_preview_urls.append(i)
                else:
                    self._service_preview_urls.append(ServiceProductPreviewInfo.from_alipay_dict(i))
    @property
    def service_product_ability_info(self):
        return self._service_product_ability_info

    @service_product_ability_info.setter
    def service_product_ability_info(self, value):
        if isinstance(value, list):
            self._service_product_ability_info = list()
            for i in value:
                if isinstance(i, ServiceProductAbilityInfo):
                    self._service_product_ability_info.append(i)
                else:
                    self._service_product_ability_info.append(ServiceProductAbilityInfo.from_alipay_dict(i))
    @property
    def service_publish_id(self):
        return self._service_publish_id

    @service_publish_id.setter
    def service_publish_id(self, value):
        self._service_publish_id = value
    @property
    def service_publish_name(self):
        return self._service_publish_name

    @service_publish_name.setter
    def service_publish_name(self, value):
        self._service_publish_name = value
    @property
    def service_publish_type(self):
        return self._service_publish_type

    @service_publish_type.setter
    def service_publish_type(self, value):
        self._service_publish_type = value
    @property
    def service_sign_type(self):
        return self._service_sign_type

    @service_sign_type.setter
    def service_sign_type(self, value):
        self._service_sign_type = value
    @property
    def service_status(self):
        return self._service_status

    @service_status.setter
    def service_status(self, value):
        self._service_status = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_desc:
            if hasattr(self.service_desc, 'to_alipay_dict'):
                params['service_desc'] = self.service_desc.to_alipay_dict()
            else:
                params['service_desc'] = self.service_desc
        if self.service_expense_sub_type:
            if hasattr(self.service_expense_sub_type, 'to_alipay_dict'):
                params['service_expense_sub_type'] = self.service_expense_sub_type.to_alipay_dict()
            else:
                params['service_expense_sub_type'] = self.service_expense_sub_type
        if self.service_expense_sub_type_name:
            if hasattr(self.service_expense_sub_type_name, 'to_alipay_dict'):
                params['service_expense_sub_type_name'] = self.service_expense_sub_type_name.to_alipay_dict()
            else:
                params['service_expense_sub_type_name'] = self.service_expense_sub_type_name
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_order_model:
            if hasattr(self.service_order_model, 'to_alipay_dict'):
                params['service_order_model'] = self.service_order_model.to_alipay_dict()
            else:
                params['service_order_model'] = self.service_order_model
        if self.service_point:
            if hasattr(self.service_point, 'to_alipay_dict'):
                params['service_point'] = self.service_point.to_alipay_dict()
            else:
                params['service_point'] = self.service_point
        if self.service_preview_urls:
            if isinstance(self.service_preview_urls, list):
                for i in range(0, len(self.service_preview_urls)):
                    element = self.service_preview_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_preview_urls[i] = element.to_alipay_dict()
            if hasattr(self.service_preview_urls, 'to_alipay_dict'):
                params['service_preview_urls'] = self.service_preview_urls.to_alipay_dict()
            else:
                params['service_preview_urls'] = self.service_preview_urls
        if self.service_product_ability_info:
            if isinstance(self.service_product_ability_info, list):
                for i in range(0, len(self.service_product_ability_info)):
                    element = self.service_product_ability_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_product_ability_info[i] = element.to_alipay_dict()
            if hasattr(self.service_product_ability_info, 'to_alipay_dict'):
                params['service_product_ability_info'] = self.service_product_ability_info.to_alipay_dict()
            else:
                params['service_product_ability_info'] = self.service_product_ability_info
        if self.service_publish_id:
            if hasattr(self.service_publish_id, 'to_alipay_dict'):
                params['service_publish_id'] = self.service_publish_id.to_alipay_dict()
            else:
                params['service_publish_id'] = self.service_publish_id
        if self.service_publish_name:
            if hasattr(self.service_publish_name, 'to_alipay_dict'):
                params['service_publish_name'] = self.service_publish_name.to_alipay_dict()
            else:
                params['service_publish_name'] = self.service_publish_name
        if self.service_publish_type:
            if hasattr(self.service_publish_type, 'to_alipay_dict'):
                params['service_publish_type'] = self.service_publish_type.to_alipay_dict()
            else:
                params['service_publish_type'] = self.service_publish_type
        if self.service_sign_type:
            if hasattr(self.service_sign_type, 'to_alipay_dict'):
                params['service_sign_type'] = self.service_sign_type.to_alipay_dict()
            else:
                params['service_sign_type'] = self.service_sign_type
        if self.service_status:
            if hasattr(self.service_status, 'to_alipay_dict'):
                params['service_status'] = self.service_status.to_alipay_dict()
            else:
                params['service_status'] = self.service_status
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceProductInfo()
        if 'service_desc' in d:
            o.service_desc = d['service_desc']
        if 'service_expense_sub_type' in d:
            o.service_expense_sub_type = d['service_expense_sub_type']
        if 'service_expense_sub_type_name' in d:
            o.service_expense_sub_type_name = d['service_expense_sub_type_name']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_order_model' in d:
            o.service_order_model = d['service_order_model']
        if 'service_point' in d:
            o.service_point = d['service_point']
        if 'service_preview_urls' in d:
            o.service_preview_urls = d['service_preview_urls']
        if 'service_product_ability_info' in d:
            o.service_product_ability_info = d['service_product_ability_info']
        if 'service_publish_id' in d:
            o.service_publish_id = d['service_publish_id']
        if 'service_publish_name' in d:
            o.service_publish_name = d['service_publish_name']
        if 'service_publish_type' in d:
            o.service_publish_type = d['service_publish_type']
        if 'service_sign_type' in d:
            o.service_sign_type = d['service_sign_type']
        if 'service_status' in d:
            o.service_status = d['service_status']
        if 'service_type' in d:
            o.service_type = d['service_type']
        return o


