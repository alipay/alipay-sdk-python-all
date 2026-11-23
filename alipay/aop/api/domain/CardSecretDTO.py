#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardSecretDTO(object):

    def __init__(self):
        self._virtual_card_no = None
        self._virtual_card_password = None

    @property
    def virtual_card_no(self):
        return self._virtual_card_no

    @virtual_card_no.setter
    def virtual_card_no(self, value):
        self._virtual_card_no = value
    @property
    def virtual_card_password(self):
        return self._virtual_card_password

    @virtual_card_password.setter
    def virtual_card_password(self, value):
        self._virtual_card_password = value


    def to_alipay_dict(self):
        params = dict()
        if self.virtual_card_no:
            if hasattr(self.virtual_card_no, 'to_alipay_dict'):
                params['virtual_card_no'] = self.virtual_card_no.to_alipay_dict()
            else:
                params['virtual_card_no'] = self.virtual_card_no
        if self.virtual_card_password:
            if hasattr(self.virtual_card_password, 'to_alipay_dict'):
                params['virtual_card_password'] = self.virtual_card_password.to_alipay_dict()
            else:
                params['virtual_card_password'] = self.virtual_card_password
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardSecretDTO()
        if 'virtual_card_no' in d:
            o.virtual_card_no = d['virtual_card_no']
        if 'virtual_card_password' in d:
            o.virtual_card_password = d['virtual_card_password']
        return o


