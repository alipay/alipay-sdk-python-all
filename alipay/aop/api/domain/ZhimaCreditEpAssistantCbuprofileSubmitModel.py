#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpAssistantCbuprofileSubmitModel(object):

    def __init__(self):
        self._ali_id = None
        self._company_type = None
        self._cooperation_model = None
        self._main_cate_1_name = None
        self._main_cate_2_name = None
        self._sale_channels = None
        self._target_customer_type = None

    @property
    def ali_id(self):
        return self._ali_id

    @ali_id.setter
    def ali_id(self, value):
        self._ali_id = value
    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def cooperation_model(self):
        return self._cooperation_model

    @cooperation_model.setter
    def cooperation_model(self, value):
        if isinstance(value, list):
            self._cooperation_model = list()
            for i in value:
                self._cooperation_model.append(i)
    @property
    def main_cate_1_name(self):
        return self._main_cate_1_name

    @main_cate_1_name.setter
    def main_cate_1_name(self, value):
        self._main_cate_1_name = value
    @property
    def main_cate_2_name(self):
        return self._main_cate_2_name

    @main_cate_2_name.setter
    def main_cate_2_name(self, value):
        self._main_cate_2_name = value
    @property
    def sale_channels(self):
        return self._sale_channels

    @sale_channels.setter
    def sale_channels(self, value):
        if isinstance(value, list):
            self._sale_channels = list()
            for i in value:
                self._sale_channels.append(i)
    @property
    def target_customer_type(self):
        return self._target_customer_type

    @target_customer_type.setter
    def target_customer_type(self, value):
        if isinstance(value, list):
            self._target_customer_type = list()
            for i in value:
                self._target_customer_type.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.ali_id:
            if hasattr(self.ali_id, 'to_alipay_dict'):
                params['ali_id'] = self.ali_id.to_alipay_dict()
            else:
                params['ali_id'] = self.ali_id
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.cooperation_model:
            if isinstance(self.cooperation_model, list):
                for i in range(0, len(self.cooperation_model)):
                    element = self.cooperation_model[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cooperation_model[i] = element.to_alipay_dict()
            if hasattr(self.cooperation_model, 'to_alipay_dict'):
                params['cooperation_model'] = self.cooperation_model.to_alipay_dict()
            else:
                params['cooperation_model'] = self.cooperation_model
        if self.main_cate_1_name:
            if hasattr(self.main_cate_1_name, 'to_alipay_dict'):
                params['main_cate_1_name'] = self.main_cate_1_name.to_alipay_dict()
            else:
                params['main_cate_1_name'] = self.main_cate_1_name
        if self.main_cate_2_name:
            if hasattr(self.main_cate_2_name, 'to_alipay_dict'):
                params['main_cate_2_name'] = self.main_cate_2_name.to_alipay_dict()
            else:
                params['main_cate_2_name'] = self.main_cate_2_name
        if self.sale_channels:
            if isinstance(self.sale_channels, list):
                for i in range(0, len(self.sale_channels)):
                    element = self.sale_channels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sale_channels[i] = element.to_alipay_dict()
            if hasattr(self.sale_channels, 'to_alipay_dict'):
                params['sale_channels'] = self.sale_channels.to_alipay_dict()
            else:
                params['sale_channels'] = self.sale_channels
        if self.target_customer_type:
            if isinstance(self.target_customer_type, list):
                for i in range(0, len(self.target_customer_type)):
                    element = self.target_customer_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_customer_type[i] = element.to_alipay_dict()
            if hasattr(self.target_customer_type, 'to_alipay_dict'):
                params['target_customer_type'] = self.target_customer_type.to_alipay_dict()
            else:
                params['target_customer_type'] = self.target_customer_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAssistantCbuprofileSubmitModel()
        if 'ali_id' in d:
            o.ali_id = d['ali_id']
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'cooperation_model' in d:
            o.cooperation_model = d['cooperation_model']
        if 'main_cate_1_name' in d:
            o.main_cate_1_name = d['main_cate_1_name']
        if 'main_cate_2_name' in d:
            o.main_cate_2_name = d['main_cate_2_name']
        if 'sale_channels' in d:
            o.sale_channels = d['sale_channels']
        if 'target_customer_type' in d:
            o.target_customer_type = d['target_customer_type']
        return o


