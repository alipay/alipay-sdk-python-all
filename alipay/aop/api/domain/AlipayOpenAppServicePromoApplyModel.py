#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoContentBizVO import PromoContentBizVO


class AlipayOpenAppServicePromoApplyModel(object):

    def __init__(self):
        self._promo_booth_id = None
        self._promo_contents = None
        self._promo_entity_codes = None
        self._promo_entity_type = None

    @property
    def promo_booth_id(self):
        return self._promo_booth_id

    @promo_booth_id.setter
    def promo_booth_id(self, value):
        self._promo_booth_id = value
    @property
    def promo_contents(self):
        return self._promo_contents

    @promo_contents.setter
    def promo_contents(self, value):
        if isinstance(value, list):
            self._promo_contents = list()
            for i in value:
                if isinstance(i, PromoContentBizVO):
                    self._promo_contents.append(i)
                else:
                    self._promo_contents.append(PromoContentBizVO.from_alipay_dict(i))
    @property
    def promo_entity_codes(self):
        return self._promo_entity_codes

    @promo_entity_codes.setter
    def promo_entity_codes(self, value):
        self._promo_entity_codes = value
    @property
    def promo_entity_type(self):
        return self._promo_entity_type

    @promo_entity_type.setter
    def promo_entity_type(self, value):
        self._promo_entity_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.promo_booth_id:
            if hasattr(self.promo_booth_id, 'to_alipay_dict'):
                params['promo_booth_id'] = self.promo_booth_id.to_alipay_dict()
            else:
                params['promo_booth_id'] = self.promo_booth_id
        if self.promo_contents:
            if isinstance(self.promo_contents, list):
                for i in range(0, len(self.promo_contents)):
                    element = self.promo_contents[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_contents[i] = element.to_alipay_dict()
            if hasattr(self.promo_contents, 'to_alipay_dict'):
                params['promo_contents'] = self.promo_contents.to_alipay_dict()
            else:
                params['promo_contents'] = self.promo_contents
        if self.promo_entity_codes:
            if hasattr(self.promo_entity_codes, 'to_alipay_dict'):
                params['promo_entity_codes'] = self.promo_entity_codes.to_alipay_dict()
            else:
                params['promo_entity_codes'] = self.promo_entity_codes
        if self.promo_entity_type:
            if hasattr(self.promo_entity_type, 'to_alipay_dict'):
                params['promo_entity_type'] = self.promo_entity_type.to_alipay_dict()
            else:
                params['promo_entity_type'] = self.promo_entity_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppServicePromoApplyModel()
        if 'promo_booth_id' in d:
            o.promo_booth_id = d['promo_booth_id']
        if 'promo_contents' in d:
            o.promo_contents = d['promo_contents']
        if 'promo_entity_codes' in d:
            o.promo_entity_codes = d['promo_entity_codes']
        if 'promo_entity_type' in d:
            o.promo_entity_type = d['promo_entity_type']
        return o


