#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApiContractItem import ApiContractItem
from alipay.aop.api.domain.ApiContractItem import ApiContractItem
from alipay.aop.api.domain.ApiContractParticipant import ApiContractParticipant


class ApiContractDetail(object):

    def __init__(self):
        self._cancel_date = None
        self._complete_date = None
        self._contract_items = None
        self._contract_no = None
        self._contract_status = None
        self._contract_sub_status = None
        self._effect_date = None
        self._invalid_date = None
        self._items = None
        self._join_history_people = None
        self._offer_no = None
        self._offer_principal_id = None
        self._participants = None
        self._template_no = None

    @property
    def cancel_date(self):
        return self._cancel_date

    @cancel_date.setter
    def cancel_date(self, value):
        self._cancel_date = value
    @property
    def complete_date(self):
        return self._complete_date

    @complete_date.setter
    def complete_date(self, value):
        self._complete_date = value
    @property
    def contract_items(self):
        return self._contract_items

    @contract_items.setter
    def contract_items(self, value):
        if isinstance(value, list):
            self._contract_items = list()
            for i in value:
                if isinstance(i, ApiContractItem):
                    self._contract_items.append(i)
                else:
                    self._contract_items.append(ApiContractItem.from_alipay_dict(i))
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def contract_status(self):
        return self._contract_status

    @contract_status.setter
    def contract_status(self, value):
        self._contract_status = value
    @property
    def contract_sub_status(self):
        return self._contract_sub_status

    @contract_sub_status.setter
    def contract_sub_status(self, value):
        self._contract_sub_status = value
    @property
    def effect_date(self):
        return self._effect_date

    @effect_date.setter
    def effect_date(self, value):
        self._effect_date = value
    @property
    def invalid_date(self):
        return self._invalid_date

    @invalid_date.setter
    def invalid_date(self, value):
        self._invalid_date = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, ApiContractItem):
            self._items = value
        else:
            self._items = ApiContractItem.from_alipay_dict(value)
    @property
    def join_history_people(self):
        return self._join_history_people

    @join_history_people.setter
    def join_history_people(self, value):
        self._join_history_people = value
    @property
    def offer_no(self):
        return self._offer_no

    @offer_no.setter
    def offer_no(self, value):
        self._offer_no = value
    @property
    def offer_principal_id(self):
        return self._offer_principal_id

    @offer_principal_id.setter
    def offer_principal_id(self, value):
        self._offer_principal_id = value
    @property
    def participants(self):
        return self._participants

    @participants.setter
    def participants(self, value):
        if isinstance(value, list):
            self._participants = list()
            for i in value:
                if isinstance(i, ApiContractParticipant):
                    self._participants.append(i)
                else:
                    self._participants.append(ApiContractParticipant.from_alipay_dict(i))
    @property
    def template_no(self):
        return self._template_no

    @template_no.setter
    def template_no(self, value):
        self._template_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_date:
            if hasattr(self.cancel_date, 'to_alipay_dict'):
                params['cancel_date'] = self.cancel_date.to_alipay_dict()
            else:
                params['cancel_date'] = self.cancel_date
        if self.complete_date:
            if hasattr(self.complete_date, 'to_alipay_dict'):
                params['complete_date'] = self.complete_date.to_alipay_dict()
            else:
                params['complete_date'] = self.complete_date
        if self.contract_items:
            if isinstance(self.contract_items, list):
                for i in range(0, len(self.contract_items)):
                    element = self.contract_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_items[i] = element.to_alipay_dict()
            if hasattr(self.contract_items, 'to_alipay_dict'):
                params['contract_items'] = self.contract_items.to_alipay_dict()
            else:
                params['contract_items'] = self.contract_items
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.contract_status:
            if hasattr(self.contract_status, 'to_alipay_dict'):
                params['contract_status'] = self.contract_status.to_alipay_dict()
            else:
                params['contract_status'] = self.contract_status
        if self.contract_sub_status:
            if hasattr(self.contract_sub_status, 'to_alipay_dict'):
                params['contract_sub_status'] = self.contract_sub_status.to_alipay_dict()
            else:
                params['contract_sub_status'] = self.contract_sub_status
        if self.effect_date:
            if hasattr(self.effect_date, 'to_alipay_dict'):
                params['effect_date'] = self.effect_date.to_alipay_dict()
            else:
                params['effect_date'] = self.effect_date
        if self.invalid_date:
            if hasattr(self.invalid_date, 'to_alipay_dict'):
                params['invalid_date'] = self.invalid_date.to_alipay_dict()
            else:
                params['invalid_date'] = self.invalid_date
        if self.items:
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        if self.join_history_people:
            if hasattr(self.join_history_people, 'to_alipay_dict'):
                params['join_history_people'] = self.join_history_people.to_alipay_dict()
            else:
                params['join_history_people'] = self.join_history_people
        if self.offer_no:
            if hasattr(self.offer_no, 'to_alipay_dict'):
                params['offer_no'] = self.offer_no.to_alipay_dict()
            else:
                params['offer_no'] = self.offer_no
        if self.offer_principal_id:
            if hasattr(self.offer_principal_id, 'to_alipay_dict'):
                params['offer_principal_id'] = self.offer_principal_id.to_alipay_dict()
            else:
                params['offer_principal_id'] = self.offer_principal_id
        if self.participants:
            if isinstance(self.participants, list):
                for i in range(0, len(self.participants)):
                    element = self.participants[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.participants[i] = element.to_alipay_dict()
            if hasattr(self.participants, 'to_alipay_dict'):
                params['participants'] = self.participants.to_alipay_dict()
            else:
                params['participants'] = self.participants
        if self.template_no:
            if hasattr(self.template_no, 'to_alipay_dict'):
                params['template_no'] = self.template_no.to_alipay_dict()
            else:
                params['template_no'] = self.template_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApiContractDetail()
        if 'cancel_date' in d:
            o.cancel_date = d['cancel_date']
        if 'complete_date' in d:
            o.complete_date = d['complete_date']
        if 'contract_items' in d:
            o.contract_items = d['contract_items']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'contract_status' in d:
            o.contract_status = d['contract_status']
        if 'contract_sub_status' in d:
            o.contract_sub_status = d['contract_sub_status']
        if 'effect_date' in d:
            o.effect_date = d['effect_date']
        if 'invalid_date' in d:
            o.invalid_date = d['invalid_date']
        if 'items' in d:
            o.items = d['items']
        if 'join_history_people' in d:
            o.join_history_people = d['join_history_people']
        if 'offer_no' in d:
            o.offer_no = d['offer_no']
        if 'offer_principal_id' in d:
            o.offer_principal_id = d['offer_principal_id']
        if 'participants' in d:
            o.participants = d['participants']
        if 'template_no' in d:
            o.template_no = d['template_no']
        return o


