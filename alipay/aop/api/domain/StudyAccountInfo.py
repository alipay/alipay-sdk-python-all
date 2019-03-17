#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StudyAccountInfo(object):

    def __init__(self):
        self._alipay_card_no = None
        self._card_type = None
        self._study_id = None

    @property
    def alipay_card_no(self):
        return self._alipay_card_no

    @alipay_card_no.setter
    def alipay_card_no(self, value):
        self._alipay_card_no = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def study_id(self):
        return self._study_id

    @study_id.setter
    def study_id(self, value):
        self._study_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_card_no:
            if hasattr(self.alipay_card_no, 'to_alipay_dict'):
                params['alipay_card_no'] = self.alipay_card_no.to_alipay_dict()
            else:
                params['alipay_card_no'] = self.alipay_card_no
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.study_id:
            if hasattr(self.study_id, 'to_alipay_dict'):
                params['study_id'] = self.study_id.to_alipay_dict()
            else:
                params['study_id'] = self.study_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StudyAccountInfo()
        if 'alipay_card_no' in d:
            o.alipay_card_no = d['alipay_card_no']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'study_id' in d:
            o.study_id = d['study_id']
        return o


