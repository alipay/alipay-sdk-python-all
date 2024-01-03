#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ParticipantForm import ParticipantForm


class ExtendStrategy(object):

    def __init__(self):
        self._participant_form = None
        self._strategy = None

    @property
    def participant_form(self):
        return self._participant_form

    @participant_form.setter
    def participant_form(self, value):
        if isinstance(value, ParticipantForm):
            self._participant_form = value
        else:
            self._participant_form = ParticipantForm.from_alipay_dict(value)
    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, value):
        self._strategy = value


    def to_alipay_dict(self):
        params = dict()
        if self.participant_form:
            if hasattr(self.participant_form, 'to_alipay_dict'):
                params['participant_form'] = self.participant_form.to_alipay_dict()
            else:
                params['participant_form'] = self.participant_form
        if self.strategy:
            if hasattr(self.strategy, 'to_alipay_dict'):
                params['strategy'] = self.strategy.to_alipay_dict()
            else:
                params['strategy'] = self.strategy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtendStrategy()
        if 'participant_form' in d:
            o.participant_form = d['participant_form']
        if 'strategy' in d:
            o.strategy = d['strategy']
        return o


