#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FinAdditionArgs import FinAdditionArgs


class FinSessionDetail(object):

    def __init__(self):
        self._additional_args = None
        self._identity_id = None
        self._last_active_time = None
        self._session_id = None
        self._session_title = None

    @property
    def additional_args(self):
        return self._additional_args

    @additional_args.setter
    def additional_args(self, value):
        if isinstance(value, FinAdditionArgs):
            self._additional_args = value
        else:
            self._additional_args = FinAdditionArgs.from_alipay_dict(value)
    @property
    def identity_id(self):
        return self._identity_id

    @identity_id.setter
    def identity_id(self, value):
        self._identity_id = value
    @property
    def last_active_time(self):
        return self._last_active_time

    @last_active_time.setter
    def last_active_time(self, value):
        self._last_active_time = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def session_title(self):
        return self._session_title

    @session_title.setter
    def session_title(self, value):
        self._session_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_args:
            if hasattr(self.additional_args, 'to_alipay_dict'):
                params['additional_args'] = self.additional_args.to_alipay_dict()
            else:
                params['additional_args'] = self.additional_args
        if self.identity_id:
            if hasattr(self.identity_id, 'to_alipay_dict'):
                params['identity_id'] = self.identity_id.to_alipay_dict()
            else:
                params['identity_id'] = self.identity_id
        if self.last_active_time:
            if hasattr(self.last_active_time, 'to_alipay_dict'):
                params['last_active_time'] = self.last_active_time.to_alipay_dict()
            else:
                params['last_active_time'] = self.last_active_time
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.session_title:
            if hasattr(self.session_title, 'to_alipay_dict'):
                params['session_title'] = self.session_title.to_alipay_dict()
            else:
                params['session_title'] = self.session_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinSessionDetail()
        if 'additional_args' in d:
            o.additional_args = d['additional_args']
        if 'identity_id' in d:
            o.identity_id = d['identity_id']
        if 'last_active_time' in d:
            o.last_active_time = d['last_active_time']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'session_title' in d:
            o.session_title = d['session_title']
        return o


