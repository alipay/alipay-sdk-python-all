#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsPayEntryDTO import InsPayEntryDTO
from alipay.aop.api.domain.InsPayEntryDTO import InsPayEntryDTO


class AlipayInsSceneClaimOverdueCloseModel(object):

    def __init__(self):
        self._claim_no = None
        self._out_order_id = None
        self._overdue_no = None
        self._partner_org_id = None
        self._pay_entry_dto = None
        self._pay_entry_dto_list = None
        self._policy_no = None
        self._product_plan_id = None

    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def overdue_no(self):
        return self._overdue_no

    @overdue_no.setter
    def overdue_no(self, value):
        self._overdue_no = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def pay_entry_dto(self):
        return self._pay_entry_dto

    @pay_entry_dto.setter
    def pay_entry_dto(self, value):
        if isinstance(value, InsPayEntryDTO):
            self._pay_entry_dto = value
        else:
            self._pay_entry_dto = InsPayEntryDTO.from_alipay_dict(value)
    @property
    def pay_entry_dto_list(self):
        return self._pay_entry_dto_list

    @pay_entry_dto_list.setter
    def pay_entry_dto_list(self, value):
        if isinstance(value, list):
            self._pay_entry_dto_list = list()
            for i in value:
                if isinstance(i, InsPayEntryDTO):
                    self._pay_entry_dto_list.append(i)
                else:
                    self._pay_entry_dto_list.append(InsPayEntryDTO.from_alipay_dict(i))
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def product_plan_id(self):
        return self._product_plan_id

    @product_plan_id.setter
    def product_plan_id(self, value):
        self._product_plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.overdue_no:
            if hasattr(self.overdue_no, 'to_alipay_dict'):
                params['overdue_no'] = self.overdue_no.to_alipay_dict()
            else:
                params['overdue_no'] = self.overdue_no
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.pay_entry_dto:
            if hasattr(self.pay_entry_dto, 'to_alipay_dict'):
                params['pay_entry_dto'] = self.pay_entry_dto.to_alipay_dict()
            else:
                params['pay_entry_dto'] = self.pay_entry_dto
        if self.pay_entry_dto_list:
            if isinstance(self.pay_entry_dto_list, list):
                for i in range(0, len(self.pay_entry_dto_list)):
                    element = self.pay_entry_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pay_entry_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.pay_entry_dto_list, 'to_alipay_dict'):
                params['pay_entry_dto_list'] = self.pay_entry_dto_list.to_alipay_dict()
            else:
                params['pay_entry_dto_list'] = self.pay_entry_dto_list
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.product_plan_id:
            if hasattr(self.product_plan_id, 'to_alipay_dict'):
                params['product_plan_id'] = self.product_plan_id.to_alipay_dict()
            else:
                params['product_plan_id'] = self.product_plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneClaimOverdueCloseModel()
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'overdue_no' in d:
            o.overdue_no = d['overdue_no']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'pay_entry_dto' in d:
            o.pay_entry_dto = d['pay_entry_dto']
        if 'pay_entry_dto_list' in d:
            o.pay_entry_dto_list = d['pay_entry_dto_list']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'product_plan_id' in d:
            o.product_plan_id = d['product_plan_id']
        return o


