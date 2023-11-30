#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrivateInfo(object):

    def __init__(self):
        self._id_card_no = None
        self._phone_no = None

    @property
    def id_card_no(self):
        return self._id_card_no

    @id_card_no.setter
    def id_card_no(self, value):
        self._id_card_no = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.id_card_no:
            if hasattr(self.id_card_no, 'to_alipay_dict'):
                params['id_card_no'] = self.id_card_no.to_alipay_dict()
            else:
                params['id_card_no'] = self.id_card_no
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrivateInfo()
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        return o


