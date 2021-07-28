#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationSsffDeeQueryModel(object):

    def __init__(self):
        self._df = None

    @property
    def df(self):
        return self._df

    @df.setter
    def df(self, value):
        self._df = value


    def to_alipay_dict(self):
        params = dict()
        if self.df:
            if hasattr(self.df, 'to_alipay_dict'):
                params['df'] = self.df.to_alipay_dict()
            else:
                params['df'] = self.df
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationSsffDeeQueryModel()
        if 'df' in d:
            o.df = d['df']
        return o


