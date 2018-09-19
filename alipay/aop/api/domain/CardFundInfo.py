#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardFundInfo(object):

    def __init__(self):
        self._fundaccount = None
        self._fundtype = None

    @property
    def fundaccount(self):
        return self._fundaccount

    @fundaccount.setter
    def fundaccount(self, value):
        self._fundaccount = value
    @property
    def fundtype(self):
        return self._fundtype

    @fundtype.setter
    def fundtype(self, value):
        self._fundtype = value


    def to_alipay_dict(self):
        params = dict()
        if self.fundaccount:
            if hasattr(self.fundaccount, 'to_alipay_dict'):
                params['fundaccount'] = self.fundaccount.to_alipay_dict()
            else:
                params['fundaccount'] = self.fundaccount
        if self.fundtype:
            if hasattr(self.fundtype, 'to_alipay_dict'):
                params['fundtype'] = self.fundtype.to_alipay_dict()
            else:
                params['fundtype'] = self.fundtype
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardFundInfo()
        if 'fundaccount' in d:
            o.fundaccount = d['fundaccount']
        if 'fundtype' in d:
            o.fundtype = d['fundtype']
        return o


