#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceDecorationPolicyCancelApplyModel(object):

    def __init__(self):
        self._inst_policy_no = None
        self._order_no = None
        self._out_order_no = None
        self._policy_no = None
        self._surrender_flow_no = None

    @property
    def inst_policy_no(self):
        return self._inst_policy_no

    @inst_policy_no.setter
    def inst_policy_no(self, value):
        self._inst_policy_no = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def surrender_flow_no(self):
        return self._surrender_flow_no

    @surrender_flow_no.setter
    def surrender_flow_no(self, value):
        self._surrender_flow_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_policy_no:
            if hasattr(self.inst_policy_no, 'to_alipay_dict'):
                params['inst_policy_no'] = self.inst_policy_no.to_alipay_dict()
            else:
                params['inst_policy_no'] = self.inst_policy_no
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.surrender_flow_no:
            if hasattr(self.surrender_flow_no, 'to_alipay_dict'):
                params['surrender_flow_no'] = self.surrender_flow_no.to_alipay_dict()
            else:
                params['surrender_flow_no'] = self.surrender_flow_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceDecorationPolicyCancelApplyModel()
        if 'inst_policy_no' in d:
            o.inst_policy_no = d['inst_policy_no']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'surrender_flow_no' in d:
            o.surrender_flow_no = d['surrender_flow_no']
        return o


