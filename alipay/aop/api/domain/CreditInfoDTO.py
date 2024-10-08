#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditInfoDTO(object):

    def __init__(self):
        self._acceptance_jump_url = None
        self._no_need_verify_identity = None
        self._out_agreement_no = None
        self._zm_service_id = None

    @property
    def acceptance_jump_url(self):
        return self._acceptance_jump_url

    @acceptance_jump_url.setter
    def acceptance_jump_url(self, value):
        self._acceptance_jump_url = value
    @property
    def no_need_verify_identity(self):
        return self._no_need_verify_identity

    @no_need_verify_identity.setter
    def no_need_verify_identity(self, value):
        self._no_need_verify_identity = value
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value
    @property
    def zm_service_id(self):
        return self._zm_service_id

    @zm_service_id.setter
    def zm_service_id(self, value):
        self._zm_service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.acceptance_jump_url:
            if hasattr(self.acceptance_jump_url, 'to_alipay_dict'):
                params['acceptance_jump_url'] = self.acceptance_jump_url.to_alipay_dict()
            else:
                params['acceptance_jump_url'] = self.acceptance_jump_url
        if self.no_need_verify_identity:
            if hasattr(self.no_need_verify_identity, 'to_alipay_dict'):
                params['no_need_verify_identity'] = self.no_need_verify_identity.to_alipay_dict()
            else:
                params['no_need_verify_identity'] = self.no_need_verify_identity
        if self.out_agreement_no:
            if hasattr(self.out_agreement_no, 'to_alipay_dict'):
                params['out_agreement_no'] = self.out_agreement_no.to_alipay_dict()
            else:
                params['out_agreement_no'] = self.out_agreement_no
        if self.zm_service_id:
            if hasattr(self.zm_service_id, 'to_alipay_dict'):
                params['zm_service_id'] = self.zm_service_id.to_alipay_dict()
            else:
                params['zm_service_id'] = self.zm_service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditInfoDTO()
        if 'acceptance_jump_url' in d:
            o.acceptance_jump_url = d['acceptance_jump_url']
        if 'no_need_verify_identity' in d:
            o.no_need_verify_identity = d['no_need_verify_identity']
        if 'out_agreement_no' in d:
            o.out_agreement_no = d['out_agreement_no']
        if 'zm_service_id' in d:
            o.zm_service_id = d['zm_service_id']
        return o


