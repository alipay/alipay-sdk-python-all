#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LeadsProductTypeDTO(object):

    def __init__(self):
        self._activation_start_date_time = None
        self._amortization_end_date_time = None
        self._ep_name = None
        self._id = None
        self._offline_commodity_description = None
        self._product_model = None

    @property
    def activation_start_date_time(self):
        return self._activation_start_date_time

    @activation_start_date_time.setter
    def activation_start_date_time(self, value):
        self._activation_start_date_time = value
    @property
    def amortization_end_date_time(self):
        return self._amortization_end_date_time

    @amortization_end_date_time.setter
    def amortization_end_date_time(self, value):
        self._amortization_end_date_time = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def offline_commodity_description(self):
        return self._offline_commodity_description

    @offline_commodity_description.setter
    def offline_commodity_description(self, value):
        self._offline_commodity_description = value
    @property
    def product_model(self):
        return self._product_model

    @product_model.setter
    def product_model(self, value):
        self._product_model = value


    def to_alipay_dict(self):
        params = dict()
        if self.activation_start_date_time:
            if hasattr(self.activation_start_date_time, 'to_alipay_dict'):
                params['activation_start_date_time'] = self.activation_start_date_time.to_alipay_dict()
            else:
                params['activation_start_date_time'] = self.activation_start_date_time
        if self.amortization_end_date_time:
            if hasattr(self.amortization_end_date_time, 'to_alipay_dict'):
                params['amortization_end_date_time'] = self.amortization_end_date_time.to_alipay_dict()
            else:
                params['amortization_end_date_time'] = self.amortization_end_date_time
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.offline_commodity_description:
            if hasattr(self.offline_commodity_description, 'to_alipay_dict'):
                params['offline_commodity_description'] = self.offline_commodity_description.to_alipay_dict()
            else:
                params['offline_commodity_description'] = self.offline_commodity_description
        if self.product_model:
            if hasattr(self.product_model, 'to_alipay_dict'):
                params['product_model'] = self.product_model.to_alipay_dict()
            else:
                params['product_model'] = self.product_model
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LeadsProductTypeDTO()
        if 'activation_start_date_time' in d:
            o.activation_start_date_time = d['activation_start_date_time']
        if 'amortization_end_date_time' in d:
            o.amortization_end_date_time = d['amortization_end_date_time']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'id' in d:
            o.id = d['id']
        if 'offline_commodity_description' in d:
            o.offline_commodity_description = d['offline_commodity_description']
        if 'product_model' in d:
            o.product_model = d['product_model']
        return o


