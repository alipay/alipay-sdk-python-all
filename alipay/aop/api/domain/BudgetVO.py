#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BudgetVO(object):

    def __init__(self):
        self._need_repay_total = None
        self._nom_int = None
        self._nom_prin = None
        self._ovd_int = None
        self._ovd_int_pen_int = None
        self._ovd_prin = None
        self._ovd_prin_pen_int = None

    @property
    def need_repay_total(self):
        return self._need_repay_total

    @need_repay_total.setter
    def need_repay_total(self, value):
        self._need_repay_total = value
    @property
    def nom_int(self):
        return self._nom_int

    @nom_int.setter
    def nom_int(self, value):
        self._nom_int = value
    @property
    def nom_prin(self):
        return self._nom_prin

    @nom_prin.setter
    def nom_prin(self, value):
        self._nom_prin = value
    @property
    def ovd_int(self):
        return self._ovd_int

    @ovd_int.setter
    def ovd_int(self, value):
        self._ovd_int = value
    @property
    def ovd_int_pen_int(self):
        return self._ovd_int_pen_int

    @ovd_int_pen_int.setter
    def ovd_int_pen_int(self, value):
        self._ovd_int_pen_int = value
    @property
    def ovd_prin(self):
        return self._ovd_prin

    @ovd_prin.setter
    def ovd_prin(self, value):
        self._ovd_prin = value
    @property
    def ovd_prin_pen_int(self):
        return self._ovd_prin_pen_int

    @ovd_prin_pen_int.setter
    def ovd_prin_pen_int(self, value):
        self._ovd_prin_pen_int = value


    def to_alipay_dict(self):
        params = dict()
        if self.need_repay_total:
            if hasattr(self.need_repay_total, 'to_alipay_dict'):
                params['need_repay_total'] = self.need_repay_total.to_alipay_dict()
            else:
                params['need_repay_total'] = self.need_repay_total
        if self.nom_int:
            if hasattr(self.nom_int, 'to_alipay_dict'):
                params['nom_int'] = self.nom_int.to_alipay_dict()
            else:
                params['nom_int'] = self.nom_int
        if self.nom_prin:
            if hasattr(self.nom_prin, 'to_alipay_dict'):
                params['nom_prin'] = self.nom_prin.to_alipay_dict()
            else:
                params['nom_prin'] = self.nom_prin
        if self.ovd_int:
            if hasattr(self.ovd_int, 'to_alipay_dict'):
                params['ovd_int'] = self.ovd_int.to_alipay_dict()
            else:
                params['ovd_int'] = self.ovd_int
        if self.ovd_int_pen_int:
            if hasattr(self.ovd_int_pen_int, 'to_alipay_dict'):
                params['ovd_int_pen_int'] = self.ovd_int_pen_int.to_alipay_dict()
            else:
                params['ovd_int_pen_int'] = self.ovd_int_pen_int
        if self.ovd_prin:
            if hasattr(self.ovd_prin, 'to_alipay_dict'):
                params['ovd_prin'] = self.ovd_prin.to_alipay_dict()
            else:
                params['ovd_prin'] = self.ovd_prin
        if self.ovd_prin_pen_int:
            if hasattr(self.ovd_prin_pen_int, 'to_alipay_dict'):
                params['ovd_prin_pen_int'] = self.ovd_prin_pen_int.to_alipay_dict()
            else:
                params['ovd_prin_pen_int'] = self.ovd_prin_pen_int
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BudgetVO()
        if 'need_repay_total' in d:
            o.need_repay_total = d['need_repay_total']
        if 'nom_int' in d:
            o.nom_int = d['nom_int']
        if 'nom_prin' in d:
            o.nom_prin = d['nom_prin']
        if 'ovd_int' in d:
            o.ovd_int = d['ovd_int']
        if 'ovd_int_pen_int' in d:
            o.ovd_int_pen_int = d['ovd_int_pen_int']
        if 'ovd_prin' in d:
            o.ovd_prin = d['ovd_prin']
        if 'ovd_prin_pen_int' in d:
            o.ovd_prin_pen_int = d['ovd_prin_pen_int']
        return o


