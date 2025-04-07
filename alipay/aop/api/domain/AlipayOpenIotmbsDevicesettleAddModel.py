#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsDevicesettleAddModel(object):

    def __init__(self):
        self._device_company_name = None
        self._owner_id = None
        self._sns = None
        self._source = None
        self._unique_id = None

    @property
    def device_company_name(self):
        return self._device_company_name

    @device_company_name.setter
    def device_company_name(self, value):
        self._device_company_name = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def sns(self):
        return self._sns

    @sns.setter
    def sns(self, value):
        if isinstance(value, list):
            self._sns = list()
            for i in value:
                self._sns.append(i)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_company_name:
            if hasattr(self.device_company_name, 'to_alipay_dict'):
                params['device_company_name'] = self.device_company_name.to_alipay_dict()
            else:
                params['device_company_name'] = self.device_company_name
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.sns:
            if isinstance(self.sns, list):
                for i in range(0, len(self.sns)):
                    element = self.sns[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sns[i] = element.to_alipay_dict()
            if hasattr(self.sns, 'to_alipay_dict'):
                params['sns'] = self.sns.to_alipay_dict()
            else:
                params['sns'] = self.sns
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsDevicesettleAddModel()
        if 'device_company_name' in d:
            o.device_company_name = d['device_company_name']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'sns' in d:
            o.sns = d['sns']
        if 'source' in d:
            o.source = d['source']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        return o


