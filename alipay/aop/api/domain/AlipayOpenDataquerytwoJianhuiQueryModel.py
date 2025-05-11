#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FDataJianTestOne import FDataJianTestOne


class AlipayOpenDataquerytwoJianhuiQueryModel(object):

    def __init__(self):
        self._fzcsone = None
        self._testone = None

    @property
    def fzcsone(self):
        return self._fzcsone

    @fzcsone.setter
    def fzcsone(self, value):
        if isinstance(value, FDataJianTestOne):
            self._fzcsone = value
        else:
            self._fzcsone = FDataJianTestOne.from_alipay_dict(value)
    @property
    def testone(self):
        return self._testone

    @testone.setter
    def testone(self, value):
        self._testone = value


    def to_alipay_dict(self):
        params = dict()
        if self.fzcsone:
            if hasattr(self.fzcsone, 'to_alipay_dict'):
                params['fzcsone'] = self.fzcsone.to_alipay_dict()
            else:
                params['fzcsone'] = self.fzcsone
        if self.testone:
            if hasattr(self.testone, 'to_alipay_dict'):
                params['testone'] = self.testone.to_alipay_dict()
            else:
                params['testone'] = self.testone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenDataquerytwoJianhuiQueryModel()
        if 'fzcsone' in d:
            o.fzcsone = d['fzcsone']
        if 'testone' in d:
            o.testone = d['testone']
        return o


