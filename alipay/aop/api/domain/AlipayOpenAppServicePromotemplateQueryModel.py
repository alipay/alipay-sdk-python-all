#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppServicePromotemplateQueryModel(object):

    def __init__(self):
        self._promo_booth_id = None
        self._promo_booth_version = None

    @property
    def promo_booth_id(self):
        return self._promo_booth_id

    @promo_booth_id.setter
    def promo_booth_id(self, value):
        self._promo_booth_id = value
    @property
    def promo_booth_version(self):
        return self._promo_booth_version

    @promo_booth_version.setter
    def promo_booth_version(self, value):
        self._promo_booth_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.promo_booth_id:
            if hasattr(self.promo_booth_id, 'to_alipay_dict'):
                params['promo_booth_id'] = self.promo_booth_id.to_alipay_dict()
            else:
                params['promo_booth_id'] = self.promo_booth_id
        if self.promo_booth_version:
            if hasattr(self.promo_booth_version, 'to_alipay_dict'):
                params['promo_booth_version'] = self.promo_booth_version.to_alipay_dict()
            else:
                params['promo_booth_version'] = self.promo_booth_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppServicePromotemplateQueryModel()
        if 'promo_booth_id' in d:
            o.promo_booth_id = d['promo_booth_id']
        if 'promo_booth_version' in d:
            o.promo_booth_version = d['promo_booth_version']
        return o


