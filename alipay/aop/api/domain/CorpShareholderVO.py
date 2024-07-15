#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CorpShareholderTotal import CorpShareholderTotal


class CorpShareholderVO(object):

    def __init__(self):
        self._divestment_date = None
        self._shareholder_date = None
        self._shareholder_name = None
        self._totals = None
        self._transfer_date = None

    @property
    def divestment_date(self):
        return self._divestment_date

    @divestment_date.setter
    def divestment_date(self, value):
        self._divestment_date = value
    @property
    def shareholder_date(self):
        return self._shareholder_date

    @shareholder_date.setter
    def shareholder_date(self, value):
        self._shareholder_date = value
    @property
    def shareholder_name(self):
        return self._shareholder_name

    @shareholder_name.setter
    def shareholder_name(self, value):
        self._shareholder_name = value
    @property
    def totals(self):
        return self._totals

    @totals.setter
    def totals(self, value):
        if isinstance(value, list):
            self._totals = list()
            for i in value:
                if isinstance(i, CorpShareholderTotal):
                    self._totals.append(i)
                else:
                    self._totals.append(CorpShareholderTotal.from_alipay_dict(i))
    @property
    def transfer_date(self):
        return self._transfer_date

    @transfer_date.setter
    def transfer_date(self, value):
        self._transfer_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.divestment_date:
            if hasattr(self.divestment_date, 'to_alipay_dict'):
                params['divestment_date'] = self.divestment_date.to_alipay_dict()
            else:
                params['divestment_date'] = self.divestment_date
        if self.shareholder_date:
            if hasattr(self.shareholder_date, 'to_alipay_dict'):
                params['shareholder_date'] = self.shareholder_date.to_alipay_dict()
            else:
                params['shareholder_date'] = self.shareholder_date
        if self.shareholder_name:
            if hasattr(self.shareholder_name, 'to_alipay_dict'):
                params['shareholder_name'] = self.shareholder_name.to_alipay_dict()
            else:
                params['shareholder_name'] = self.shareholder_name
        if self.totals:
            if isinstance(self.totals, list):
                for i in range(0, len(self.totals)):
                    element = self.totals[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.totals[i] = element.to_alipay_dict()
            if hasattr(self.totals, 'to_alipay_dict'):
                params['totals'] = self.totals.to_alipay_dict()
            else:
                params['totals'] = self.totals
        if self.transfer_date:
            if hasattr(self.transfer_date, 'to_alipay_dict'):
                params['transfer_date'] = self.transfer_date.to_alipay_dict()
            else:
                params['transfer_date'] = self.transfer_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CorpShareholderVO()
        if 'divestment_date' in d:
            o.divestment_date = d['divestment_date']
        if 'shareholder_date' in d:
            o.shareholder_date = d['shareholder_date']
        if 'shareholder_name' in d:
            o.shareholder_name = d['shareholder_name']
        if 'totals' in d:
            o.totals = d['totals']
        if 'transfer_date' in d:
            o.transfer_date = d['transfer_date']
        return o


