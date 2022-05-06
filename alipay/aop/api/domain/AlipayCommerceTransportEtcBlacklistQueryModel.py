#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcBlacklistQueryModel(object):

    def __init__(self):
        self._biz_agreement_no = None

    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_agreement_no:
            if hasattr(self.biz_agreement_no, 'to_alipay_dict'):
                params['biz_agreement_no'] = self.biz_agreement_no.to_alipay_dict()
            else:
                params['biz_agreement_no'] = self.biz_agreement_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcBlacklistQueryModel()
        if 'biz_agreement_no' in d:
            o.biz_agreement_no = d['biz_agreement_no']
        return o


