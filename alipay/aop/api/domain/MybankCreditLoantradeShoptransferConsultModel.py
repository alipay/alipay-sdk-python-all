#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoantradeShoptransferConsultModel(object):

    def __init__(self):
        self._biz_type = None
        self._receive_alipay_id = None
        self._taobao_id = None
        self._trans_no = None
        self._transfer_alipay_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def receive_alipay_id(self):
        return self._receive_alipay_id

    @receive_alipay_id.setter
    def receive_alipay_id(self, value):
        self._receive_alipay_id = value
    @property
    def taobao_id(self):
        return self._taobao_id

    @taobao_id.setter
    def taobao_id(self, value):
        self._taobao_id = value
    @property
    def trans_no(self):
        return self._trans_no

    @trans_no.setter
    def trans_no(self, value):
        self._trans_no = value
    @property
    def transfer_alipay_id(self):
        return self._transfer_alipay_id

    @transfer_alipay_id.setter
    def transfer_alipay_id(self, value):
        self._transfer_alipay_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.receive_alipay_id:
            if hasattr(self.receive_alipay_id, 'to_alipay_dict'):
                params['receive_alipay_id'] = self.receive_alipay_id.to_alipay_dict()
            else:
                params['receive_alipay_id'] = self.receive_alipay_id
        if self.taobao_id:
            if hasattr(self.taobao_id, 'to_alipay_dict'):
                params['taobao_id'] = self.taobao_id.to_alipay_dict()
            else:
                params['taobao_id'] = self.taobao_id
        if self.trans_no:
            if hasattr(self.trans_no, 'to_alipay_dict'):
                params['trans_no'] = self.trans_no.to_alipay_dict()
            else:
                params['trans_no'] = self.trans_no
        if self.transfer_alipay_id:
            if hasattr(self.transfer_alipay_id, 'to_alipay_dict'):
                params['transfer_alipay_id'] = self.transfer_alipay_id.to_alipay_dict()
            else:
                params['transfer_alipay_id'] = self.transfer_alipay_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeShoptransferConsultModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'receive_alipay_id' in d:
            o.receive_alipay_id = d['receive_alipay_id']
        if 'taobao_id' in d:
            o.taobao_id = d['taobao_id']
        if 'trans_no' in d:
            o.trans_no = d['trans_no']
        if 'transfer_alipay_id' in d:
            o.transfer_alipay_id = d['transfer_alipay_id']
        return o


