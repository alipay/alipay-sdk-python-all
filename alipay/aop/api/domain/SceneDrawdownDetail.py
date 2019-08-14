#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneDrawdownDetail(object):

    def __init__(self):
        self._drawdown_no = None
        self._fin_drawdown_no = None

    @property
    def drawdown_no(self):
        return self._drawdown_no

    @drawdown_no.setter
    def drawdown_no(self, value):
        self._drawdown_no = value
    @property
    def fin_drawdown_no(self):
        return self._fin_drawdown_no

    @fin_drawdown_no.setter
    def fin_drawdown_no(self, value):
        self._fin_drawdown_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.drawdown_no:
            if hasattr(self.drawdown_no, 'to_alipay_dict'):
                params['drawdown_no'] = self.drawdown_no.to_alipay_dict()
            else:
                params['drawdown_no'] = self.drawdown_no
        if self.fin_drawdown_no:
            if hasattr(self.fin_drawdown_no, 'to_alipay_dict'):
                params['fin_drawdown_no'] = self.fin_drawdown_no.to_alipay_dict()
            else:
                params['fin_drawdown_no'] = self.fin_drawdown_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneDrawdownDetail()
        if 'drawdown_no' in d:
            o.drawdown_no = d['drawdown_no']
        if 'fin_drawdown_no' in d:
            o.fin_drawdown_no = d['fin_drawdown_no']
        return o


