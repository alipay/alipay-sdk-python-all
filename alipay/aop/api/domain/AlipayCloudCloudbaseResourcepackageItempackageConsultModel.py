#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseResourcepackageItempackageConsultModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._commodity_code = None
        self._effective_period_num = None
        self._effective_period_type = None
        self._purchase_number = None
        self._spec_code = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def commodity_code(self):
        return self._commodity_code

    @commodity_code.setter
    def commodity_code(self, value):
        self._commodity_code = value
    @property
    def effective_period_num(self):
        return self._effective_period_num

    @effective_period_num.setter
    def effective_period_num(self, value):
        self._effective_period_num = value
    @property
    def effective_period_type(self):
        return self._effective_period_type

    @effective_period_type.setter
    def effective_period_type(self, value):
        self._effective_period_type = value
    @property
    def purchase_number(self):
        return self._purchase_number

    @purchase_number.setter
    def purchase_number(self, value):
        self._purchase_number = value
    @property
    def spec_code(self):
        return self._spec_code

    @spec_code.setter
    def spec_code(self, value):
        self._spec_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.commodity_code:
            if hasattr(self.commodity_code, 'to_alipay_dict'):
                params['commodity_code'] = self.commodity_code.to_alipay_dict()
            else:
                params['commodity_code'] = self.commodity_code
        if self.effective_period_num:
            if hasattr(self.effective_period_num, 'to_alipay_dict'):
                params['effective_period_num'] = self.effective_period_num.to_alipay_dict()
            else:
                params['effective_period_num'] = self.effective_period_num
        if self.effective_period_type:
            if hasattr(self.effective_period_type, 'to_alipay_dict'):
                params['effective_period_type'] = self.effective_period_type.to_alipay_dict()
            else:
                params['effective_period_type'] = self.effective_period_type
        if self.purchase_number:
            if hasattr(self.purchase_number, 'to_alipay_dict'):
                params['purchase_number'] = self.purchase_number.to_alipay_dict()
            else:
                params['purchase_number'] = self.purchase_number
        if self.spec_code:
            if hasattr(self.spec_code, 'to_alipay_dict'):
                params['spec_code'] = self.spec_code.to_alipay_dict()
            else:
                params['spec_code'] = self.spec_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseResourcepackageItempackageConsultModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'commodity_code' in d:
            o.commodity_code = d['commodity_code']
        if 'effective_period_num' in d:
            o.effective_period_num = d['effective_period_num']
        if 'effective_period_type' in d:
            o.effective_period_type = d['effective_period_type']
        if 'purchase_number' in d:
            o.purchase_number = d['purchase_number']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        return o


