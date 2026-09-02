#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeAgentDelegationPayModel(object):

    def __init__(self):
        self._agent_id = None
        self._agreement_no = None
        self._biz_order_no = None
        self._delegation_id = None
        self._out_request_no = None
        self._prepay_id = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def biz_order_no(self):
        return self._biz_order_no

    @biz_order_no.setter
    def biz_order_no(self, value):
        self._biz_order_no = value
    @property
    def delegation_id(self):
        return self._delegation_id

    @delegation_id.setter
    def delegation_id(self, value):
        self._delegation_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def prepay_id(self):
        return self._prepay_id

    @prepay_id.setter
    def prepay_id(self, value):
        self._prepay_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.biz_order_no:
            if hasattr(self.biz_order_no, 'to_alipay_dict'):
                params['biz_order_no'] = self.biz_order_no.to_alipay_dict()
            else:
                params['biz_order_no'] = self.biz_order_no
        if self.delegation_id:
            if hasattr(self.delegation_id, 'to_alipay_dict'):
                params['delegation_id'] = self.delegation_id.to_alipay_dict()
            else:
                params['delegation_id'] = self.delegation_id
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.prepay_id:
            if hasattr(self.prepay_id, 'to_alipay_dict'):
                params['prepay_id'] = self.prepay_id.to_alipay_dict()
            else:
                params['prepay_id'] = self.prepay_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeAgentDelegationPayModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'biz_order_no' in d:
            o.biz_order_no = d['biz_order_no']
        if 'delegation_id' in d:
            o.delegation_id = d['delegation_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'prepay_id' in d:
            o.prepay_id = d['prepay_id']
        return o


