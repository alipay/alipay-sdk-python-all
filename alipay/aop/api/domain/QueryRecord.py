#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryRecord(object):

    def __init__(self):
        self._block_addr = None
        self._block_height = None
        self._corp_code = None
        self._corp_name = None
        self._notary_status = None
        self._opr_cert_name = None
        self._refuse_reason = None
        self._sign_order = None
        self._sign_time = None
        self._sign_type_code = None
        self._syn_time = None
        self._tx_hash_code = None

    @property
    def block_addr(self):
        return self._block_addr

    @block_addr.setter
    def block_addr(self, value):
        self._block_addr = value
    @property
    def block_height(self):
        return self._block_height

    @block_height.setter
    def block_height(self, value):
        self._block_height = value
    @property
    def corp_code(self):
        return self._corp_code

    @corp_code.setter
    def corp_code(self, value):
        self._corp_code = value
    @property
    def corp_name(self):
        return self._corp_name

    @corp_name.setter
    def corp_name(self, value):
        self._corp_name = value
    @property
    def notary_status(self):
        return self._notary_status

    @notary_status.setter
    def notary_status(self, value):
        self._notary_status = value
    @property
    def opr_cert_name(self):
        return self._opr_cert_name

    @opr_cert_name.setter
    def opr_cert_name(self, value):
        self._opr_cert_name = value
    @property
    def refuse_reason(self):
        return self._refuse_reason

    @refuse_reason.setter
    def refuse_reason(self, value):
        self._refuse_reason = value
    @property
    def sign_order(self):
        return self._sign_order

    @sign_order.setter
    def sign_order(self, value):
        self._sign_order = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def sign_type_code(self):
        return self._sign_type_code

    @sign_type_code.setter
    def sign_type_code(self, value):
        self._sign_type_code = value
    @property
    def syn_time(self):
        return self._syn_time

    @syn_time.setter
    def syn_time(self, value):
        self._syn_time = value
    @property
    def tx_hash_code(self):
        return self._tx_hash_code

    @tx_hash_code.setter
    def tx_hash_code(self, value):
        self._tx_hash_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.block_addr:
            if hasattr(self.block_addr, 'to_alipay_dict'):
                params['block_addr'] = self.block_addr.to_alipay_dict()
            else:
                params['block_addr'] = self.block_addr
        if self.block_height:
            if hasattr(self.block_height, 'to_alipay_dict'):
                params['block_height'] = self.block_height.to_alipay_dict()
            else:
                params['block_height'] = self.block_height
        if self.corp_code:
            if hasattr(self.corp_code, 'to_alipay_dict'):
                params['corp_code'] = self.corp_code.to_alipay_dict()
            else:
                params['corp_code'] = self.corp_code
        if self.corp_name:
            if hasattr(self.corp_name, 'to_alipay_dict'):
                params['corp_name'] = self.corp_name.to_alipay_dict()
            else:
                params['corp_name'] = self.corp_name
        if self.notary_status:
            if hasattr(self.notary_status, 'to_alipay_dict'):
                params['notary_status'] = self.notary_status.to_alipay_dict()
            else:
                params['notary_status'] = self.notary_status
        if self.opr_cert_name:
            if hasattr(self.opr_cert_name, 'to_alipay_dict'):
                params['opr_cert_name'] = self.opr_cert_name.to_alipay_dict()
            else:
                params['opr_cert_name'] = self.opr_cert_name
        if self.refuse_reason:
            if hasattr(self.refuse_reason, 'to_alipay_dict'):
                params['refuse_reason'] = self.refuse_reason.to_alipay_dict()
            else:
                params['refuse_reason'] = self.refuse_reason
        if self.sign_order:
            if hasattr(self.sign_order, 'to_alipay_dict'):
                params['sign_order'] = self.sign_order.to_alipay_dict()
            else:
                params['sign_order'] = self.sign_order
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        if self.sign_type_code:
            if hasattr(self.sign_type_code, 'to_alipay_dict'):
                params['sign_type_code'] = self.sign_type_code.to_alipay_dict()
            else:
                params['sign_type_code'] = self.sign_type_code
        if self.syn_time:
            if hasattr(self.syn_time, 'to_alipay_dict'):
                params['syn_time'] = self.syn_time.to_alipay_dict()
            else:
                params['syn_time'] = self.syn_time
        if self.tx_hash_code:
            if hasattr(self.tx_hash_code, 'to_alipay_dict'):
                params['tx_hash_code'] = self.tx_hash_code.to_alipay_dict()
            else:
                params['tx_hash_code'] = self.tx_hash_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryRecord()
        if 'block_addr' in d:
            o.block_addr = d['block_addr']
        if 'block_height' in d:
            o.block_height = d['block_height']
        if 'corp_code' in d:
            o.corp_code = d['corp_code']
        if 'corp_name' in d:
            o.corp_name = d['corp_name']
        if 'notary_status' in d:
            o.notary_status = d['notary_status']
        if 'opr_cert_name' in d:
            o.opr_cert_name = d['opr_cert_name']
        if 'refuse_reason' in d:
            o.refuse_reason = d['refuse_reason']
        if 'sign_order' in d:
            o.sign_order = d['sign_order']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        if 'sign_type_code' in d:
            o.sign_type_code = d['sign_type_code']
        if 'syn_time' in d:
            o.syn_time = d['syn_time']
        if 'tx_hash_code' in d:
            o.tx_hash_code = d['tx_hash_code']
        return o


