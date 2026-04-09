#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FreightFlowSpdbSpecParams import FreightFlowSpdbSpecParams


class AlipayCommerceLogisticsFreightflowTradereconApplyModel(object):

    def __init__(self):
        self._logistics_code = None
        self._mode = None
        self._mybank_app_id = None
        self._out_request_no = None
        self._parent_card_no = None
        self._partner_id = None
        self._query_date = None
        self._query_num = None
        self._query_type = None
        self._spdb_spec_params = None
        self._start_num = None
        self._sub_card_no = None

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
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def parent_card_no(self):
        return self._parent_card_no

    @parent_card_no.setter
    def parent_card_no(self, value):
        self._parent_card_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def query_date(self):
        return self._query_date

    @query_date.setter
    def query_date(self, value):
        self._query_date = value
    @property
    def query_num(self):
        return self._query_num

    @query_num.setter
    def query_num(self, value):
        self._query_num = value
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
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
    def start_num(self):
        return self._start_num

    @start_num.setter
    def start_num(self, value):
        self._start_num = value
    @property
    def sub_card_no(self):
        return self._sub_card_no

    @sub_card_no.setter
    def sub_card_no(self, value):
        self._sub_card_no = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.parent_card_no:
            if hasattr(self.parent_card_no, 'to_alipay_dict'):
                params['parent_card_no'] = self.parent_card_no.to_alipay_dict()
            else:
                params['parent_card_no'] = self.parent_card_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.query_date:
            if hasattr(self.query_date, 'to_alipay_dict'):
                params['query_date'] = self.query_date.to_alipay_dict()
            else:
                params['query_date'] = self.query_date
        if self.query_num:
            if hasattr(self.query_num, 'to_alipay_dict'):
                params['query_num'] = self.query_num.to_alipay_dict()
            else:
                params['query_num'] = self.query_num
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.spdb_spec_params:
            if hasattr(self.spdb_spec_params, 'to_alipay_dict'):
                params['spdb_spec_params'] = self.spdb_spec_params.to_alipay_dict()
            else:
                params['spdb_spec_params'] = self.spdb_spec_params
        if self.start_num:
            if hasattr(self.start_num, 'to_alipay_dict'):
                params['start_num'] = self.start_num.to_alipay_dict()
            else:
                params['start_num'] = self.start_num
        if self.sub_card_no:
            if hasattr(self.sub_card_no, 'to_alipay_dict'):
                params['sub_card_no'] = self.sub_card_no.to_alipay_dict()
            else:
                params['sub_card_no'] = self.sub_card_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsFreightflowTradereconApplyModel()
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'mode' in d:
            o.mode = d['mode']
        if 'mybank_app_id' in d:
            o.mybank_app_id = d['mybank_app_id']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'parent_card_no' in d:
            o.parent_card_no = d['parent_card_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'query_date' in d:
            o.query_date = d['query_date']
        if 'query_num' in d:
            o.query_num = d['query_num']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'spdb_spec_params' in d:
            o.spdb_spec_params = d['spdb_spec_params']
        if 'start_num' in d:
            o.start_num = d['start_num']
        if 'sub_card_no' in d:
            o.sub_card_no = d['sub_card_no']
        return o


