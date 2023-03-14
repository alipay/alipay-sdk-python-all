#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntlcSignerRequest import AntlcSignerRequest


class AlipayBossProdAntlegalchainNdasignerCreateModel(object):

    def __init__(self):
        self._app_code = None
        self._instl_id = None
        self._opr_staff_id = None
        self._signer_list = None
        self._tenant = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def instl_id(self):
        return self._instl_id

    @instl_id.setter
    def instl_id(self, value):
        self._instl_id = value
    @property
    def opr_staff_id(self):
        return self._opr_staff_id

    @opr_staff_id.setter
    def opr_staff_id(self, value):
        self._opr_staff_id = value
    @property
    def signer_list(self):
        return self._signer_list

    @signer_list.setter
    def signer_list(self, value):
        if isinstance(value, list):
            self._signer_list = list()
            for i in value:
                if isinstance(i, AntlcSignerRequest):
                    self._signer_list.append(i)
                else:
                    self._signer_list.append(AntlcSignerRequest.from_alipay_dict(i))
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.instl_id:
            if hasattr(self.instl_id, 'to_alipay_dict'):
                params['instl_id'] = self.instl_id.to_alipay_dict()
            else:
                params['instl_id'] = self.instl_id
        if self.opr_staff_id:
            if hasattr(self.opr_staff_id, 'to_alipay_dict'):
                params['opr_staff_id'] = self.opr_staff_id.to_alipay_dict()
            else:
                params['opr_staff_id'] = self.opr_staff_id
        if self.signer_list:
            if isinstance(self.signer_list, list):
                for i in range(0, len(self.signer_list)):
                    element = self.signer_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.signer_list[i] = element.to_alipay_dict()
            if hasattr(self.signer_list, 'to_alipay_dict'):
                params['signer_list'] = self.signer_list.to_alipay_dict()
            else:
                params['signer_list'] = self.signer_list
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlegalchainNdasignerCreateModel()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'instl_id' in d:
            o.instl_id = d['instl_id']
        if 'opr_staff_id' in d:
            o.opr_staff_id = d['opr_staff_id']
        if 'signer_list' in d:
            o.signer_list = d['signer_list']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


