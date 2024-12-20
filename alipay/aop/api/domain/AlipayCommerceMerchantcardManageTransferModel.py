#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardManageTransferModel(object):

    def __init__(self):
        self._card_template_ids = None

    @property
    def card_template_ids(self):
        return self._card_template_ids

    @card_template_ids.setter
    def card_template_ids(self, value):
        if isinstance(value, list):
            self._card_template_ids = list()
            for i in value:
                self._card_template_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.card_template_ids:
            if isinstance(self.card_template_ids, list):
                for i in range(0, len(self.card_template_ids)):
                    element = self.card_template_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_template_ids[i] = element.to_alipay_dict()
            if hasattr(self.card_template_ids, 'to_alipay_dict'):
                params['card_template_ids'] = self.card_template_ids.to_alipay_dict()
            else:
                params['card_template_ids'] = self.card_template_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardManageTransferModel()
        if 'card_template_ids' in d:
            o.card_template_ids = d['card_template_ids']
        return o


