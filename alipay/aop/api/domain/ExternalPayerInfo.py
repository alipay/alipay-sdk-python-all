#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExternalPayerInfo(object):

    def __init__(self):
        self._out_inst_card_no = None
        self._out_inst_payer_inst_id = None
        self._out_payer_account_name = None

    @property
    def out_inst_card_no(self):
        return self._out_inst_card_no

    @out_inst_card_no.setter
    def out_inst_card_no(self, value):
        self._out_inst_card_no = value
    @property
    def out_inst_payer_inst_id(self):
        return self._out_inst_payer_inst_id

    @out_inst_payer_inst_id.setter
    def out_inst_payer_inst_id(self, value):
        self._out_inst_payer_inst_id = value
    @property
    def out_payer_account_name(self):
        return self._out_payer_account_name

    @out_payer_account_name.setter
    def out_payer_account_name(self, value):
        self._out_payer_account_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_inst_card_no:
            if hasattr(self.out_inst_card_no, 'to_alipay_dict'):
                params['out_inst_card_no'] = self.out_inst_card_no.to_alipay_dict()
            else:
                params['out_inst_card_no'] = self.out_inst_card_no
        if self.out_inst_payer_inst_id:
            if hasattr(self.out_inst_payer_inst_id, 'to_alipay_dict'):
                params['out_inst_payer_inst_id'] = self.out_inst_payer_inst_id.to_alipay_dict()
            else:
                params['out_inst_payer_inst_id'] = self.out_inst_payer_inst_id
        if self.out_payer_account_name:
            if hasattr(self.out_payer_account_name, 'to_alipay_dict'):
                params['out_payer_account_name'] = self.out_payer_account_name.to_alipay_dict()
            else:
                params['out_payer_account_name'] = self.out_payer_account_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExternalPayerInfo()
        if 'out_inst_card_no' in d:
            o.out_inst_card_no = d['out_inst_card_no']
        if 'out_inst_payer_inst_id' in d:
            o.out_inst_payer_inst_id = d['out_inst_payer_inst_id']
        if 'out_payer_account_name' in d:
            o.out_payer_account_name = d['out_payer_account_name']
        return o


