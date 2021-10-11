#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenAPIContractRiskResult(object):

    def __init__(self):
        self._content = None
        self._deal_tip = None
        self._is_block = None
        self._result = None
        self._result_code = None
        self._result_msg = None
        self._risk_level = None
        self._risk_name = None
        self._risk_type = None
        self._summay = None
        self._v_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def deal_tip(self):
        return self._deal_tip

    @deal_tip.setter
    def deal_tip(self, value):
        self._deal_tip = value
    @property
    def is_block(self):
        return self._is_block

    @is_block.setter
    def is_block(self, value):
        self._is_block = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def risk_name(self):
        return self._risk_name

    @risk_name.setter
    def risk_name(self, value):
        self._risk_name = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value
    @property
    def summay(self):
        return self._summay

    @summay.setter
    def summay(self, value):
        self._summay = value
    @property
    def v_id(self):
        return self._v_id

    @v_id.setter
    def v_id(self, value):
        self._v_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.deal_tip:
            if hasattr(self.deal_tip, 'to_alipay_dict'):
                params['deal_tip'] = self.deal_tip.to_alipay_dict()
            else:
                params['deal_tip'] = self.deal_tip
        if self.is_block:
            if hasattr(self.is_block, 'to_alipay_dict'):
                params['is_block'] = self.is_block.to_alipay_dict()
            else:
                params['is_block'] = self.is_block
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.result_msg:
            if hasattr(self.result_msg, 'to_alipay_dict'):
                params['result_msg'] = self.result_msg.to_alipay_dict()
            else:
                params['result_msg'] = self.result_msg
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.risk_name:
            if hasattr(self.risk_name, 'to_alipay_dict'):
                params['risk_name'] = self.risk_name.to_alipay_dict()
            else:
                params['risk_name'] = self.risk_name
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        if self.summay:
            if hasattr(self.summay, 'to_alipay_dict'):
                params['summay'] = self.summay.to_alipay_dict()
            else:
                params['summay'] = self.summay
        if self.v_id:
            if hasattr(self.v_id, 'to_alipay_dict'):
                params['v_id'] = self.v_id.to_alipay_dict()
            else:
                params['v_id'] = self.v_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenAPIContractRiskResult()
        if 'content' in d:
            o.content = d['content']
        if 'deal_tip' in d:
            o.deal_tip = d['deal_tip']
        if 'is_block' in d:
            o.is_block = d['is_block']
        if 'result' in d:
            o.result = d['result']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_msg' in d:
            o.result_msg = d['result_msg']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'risk_name' in d:
            o.risk_name = d['risk_name']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        if 'summay' in d:
            o.summay = d['summay']
        if 'v_id' in d:
            o.v_id = d['v_id']
        return o


