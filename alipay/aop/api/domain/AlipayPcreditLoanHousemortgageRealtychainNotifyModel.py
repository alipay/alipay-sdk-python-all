#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContractSignatory import ContractSignatory


class AlipayPcreditLoanHousemortgageRealtychainNotifyModel(object):

    def __init__(self):
        self._contract_signatory = None
        self._fail_code = None
        self._out_no = None
        self._rcp_flow = None
        self._rcp_no = None
        self._scene = None

    @property
    def contract_signatory(self):
        return self._contract_signatory

    @contract_signatory.setter
    def contract_signatory(self, value):
        if isinstance(value, ContractSignatory):
            self._contract_signatory = value
        else:
            self._contract_signatory = ContractSignatory.from_alipay_dict(value)
    @property
    def fail_code(self):
        return self._fail_code

    @fail_code.setter
    def fail_code(self, value):
        self._fail_code = value
    @property
    def out_no(self):
        return self._out_no

    @out_no.setter
    def out_no(self, value):
        self._out_no = value
    @property
    def rcp_flow(self):
        return self._rcp_flow

    @rcp_flow.setter
    def rcp_flow(self, value):
        self._rcp_flow = value
    @property
    def rcp_no(self):
        return self._rcp_no

    @rcp_no.setter
    def rcp_no(self, value):
        self._rcp_no = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.contract_signatory:
            if hasattr(self.contract_signatory, 'to_alipay_dict'):
                params['contract_signatory'] = self.contract_signatory.to_alipay_dict()
            else:
                params['contract_signatory'] = self.contract_signatory
        if self.fail_code:
            if hasattr(self.fail_code, 'to_alipay_dict'):
                params['fail_code'] = self.fail_code.to_alipay_dict()
            else:
                params['fail_code'] = self.fail_code
        if self.out_no:
            if hasattr(self.out_no, 'to_alipay_dict'):
                params['out_no'] = self.out_no.to_alipay_dict()
            else:
                params['out_no'] = self.out_no
        if self.rcp_flow:
            if hasattr(self.rcp_flow, 'to_alipay_dict'):
                params['rcp_flow'] = self.rcp_flow.to_alipay_dict()
            else:
                params['rcp_flow'] = self.rcp_flow
        if self.rcp_no:
            if hasattr(self.rcp_no, 'to_alipay_dict'):
                params['rcp_no'] = self.rcp_no.to_alipay_dict()
            else:
                params['rcp_no'] = self.rcp_no
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanHousemortgageRealtychainNotifyModel()
        if 'contract_signatory' in d:
            o.contract_signatory = d['contract_signatory']
        if 'fail_code' in d:
            o.fail_code = d['fail_code']
        if 'out_no' in d:
            o.out_no = d['out_no']
        if 'rcp_flow' in d:
            o.rcp_flow = d['rcp_flow']
        if 'rcp_no' in d:
            o.rcp_no = d['rcp_no']
        if 'scene' in d:
            o.scene = d['scene']
        return o


