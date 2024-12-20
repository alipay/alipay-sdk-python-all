#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpBusinessCompetitionInfo(object):

    def __init__(self):
        self._clue_source = None
        self._clue_total = None
        self._manager_state = None
        self._name = None
        self._register_capital = None
        self._register_date = None
        self._relation = None
        self._tyshxydm = None

    @property
    def clue_source(self):
        return self._clue_source

    @clue_source.setter
    def clue_source(self, value):
        self._clue_source = value
    @property
    def clue_total(self):
        return self._clue_total

    @clue_total.setter
    def clue_total(self, value):
        self._clue_total = value
    @property
    def manager_state(self):
        return self._manager_state

    @manager_state.setter
    def manager_state(self, value):
        self._manager_state = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def register_capital(self):
        return self._register_capital

    @register_capital.setter
    def register_capital(self, value):
        self._register_capital = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def relation(self):
        return self._relation

    @relation.setter
    def relation(self, value):
        self._relation = value
    @property
    def tyshxydm(self):
        return self._tyshxydm

    @tyshxydm.setter
    def tyshxydm(self, value):
        self._tyshxydm = value


    def to_alipay_dict(self):
        params = dict()
        if self.clue_source:
            if hasattr(self.clue_source, 'to_alipay_dict'):
                params['clue_source'] = self.clue_source.to_alipay_dict()
            else:
                params['clue_source'] = self.clue_source
        if self.clue_total:
            if hasattr(self.clue_total, 'to_alipay_dict'):
                params['clue_total'] = self.clue_total.to_alipay_dict()
            else:
                params['clue_total'] = self.clue_total
        if self.manager_state:
            if hasattr(self.manager_state, 'to_alipay_dict'):
                params['manager_state'] = self.manager_state.to_alipay_dict()
            else:
                params['manager_state'] = self.manager_state
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.register_capital:
            if hasattr(self.register_capital, 'to_alipay_dict'):
                params['register_capital'] = self.register_capital.to_alipay_dict()
            else:
                params['register_capital'] = self.register_capital
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.relation:
            if hasattr(self.relation, 'to_alipay_dict'):
                params['relation'] = self.relation.to_alipay_dict()
            else:
                params['relation'] = self.relation
        if self.tyshxydm:
            if hasattr(self.tyshxydm, 'to_alipay_dict'):
                params['tyshxydm'] = self.tyshxydm.to_alipay_dict()
            else:
                params['tyshxydm'] = self.tyshxydm
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpBusinessCompetitionInfo()
        if 'clue_source' in d:
            o.clue_source = d['clue_source']
        if 'clue_total' in d:
            o.clue_total = d['clue_total']
        if 'manager_state' in d:
            o.manager_state = d['manager_state']
        if 'name' in d:
            o.name = d['name']
        if 'register_capital' in d:
            o.register_capital = d['register_capital']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'relation' in d:
            o.relation = d['relation']
        if 'tyshxydm' in d:
            o.tyshxydm = d['tyshxydm']
        return o


