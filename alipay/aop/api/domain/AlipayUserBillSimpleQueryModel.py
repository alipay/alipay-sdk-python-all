#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserBillSimpleQueryModel(object):

    def __init__(self):
        self._biz_no = None
        self._owner_card_no = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def owner_card_no(self):
        return self._owner_card_no

    @owner_card_no.setter
    def owner_card_no(self, value):
        self._owner_card_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.owner_card_no:
            if hasattr(self.owner_card_no, 'to_alipay_dict'):
                params['owner_card_no'] = self.owner_card_no.to_alipay_dict()
            else:
                params['owner_card_no'] = self.owner_card_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserBillSimpleQueryModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'owner_card_no' in d:
            o.owner_card_no = d['owner_card_no']
        return o


