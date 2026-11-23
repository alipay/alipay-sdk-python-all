#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TreatTipsRedEnvelope import TreatTipsRedEnvelope


class TreatTips(object):

    def __init__(self):
        self._second_title = None
        self._title = None
        self._treat_action_query = None
        self._treat_action_txt = None
        self._treat_logo = None
        self._treat_style = None
        self._treat_tips_red_envelope = None

    @property
    def second_title(self):
        return self._second_title

    @second_title.setter
    def second_title(self, value):
        self._second_title = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def treat_action_query(self):
        return self._treat_action_query

    @treat_action_query.setter
    def treat_action_query(self, value):
        self._treat_action_query = value
    @property
    def treat_action_txt(self):
        return self._treat_action_txt

    @treat_action_txt.setter
    def treat_action_txt(self, value):
        self._treat_action_txt = value
    @property
    def treat_logo(self):
        return self._treat_logo

    @treat_logo.setter
    def treat_logo(self, value):
        self._treat_logo = value
    @property
    def treat_style(self):
        return self._treat_style

    @treat_style.setter
    def treat_style(self, value):
        self._treat_style = value
    @property
    def treat_tips_red_envelope(self):
        return self._treat_tips_red_envelope

    @treat_tips_red_envelope.setter
    def treat_tips_red_envelope(self, value):
        if isinstance(value, TreatTipsRedEnvelope):
            self._treat_tips_red_envelope = value
        else:
            self._treat_tips_red_envelope = TreatTipsRedEnvelope.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.second_title:
            if hasattr(self.second_title, 'to_alipay_dict'):
                params['second_title'] = self.second_title.to_alipay_dict()
            else:
                params['second_title'] = self.second_title
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.treat_action_query:
            if hasattr(self.treat_action_query, 'to_alipay_dict'):
                params['treat_action_query'] = self.treat_action_query.to_alipay_dict()
            else:
                params['treat_action_query'] = self.treat_action_query
        if self.treat_action_txt:
            if hasattr(self.treat_action_txt, 'to_alipay_dict'):
                params['treat_action_txt'] = self.treat_action_txt.to_alipay_dict()
            else:
                params['treat_action_txt'] = self.treat_action_txt
        if self.treat_logo:
            if hasattr(self.treat_logo, 'to_alipay_dict'):
                params['treat_logo'] = self.treat_logo.to_alipay_dict()
            else:
                params['treat_logo'] = self.treat_logo
        if self.treat_style:
            if hasattr(self.treat_style, 'to_alipay_dict'):
                params['treat_style'] = self.treat_style.to_alipay_dict()
            else:
                params['treat_style'] = self.treat_style
        if self.treat_tips_red_envelope:
            if hasattr(self.treat_tips_red_envelope, 'to_alipay_dict'):
                params['treat_tips_red_envelope'] = self.treat_tips_red_envelope.to_alipay_dict()
            else:
                params['treat_tips_red_envelope'] = self.treat_tips_red_envelope
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TreatTips()
        if 'second_title' in d:
            o.second_title = d['second_title']
        if 'title' in d:
            o.title = d['title']
        if 'treat_action_query' in d:
            o.treat_action_query = d['treat_action_query']
        if 'treat_action_txt' in d:
            o.treat_action_txt = d['treat_action_txt']
        if 'treat_logo' in d:
            o.treat_logo = d['treat_logo']
        if 'treat_style' in d:
            o.treat_style = d['treat_style']
        if 'treat_tips_red_envelope' in d:
            o.treat_tips_red_envelope = d['treat_tips_red_envelope']
        return o


