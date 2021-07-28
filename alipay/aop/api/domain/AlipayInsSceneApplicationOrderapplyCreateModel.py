#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ClaimStrategy import ClaimStrategy
from alipay.aop.api.domain.InsOrderInfo import InsOrderInfo


class AlipayInsSceneApplicationOrderapplyCreateModel(object):

    def __init__(self):
        self._biz_data = None
        self._claim_strategy_list = None
        self._havana_id = None
        self._order_info = None
        self._out_biz_no = None
        self._policy_no = None
        self._prod_code = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def claim_strategy_list(self):
        return self._claim_strategy_list

    @claim_strategy_list.setter
    def claim_strategy_list(self, value):
        if isinstance(value, list):
            self._claim_strategy_list = list()
            for i in value:
                if isinstance(i, ClaimStrategy):
                    self._claim_strategy_list.append(i)
                else:
                    self._claim_strategy_list.append(ClaimStrategy.from_alipay_dict(i))
    @property
    def havana_id(self):
        return self._havana_id

    @havana_id.setter
    def havana_id(self, value):
        self._havana_id = value
    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, value):
        if isinstance(value, InsOrderInfo):
            self._order_info = value
        else:
            self._order_info = InsOrderInfo.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.claim_strategy_list:
            if isinstance(self.claim_strategy_list, list):
                for i in range(0, len(self.claim_strategy_list)):
                    element = self.claim_strategy_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.claim_strategy_list[i] = element.to_alipay_dict()
            if hasattr(self.claim_strategy_list, 'to_alipay_dict'):
                params['claim_strategy_list'] = self.claim_strategy_list.to_alipay_dict()
            else:
                params['claim_strategy_list'] = self.claim_strategy_list
        if self.havana_id:
            if hasattr(self.havana_id, 'to_alipay_dict'):
                params['havana_id'] = self.havana_id.to_alipay_dict()
            else:
                params['havana_id'] = self.havana_id
        if self.order_info:
            if hasattr(self.order_info, 'to_alipay_dict'):
                params['order_info'] = self.order_info.to_alipay_dict()
            else:
                params['order_info'] = self.order_info
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneApplicationOrderapplyCreateModel()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'claim_strategy_list' in d:
            o.claim_strategy_list = d['claim_strategy_list']
        if 'havana_id' in d:
            o.havana_id = d['havana_id']
        if 'order_info' in d:
            o.order_info = d['order_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        return o


