#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoContentBizVO import PromoContentBizVO


class AlipayOpenAppServicePromoModifyModel(object):

    def __init__(self):
        self._promo_contents = None
        self._promo_record_id = None

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
    def promo_record_id(self):
        return self._promo_record_id

    @promo_record_id.setter
    def promo_record_id(self, value):
        self._promo_record_id = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayOpenAppServicePromoModifyModel()
        if 'promo_contents' in d:
            o.promo_contents = d['promo_contents']
        if 'promo_record_id' in d:
            o.promo_record_id = d['promo_record_id']
        return o


