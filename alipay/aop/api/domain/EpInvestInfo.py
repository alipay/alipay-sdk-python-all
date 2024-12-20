#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpInvestInfo(object):

    def __init__(self):
        self._approval_date = None
        self._holding_rate = None
        self._inv_amount = None
        self._legal_representative = None
        self._name = None
        self._old_name = None
        self._registe_organ = None
        self._registr_id = None
        self._registration_state = None
        self._tyshxydm = None

    @property
    def approval_date(self):
        return self._approval_date

    @approval_date.setter
    def approval_date(self, value):
        self._approval_date = value
    @property
    def holding_rate(self):
        return self._holding_rate

    @holding_rate.setter
    def holding_rate(self, value):
        self._holding_rate = value
    @property
    def inv_amount(self):
        return self._inv_amount

    @inv_amount.setter
    def inv_amount(self, value):
        self._inv_amount = value
    @property
    def legal_representative(self):
        return self._legal_representative

    @legal_representative.setter
    def legal_representative(self, value):
        self._legal_representative = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def old_name(self):
        return self._old_name

    @old_name.setter
    def old_name(self, value):
        if isinstance(value, list):
            self._old_name = list()
            for i in value:
                self._old_name.append(i)
    @property
    def registe_organ(self):
        return self._registe_organ

    @registe_organ.setter
    def registe_organ(self, value):
        self._registe_organ = value
    @property
    def registr_id(self):
        return self._registr_id

    @registr_id.setter
    def registr_id(self, value):
        self._registr_id = value
    @property
    def registration_state(self):
        return self._registration_state

    @registration_state.setter
    def registration_state(self, value):
        self._registration_state = value
    @property
    def tyshxydm(self):
        return self._tyshxydm

    @tyshxydm.setter
    def tyshxydm(self, value):
        self._tyshxydm = value


    def to_alipay_dict(self):
        params = dict()
        if self.approval_date:
            if hasattr(self.approval_date, 'to_alipay_dict'):
                params['approval_date'] = self.approval_date.to_alipay_dict()
            else:
                params['approval_date'] = self.approval_date
        if self.holding_rate:
            if hasattr(self.holding_rate, 'to_alipay_dict'):
                params['holding_rate'] = self.holding_rate.to_alipay_dict()
            else:
                params['holding_rate'] = self.holding_rate
        if self.inv_amount:
            if hasattr(self.inv_amount, 'to_alipay_dict'):
                params['inv_amount'] = self.inv_amount.to_alipay_dict()
            else:
                params['inv_amount'] = self.inv_amount
        if self.legal_representative:
            if hasattr(self.legal_representative, 'to_alipay_dict'):
                params['legal_representative'] = self.legal_representative.to_alipay_dict()
            else:
                params['legal_representative'] = self.legal_representative
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.old_name:
            if isinstance(self.old_name, list):
                for i in range(0, len(self.old_name)):
                    element = self.old_name[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.old_name[i] = element.to_alipay_dict()
            if hasattr(self.old_name, 'to_alipay_dict'):
                params['old_name'] = self.old_name.to_alipay_dict()
            else:
                params['old_name'] = self.old_name
        if self.registe_organ:
            if hasattr(self.registe_organ, 'to_alipay_dict'):
                params['registe_organ'] = self.registe_organ.to_alipay_dict()
            else:
                params['registe_organ'] = self.registe_organ
        if self.registr_id:
            if hasattr(self.registr_id, 'to_alipay_dict'):
                params['registr_id'] = self.registr_id.to_alipay_dict()
            else:
                params['registr_id'] = self.registr_id
        if self.registration_state:
            if hasattr(self.registration_state, 'to_alipay_dict'):
                params['registration_state'] = self.registration_state.to_alipay_dict()
            else:
                params['registration_state'] = self.registration_state
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
        o = EpInvestInfo()
        if 'approval_date' in d:
            o.approval_date = d['approval_date']
        if 'holding_rate' in d:
            o.holding_rate = d['holding_rate']
        if 'inv_amount' in d:
            o.inv_amount = d['inv_amount']
        if 'legal_representative' in d:
            o.legal_representative = d['legal_representative']
        if 'name' in d:
            o.name = d['name']
        if 'old_name' in d:
            o.old_name = d['old_name']
        if 'registe_organ' in d:
            o.registe_organ = d['registe_organ']
        if 'registr_id' in d:
            o.registr_id = d['registr_id']
        if 'registration_state' in d:
            o.registration_state = d['registration_state']
        if 'tyshxydm' in d:
            o.tyshxydm = d['tyshxydm']
        return o


