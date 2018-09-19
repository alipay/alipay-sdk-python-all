#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardFundInfo import CardFundInfo
from alipay.aop.api.domain.CardCreditInfo import CardCreditInfo


class AlipayAssetCardNewtemplateCreateModel(object):

    def __init__(self):
        self._account_model = None
        self._assets_code = None
        self._biz_from = None
        self._card_fund_infos = None
        self._card_model = None
        self._card_name = None
        self._creator = None
        self._credit_info = None
        self._extend_info = None
        self._operator = None
        self._out_biz_no = None
        self._partner_id = None
        self._period_type = None
        self._product_code = None
        self._settle_user_id = None

    @property
    def account_model(self):
        return self._account_model

    @account_model.setter
    def account_model(self, value):
        self._account_model = value
    @property
    def assets_code(self):
        return self._assets_code

    @assets_code.setter
    def assets_code(self, value):
        self._assets_code = value
    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def card_fund_infos(self):
        return self._card_fund_infos

    @card_fund_infos.setter
    def card_fund_infos(self, value):
        if isinstance(value, list):
            self._card_fund_infos = list()
            for i in value:
                if isinstance(i, CardFundInfo):
                    self._card_fund_infos.append(i)
                else:
                    self._card_fund_infos.append(CardFundInfo.from_alipay_dict(i))
    @property
    def card_model(self):
        return self._card_model

    @card_model.setter
    def card_model(self, value):
        self._card_model = value
    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def credit_info(self):
        return self._credit_info

    @credit_info.setter
    def credit_info(self, value):
        if isinstance(value, CardCreditInfo):
            self._credit_info = value
        else:
            self._credit_info = CardCreditInfo.from_alipay_dict(value)
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def settle_user_id(self):
        return self._settle_user_id

    @settle_user_id.setter
    def settle_user_id(self, value):
        self._settle_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_model:
            if hasattr(self.account_model, 'to_alipay_dict'):
                params['account_model'] = self.account_model.to_alipay_dict()
            else:
                params['account_model'] = self.account_model
        if self.assets_code:
            if hasattr(self.assets_code, 'to_alipay_dict'):
                params['assets_code'] = self.assets_code.to_alipay_dict()
            else:
                params['assets_code'] = self.assets_code
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.card_fund_infos:
            if isinstance(self.card_fund_infos, list):
                for i in range(0, len(self.card_fund_infos)):
                    element = self.card_fund_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_fund_infos[i] = element.to_alipay_dict()
            if hasattr(self.card_fund_infos, 'to_alipay_dict'):
                params['card_fund_infos'] = self.card_fund_infos.to_alipay_dict()
            else:
                params['card_fund_infos'] = self.card_fund_infos
        if self.card_model:
            if hasattr(self.card_model, 'to_alipay_dict'):
                params['card_model'] = self.card_model.to_alipay_dict()
            else:
                params['card_model'] = self.card_model
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.credit_info:
            if hasattr(self.credit_info, 'to_alipay_dict'):
                params['credit_info'] = self.credit_info.to_alipay_dict()
            else:
                params['credit_info'] = self.credit_info
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.period_type:
            if hasattr(self.period_type, 'to_alipay_dict'):
                params['period_type'] = self.period_type.to_alipay_dict()
            else:
                params['period_type'] = self.period_type
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.settle_user_id:
            if hasattr(self.settle_user_id, 'to_alipay_dict'):
                params['settle_user_id'] = self.settle_user_id.to_alipay_dict()
            else:
                params['settle_user_id'] = self.settle_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAssetCardNewtemplateCreateModel()
        if 'account_model' in d:
            o.account_model = d['account_model']
        if 'assets_code' in d:
            o.assets_code = d['assets_code']
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'card_fund_infos' in d:
            o.card_fund_infos = d['card_fund_infos']
        if 'card_model' in d:
            o.card_model = d['card_model']
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'creator' in d:
            o.creator = d['creator']
        if 'credit_info' in d:
            o.credit_info = d['credit_info']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'operator' in d:
            o.operator = d['operator']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'period_type' in d:
            o.period_type = d['period_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'settle_user_id' in d:
            o.settle_user_id = d['settle_user_id']
        return o


