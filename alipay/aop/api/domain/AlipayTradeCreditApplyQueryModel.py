#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeCreditApplyQueryModel(object):

    def __init__(self):
        self._buyer_credit_source = None
        self._buyer_user_id = None
        self._credit_scene = None
        self._grant_operation_no = None
        self._out_request_no = None

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
    def credit_scene(self):
        return self._credit_scene

    @credit_scene.setter
    def credit_scene(self, value):
        self._credit_scene = value
    @property
    def grant_operation_no(self):
        return self._grant_operation_no

    @grant_operation_no.setter
    def grant_operation_no(self, value):
        self._grant_operation_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value


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
        if self.credit_scene:
            if hasattr(self.credit_scene, 'to_alipay_dict'):
                params['credit_scene'] = self.credit_scene.to_alipay_dict()
            else:
                params['credit_scene'] = self.credit_scene
        if self.grant_operation_no:
            if hasattr(self.grant_operation_no, 'to_alipay_dict'):
                params['grant_operation_no'] = self.grant_operation_no.to_alipay_dict()
            else:
                params['grant_operation_no'] = self.grant_operation_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeCreditApplyQueryModel()
        if 'buyer_credit_source' in d:
            o.buyer_credit_source = d['buyer_credit_source']
        if 'buyer_user_id' in d:
            o.buyer_user_id = d['buyer_user_id']
        if 'credit_scene' in d:
            o.credit_scene = d['credit_scene']
        if 'grant_operation_no' in d:
            o.grant_operation_no = d['grant_operation_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        return o


