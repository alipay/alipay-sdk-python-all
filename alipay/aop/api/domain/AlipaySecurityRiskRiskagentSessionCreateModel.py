#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskRiskagentSessionCreateModel(object):

    def __init__(self):
        self._action_context = None
        self._action_type = None
        self._business_code = None
        self._business_scene = None
        self._gmt_occur = None
        self._main_id = None
        self._main_id_type = None
        self._query_context = None
        self._query_id = None
        self._query_property = None
        self._query_type = None
        self._query_user_id = None
        self._risk_label = None
        self._secondary_id = None
        self._secondary_id_type = None
        self._trade_amount = None
        self._trade_no = None

    @property
    def action_context(self):
        return self._action_context

    @action_context.setter
    def action_context(self, value):
        self._action_context = value
    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def business_code(self):
        return self._business_code

    @business_code.setter
    def business_code(self, value):
        self._business_code = value
    @property
    def business_scene(self):
        return self._business_scene

    @business_scene.setter
    def business_scene(self, value):
        self._business_scene = value
    @property
    def gmt_occur(self):
        return self._gmt_occur

    @gmt_occur.setter
    def gmt_occur(self, value):
        self._gmt_occur = value
    @property
    def main_id(self):
        return self._main_id

    @main_id.setter
    def main_id(self, value):
        self._main_id = value
    @property
    def main_id_type(self):
        return self._main_id_type

    @main_id_type.setter
    def main_id_type(self, value):
        self._main_id_type = value
    @property
    def query_context(self):
        return self._query_context

    @query_context.setter
    def query_context(self, value):
        self._query_context = value
    @property
    def query_id(self):
        return self._query_id

    @query_id.setter
    def query_id(self, value):
        self._query_id = value
    @property
    def query_property(self):
        return self._query_property

    @query_property.setter
    def query_property(self, value):
        self._query_property = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def query_user_id(self):
        return self._query_user_id

    @query_user_id.setter
    def query_user_id(self, value):
        self._query_user_id = value
    @property
    def risk_label(self):
        return self._risk_label

    @risk_label.setter
    def risk_label(self, value):
        self._risk_label = value
    @property
    def secondary_id(self):
        return self._secondary_id

    @secondary_id.setter
    def secondary_id(self, value):
        self._secondary_id = value
    @property
    def secondary_id_type(self):
        return self._secondary_id_type

    @secondary_id_type.setter
    def secondary_id_type(self, value):
        self._secondary_id_type = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_context:
            if hasattr(self.action_context, 'to_alipay_dict'):
                params['action_context'] = self.action_context.to_alipay_dict()
            else:
                params['action_context'] = self.action_context
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.business_code:
            if hasattr(self.business_code, 'to_alipay_dict'):
                params['business_code'] = self.business_code.to_alipay_dict()
            else:
                params['business_code'] = self.business_code
        if self.business_scene:
            if hasattr(self.business_scene, 'to_alipay_dict'):
                params['business_scene'] = self.business_scene.to_alipay_dict()
            else:
                params['business_scene'] = self.business_scene
        if self.gmt_occur:
            if hasattr(self.gmt_occur, 'to_alipay_dict'):
                params['gmt_occur'] = self.gmt_occur.to_alipay_dict()
            else:
                params['gmt_occur'] = self.gmt_occur
        if self.main_id:
            if hasattr(self.main_id, 'to_alipay_dict'):
                params['main_id'] = self.main_id.to_alipay_dict()
            else:
                params['main_id'] = self.main_id
        if self.main_id_type:
            if hasattr(self.main_id_type, 'to_alipay_dict'):
                params['main_id_type'] = self.main_id_type.to_alipay_dict()
            else:
                params['main_id_type'] = self.main_id_type
        if self.query_context:
            if hasattr(self.query_context, 'to_alipay_dict'):
                params['query_context'] = self.query_context.to_alipay_dict()
            else:
                params['query_context'] = self.query_context
        if self.query_id:
            if hasattr(self.query_id, 'to_alipay_dict'):
                params['query_id'] = self.query_id.to_alipay_dict()
            else:
                params['query_id'] = self.query_id
        if self.query_property:
            if hasattr(self.query_property, 'to_alipay_dict'):
                params['query_property'] = self.query_property.to_alipay_dict()
            else:
                params['query_property'] = self.query_property
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.query_user_id:
            if hasattr(self.query_user_id, 'to_alipay_dict'):
                params['query_user_id'] = self.query_user_id.to_alipay_dict()
            else:
                params['query_user_id'] = self.query_user_id
        if self.risk_label:
            if hasattr(self.risk_label, 'to_alipay_dict'):
                params['risk_label'] = self.risk_label.to_alipay_dict()
            else:
                params['risk_label'] = self.risk_label
        if self.secondary_id:
            if hasattr(self.secondary_id, 'to_alipay_dict'):
                params['secondary_id'] = self.secondary_id.to_alipay_dict()
            else:
                params['secondary_id'] = self.secondary_id
        if self.secondary_id_type:
            if hasattr(self.secondary_id_type, 'to_alipay_dict'):
                params['secondary_id_type'] = self.secondary_id_type.to_alipay_dict()
            else:
                params['secondary_id_type'] = self.secondary_id_type
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskRiskagentSessionCreateModel()
        if 'action_context' in d:
            o.action_context = d['action_context']
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'business_scene' in d:
            o.business_scene = d['business_scene']
        if 'gmt_occur' in d:
            o.gmt_occur = d['gmt_occur']
        if 'main_id' in d:
            o.main_id = d['main_id']
        if 'main_id_type' in d:
            o.main_id_type = d['main_id_type']
        if 'query_context' in d:
            o.query_context = d['query_context']
        if 'query_id' in d:
            o.query_id = d['query_id']
        if 'query_property' in d:
            o.query_property = d['query_property']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'query_user_id' in d:
            o.query_user_id = d['query_user_id']
        if 'risk_label' in d:
            o.risk_label = d['risk_label']
        if 'secondary_id' in d:
            o.secondary_id = d['secondary_id']
        if 'secondary_id_type' in d:
            o.secondary_id_type = d['secondary_id_type']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


