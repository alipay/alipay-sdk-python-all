#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EtcAuthResult(object):

    def __init__(self):
        self._auth_agreement_no = None
        self._auth_time = None
        self._card_no = None
        self._issue_name = None
        self._out_agreement_no = None
        self._plate_color = None
        self._plate_no = None
        self._service_status = None
        self._unauth_time = None

    @property
    def auth_agreement_no(self):
        return self._auth_agreement_no

    @auth_agreement_no.setter
    def auth_agreement_no(self, value):
        self._auth_agreement_no = value
    @property
    def auth_time(self):
        return self._auth_time

    @auth_time.setter
    def auth_time(self, value):
        self._auth_time = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def issue_name(self):
        return self._issue_name

    @issue_name.setter
    def issue_name(self, value):
        self._issue_name = value
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def service_status(self):
        return self._service_status

    @service_status.setter
    def service_status(self, value):
        self._service_status = value
    @property
    def unauth_time(self):
        return self._unauth_time

    @unauth_time.setter
    def unauth_time(self, value):
        self._unauth_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_agreement_no:
            if hasattr(self.auth_agreement_no, 'to_alipay_dict'):
                params['auth_agreement_no'] = self.auth_agreement_no.to_alipay_dict()
            else:
                params['auth_agreement_no'] = self.auth_agreement_no
        if self.auth_time:
            if hasattr(self.auth_time, 'to_alipay_dict'):
                params['auth_time'] = self.auth_time.to_alipay_dict()
            else:
                params['auth_time'] = self.auth_time
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.issue_name:
            if hasattr(self.issue_name, 'to_alipay_dict'):
                params['issue_name'] = self.issue_name.to_alipay_dict()
            else:
                params['issue_name'] = self.issue_name
        if self.out_agreement_no:
            if hasattr(self.out_agreement_no, 'to_alipay_dict'):
                params['out_agreement_no'] = self.out_agreement_no.to_alipay_dict()
            else:
                params['out_agreement_no'] = self.out_agreement_no
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.service_status:
            if hasattr(self.service_status, 'to_alipay_dict'):
                params['service_status'] = self.service_status.to_alipay_dict()
            else:
                params['service_status'] = self.service_status
        if self.unauth_time:
            if hasattr(self.unauth_time, 'to_alipay_dict'):
                params['unauth_time'] = self.unauth_time.to_alipay_dict()
            else:
                params['unauth_time'] = self.unauth_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EtcAuthResult()
        if 'auth_agreement_no' in d:
            o.auth_agreement_no = d['auth_agreement_no']
        if 'auth_time' in d:
            o.auth_time = d['auth_time']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'issue_name' in d:
            o.issue_name = d['issue_name']
        if 'out_agreement_no' in d:
            o.out_agreement_no = d['out_agreement_no']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'service_status' in d:
            o.service_status = d['service_status']
        if 'unauth_time' in d:
            o.unauth_time = d['unauth_time']
        return o


