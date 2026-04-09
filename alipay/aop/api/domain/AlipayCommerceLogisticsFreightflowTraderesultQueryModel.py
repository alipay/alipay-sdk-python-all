#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FreigtFlowSpdbBizSeqNo import FreigtFlowSpdbBizSeqNo
from alipay.aop.api.domain.FreightFlowSpdbSpecParams import FreightFlowSpdbSpecParams


class AlipayCommerceLogisticsFreightflowTraderesultQueryModel(object):

    def __init__(self):
        self._biz_no = None
        self._biz_scene = None
        self._logistics_code = None
        self._mode = None
        self._mybank_app_id = None
        self._operate_no = None
        self._partner_id = None
        self._spdb_parent_account_no = None
        self._spdb_seq_no = None
        self._spdb_spec_params = None
        self._spdb_tran_tp_dsc = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
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
    def mybank_app_id(self):
        return self._mybank_app_id

    @mybank_app_id.setter
    def mybank_app_id(self, value):
        self._mybank_app_id = value
    @property
    def operate_no(self):
        return self._operate_no

    @operate_no.setter
    def operate_no(self, value):
        self._operate_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def spdb_parent_account_no(self):
        return self._spdb_parent_account_no

    @spdb_parent_account_no.setter
    def spdb_parent_account_no(self, value):
        self._spdb_parent_account_no = value
    @property
    def spdb_seq_no(self):
        return self._spdb_seq_no

    @spdb_seq_no.setter
    def spdb_seq_no(self, value):
        if isinstance(value, FreigtFlowSpdbBizSeqNo):
            self._spdb_seq_no = value
        else:
            self._spdb_seq_no = FreigtFlowSpdbBizSeqNo.from_alipay_dict(value)
    @property
    def spdb_spec_params(self):
        return self._spdb_spec_params

    @spdb_spec_params.setter
    def spdb_spec_params(self, value):
        if isinstance(value, FreightFlowSpdbSpecParams):
            self._spdb_spec_params = value
        else:
            self._spdb_spec_params = FreightFlowSpdbSpecParams.from_alipay_dict(value)
    @property
    def spdb_tran_tp_dsc(self):
        return self._spdb_tran_tp_dsc

    @spdb_tran_tp_dsc.setter
    def spdb_tran_tp_dsc(self, value):
        self._spdb_tran_tp_dsc = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
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
        if self.mybank_app_id:
            if hasattr(self.mybank_app_id, 'to_alipay_dict'):
                params['mybank_app_id'] = self.mybank_app_id.to_alipay_dict()
            else:
                params['mybank_app_id'] = self.mybank_app_id
        if self.operate_no:
            if hasattr(self.operate_no, 'to_alipay_dict'):
                params['operate_no'] = self.operate_no.to_alipay_dict()
            else:
                params['operate_no'] = self.operate_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.spdb_parent_account_no:
            if hasattr(self.spdb_parent_account_no, 'to_alipay_dict'):
                params['spdb_parent_account_no'] = self.spdb_parent_account_no.to_alipay_dict()
            else:
                params['spdb_parent_account_no'] = self.spdb_parent_account_no
        if self.spdb_seq_no:
            if hasattr(self.spdb_seq_no, 'to_alipay_dict'):
                params['spdb_seq_no'] = self.spdb_seq_no.to_alipay_dict()
            else:
                params['spdb_seq_no'] = self.spdb_seq_no
        if self.spdb_spec_params:
            if hasattr(self.spdb_spec_params, 'to_alipay_dict'):
                params['spdb_spec_params'] = self.spdb_spec_params.to_alipay_dict()
            else:
                params['spdb_spec_params'] = self.spdb_spec_params
        if self.spdb_tran_tp_dsc:
            if hasattr(self.spdb_tran_tp_dsc, 'to_alipay_dict'):
                params['spdb_tran_tp_dsc'] = self.spdb_tran_tp_dsc.to_alipay_dict()
            else:
                params['spdb_tran_tp_dsc'] = self.spdb_tran_tp_dsc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsFreightflowTraderesultQueryModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'mode' in d:
            o.mode = d['mode']
        if 'mybank_app_id' in d:
            o.mybank_app_id = d['mybank_app_id']
        if 'operate_no' in d:
            o.operate_no = d['operate_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'spdb_parent_account_no' in d:
            o.spdb_parent_account_no = d['spdb_parent_account_no']
        if 'spdb_seq_no' in d:
            o.spdb_seq_no = d['spdb_seq_no']
        if 'spdb_spec_params' in d:
            o.spdb_spec_params = d['spdb_spec_params']
        if 'spdb_tran_tp_dsc' in d:
            o.spdb_tran_tp_dsc = d['spdb_tran_tp_dsc']
        return o


