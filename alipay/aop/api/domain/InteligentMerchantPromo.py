#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InteligentGeneralMerchantPromo import InteligentGeneralMerchantPromo


class InteligentMerchantPromo(object):

    def __init__(self):
        self._general_promo = None
        self._promo_type = None

    @property
    def general_promo(self):
        return self._general_promo

    @general_promo.setter
    def general_promo(self, value):
        if isinstance(value, InteligentGeneralMerchantPromo):
            self._general_promo = value
        else:
            self._general_promo = InteligentGeneralMerchantPromo.from_alipay_dict(value)
    @property
    def promo_type(self):
        return self._promo_type

    @promo_type.setter
    def promo_type(self, value):
        self._promo_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.general_promo:
            if hasattr(self.general_promo, 'to_alipay_dict'):
                params['general_promo'] = self.general_promo.to_alipay_dict()
            else:
                params['general_promo'] = self.general_promo
        if self.promo_type:
            if hasattr(self.promo_type, 'to_alipay_dict'):
                params['promo_type'] = self.promo_type.to_alipay_dict()
            else:
                params['promo_type'] = self.promo_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteligentMerchantPromo()
        if 'general_promo' in d:
            o.general_promo = d['general_promo']
        if 'promo_type' in d:
            o.promo_type = d['promo_type']
        return o


