#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseResourcepackageOpenConsultModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._purchase_month = None
        self._spec_code = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def purchase_month(self):
        return self._purchase_month

    @purchase_month.setter
    def purchase_month(self, value):
        self._purchase_month = value
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
        if self.purchase_month:
            if hasattr(self.purchase_month, 'to_alipay_dict'):
                params['purchase_month'] = self.purchase_month.to_alipay_dict()
            else:
                params['purchase_month'] = self.purchase_month
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
        o = AlipayCloudCloudbaseResourcepackageOpenConsultModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'purchase_month' in d:
            o.purchase_month = d['purchase_month']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        return o


