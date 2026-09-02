#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppJobinterviewInterviewQueryModel(object):

    def __init__(self):
        self._candidate_id = None
        self._external_candidate_id = None
        self._id_card = None
        self._room_id = None
        self._tenant_id = None

    @property
    def candidate_id(self):
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, value):
        self._candidate_id = value
    @property
    def external_candidate_id(self):
        return self._external_candidate_id

    @external_candidate_id.setter
    def external_candidate_id(self, value):
        self._external_candidate_id = value
    @property
    def id_card(self):
        return self._id_card

    @id_card.setter
    def id_card(self, value):
        self._id_card = value
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.candidate_id:
            if hasattr(self.candidate_id, 'to_alipay_dict'):
                params['candidate_id'] = self.candidate_id.to_alipay_dict()
            else:
                params['candidate_id'] = self.candidate_id
        if self.external_candidate_id:
            if hasattr(self.external_candidate_id, 'to_alipay_dict'):
                params['external_candidate_id'] = self.external_candidate_id.to_alipay_dict()
            else:
                params['external_candidate_id'] = self.external_candidate_id
        if self.id_card:
            if hasattr(self.id_card, 'to_alipay_dict'):
                params['id_card'] = self.id_card.to_alipay_dict()
            else:
                params['id_card'] = self.id_card
        if self.room_id:
            if hasattr(self.room_id, 'to_alipay_dict'):
                params['room_id'] = self.room_id.to_alipay_dict()
            else:
                params['room_id'] = self.room_id
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppJobinterviewInterviewQueryModel()
        if 'candidate_id' in d:
            o.candidate_id = d['candidate_id']
        if 'external_candidate_id' in d:
            o.external_candidate_id = d['external_candidate_id']
        if 'id_card' in d:
            o.id_card = d['id_card']
        if 'room_id' in d:
            o.room_id = d['room_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


