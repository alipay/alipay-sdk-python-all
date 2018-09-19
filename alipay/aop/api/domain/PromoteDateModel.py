#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoteDataModel import PromoteDataModel


class PromoteDateModel(object):

    def __init__(self):
        self._date = None
        self._promote_data = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def promote_data(self):
        return self._promote_data

    @promote_data.setter
    def promote_data(self, value):
        if isinstance(value, PromoteDataModel):
            self._promote_data = value
        else:
            self._promote_data = PromoteDataModel.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.promote_data:
            if hasattr(self.promote_data, 'to_alipay_dict'):
                params['promote_data'] = self.promote_data.to_alipay_dict()
            else:
                params['promote_data'] = self.promote_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoteDateModel()
        if 'date' in d:
            o.date = d['date']
        if 'promote_data' in d:
            o.promote_data = d['promote_data']
        return o


