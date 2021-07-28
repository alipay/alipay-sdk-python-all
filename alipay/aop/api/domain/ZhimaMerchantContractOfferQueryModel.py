#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantContractOfferQueryModel(object):

    def __init__(self):
        self._offer_no = None

    @property
    def offer_no(self):
        return self._offer_no

    @offer_no.setter
    def offer_no(self, value):
        self._offer_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.offer_no:
            if hasattr(self.offer_no, 'to_alipay_dict'):
                params['offer_no'] = self.offer_no.to_alipay_dict()
            else:
                params['offer_no'] = self.offer_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantContractOfferQueryModel()
        if 'offer_no' in d:
            o.offer_no = d['offer_no']
        return o


