#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeBuyerCreditApplyModel(object):

    def __init__(self):
        self._buyer_credit_source = None
        self._buyer_user_id = None
        self._credit_period = None
        self._credit_scene = None
        self._grant_credit_quota = None
        self._merchant_credit_source = None
        self._merchant_user_id = None
        self._operation_type = None
        self._out_request_no = None
        self._previous_credit_quota = None

    @property
    def buyer_credit_source(self):
        return self._buyer_credit_source

    @buyer_credit_source.setter
    def buyer_credit_source(self, value):
        self._buyer_credit_source = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def credit_period(self):
        return self._credit_period

    @credit_period.setter
    def credit_period(self, value):
        self._credit_period = value
    @property
    def credit_scene(self):
        return self._credit_scene

    @credit_scene.setter
    def credit_scene(self, value):
        self._credit_scene = value
    @property
    def grant_credit_quota(self):
        return self._grant_credit_quota

    @grant_credit_quota.setter
    def grant_credit_quota(self, value):
        self._grant_credit_quota = value
    @property
    def merchant_credit_source(self):
        return self._merchant_credit_source

    @merchant_credit_source.setter
    def merchant_credit_source(self, value):
        self._merchant_credit_source = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def previous_credit_quota(self):
        return self._previous_credit_quota

    @previous_credit_quota.setter
    def previous_credit_quota(self, value):
        self._previous_credit_quota = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_credit_source:
            if hasattr(self.buyer_credit_source, 'to_alipay_dict'):
                params['buyer_credit_source'] = self.buyer_credit_source.to_alipay_dict()
            else:
                params['buyer_credit_source'] = self.buyer_credit_source
        if self.buyer_user_id:
            if hasattr(self.buyer_user_id, 'to_alipay_dict'):
                params['buyer_user_id'] = self.buyer_user_id.to_alipay_dict()
            else:
                params['buyer_user_id'] = self.buyer_user_id
        if self.credit_period:
            if hasattr(self.credit_period, 'to_alipay_dict'):
                params['credit_period'] = self.credit_period.to_alipay_dict()
            else:
                params['credit_period'] = self.credit_period
        if self.credit_scene:
            if hasattr(self.credit_scene, 'to_alipay_dict'):
                params['credit_scene'] = self.credit_scene.to_alipay_dict()
            else:
                params['credit_scene'] = self.credit_scene
        if self.grant_credit_quota:
            if hasattr(self.grant_credit_quota, 'to_alipay_dict'):
                params['grant_credit_quota'] = self.grant_credit_quota.to_alipay_dict()
            else:
                params['grant_credit_quota'] = self.grant_credit_quota
        if self.merchant_credit_source:
            if hasattr(self.merchant_credit_source, 'to_alipay_dict'):
                params['merchant_credit_source'] = self.merchant_credit_source.to_alipay_dict()
            else:
                params['merchant_credit_source'] = self.merchant_credit_source
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.previous_credit_quota:
            if hasattr(self.previous_credit_quota, 'to_alipay_dict'):
                params['previous_credit_quota'] = self.previous_credit_quota.to_alipay_dict()
            else:
                params['previous_credit_quota'] = self.previous_credit_quota
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeBuyerCreditApplyModel()
        if 'buyer_credit_source' in d:
            o.buyer_credit_source = d['buyer_credit_source']
        if 'buyer_user_id' in d:
            o.buyer_user_id = d['buyer_user_id']
        if 'credit_period' in d:
            o.credit_period = d['credit_period']
        if 'credit_scene' in d:
            o.credit_scene = d['credit_scene']
        if 'grant_credit_quota' in d:
            o.grant_credit_quota = d['grant_credit_quota']
        if 'merchant_credit_source' in d:
            o.merchant_credit_source = d['merchant_credit_source']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'previous_credit_quota' in d:
            o.previous_credit_quota = d['previous_credit_quota']
        return o


