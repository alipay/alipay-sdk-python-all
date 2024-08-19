#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CardTemplateSale import CardTemplateSale


class AlipayCommerceMerchantcardTemplatequickModifyModel(object):

    def __init__(self):
        self._card_template_id = None
        self._sale_info = None
        self._saleable_count = None

    @property
    def card_template_id(self):
        return self._card_template_id

    @card_template_id.setter
    def card_template_id(self, value):
        self._card_template_id = value
    @property
    def sale_info(self):
        return self._sale_info

    @sale_info.setter
    def sale_info(self, value):
        if isinstance(value, CardTemplateSale):
            self._sale_info = value
        else:
            self._sale_info = CardTemplateSale.from_alipay_dict(value)
    @property
    def saleable_count(self):
        return self._saleable_count

    @saleable_count.setter
    def saleable_count(self, value):
        self._saleable_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_id:
            if hasattr(self.card_template_id, 'to_alipay_dict'):
                params['card_template_id'] = self.card_template_id.to_alipay_dict()
            else:
                params['card_template_id'] = self.card_template_id
        if self.sale_info:
            if hasattr(self.sale_info, 'to_alipay_dict'):
                params['sale_info'] = self.sale_info.to_alipay_dict()
            else:
                params['sale_info'] = self.sale_info
        if self.saleable_count:
            if hasattr(self.saleable_count, 'to_alipay_dict'):
                params['saleable_count'] = self.saleable_count.to_alipay_dict()
            else:
                params['saleable_count'] = self.saleable_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardTemplatequickModifyModel()
        if 'card_template_id' in d:
            o.card_template_id = d['card_template_id']
        if 'sale_info' in d:
            o.sale_info = d['sale_info']
        if 'saleable_count' in d:
            o.saleable_count = d['saleable_count']
        return o


