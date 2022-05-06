#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WithdrawPrincipalDTO(object):

    def __init__(self):
        self._external_entity_id = None
        self._partner_card_no = None
        self._principal_id = None
        self._principal_type = None

    @property
    def external_entity_id(self):
        return self._external_entity_id

    @external_entity_id.setter
    def external_entity_id(self, value):
        self._external_entity_id = value
    @property
    def partner_card_no(self):
        return self._partner_card_no

    @partner_card_no.setter
    def partner_card_no(self, value):
        self._partner_card_no = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_type(self):
        return self._principal_type

    @principal_type.setter
    def principal_type(self, value):
        self._principal_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_entity_id:
            if hasattr(self.external_entity_id, 'to_alipay_dict'):
                params['external_entity_id'] = self.external_entity_id.to_alipay_dict()
            else:
                params['external_entity_id'] = self.external_entity_id
        if self.partner_card_no:
            if hasattr(self.partner_card_no, 'to_alipay_dict'):
                params['partner_card_no'] = self.partner_card_no.to_alipay_dict()
            else:
                params['partner_card_no'] = self.partner_card_no
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_type:
            if hasattr(self.principal_type, 'to_alipay_dict'):
                params['principal_type'] = self.principal_type.to_alipay_dict()
            else:
                params['principal_type'] = self.principal_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WithdrawPrincipalDTO()
        if 'external_entity_id' in d:
            o.external_entity_id = d['external_entity_id']
        if 'partner_card_no' in d:
            o.partner_card_no = d['partner_card_no']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_type' in d:
            o.principal_type = d['principal_type']
        return o


