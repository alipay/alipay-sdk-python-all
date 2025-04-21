#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundJointaccountRelationQueryModel(object):

    def __init__(self):
        self._account_id = None
        self._biz_scene = None
        self._out_biz_no = None
        self._product_code = None
        self._query_payment = None
        self._relation_id = None
        self._request_open_id = None
        self._request_user_id = None
        self._request_user_type = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def query_payment(self):
        return self._query_payment

    @query_payment.setter
    def query_payment(self, value):
        self._query_payment = value
    @property
    def relation_id(self):
        return self._relation_id

    @relation_id.setter
    def relation_id(self, value):
        self._relation_id = value
    @property
    def request_open_id(self):
        return self._request_open_id

    @request_open_id.setter
    def request_open_id(self, value):
        self._request_open_id = value
    @property
    def request_user_id(self):
        return self._request_user_id

    @request_user_id.setter
    def request_user_id(self, value):
        self._request_user_id = value
    @property
    def request_user_type(self):
        return self._request_user_type

    @request_user_type.setter
    def request_user_type(self, value):
        self._request_user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.query_payment:
            if hasattr(self.query_payment, 'to_alipay_dict'):
                params['query_payment'] = self.query_payment.to_alipay_dict()
            else:
                params['query_payment'] = self.query_payment
        if self.relation_id:
            if hasattr(self.relation_id, 'to_alipay_dict'):
                params['relation_id'] = self.relation_id.to_alipay_dict()
            else:
                params['relation_id'] = self.relation_id
        if self.request_open_id:
            if hasattr(self.request_open_id, 'to_alipay_dict'):
                params['request_open_id'] = self.request_open_id.to_alipay_dict()
            else:
                params['request_open_id'] = self.request_open_id
        if self.request_user_id:
            if hasattr(self.request_user_id, 'to_alipay_dict'):
                params['request_user_id'] = self.request_user_id.to_alipay_dict()
            else:
                params['request_user_id'] = self.request_user_id
        if self.request_user_type:
            if hasattr(self.request_user_type, 'to_alipay_dict'):
                params['request_user_type'] = self.request_user_type.to_alipay_dict()
            else:
                params['request_user_type'] = self.request_user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundJointaccountRelationQueryModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'query_payment' in d:
            o.query_payment = d['query_payment']
        if 'relation_id' in d:
            o.relation_id = d['relation_id']
        if 'request_open_id' in d:
            o.request_open_id = d['request_open_id']
        if 'request_user_id' in d:
            o.request_user_id = d['request_user_id']
        if 'request_user_type' in d:
            o.request_user_type = d['request_user_type']
        return o


