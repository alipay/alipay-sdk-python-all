#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsQuoteDTO import InsQuoteDTO


class InsPreOrderDTO(object):

    def __init__(self):
        self._biz_id = None
        self._partner_org_id = None
        self._policy_no = None
        self._pre_order_id = None
        self._product_plan_id = None
        self._quote_info = None
        self._recommend_flow_id = None
        self._status = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value
    @property
    def quote_info(self):
        return self._quote_info

    @quote_info.setter
    def quote_info(self, value):
        if isinstance(value, InsQuoteDTO):
            self._quote_info = value
        else:
            self._quote_info = InsQuoteDTO.from_alipay_dict(value)
    @property
    def recommend_flow_id(self):
        return self._recommend_flow_id

    @recommend_flow_id.setter
    def recommend_flow_id(self, value):
        self._recommend_flow_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.pre_order_id:
            if hasattr(self.pre_order_id, 'to_alipay_dict'):
                params['pre_order_id'] = self.pre_order_id.to_alipay_dict()
            else:
                params['pre_order_id'] = self.pre_order_id
        if self.product_plan_id:
            if hasattr(self.product_plan_id, 'to_alipay_dict'):
                params['product_plan_id'] = self.product_plan_id.to_alipay_dict()
            else:
                params['product_plan_id'] = self.product_plan_id
        if self.quote_info:
            if hasattr(self.quote_info, 'to_alipay_dict'):
                params['quote_info'] = self.quote_info.to_alipay_dict()
            else:
                params['quote_info'] = self.quote_info
        if self.recommend_flow_id:
            if hasattr(self.recommend_flow_id, 'to_alipay_dict'):
                params['recommend_flow_id'] = self.recommend_flow_id.to_alipay_dict()
            else:
                params['recommend_flow_id'] = self.recommend_flow_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsPreOrderDTO()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        if 'quote_info' in d:
            o.quote_info = d['quote_info']
        if 'recommend_flow_id' in d:
            o.recommend_flow_id = d['recommend_flow_id']
        if 'status' in d:
            o.status = d['status']
        return o


