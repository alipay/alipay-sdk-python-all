#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppServicePromoQueryModel(object):

    def __init__(self):
        self._promo_record_id = None

    @property
    def promo_record_id(self):
        return self._promo_record_id

    @promo_record_id.setter
    def promo_record_id(self, value):
        self._promo_record_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.promo_record_id:
            if hasattr(self.promo_record_id, 'to_alipay_dict'):
                params['promo_record_id'] = self.promo_record_id.to_alipay_dict()
            else:
                params['promo_record_id'] = self.promo_record_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppServicePromoQueryModel()
        if 'promo_record_id' in d:
            o.promo_record_id = d['promo_record_id']
        return o


