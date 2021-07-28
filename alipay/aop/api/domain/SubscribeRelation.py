#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubscribeRelation(object):

    def __init__(self):
        self._keep_state = None
        self._show = None
        self._subscribe_state = None
        self._subscribe_type = None
        self._template_id = None

    @property
    def keep_state(self):
        return self._keep_state

    @keep_state.setter
    def keep_state(self, value):
        self._keep_state = value
    @property
    def show(self):
        return self._show

    @show.setter
    def show(self, value):
        self._show = value
    @property
    def subscribe_state(self):
        return self._subscribe_state

    @subscribe_state.setter
    def subscribe_state(self, value):
        self._subscribe_state = value
    @property
    def subscribe_type(self):
        return self._subscribe_type

    @subscribe_type.setter
    def subscribe_type(self, value):
        self._subscribe_type = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.keep_state:
            if hasattr(self.keep_state, 'to_alipay_dict'):
                params['keep_state'] = self.keep_state.to_alipay_dict()
            else:
                params['keep_state'] = self.keep_state
        if self.show:
            if hasattr(self.show, 'to_alipay_dict'):
                params['show'] = self.show.to_alipay_dict()
            else:
                params['show'] = self.show
        if self.subscribe_state:
            if hasattr(self.subscribe_state, 'to_alipay_dict'):
                params['subscribe_state'] = self.subscribe_state.to_alipay_dict()
            else:
                params['subscribe_state'] = self.subscribe_state
        if self.subscribe_type:
            if hasattr(self.subscribe_type, 'to_alipay_dict'):
                params['subscribe_type'] = self.subscribe_type.to_alipay_dict()
            else:
                params['subscribe_type'] = self.subscribe_type
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubscribeRelation()
        if 'keep_state' in d:
            o.keep_state = d['keep_state']
        if 'show' in d:
            o.show = d['show']
        if 'subscribe_state' in d:
            o.subscribe_state = d['subscribe_state']
        if 'subscribe_type' in d:
            o.subscribe_type = d['subscribe_type']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


