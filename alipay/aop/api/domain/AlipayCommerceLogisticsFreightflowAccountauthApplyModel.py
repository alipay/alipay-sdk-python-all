#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FreigtFlowAuthAccount import FreigtFlowAuthAccount
from alipay.aop.api.domain.FreigtFlowAuthAccount import FreigtFlowAuthAccount


class AlipayCommerceLogisticsFreightflowAccountauthApplyModel(object):

    def __init__(self):
        self._apply_request_no = None
        self._authorizee_info = None
        self._authorizer_info = None
        self._expiration_time = None
        self._logistics_code = None
        self._mode = None
        self._partner_id = None

    @property
    def apply_request_no(self):
        return self._apply_request_no

    @apply_request_no.setter
    def apply_request_no(self, value):
        self._apply_request_no = value
    @property
    def authorizee_info(self):
        return self._authorizee_info

    @authorizee_info.setter
    def authorizee_info(self, value):
        if isinstance(value, FreigtFlowAuthAccount):
            self._authorizee_info = value
        else:
            self._authorizee_info = FreigtFlowAuthAccount.from_alipay_dict(value)
    @property
    def authorizer_info(self):
        return self._authorizer_info

    @authorizer_info.setter
    def authorizer_info(self, value):
        if isinstance(value, FreigtFlowAuthAccount):
            self._authorizer_info = value
        else:
            self._authorizer_info = FreigtFlowAuthAccount.from_alipay_dict(value)
    @property
    def expiration_time(self):
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, value):
        self._expiration_time = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_request_no:
            if hasattr(self.apply_request_no, 'to_alipay_dict'):
                params['apply_request_no'] = self.apply_request_no.to_alipay_dict()
            else:
                params['apply_request_no'] = self.apply_request_no
        if self.authorizee_info:
            if hasattr(self.authorizee_info, 'to_alipay_dict'):
                params['authorizee_info'] = self.authorizee_info.to_alipay_dict()
            else:
                params['authorizee_info'] = self.authorizee_info
        if self.authorizer_info:
            if hasattr(self.authorizer_info, 'to_alipay_dict'):
                params['authorizer_info'] = self.authorizer_info.to_alipay_dict()
            else:
                params['authorizer_info'] = self.authorizer_info
        if self.expiration_time:
            if hasattr(self.expiration_time, 'to_alipay_dict'):
                params['expiration_time'] = self.expiration_time.to_alipay_dict()
            else:
                params['expiration_time'] = self.expiration_time
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsFreightflowAccountauthApplyModel()
        if 'apply_request_no' in d:
            o.apply_request_no = d['apply_request_no']
        if 'authorizee_info' in d:
            o.authorizee_info = d['authorizee_info']
        if 'authorizer_info' in d:
            o.authorizer_info = d['authorizer_info']
        if 'expiration_time' in d:
            o.expiration_time = d['expiration_time']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'mode' in d:
            o.mode = d['mode']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        return o


