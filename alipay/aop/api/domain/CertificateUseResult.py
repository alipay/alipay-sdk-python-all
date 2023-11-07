#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CertificateInstanceAmountInfo import CertificateInstanceAmountInfo
from alipay.aop.api.domain.CertificateSerialInfo import CertificateSerialInfo


class CertificateUseResult(object):

    def __init__(self):
        self._amount_info = None
        self._certificate_id = None
        self._code = None
        self._encrypted_code = None
        self._msg = None
        self._order_id = None
        self._out_order_id = None
        self._result = None
        self._serial_info_list = None
        self._use_order_no = None

    @property
    def amount_info(self):
        return self._amount_info

    @amount_info.setter
    def amount_info(self, value):
        if isinstance(value, CertificateInstanceAmountInfo):
            self._amount_info = value
        else:
            self._amount_info = CertificateInstanceAmountInfo.from_alipay_dict(value)
    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def encrypted_code(self):
        return self._encrypted_code

    @encrypted_code.setter
    def encrypted_code(self, value):
        self._encrypted_code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def serial_info_list(self):
        return self._serial_info_list

    @serial_info_list.setter
    def serial_info_list(self, value):
        if isinstance(value, CertificateSerialInfo):
            self._serial_info_list = value
        else:
            self._serial_info_list = CertificateSerialInfo.from_alipay_dict(value)
    @property
    def use_order_no(self):
        return self._use_order_no

    @use_order_no.setter
    def use_order_no(self, value):
        self._use_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_info:
            if hasattr(self.amount_info, 'to_alipay_dict'):
                params['amount_info'] = self.amount_info.to_alipay_dict()
            else:
                params['amount_info'] = self.amount_info
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.encrypted_code:
            if hasattr(self.encrypted_code, 'to_alipay_dict'):
                params['encrypted_code'] = self.encrypted_code.to_alipay_dict()
            else:
                params['encrypted_code'] = self.encrypted_code
        if self.msg:
            if hasattr(self.msg, 'to_alipay_dict'):
                params['msg'] = self.msg.to_alipay_dict()
            else:
                params['msg'] = self.msg
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.serial_info_list:
            if hasattr(self.serial_info_list, 'to_alipay_dict'):
                params['serial_info_list'] = self.serial_info_list.to_alipay_dict()
            else:
                params['serial_info_list'] = self.serial_info_list
        if self.use_order_no:
            if hasattr(self.use_order_no, 'to_alipay_dict'):
                params['use_order_no'] = self.use_order_no.to_alipay_dict()
            else:
                params['use_order_no'] = self.use_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateUseResult()
        if 'amount_info' in d:
            o.amount_info = d['amount_info']
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'code' in d:
            o.code = d['code']
        if 'encrypted_code' in d:
            o.encrypted_code = d['encrypted_code']
        if 'msg' in d:
            o.msg = d['msg']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'result' in d:
            o.result = d['result']
        if 'serial_info_list' in d:
            o.serial_info_list = d['serial_info_list']
        if 'use_order_no' in d:
            o.use_order_no = d['use_order_no']
        return o


