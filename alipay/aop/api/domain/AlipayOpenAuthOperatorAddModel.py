#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperatorAddVO import OperatorAddVO


class AlipayOpenAuthOperatorAddModel(object):

    def __init__(self):
        self._operator_add_vo = None

    @property
    def operator_add_vo(self):
        return self._operator_add_vo

    @operator_add_vo.setter
    def operator_add_vo(self, value):
        if isinstance(value, OperatorAddVO):
            self._operator_add_vo = value
        else:
            self._operator_add_vo = OperatorAddVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.operator_add_vo:
            if hasattr(self.operator_add_vo, 'to_alipay_dict'):
                params['operator_add_vo'] = self.operator_add_vo.to_alipay_dict()
            else:
                params['operator_add_vo'] = self.operator_add_vo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAuthOperatorAddModel()
        if 'operator_add_vo' in d:
            o.operator_add_vo = d['operator_add_vo']
        return o


