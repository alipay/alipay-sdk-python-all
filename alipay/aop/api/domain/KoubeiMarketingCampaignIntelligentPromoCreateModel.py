#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoOperatorInfo import PromoOperatorInfo
from alipay.aop.api.domain.IntelligentPromo import IntelligentPromo


class KoubeiMarketingCampaignIntelligentPromoCreateModel(object):

    def __init__(self):
        self._operator_context = None
        self._out_request_no = None
        self._promo = None

    @property
    def operator_context(self):
        return self._operator_context

    @operator_context.setter
    def operator_context(self, value):
        if isinstance(value, PromoOperatorInfo):
            self._operator_context = value
        else:
            self._operator_context = PromoOperatorInfo.from_alipay_dict(value)
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def promo(self):
        return self._promo

    @promo.setter
    def promo(self, value):
        if isinstance(value, IntelligentPromo):
            self._promo = value
        else:
            self._promo = IntelligentPromo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.operator_context:
            if hasattr(self.operator_context, 'to_alipay_dict'):
                params['operator_context'] = self.operator_context.to_alipay_dict()
            else:
                params['operator_context'] = self.operator_context
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.promo:
            if hasattr(self.promo, 'to_alipay_dict'):
                params['promo'] = self.promo.to_alipay_dict()
            else:
                params['promo'] = self.promo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignIntelligentPromoCreateModel()
        if 'operator_context' in d:
            o.operator_context = d['operator_context']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'promo' in d:
            o.promo = d['promo']
        return o


