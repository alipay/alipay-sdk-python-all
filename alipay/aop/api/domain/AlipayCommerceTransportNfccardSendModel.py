#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportNfccardSendModel(object):

    def __init__(self):
        self._card_issuer_pid = None
        self._card_no = None
        self._card_status = None
        self._ext_info = None
        self._issue_org_no = None
        self._sign_status = None
        self._sign_time = None
        self._unsign_time = None
        self._withhold_agreement_no = None

    @property
    def card_issuer_pid(self):
        return self._card_issuer_pid

    @card_issuer_pid.setter
    def card_issuer_pid(self, value):
        self._card_issuer_pid = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_status(self):
        return self._card_status

    @card_status.setter
    def card_status(self, value):
        self._card_status = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def issue_org_no(self):
        return self._issue_org_no

    @issue_org_no.setter
    def issue_org_no(self, value):
        self._issue_org_no = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def unsign_time(self):
        return self._unsign_time

    @unsign_time.setter
    def unsign_time(self, value):
        self._unsign_time = value
    @property
    def withhold_agreement_no(self):
        return self._withhold_agreement_no

    @withhold_agreement_no.setter
    def withhold_agreement_no(self, value):
        self._withhold_agreement_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_issuer_pid:
            if hasattr(self.card_issuer_pid, 'to_alipay_dict'):
                params['card_issuer_pid'] = self.card_issuer_pid.to_alipay_dict()
            else:
                params['card_issuer_pid'] = self.card_issuer_pid
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_status:
            if hasattr(self.card_status, 'to_alipay_dict'):
                params['card_status'] = self.card_status.to_alipay_dict()
            else:
                params['card_status'] = self.card_status
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.issue_org_no:
            if hasattr(self.issue_org_no, 'to_alipay_dict'):
                params['issue_org_no'] = self.issue_org_no.to_alipay_dict()
            else:
                params['issue_org_no'] = self.issue_org_no
        if self.sign_status:
            if hasattr(self.sign_status, 'to_alipay_dict'):
                params['sign_status'] = self.sign_status.to_alipay_dict()
            else:
                params['sign_status'] = self.sign_status
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        if self.unsign_time:
            if hasattr(self.unsign_time, 'to_alipay_dict'):
                params['unsign_time'] = self.unsign_time.to_alipay_dict()
            else:
                params['unsign_time'] = self.unsign_time
        if self.withhold_agreement_no:
            if hasattr(self.withhold_agreement_no, 'to_alipay_dict'):
                params['withhold_agreement_no'] = self.withhold_agreement_no.to_alipay_dict()
            else:
                params['withhold_agreement_no'] = self.withhold_agreement_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportNfccardSendModel()
        if 'card_issuer_pid' in d:
            o.card_issuer_pid = d['card_issuer_pid']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_status' in d:
            o.card_status = d['card_status']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'issue_org_no' in d:
            o.issue_org_no = d['issue_org_no']
        if 'sign_status' in d:
            o.sign_status = d['sign_status']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        if 'unsign_time' in d:
            o.unsign_time = d['unsign_time']
        if 'withhold_agreement_no' in d:
            o.withhold_agreement_no = d['withhold_agreement_no']
        return o


