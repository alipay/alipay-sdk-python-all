#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceServicerightsusageQueryModel(object):

    def __init__(self):
        self._company_type = None
        self._fulfillment_id = None
        self._open_id = None
        self._user_id = None

    @property
    def company_type(self):
        return self._company_type

    @company_type.setter
    def company_type(self, value):
        self._company_type = value
    @property
    def fulfillment_id(self):
        return self._fulfillment_id

    @fulfillment_id.setter
    def fulfillment_id(self, value):
        self._fulfillment_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_type:
            if hasattr(self.company_type, 'to_alipay_dict'):
                params['company_type'] = self.company_type.to_alipay_dict()
            else:
                params['company_type'] = self.company_type
        if self.fulfillment_id:
            if hasattr(self.fulfillment_id, 'to_alipay_dict'):
                params['fulfillment_id'] = self.fulfillment_id.to_alipay_dict()
            else:
                params['fulfillment_id'] = self.fulfillment_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceServicerightsusageQueryModel()
        if 'company_type' in d:
            o.company_type = d['company_type']
        if 'fulfillment_id' in d:
            o.fulfillment_id = d['fulfillment_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


