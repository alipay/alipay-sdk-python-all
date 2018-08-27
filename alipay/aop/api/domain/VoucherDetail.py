#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContributeDetail import ContributeDetail


class VoucherDetail(object):

    def __init__(self):
        self._amount = None
        self._id = None
        self._memo = None
        self._merchant_contribute = None
        self._name = None
        self._other_contribute = None
        self._other_contribute_detail = None
        self._purchase_ant_contribute = None
        self._purchase_buyer_contribute = None
        self._purchase_merchant_contribute = None
        self._template_id = None
        self._type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_contribute(self):
        return self._merchant_contribute

    @merchant_contribute.setter
    def merchant_contribute(self, value):
        self._merchant_contribute = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def other_contribute(self):
        return self._other_contribute

    @other_contribute.setter
    def other_contribute(self, value):
        self._other_contribute = value
    @property
    def other_contribute_detail(self):
        return self._other_contribute_detail

    @other_contribute_detail.setter
    def other_contribute_detail(self, value):
        if isinstance(value, list):
            self._other_contribute_detail = list()
            for i in value:
                if isinstance(i, ContributeDetail):
                    self._other_contribute_detail.append(i)
                else:
                    self._other_contribute_detail.append(ContributeDetail.from_alipay_dict(i))
    @property
    def purchase_ant_contribute(self):
        return self._purchase_ant_contribute

    @purchase_ant_contribute.setter
    def purchase_ant_contribute(self, value):
        self._purchase_ant_contribute = value
    @property
    def purchase_buyer_contribute(self):
        return self._purchase_buyer_contribute

    @purchase_buyer_contribute.setter
    def purchase_buyer_contribute(self, value):
        self._purchase_buyer_contribute = value
    @property
    def purchase_merchant_contribute(self):
        return self._purchase_merchant_contribute

    @purchase_merchant_contribute.setter
    def purchase_merchant_contribute(self, value):
        self._purchase_merchant_contribute = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.merchant_contribute:
            if hasattr(self.merchant_contribute, 'to_alipay_dict'):
                params['merchant_contribute'] = self.merchant_contribute.to_alipay_dict()
            else:
                params['merchant_contribute'] = self.merchant_contribute
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.other_contribute:
            if hasattr(self.other_contribute, 'to_alipay_dict'):
                params['other_contribute'] = self.other_contribute.to_alipay_dict()
            else:
                params['other_contribute'] = self.other_contribute
        if self.other_contribute_detail:
            if isinstance(self.other_contribute_detail, list):
                for i in range(0, len(self.other_contribute_detail)):
                    element = self.other_contribute_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_contribute_detail[i] = element.to_alipay_dict()
            if hasattr(self.other_contribute_detail, 'to_alipay_dict'):
                params['other_contribute_detail'] = self.other_contribute_detail.to_alipay_dict()
            else:
                params['other_contribute_detail'] = self.other_contribute_detail
        if self.purchase_ant_contribute:
            if hasattr(self.purchase_ant_contribute, 'to_alipay_dict'):
                params['purchase_ant_contribute'] = self.purchase_ant_contribute.to_alipay_dict()
            else:
                params['purchase_ant_contribute'] = self.purchase_ant_contribute
        if self.purchase_buyer_contribute:
            if hasattr(self.purchase_buyer_contribute, 'to_alipay_dict'):
                params['purchase_buyer_contribute'] = self.purchase_buyer_contribute.to_alipay_dict()
            else:
                params['purchase_buyer_contribute'] = self.purchase_buyer_contribute
        if self.purchase_merchant_contribute:
            if hasattr(self.purchase_merchant_contribute, 'to_alipay_dict'):
                params['purchase_merchant_contribute'] = self.purchase_merchant_contribute.to_alipay_dict()
            else:
                params['purchase_merchant_contribute'] = self.purchase_merchant_contribute
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'id' in d:
            o.id = d['id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'merchant_contribute' in d:
            o.merchant_contribute = d['merchant_contribute']
        if 'name' in d:
            o.name = d['name']
        if 'other_contribute' in d:
            o.other_contribute = d['other_contribute']
        if 'other_contribute_detail' in d:
            o.other_contribute_detail = d['other_contribute_detail']
        if 'purchase_ant_contribute' in d:
            o.purchase_ant_contribute = d['purchase_ant_contribute']
        if 'purchase_buyer_contribute' in d:
            o.purchase_buyer_contribute = d['purchase_buyer_contribute']
        if 'purchase_merchant_contribute' in d:
            o.purchase_merchant_contribute = d['purchase_merchant_contribute']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'type' in d:
            o.type = d['type']
        return o


