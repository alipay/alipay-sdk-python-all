#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgreementParams import AgreementParams
from alipay.aop.api.domain.ExtendParams import ExtendParams
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.IndustryPayParams import IndustryPayParams
from alipay.aop.api.domain.IndustryPromoParam import IndustryPromoParam
from alipay.aop.api.domain.IndustryWithholdPlanDTO import IndustryWithholdPlanDTO


class AlipayCommerceWithholdrepayorderTradePayModel(object):

    def __init__(self):
        self._agreement_params = None
        self._extend_params = None
        self._goods_detail = None
        self._out_trade_no = None
        self._pay_params = None
        self._product_code = None
        self._promo_params = None
        self._query_options = None
        self._repay_plan = None
        self._seller_id = None
        self._subject = None
        self._total_amount = None

    @property
    def agreement_params(self):
        return self._agreement_params

    @agreement_params.setter
    def agreement_params(self, value):
        if isinstance(value, AgreementParams):
            self._agreement_params = value
        else:
            self._agreement_params = AgreementParams.from_alipay_dict(value)
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, ExtendParams):
            self._extend_params = value
        else:
            self._extend_params = ExtendParams.from_alipay_dict(value)
    @property
    def goods_detail(self):
        return self._goods_detail

    @goods_detail.setter
    def goods_detail(self, value):
        if isinstance(value, GoodsDetail):
            self._goods_detail = value
        else:
            self._goods_detail = GoodsDetail.from_alipay_dict(value)
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_params(self):
        return self._pay_params

    @pay_params.setter
    def pay_params(self, value):
        if isinstance(value, IndustryPayParams):
            self._pay_params = value
        else:
            self._pay_params = IndustryPayParams.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def promo_params(self):
        return self._promo_params

    @promo_params.setter
    def promo_params(self, value):
        if isinstance(value, IndustryPromoParam):
            self._promo_params = value
        else:
            self._promo_params = IndustryPromoParam.from_alipay_dict(value)
    @property
    def query_options(self):
        return self._query_options

    @query_options.setter
    def query_options(self, value):
        if isinstance(value, list):
            self._query_options = list()
            for i in value:
                self._query_options.append(i)
    @property
    def repay_plan(self):
        return self._repay_plan

    @repay_plan.setter
    def repay_plan(self, value):
        if isinstance(value, list):
            self._repay_plan = list()
            for i in value:
                if isinstance(i, IndustryWithholdPlanDTO):
                    self._repay_plan.append(i)
                else:
                    self._repay_plan.append(IndustryWithholdPlanDTO.from_alipay_dict(i))
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_params:
            if hasattr(self.agreement_params, 'to_alipay_dict'):
                params['agreement_params'] = self.agreement_params.to_alipay_dict()
            else:
                params['agreement_params'] = self.agreement_params
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.goods_detail:
            if hasattr(self.goods_detail, 'to_alipay_dict'):
                params['goods_detail'] = self.goods_detail.to_alipay_dict()
            else:
                params['goods_detail'] = self.goods_detail
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pay_params:
            if hasattr(self.pay_params, 'to_alipay_dict'):
                params['pay_params'] = self.pay_params.to_alipay_dict()
            else:
                params['pay_params'] = self.pay_params
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.promo_params:
            if hasattr(self.promo_params, 'to_alipay_dict'):
                params['promo_params'] = self.promo_params.to_alipay_dict()
            else:
                params['promo_params'] = self.promo_params
        if self.query_options:
            if isinstance(self.query_options, list):
                for i in range(0, len(self.query_options)):
                    element = self.query_options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.query_options[i] = element.to_alipay_dict()
            if hasattr(self.query_options, 'to_alipay_dict'):
                params['query_options'] = self.query_options.to_alipay_dict()
            else:
                params['query_options'] = self.query_options
        if self.repay_plan:
            if isinstance(self.repay_plan, list):
                for i in range(0, len(self.repay_plan)):
                    element = self.repay_plan[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.repay_plan[i] = element.to_alipay_dict()
            if hasattr(self.repay_plan, 'to_alipay_dict'):
                params['repay_plan'] = self.repay_plan.to_alipay_dict()
            else:
                params['repay_plan'] = self.repay_plan
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceWithholdrepayorderTradePayModel()
        if 'agreement_params' in d:
            o.agreement_params = d['agreement_params']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'goods_detail' in d:
            o.goods_detail = d['goods_detail']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pay_params' in d:
            o.pay_params = d['pay_params']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'promo_params' in d:
            o.promo_params = d['promo_params']
        if 'query_options' in d:
            o.query_options = d['query_options']
        if 'repay_plan' in d:
            o.repay_plan = d['repay_plan']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


